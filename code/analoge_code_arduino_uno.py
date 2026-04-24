int buttonPin = 13; //pins ingeven
int ledPin_1 = 2;
int ledPin_2 = 3;
int ledPin_3 = 4;
int ledPin_4 = 5;
int ledPin_5 = 6;
int ledPin_6 = 7;

bool led_1Aan = false; //onthoud of de LED aan of uit is
bool led_2Aan = false;
bool led_3Aan = false;
bool led_4Aan = false;
bool led_5Aan = false;
bool led_6Aan = false;

int wachtTijd = 750; //wachttijd makkelijk veranderen van leds

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin_1, OUTPUT);
  pinMode(ledPin_2, OUTPUT);
  pinMode(ledPin_3, OUTPUT);
  pinMode(ledPin_4, OUTPUT);
  pinMode(ledPin_5, OUTPUT);
  pinMode(ledPin_6, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(115200);
  randomSeed(analogRead(0));
  analogWrite(ledPin_1, LOW); //led initieel uit
  analogWrite(ledPin_2, LOW);
  analogWrite(ledPin_3, LOW);
  analogWrite(ledPin_4, LOW);
  analogWrite(ledPin_5, LOW);
  analogWrite(ledPin_6, LOW);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  // if button is pressed, random amout of leds between 1-6 light up
  int pinVal = analogRead(buttonPin);
  //Serial.println(pinVal);
  int randomNumber=0;
  if ((pinVal) == 0) {
    randomNumber = random(1, 7);
    Serial.println(randomNumber);
    delay(250);
  }

  //okay

  //aatal leds gelijk aan radomNumber laten oplichtn

  if (randomNumber == 1){
    analogWrite(ledPin_1, HIGH);  //led aan
    delay(wachtTijd);            // wachten
    analogWrite(ledPin_1, LOW); //led uit
  }
  if (randomNumber ==2){
    analogWrite(ledPin_1, HIGH);  //led aan
    analogWrite(ledPin_2,HIGH);
    delay(wachtTijd);            // wachten
    analogWrite(ledPin_1, LOW);
    analogWrite(ledPin_2,LOW);
  }
  if (randomNumber == 3){
    analogWrite(ledPin_1, HIGH);  //led aan
    analogWrite(ledPin_2,HIGH);
    analogWrite(ledPin_3,HIGH);
    delay(wachtTijd);
    analogWrite(ledPin_1, LOW);
    analogWrite(ledPin_2,LOW);
    analogWrite(ledPin_3,LOW);
  }
  if (randomNumber == 4){
    analogWrite(ledPin_1, HIGH);  //led aan
    analogWrite(ledPin_2,HIGH);
    analogWrite(ledPin_3,HIGH);
    analogWrite(ledPin_4,HIGH);
    delay(wachtTijd);
    analogWrite(ledPin_1, LOW);
    analogWrite(ledPin_2,LOW);
    analogWrite(ledPin_3,LOW);
    analogWrite(ledPin_4,LOW);
  }
  if (randomNumber==5){
    analogWrite(ledPin_1, HIGH);  //led aan
    analogWrite(ledPin_2,HIGH);
    analogWrite(ledPin_3,HIGH);
    analogWrite(ledPin_4,HIGH);
    analogWrite(ledPin_5,HIGH);
    delay(wachtTijd);
    analogWrite(ledPin_1, LOW);
    analogWrite(ledPin_2,LOW);
    analogWrite(ledPin_3,LOW);
    analogWrite(ledPin_4,LOW);
    analogWrite(ledPin_5,LOW);
  }
  if (randomNumber == 6){
    analogWrite(ledPin_1, HIGH);  //led aan
    analogWrite(ledPin_2,HIGH);
    analogWrite(ledPin_3,HIGH);
    analogWrite(ledPin_4,HIGH);
    analogWrite(ledPin_5,HIGH);
    analogWrite(ledPin_6,HIGH);
    delay(wachtTijd);
    analogWrite(ledPin_1, LOW);
    analogWrite(ledPin_2,LOW);
    analogWrite(ledPin_3,LOW);
    analogWrite(ledPin_4,LOW);
    analogWrite(ledPin_5,LOW);
    analogWrite(ledPin_6,LOW);
  }

  //ok
  
}


