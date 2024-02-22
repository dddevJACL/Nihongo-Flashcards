import React, { useState, useEffect } from 'react'
import { Link, useParams, useNavigate } from 'react-router-dom'



const StudyCardPage = () => {
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

    let correct = () => {
        card.correct_streak += 1
        card.num_times_correct += 1
        if (card.correct_streak >= 2) {
            card.days_until_next_study = 2 ^ (card.correct_streak - 2)
        }
        updateCard()
        navigate('/studylist')
    }

 function incorrect() {
    card.correct_streak = 0
    card.num_times_wrong += 1
    updateCard()
    navigate('/studylist')
    }


    return (
        <div className='note'>
            <div className='note-header'>
            </div>
            <button className='notes-title' onClick={correct} title='Review frequency decreases'>Correct!!!!!</button>
            <h1 className='app-header'>{card?.vocab_word}</h1>
            <h2 className='app-header'>{card?.example_sentence}</h2>
            <h3 className='app-header'>{card?.vocab_answer}</h3>
            <button className='notes-title' onClick={incorrect} title='Review frequency increases'>Incorrect...</button>
            <Link to={`/card/${card?.id}`}><p>Edit Card</p></Link>
        </div>
    )
}

export default StudyCardPage