#include <Servo.h>
#include <string.h>

Servo horizontal;
Servo vertical;

String incomingByte = ""; // for incoming serial data
float horizAngle = 90;
float vertAngle = 90;

void setup() {
  Serial.begin(115200); // opens serial port, sets data rate to 9600 bps
  horizontal.attach(8);
  horizontal.write(horizAngle);
  vertical.attach(9);
  vertical.write(vertAngle);
}

void eraseSubStr(String & mainStr, const String & toErase) {
	// Search for the substring in string
	size_t pos = mainStr.indexOf(toErase);
  size_t npos = -1;

	if (pos != npos)
	{
		// If found then erase it from string
		mainStr.remove(pos, toErase.length());
	}
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:

    String servo = Serial.readStringUntil('\n');
    String readFloat = Serial.readString();
    float amount = readFloat.toFloat();
    
//    incomingByte = Serial.readString();
//    String amount = incomingByte;
//    String servo = incomingByte;
//    eraseSubStr(amount, "servo1 ");
//    eraseSubStr(amount, "servo2 ");
//    eraseSubStr(servo, amount);
//    eraseSubStr(servo, " ");

    if (servo == "servo1") {
      if ((horizAngle < 180) and (horizAngle > -180)) {
        horizontal.write(amount + horizAngle);
        horizAngle = amount + horizAngle;
      }
    }

    else if (servo == "servo2") {
      if ((vertAngle < 180) and (vertAngle > -180)) {
        vertical.write(amount + vertAngle);
        vertAngle = amount + vertAngle;
      }
    }


//     // say what you got:
//     Serial.print("I received: ");
//     Serial.println(incomingByte, DEC);
  }
}
