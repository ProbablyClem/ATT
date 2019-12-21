bool lu = false;

void setup() {
  pinMode(8, INPUT_PULLUP);
  pinMode(9, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if ((digitalRead(8) == LOW) && (lu == false )){
    Serial.print(0);
    lu = true;
  }
  else if ((digitalRead(9) == LOW) && (lu == false)) {
    Serial.print(1);
    lu = true;
  }
  if ((digitalRead(8) == HIGH) && (digitalRead(9) == HIGH)) {
    lu = false;
  }
  delay(25);
   
}
