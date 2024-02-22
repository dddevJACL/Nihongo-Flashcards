import React, { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'



const CardPage = () => {
    const params  = useParams()
    const navigate = useNavigate()
    let [card, setCard] = useState(null)

    useEffect(() => {
        if(params){getCard()}
    },[params]);

    let getCard = async () => {
        try {
            let response = await fetch(`/api/vocabcard/${params.id}`)
            let data = await response.json()
            setCard(data)
        } catch (error) {
            console.error("Error retrieving card", error)
        }
    };
    
    let updateCard = async () => {
        fetch(`/api/vocabcard/${params.id}/edit/`, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(card)
        })
    }

    let handleSubmit = () => {
        updateCard()
        navigate('/flashcards')
    }

    let deleteCard = async () => {
        fetch(`/api/vocabcard/${params.id}/delete/`, {
            method: "DELETE",
            headers: {
                'Content-Type': 'application/json'
            }
        })
        navigate('/flashcards')
    }

    return (
        <div className='note'>
            <div className='note-header'>
            </div>
            <button onClick={handleSubmit} title='Save the edits you made for this card'>Save edits</button>
            <textarea onChange={(e) => {setCard({ ...card, 'vocab_word':e.target.value })}} defaultValue={card?.vocab_word}></textarea>
            <textarea onChange={(e) => {setCard({ ...card, 'example_sentence':e.target.value })}} defaultValue={card?.example_sentence}></textarea>
            <textarea onChange={(e) => {setCard({ ...card, 'vocab_answer':e.target.value })}} defaultValue={card?.vocab_answer}></textarea>
            <p>Number of times correct: {card?.num_times_correct}</p>
            <p>Number of times incorrect: {card?.num_times_wrong}</p>
            <p>Correct streak: {card?.correct_streak}</p>
            <label for='days-countdown'>Days until next study: </label>
            <input type="number" id='days-countdown' name='days-countdown' onChange={(e) => {setCard({ ...card, 'days_until_next_study':e.target.value })}} defaultValue={card?.days_until_next_study}></input>
            <p>Date last studied: {card?.date_last_studied.slice(0,10) + " " + card?.date_last_studied.slice(11,19)}</p>
            <button onClick={deleteCard} title='Permanently delete this card'>Delete Card</button>
        </div>
    )
}

export default CardPage