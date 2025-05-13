// src/App.jsx
import './App.css'; // <- Add this if it’s missing

import { useState } from 'react';
import { Container, Row, Col, Alert, Button } from 'react-bootstrap';
import { Navbar, Nav } from 'react-bootstrap';


function App() {

const [dice, setDice] = useState([1, 1, 1, 1, 1]);

  const rollDice = () => {
    const newDice = Array.from({ length: 5 }, () => Math.floor(Math.random() * 6) + 1);
    setDice(newDice);
  };



  return (
    <Container className="text-center pt-5">

    <Navbar bg="dark" variant="dark" expand="lg" className="mb-4 px-3" fixed="top">
    <Navbar.Brand href="#">Yahtzee</Navbar.Brand>
    <Navbar.Toggle aria-controls="basic-navbar-nav" />
    <Navbar.Collapse id="basic-navbar-nav">
      <Nav className="me-auto">
        <Nav.Link href="#">New Game</Nav.Link>
        <Nav.Link href="#">Rules</Nav.Link>
      </Nav>
    </Navbar.Collapse>
    </Navbar>

      <Row className="justify-content-center">
        <h1>Yahtzee for Time Travelers</h1>
        <Col xs={12} sm={10} md={8} lg={6}>
          <Alert variant="info" className="text-center">
            🎲 <strong>Welcome to Yahtzee!</strong>
          </Alert>
<Row className="mb-4">
        {dice.map((value, idx) => (
          <Col key={idx}>
            <div
              className="border rounded p-3 fs-1 bg-light"
              style={{ width: '80px', margin: '0 auto' }}
            >
              {value}
            </div>
          </Col>
        ))}
      </Row>
      <Button variant="primary" onClick={rollDice}>Roll Dice</Button>
        </Col>
      </Row>
    </Container>
  );
}

export default App;

