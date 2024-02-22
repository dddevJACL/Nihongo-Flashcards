import React from 'react';
import { Link } from 'react-router-dom'; 

const Nav = () => {
  return (
    <nav className="app-nav">
        <Link to='/' class='navBarLink'>  Home  </Link>
        <Link to='../studylist' class='navBarLink'>  Study  </Link>
        <Link to='../create' class='navBarLink'>  Create  </Link>
        <Link to='../flashcards' class='navBarLink'>  View / Edit  </Link>
    </nav>
  )
}

export default Nav
