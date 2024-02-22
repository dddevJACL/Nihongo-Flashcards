import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'


const CreatePage = () => {
  const navigate = useNavigate()
  let [card, setCard] = useState(null)


  let handleSubmit = () => {
      createCard()
      navigate('/flashcards')
  }

  let createCard = async () => {
    fetch(`/api/vocabcards/create/`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(card)
    })
    navigate('/')
}


  return (
      <div className='note'>
          <div className='note-header'>
          </div>
          <button onClick={handleSubmit} title='Create a new card with the given inputs.'>Create Flashcard</button>
          <textarea name='vocabword' required placeholder='Enter a vocabulary word for this flashcard' onChange={(e) => {setCard({ ...card, 'vocab_word':e.target.value })}}></textarea>
          <textarea name='example-sentence' placeholder='Enter an example sentence for the vocabulary word' onChange={(e) => {setCard({ ...card, 'example_sentence':e.target.value })}}></textarea>
          <textarea value={card?.vocab_answer} name='definition' required placeholder='Insert one or more definition(s), translation(s), etc. for your vocabulary word' onChange={(e) => {setCard({ ...card, 'vocab_answer':e.target.value })}}></textarea>
          <button onClick={async () => {if (card?.vocab_word === undefined) {
        return
    }
    let response = await fetch(`/api/definition/${card?.vocab_word}`)
    let data = await response.json()
    setCard({ ...card, 'vocab_answer':data })
    return
}} title='Get definitions from jisho.org.'>Get Definition</button>
      </div>
  )
}

export default CreatePage
