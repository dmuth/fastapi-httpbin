
import React from 'react';
import './Dice.css';


function Die({ value, held, onClick }) {
  return (
    <div className={`die die${value}`} onClick={onClick}>
      <span className="dot"></span>
      <span className="dot"></span>
      <span className="dot"></span>
      <span className="dot"></span>
      <span className="dot"></span>
      <span className="dot"></span>
      <span className="dot"></span>
    </div>
  );
}


export default Die;

