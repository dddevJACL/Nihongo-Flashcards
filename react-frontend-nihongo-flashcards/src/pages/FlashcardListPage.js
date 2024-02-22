import React from 'react'
import { useState, useEffect } from 'react'
import VocabCard from '../components/VocabCard'

const FlashcardListPage = () => {

    let [vocabCards, setVocabCards] = useState([])

    useEffect(() => {
        getVocabCards()
    }, [])


    let getVocabCards = async () => {
        let response = await fetch('/api/vocabcards/')
        let data = await response.json()
        setVocabCards(data)
    }

    return (
    <div className='notes'>
      <div className='notes-header'>
        <h2 className='notes-title'>&#9750; Flashcards</h2>
        <p className='notes-count'>{vocabCards.length}</p>
      </div>
      <div className='notes-list'>
        {vocabCards.map((vocabularyCard, index) => (
            <VocabCard key={index} vocabCard={vocabularyCard} />
        ))}
      </div>
    </div>
  )
}

export default FlashcardListPage
