import React from 'react';
import './Scorecard.css';

function Scorecard() {
  return (
    <>

    <div className="scorecard-wrapper">

    <div className="scorecard">
      <h5 className="text-center mb-3">Upper Section</h5>
      <div className="scorecard-grid">
        <div className="header">Category</div>
        <div className="header">Score</div>

        <div className="name">Aces</div>   <div className="score">&nbsp;</div>
        <div className="name">Twos</div>   <div className="score">&nbsp;</div>
        <div className="name">Threes</div> <div className="score">&nbsp;</div>
        <div className="name">Fours</div>  <div className="score">&nbsp;</div>
        <div className="name">Five</div>   <div className="score">&nbsp;</div>
        <div className="name">Sixes</div>  <div className="score">&nbsp;</div>

        <div className="subtotal-label">Subtotal</div> <div className="subtotal-box">&nbsp;</div>
        <div className="bonus-label">Bonus (35)</div> <div className="bonus-box">&nbsp;</div>

      </div>
    </div>

    <div className="scorecard">
      <h5 className="text-center mb-3">Lower Section</h5>
      <div className="scorecard-grid">
        <div className="header">Category</div>
        <div className="header">Score</div>

        <div className="name">3 of a Kind</div>         <div className="score">&nbsp;</div>
        <div className="name">4 of a Kind</div>         <div className="score">&nbsp;</div>
        <div className="name">Full House (25)</div>     <div className="score">&nbsp;</div>
        <div className="name">Small Straight (30)</div> <div className="score">&nbsp;</div>
        <div className="name">Large Straight (40)</div> <div className="score">&nbsp;</div>
        <div className="name">Yahtzee (50)</div>        <div className="score">&nbsp;</div>
        <div className="name">Chance</div>              <div className="score">&nbsp;</div>
        <div className="name">Yahtzee Bonus</div>       <div className="score">&nbsp;</div>

        <div className="subtotal-label">Lower Total</div> <div className="subtotal-box">&nbsp;</div>
        <div className="bonus-label">Grand Total</div>    <div className="bonus-box">&nbsp;</div>

      </div>
    </div>

    </div>

    </>

  );
}

export default Scorecard;

