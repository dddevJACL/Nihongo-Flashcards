import React from 'react'
import { useState, useEffect } from 'react'
import StudyCard from '../components/StudyCard'

const StudyListPage = () => {

  let [vocabCards, setVocabCards] = useState([])

  useEffect(() => {
      getStudyCards()
  }, [])


  let getStudyCards = async () => {
      let response = await fetch('/api/studycards/')
      let data = await response.json()
      setVocabCards(data)
  }


  return (
  <div className='notes'>
    <div className='notes-header'>
      <h2 className='notes-title'>Cards due: </h2>
      <p className='notes-count'>{vocabCards.length}</p>
    </div>
    <div className='notes-list'>
      {vocabCards.map((vocabularyCard, index) => (
          <StudyCard key={index} vocabCard={vocabularyCard} />
      ))}
    </div>
  </div>
)
}

export default StudyListPage
