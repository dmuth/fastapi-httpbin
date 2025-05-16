
import { useState } from 'react';

export function useGameState() {

  const [dice, setDice] = useState([1, 1, 1, 1, 1]);
  const [held, setHeld] = useState([false, false, false, false, false]);
  const [rollsLeft, setRollsLeft] = useState(3);

  /**
  * Roll our dice.
  */
  const rollDice = () => {
    if (rollsLeft === 0) return;

    const newDice = dice.map((die, i) => (held[i] ? die : Math.floor(Math.random() * 6) + 1));
    setDice(newDice);
    setRollsLeft(r => r - 1);
  };

  /**
  * Called when we're holding a die.
  */
  const toggleHold = (index) => {
    const newHeld = [...held];
    newHeld[index] = !newHeld[index];
    setHeld(newHeld);
  };

  /**
  * Call when we're starting a new turn.
  */
  const startNewTurn = () => {
    setHeld([false, false, false, false, false]);
    setRollsLeft(3);
    setDice([1, 1, 1, 1, 1]); // optional: clear values for visual feedback
  };

  return {
    dice,
    held,
    rollsLeft,
    rollDice,
    toggleHold,
    startNewTurn,
  };

}

