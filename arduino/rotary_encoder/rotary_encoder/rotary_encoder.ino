#include <RotaryEncoder.h>

// Setup a RoraryEncoder for pins A2 and A3:
RotaryEncoder encoder(A2, A3);

int leftTurnPin = A1;
int rightTurnPin = A0;

const int buttonPin1 = 12;
const int buttonPin2 = 13;

void setup()
{
  Serial.begin(9600);

  // You may have to modify the next 2 lines if using other pins than A2 and A3
  PCICR |= (1 << PCIE1);    // This enables Pin Change Interrupt 1 that covers the Analog input pins or Port C.
  PCMSK1 |= (1 << PCINT10) | (1 << PCINT11);  // This enables the interrupt for pin 2 and 3 of Port C.

  // rotary encoder pins
  pinMode(leftTurnPin, OUTPUT);
  pinMode(rightTurnPin, OUTPUT);
}

// The Interrupt Service Routine for Pin Change Interrupt 1
// This routine will only be called on any signal change on A2 and A3: exactly where we need to check.
ISR(PCINT1_vect) {
  encoder.tick(); // just call tick() to check the state.
}


// Read the current position of the encoder and print out when changed.
void loop()
{
  processRotaryEncoderState();
} 

void processRotaryEncoderState() {
  static int pos = 0;
  int newPos = encoder.getPosition();
  if (pos != newPos) {
    if(newPos > pos) {
      // "Right turn"
      digitalWrite(rightTurnPin, HIGH);
      digitalWrite(rightTurnPin, LOW);
      Serial.println(99, DEC);
    } else {
      // "Left turn"
      digitalWrite(leftTurnPin, HIGH);
      digitalWrite(leftTurnPin, LOW);  
      Serial.println(66, DEC);
    }
    pos = newPos;
  }
}

