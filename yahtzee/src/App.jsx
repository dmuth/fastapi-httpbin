// src/App.jsx
import './App.css';
import './Dice.css';

import { useState } from 'react';
import { Container, Row, Col, Alert, Button } from 'react-bootstrap';
import { Navbar, Nav } from 'react-bootstrap';

import Die from './Die';
import Scorecard from './Scorecard';
import { useGameState } from './useGameState';


function App() {
  
  const {
    dice,
    held,
    rollsLeft,
    rollDice,
    toggleHold,
    startNewTurn
  } = useGameState();

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

      <Container className="text-center pt-3 mt-3">
        <h1>Yahtzee for Time Travelers</h1>

        <Row className="mb-4 justify-content-center">
          {dice.map((value, idx) => (
            <Col key={idx} xs="auto"  >
              <div
                className={`die_border rounded p-2 ${held[idx] ? 'dice-held' : ''}`}
                onClick={() => toggleHold(idx)}
              >
                <Die
                  value={value}
                  held={held[idx]}
                  onClick={() => toggleHold(idx)}
                  />
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

      <Scorecard />

    </>

  );
}

export default App;

