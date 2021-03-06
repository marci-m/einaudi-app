long randNumber;
void setup()
{
  Serial.begin(9600);
}
void loop()
{
  randNumber = random(10, 25);
  Serial.println(randNumber);
  delay(800);
}
