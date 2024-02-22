import React from 'react';
import { Routes, Route } from 'react-router-dom'; 

import './App.css';
import Header from './components/Header';
import HomePage from './pages/HomePage';
import CardPage from './pages/CardPage'
import FlashcardListPage from './pages/FlashcardListPage';
import CreatePage from './pages/CreatePage';
import StudyListPage from './pages/StudyListPage';
import StudyCardPage from './pages/StudyCardPage';
import Nav from './components/Nav';



function App() {
  return (
      <div className="container dark">
        <div className="App">
          <Header />
          <Nav />
          <Routes>
            <Route path='/' element={<HomePage />} />
            <Route path='/create' element = {<CreatePage />} />
            <Route path='/studylist' element = {<StudyListPage />} />
            <Route path='/flashcards' element={<FlashcardListPage />} />
            <Route path='/card/:id' element={<CardPage />} />
            <Route path='/studycard/:id' element={<StudyCardPage />} />
          </Routes>
        </div>
      </div>
  );
}

export default App;
