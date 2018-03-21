#include <RotaryEncoder.h>

// Setup a RoraryEncoder for pins A2 and A3:
RotaryEncoder encoder(A2, A3);

const int rotaryRightMsg = 66;
const int rotaryLeftMsg = 99;

// button for rotary encoder
const int buttonPin1 = A1;
int buttonState1;             // the current reading from the input pin
int lastButtonState1 = LOW;   // the previous reading from the input pin
unsigned long lastDebounceTime1 = 0;  // the last time the output pin was toggled

// button "TA" on the radio
const int buttonPin2 = A0;
int buttonState2;             // the current reading from the input pin
int lastButtonState2 = LOW;   // the previous reading from the input pin
unsigned long lastDebounceTime2 = 0;  // the last time the output pin was toggled

// button "LW" on the radio
const int buttonPin3 = 13;
int buttonState3;             // the current reading from the input pin
int lastButtonState3 = LOW;   // the previous reading from the input pin
unsigned long lastDebounceTime3 = 0;  // the last time the output pin was toggled

// button "MW" on the radio
const int buttonPin4 = 12;
int buttonState4;             // the current reading from the input pin
int lastButtonState4 = LOW;   // the previous reading from the input pin
unsigned long lastDebounceTime4 = 0;  // the last time the output pin was toggled

// button "UW" on the radio
const int buttonPin5 = 11;
int buttonState5;             // the current reading from the input pin
int lastButtonState5 = LOW;   // the previous reading from the input pin
unsigned long lastDebounceTime5 = 0;  // the last time the output pin was toggled

// button "BASS" on the radio
const int buttonPin6 = 10;
int buttonState6;             // the current reading from the input pin
int lastButtonState6 = LOW;   // the previous reading from the input pin
unsigned long lastDebounceTime6 = 0;  // the last time the output pin was toggled

// button "BASS" on the radio
const int buttonPin7 = 9;
int buttonState7;             // the current reading from the input pin
int lastButtonState7 = LOW;   // the previous reading from the input pin
unsigned long lastDebounceTime7 = 0;  // the last time the output pin was toggled

// button "BASS" on the radio
const int buttonPin8 = 8;
int buttonState8;             // the current reading from the input pin
int lastButtonState8 = LOW;   // the previous reading from the input pin
unsigned long lastDebounceTime8 = 0;  // the last time the output pin was toggled

// button "BASS" on the radio
const int buttonPin9 = 7;
int buttonState9;             // the current reading from the input pin
int lastButtonState9 = LOW;   // the previous reading from the input pin
unsigned long lastDebounceTime9 = 0;  // the last time the output pin was toggled

unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers

void setup()
{
  Serial.begin(9600);

  // You may have to modify the next 2 lines if using other pins than A2 and A3
  PCICR |= (1 << PCIE1);    // This enables Pin Change Interrupt 1 that covers the Analog input pins or Port C.
  PCMSK1 |= (1 << PCINT10) | (1 << PCINT11);  // This enables the interrupt for pin 2 and 3 of Port C.

  // button pins
  pinMode(buttonPin1, INPUT);
  digitalWrite(buttonPin1, HIGH);
  pinMode(buttonPin2, INPUT);
  digitalWrite(buttonPin2, HIGH);
//  pinMode(buttonPin3, INPUT);
//  digitalWrite(buttonPin3, HIGH);
//  pinMode(buttonPin4, INPUT);
//  digitalWrite(buttonPin4, HIGH);
//  pinMode(buttonPin5, INPUT);
//  digitalWrite(buttonPin5, HIGH);
//  pinMode(buttonPin6, INPUT);
//  digitalWrite(buttonPin6, HIGH);
//  pinMode(buttonPin7, INPUT);
//  digitalWrite(buttonPin7, HIGH);
//  pinMode(buttonPin8, INPUT);
//  digitalWrite(buttonPin8, HIGH);
//  pinMode(buttonPin9, INPUT);
//  digitalWrite(buttonPin9, HIGH);
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
  processButtonState(&buttonPin1, &buttonState1, &lastButtonState1, &lastDebounceTime1);
  processButtonState(&buttonPin2, &buttonState2, &lastButtonState2, &lastDebounceTime2);
//  processButtonState(&buttonPin3, &buttonState3, &lastButtonState3, &lastDebounceTime3);
//  processButtonState(&buttonPin4, &buttonState4, &lastButtonState4, &lastDebounceTime4);
//  
//  processButtonState(&buttonPin5, &buttonState5, &lastButtonState5, &lastDebounceTime5);
//  processButtonState(&buttonPin6, &buttonState6, &lastButtonState6, &lastDebounceTime6);
//  processButtonState(&buttonPin7, &buttonState7, &lastButtonState7, &lastDebounceTime7);
//  processButtonState(&buttonPin8, &buttonState8, &lastButtonState8, &lastDebounceTime8);
//  processButtonState(&buttonPin9, &buttonState9, &lastButtonState9, &lastDebounceTime9);
} 

void processRotaryEncoderState() {
  static int pos = 0;
  int newPos = encoder.getPosition();
  if (pos != newPos) {
    if(newPos > pos) {
      // "Right turn"
      Serial.println(rotaryRightMsg, DEC);
    } else {
      // "Left turn"
      Serial.println(rotaryLeftMsg, DEC);
    }
    pos = newPos;
  }
}

void processButtonState(const int *buttonPin, int *buttonState, int *lastButtonState, unsigned long *lastDebounceTime) {
  // read the state of the switch into a local variable:
  int reading = digitalRead(*buttonPin);

  // check to see if you just pressed the button
  // (i.e. the input went from LOW to HIGH),  and you've waited
  // long enough since the last press to ignore any noise:

  // If the switch changed, due to noise or pressing:
  if (reading != *lastButtonState) {
    // reset the debouncing timer
    *lastDebounceTime = millis();
  }

  if ((millis() - *lastDebounceTime) > debounceDelay) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:

    // if the button state has changed:
    if (reading != *buttonState) {
      *buttonState = reading;

      // only toggle the LED if the new button state is HIGH
      if (*buttonState == HIGH) {
        Serial.println(*buttonPin, DEC);
      }
    }
  }

  // save the reading.  Next time through the loop,
  // it'll be the lastButtonState:
  *lastButtonState = reading;

}

