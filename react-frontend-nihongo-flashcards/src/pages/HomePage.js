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
        setVocabCards(data)
    }


  let updateDay = async () => {
    console.log(num_days)
    fetch(`api/home/update/${num_days}/`, {
      method: "PUT",
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(num_days)
  })

}
let num_days = 0

  return (
    <div>
      <h2 className='notes-title'>Welcome to Nihongo Flashcards!</h2>
      <label for='days-countdown'>How many days has it been since you last used Nihongo Flashcards?: </label>
      <input type="number" id='days-countdown' name='days-countdown' min={0} onChange={(e) => num_days = e.target.value} ></input>
      <button onClick={updateDay} title='Update due dates of all flashcards with the given number'>Update Due Dates</button>
    </div>
  )
}

export default HomePage
