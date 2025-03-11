#include <Servo.h>

Servo myservo;
const int trigPin = 48;
const int echoPin = 50;
const int servoPin = 52;
const int enA = 6;
const int in1 = 8;
const int in2 = 9;
const int in3 = 10;
const int in4 = 11;
const int enB = 7;

long duration;
int distance;
int servoPos = 90;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(enB, OUTPUT);
  myservo.attach(servoPin);
  myservo.write(servoPos);
  Serial.begin(9600);
}

void loop() {
  distance = getDistance();
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance < 20) {
    stopRobot();
    delay(500);
    checkDirection();
  } else {
    moveForward();
  }
  delay(50);
}

int getDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2;
}

void moveForward() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enA, 200);
  analogWrite(enB, 200);
}

void stopRobot() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  analogWrite(enA, 0);
  analogWrite(enB, 0);
}

void moveBackward() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(enA, 200);
  analogWrite(enB, 200);
}

void turnLeft() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enA, 200);
  analogWrite(enB, 200);
  delay(500);
  stopRobot();
}

void turnRight() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(enA, 200);
  analogWrite(enB, 200);
  delay(500);
  stopRobot();
}

void checkDirection() {
  int leftDistance, rightDistance;

  myservo.write(170);
  delay(500);
  leftDistance = getDistance();
  delay(100);

  myservo.write(10);
  delay(500);
  rightDistance = getDistance();
  delay(100);

  myservo.write(90);
  delay(500);

  if (leftDistance > rightDistance) {
    turnLeft();
  } else {
    turnRight();
  }
}