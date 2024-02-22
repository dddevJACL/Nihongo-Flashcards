import React from 'react'
import { Link } from 'react-router-dom'

const VocabCard = ({ vocabCard }) => {
  return (
    <Link to={`/card/${vocabCard.id}`}>
      <div className='notes-list-item'>
        <h3>{vocabCard.vocab_word}</h3>
      </div>
    </Link>
  )
}

export default VocabCard