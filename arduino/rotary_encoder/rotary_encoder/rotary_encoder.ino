#include <RotaryEncoder.h>

// Setup a RoraryEncoder for pins A2 and A3:
RotaryEncoder encoder(A2, A3);

int leftTurnPin = A1;
int rightTurnPin = A0;

void setup()
{
  Serial.begin(57600);
  Serial.println("SimplePollRotator example for the RotaryEncoder library.");

  // You may have to modify the next 2 lines if using other pins than A2 and A3
  PCICR |= (1 << PCIE1);    // This enables Pin Change Interrupt 1 that covers the Analog input pins or Port C.
  PCMSK1 |= (1 << PCINT10) | (1 << PCINT11);  // This enables the interrupt for pin 2 and 3 of Port C.

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
  static int pos = 0;
  int newPos = encoder.getPosition();
  if (pos != newPos) {
    // show state on led
    if(newPos > pos) {
      Serial.print("Right turn");
      digitalWrite(rightTurnPin, HIGH);
      digitalWrite(rightTurnPin, LOW);
    } else {
      Serial.print("Left turn");
      digitalWrite(leftTurnPin, HIGH);
      digitalWrite(leftTurnPin, LOW);  
    }
    
    // print to serial
    Serial.print(pos);
    Serial.print(newPos);
    Serial.println();
    pos = newPos;
  }
} 

