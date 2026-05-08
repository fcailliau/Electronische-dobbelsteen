int buttonPin = 13; //pins ingeven

void setup() {
    pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(115200);
  randomSeed(analogRead(0));
}

void loop() {
  // put your main code here, to run repeatedly:
  // if button is pressed, random amout of leds between 1-6 light up
  int pinVal = digitalRead(buttonPin);
  //Serial.println(pinVal);
  int randomNumber=0;
  if ((pinVal) == 0) {
    randomNumber = random(1, 7);
    Serial.println(randomNumber);
    delay(250);
  }
}