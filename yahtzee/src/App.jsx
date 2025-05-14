// src/App.jsx
import './App.css'; // <- Add this if it’s missing

import { useState } from 'react';
import { Container, Row, Col, Alert, Button } from 'react-bootstrap';
import { Navbar, Nav } from 'react-bootstrap';


function App() {

  const DICE_EMOJIS = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];

  const [dice, setDice] = useState([1, 1, 1, 1, 1]);
  const [held, setHeld] = useState([false, false, false, false, false]);
  const [rollsLeft, setRollsLeft] = useState(3);

  const rollDice = () => {
    if (rollsLeft === 0) return;

    const newDice = dice.map((die, i) => (held[i] ? die : Math.floor(Math.random() * 6) + 1));
    setDice(newDice);
    setRollsLeft(r => r - 1);
  };

  const toggleHold = (index) => {
    const newHeld = [...held];
    newHeld[index] = !newHeld[index];
    setHeld(newHeld);
  };

  const startNewTurn = () => {
    setHeld([false, false, false, false, false]);
    setRollsLeft(3);
    setDice([1, 1, 1, 1, 1]); // optional: clear values for visual feedback
  };


  return (
      <>
      <Navbar bg="dark" variant="dark" expand="lg" fixed="top">
        <Container>
          <Navbar.Brand href="#">Yahtzee</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="#" onClick={startNewTurn}>New Game</Nav.Link>
              <Nav.Link href="#">Rules</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      <Container className="text-center pt-3">
        <h1>Yahtzee for Time Travelers</h1>

        <Row className="mb-4">
          {dice.map((value, idx) => (
            <Col key={idx}>
              <div
                className={`border rounded p-3 display-1 ${held[idx] ? 'bg-warning' : 'bg-light'}`}
                style={{ width: '80px', margin: '0 auto', cursor: 'pointer' }}
                onClick={() => toggleHold(idx)}
              >
                {DICE_EMOJIS[value - 1]}
              </div>
            </Col>
          ))}
        </Row>

        <Button
          variant="primary"
          onClick={rollDice}
          disabled={rollsLeft === 0}
          className="me-2"
        >
          Roll Dice
        </Button>

        <Button
          variant="secondary"
          onClick={startNewTurn}
        >
          New Turn
        </Button>

        <Row className="mb-4 pt-3">
        <h4 className="mb-3">Rolls left: {rollsLeft}</h4>
        </Row>

      </Container>
    </>

  );
}

export default App;

