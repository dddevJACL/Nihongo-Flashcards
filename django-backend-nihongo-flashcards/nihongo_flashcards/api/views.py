from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import VocabularyCard
from .serializers import VocabCardSerializer
from datetime import date
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen



@api_view(['GET'])
def get_routes(request):

    #in wikiscraper
    routes = [
        {
            'Endpoint': '/vocabcards/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of flashcards'
        },
        {
            'Endpoint': '/vocabcard/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note flashcard'
        },
        {
            'Endpoint': '/vocabcards/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new flashcard with data sent in post request'
        },
        {
            'Endpoint': '/vocabcard/id/edit/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates a flashcard with data sent in post request'
        },
        {
            'Endpoint': '/vocabcard/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an exiting flashcard'
        },
    ]

    return Response(routes)

@api_view(['GET'])
def get_all_vocabcards(request):
    vocab_cards = VocabularyCard.objects.all().order_by('id')
    serializer = VocabCardSerializer(vocab_cards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_vocabcard(request, primary_key):
    vocab_card = VocabularyCard.objects.get(id=primary_key)
    serializer = VocabCardSerializer(vocab_card, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_studycards(request):
    vocab_cards = VocabularyCard.objects.filter(days_until_next_study=0).order_by('days_until_next_study')
    serializer = VocabCardSerializer(vocab_cards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_cards_by_last_study(request):
    vocab_cards = VocabularyCard.objects.all().order_by('date_last_studied')
    serializer = VocabCardSerializer(vocab_cards, many=True)
    last_study_time = serializer.data[-1]["date_last_studied"]
    update_day(last_study_time)
    am_pm = " A.M."
    if int(last_study_time[11:13]) >= 12:
        am_pm = " P.M."
    return Response(last_study_time[:10] + " at " + last_study_time[11:19] + am_pm)


def update_day(study_time):
    last_study = study_time[:10]
    last_study_date = date(int(last_study[:4]), int(last_study[5:7]), int(last_study[8:]))
    current_time = date.today()
    time_dif = current_time - last_study_date
    days = time_dif.days
    if days > 1:
        vocab_cards = VocabularyCard.objects.all()
        for card in vocab_cards:
            card.days_until_next_study -= days
            if card.days_until_next_study < 0:
                card.days_until_next_study = 0
            card.save()
    return "Due dates updated"

@api_view(['POST'])
def create_vocabCard(request):
    data = request.data
    try:
        vocab_card = VocabularyCard.objects.create(
            vocab_word=data['vocab_word'],
            example_sentence=data['example_sentence'],
            vocab_answer=data['vocab_answer']
            )
    except:
        vocab_card = VocabularyCard.objects.create(
            vocab_word=data['vocab_word'],
            vocab_answer=data['vocab_answer']
            )
    serializer = VocabCardSerializer(vocab_card, many=False)
    return Response(serializer.data)

def parse_encode(primary_key):
    """Encode a japanese character for URL"""
    hex_list = list()
    for byte in primary_key:
        hex_list.append("%" + str(hex(byte)).upper()[2:])
        print(str(hex(byte)).upper())
    print("".join(hex_list))
    return "".join(hex_list)


@api_view(['GET'])
def get_definition(request, primary_key):
    """Search jisho.org with a japanese search word"""
    primary_key = parse_encode(primary_key.encode())
    with urlopen(f"https://jisho.org/word/{primary_key}") as site_response:
        response = site_response.read()
    text_soup = BeautifulSoup(response, 'html.parser')
    key_word = text_soup.find("div", {"class": "concept_light-representation"})
    key_word = key_word.get_text().split("\n")[4].strip()
    furigana = text_soup.find("span", {"class": "furigana"})
    furigana = "".join(furigana.get_text().split("\n"))
    definition_list = list([f"{key_word} 【{furigana}】"])
    body_spans = text_soup.find_all("span", {"class": "meaning-meaning"})
    counter = 1
    for span_element in body_spans:
        span_text = span_element.get_text()
        char = ord(span_text[0])
        if (65 <= char <= 90) or (97 <= char <= 122):
            definition_list.append(f"{counter}. {span_text}")
            counter += 1
        else:
            definition_list.append(f"Other forms: {span_text}")
    
    definition_list.append("\n")
    flag = 1
    with urlopen(f"https://jisho.org/word/{primary_key}-{flag}") as site_response:
        response = site_response.read()
        status_code = site_response.getcode()
    while status_code == 200:
        text_soup = BeautifulSoup(response, 'html.parser')
        furigana = text_soup.find("span", {"class": "furigana"})
        furigana = "".join(furigana.get_text().split("\n"))
        definition_list.append(f"{key_word} 【{furigana}】")
        body_spans = text_soup.find_all("span", {"class": "meaning-meaning"})
        counter = 1
        for span_element in body_spans:
            span_text = span_element.get_text()
            char = ord(span_text[0])
            if (65 <= char <= 90) or (97 <= char <= 122):
                definition_list.append(f"{counter}. {span_text}")
                counter += 1
            else:
                definition_list.append(f"Other forms: {span_text}")
        definition_list.append("\n")
        flag += 1
        with urlopen(f"https://jisho.org/word/{primary_key}-{flag}") as site_response:
            response = site_response.read()
            status_code = site_response.getcode()
    definition = "\n".join(definition_list)
    print(definition)
    return Response([key_word, definition])


@api_view(['PUT'])
def edit_vocab_card(request, primary_key):
    data = request.data
    vocab_card = VocabularyCard.objects.get(id=primary_key)
    serializer = VocabCardSerializer(instance=vocab_card, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)




@api_view(['DELETE'])
def delete_vocab_card(request, primary_key):
    card = VocabularyCard.objects.get(id=primary_key)
    delete_message = 'Card: ' + card.vocab_word + 'was deleted'
    card.delete()
    return Response(delete_message)
