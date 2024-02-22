from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import VocabularyCard
from .serializers import VocabCardSerializer
# import webbrowser
import requests
from bs4 import BeautifulSoup



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
    return Response(serializer.data)

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


@api_view(['GET'])
def get_definition(request, primary_key):
    """Search jisho.org with a japanese search word"""
    response = requests.get(f"https://jisho.org/word/{primary_key}")
    text_soup = BeautifulSoup(response.content, 'html.parser')
    furigana = text_soup.find("span", {"class": "furigana"})
    furigana = "".join(furigana.get_text().split("\n"))
    definition_list = list([f"{primary_key} 【{furigana}】"])
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
    definition = "\n".join(definition_list)
    print(definition)
    return Response(definition)


@api_view(['PUT'])
def edit_vocab_card(request, primary_key):
    data = request.data
    vocab_card = VocabularyCard.objects.get(id=primary_key)
    serializer = VocabCardSerializer(instance=vocab_card, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def update_day(request, days):
    vocab_cards = VocabularyCard.objects.all()
    for card in vocab_cards:
        card.days_until_next_study -= int(days)
        if card.days_until_next_study < 0:
            card.days_until_next_study = 0
        card.save()
    return Response("Due dates updated")


@api_view(['DELETE'])
def delete_vocab_card(request, primary_key):
    card = VocabularyCard.objects.get(id=primary_key)
    delete_message = 'Card: ' + card.vocab_word + 'was deleted'
    card.delete()
    return Response(delete_message)