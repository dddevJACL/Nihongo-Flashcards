import React from 'react'
import { useState, useEffect } from 'react'

const HomePage = () => {
  let [vocabCards, setVocabCards] = useState([])

    useEffect(() => {
        getVocabCards()
    }, [])


    let getVocabCards = async () => {
        let response = await fetch('/api/home/')
        let data = await response.json()
        console.log(data)
        setVocabCards(data)
    }

  return (
    <div>
      <h2 className='notes-title'>Welcome to Nihongo Flashcards!</h2>
      <p>Your last study session was: {vocabCards}</p>
    </div>
  )
}

export default HomePage
