// src/App.jsx
import './App.css'; // <- Add this if it’s missing

import { Container, Row, Col, Alert, Button } from 'react-bootstrap';

function App() {
  return (
    <Container className="mt-5">
      <Row className="justify-content-center">
        <Col xs={12} sm={10} md={8} lg={6}>
          <Alert variant="info" className="text-center">
            🎲 <strong>Welcome to Yahtzee!</strong>
          </Alert>
          <div className="d-grid gap-2">
            <Button variant="primary" size="lg">Roll Dice</Button>
          </div>
        </Col>
      </Row>
    </Container>
  );
}

export default App;

