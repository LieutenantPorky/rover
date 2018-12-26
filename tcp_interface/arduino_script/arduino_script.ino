
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int readSerial = Serial.read();
  // print out the value you read:
    if (readSerial != -1) {
    Serial.print(char(readSerial));
  };
  delay(100);        // delay in between reads for stability
}
