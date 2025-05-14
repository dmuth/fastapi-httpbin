
import React from 'react';
import './Dice.css';

function getDotLayout(value) {

  if (value == 1) {
    return(
      <div class="die dice1 dice_element" >
        <div class="dot center"></div>
      </div>
      )

  } else if (value == 2) {
    return(
      <div class="die dice2 dice_element" >
        <div class="dot dtop dleft"></div>
        <div class="dot dbottom dright"></div>
      </div>
      )

  } else if (value == 3) {
    return(
      <div class="die dice3 dice_element" >
        <div class="dot dtop dleft"></div>
        <div class="dot center"></div>
        <div class="dot dbottom dright"></div>
      </div>
      )

  } else if (value == 4) {
    return(
      <div class="die dice4 dice_element" >
        <div class="dot dtop dleft"></div>
        <div class="dot dtop dright"></div>
        <div class="dot dbottom dleft"></div>
        <div class="dot dbottom dright"></div>
      </div>
      )

  } else if (value == 5) {
    return(
      <div class="die dice5 dice_element" >
        <div class="dot dtop dleft"></div>
        <div class="dot dtop dright"></div>
        <div class="dot center"></div>
        <div class="dot dbottom dleft"></div>
        <div class="dot dbottom dright"></div>
      </div>
      )

  } else if (value == 6) {
    return(
      <div class="die dice6 dice_element" >
        <div class="dot dtop dleft"></div>
        <div class="dot dtop dright"></div>
        <div class="dot center dleft"></div>
        <div class="dot center dright"></div>
        <div class="dot dbottom dleft"></div>
        <div class="dot dbottom dright"></div>
      </div>
      )

  }



  switch (value) {
    case 2:
      return (
        <>
          <div className="dot dtop dleft"></div>
          <div className="dot dbottom dright"></div>
        </>
      );
    // Add other cases later...
    default:
      return <div className="dot center"></div>;
  }
}

function Die({ value, held, onClick }) {
  return (
    <div
      className={`die dice${value} dice_element ${held ? 'dice-held' : ''}`}
      onClick={onClick}
    >
      {getDotLayout(value)}
    </div>
  );
}

export default Die;

