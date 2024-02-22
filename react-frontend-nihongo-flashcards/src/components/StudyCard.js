import React from 'react'
import { Link } from 'react-router-dom'

const StudyCard = ({ vocabCard }) => {
  return (
    <Link to={`/studycard/${vocabCard.id}`}>
      <div className='notes-list-item'>
        <h3>{vocabCard.vocab_word}</h3>
        <p>{vocabCard.example_sentence}</p>
      </div>
    </Link>
  )
}

export default StudyCard