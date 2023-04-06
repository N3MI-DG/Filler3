/*
    Filler3 open source can filler
    Copyright (C) 2023  David Gray https://github.com/N3MI-DG

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

#include <Arduino.h>
#include <Servo.h>
#include <AccelStepper.h>

#include "UserConfig.h"

Servo servo;
AccelStepper stepper(AccelStepper::DRIVER, STEPPER_STEP, STEPPER_DIR);

enum states {
    MOVE_HOME,
    HOME,
    MOVE_PRE_PURGE,
    PRE_PURGE,
    MOVE_FILL,
    FILLING,
    MOVE_POST_PURGE,
    POST_PURGE
};

states fillerState     = MOVE_HOME;
int currentDestination = 0;
int previousPress      = 0;
int ledValue           = 0;
int ledPrevious        = 0;
int ledPeriod          = 10;
int ledTime            = ledPeriod - 1;

// Pre defined led breathe values because fancy math is expensive
float ledArray[360] = {
0.00, 0.02, 0.08, 0.17, 0.31, 0.48, 0.70, 0.95, 1.24, 1.56, 1.93, 2.33, 2.78, 3.26, 3.77, 4.33, 4.92, 5.55, 
6.22, 6.92, 7.66, 8.44, 9.25, 10.10, 10.98, 11.90, 12.85, 13.84, 14.87, 15.92, 17.01, 18.14, 19.30, 20.49, 
21.71, 22.97, 24.26, 25.57, 26.92, 28.30, 29.71, 31.15, 32.62, 34.12, 35.64, 37.20, 38.78, 40.39, 42.02, 
43.68, 45.37, 47.08, 48.81, 50.57, 52.35, 54.16, 55.98, 57.83, 59.70, 61.59, 63.50, 65.43, 67.38, 69.34, 
71.33, 73.33, 75.34, 77.38, 79.43, 81.49, 83.56, 85.65, 87.76, 89.87, 91.99, 94.13, 96.28, 98.43, 100.60, 
102.77, 104.95, 107.13, 109.33, 111.52, 113.73, 115.93, 118.14, 120.35, 122.57, 124.78, 127.00, 129.22, 131.43, 
133.65, 135.86, 138.07, 140.28, 142.48, 144.67, 146.87, 149.05, 151.23, 153.40, 155.57, 157.72, 159.87, 162.01, 
164.13, 166.25, 168.35, 170.44, 172.51, 174.58, 176.62, 178.66, 180.67, 182.67, 184.66, 186.62, 188.57, 190.50, 
192.41, 194.30, 196.17, 198.02, 199.84, 201.65, 203.43, 205.19, 206.92, 208.63, 210.32, 211.98, 213.61, 215.22, 
216.80, 218.36, 219.88, 221.38, 222.85, 224.29, 225.70, 227.08, 228.43, 229.75, 231.03, 232.29, 233.51, 234.70, 
235.86, 236.99, 238.08, 239.13, 240.16, 241.15, 242.10, 243.02, 243.90, 244.75, 245.56, 246.34, 247.08, 247.78, 
248.45, 249.08, 249.67, 250.23, 250.75, 251.22, 251.67, 252.07, 252.44, 252.76, 253.05, 253.30, 253.52, 253.69, 
253.83, 253.92, 253.98, 254.00, 253.98, 253.92, 253.83, 253.69, 253.52, 253.30, 253.05, 252.76, 252.44, 252.07, 
251.67, 251.22, 250.74, 250.23, 249.67, 249.08, 248.45, 247.78, 247.08, 246.34, 245.56, 244.75, 243.90, 243.02, 
242.10, 241.15, 240.16, 239.13, 238.08, 236.99, 235.86, 234.70, 233.51, 232.29, 231.03, 229.75, 228.43, 227.08, 
225.70, 224.29, 222.85, 221.38, 219.88, 218.36, 216.80, 215.22, 213.61, 211.98, 210.32, 208.63, 206.92, 205.19, 
203.43, 201.65, 199.84, 198.02, 196.17, 194.30, 192.41, 190.50, 188.57, 186.62, 184.66, 182.67, 180.67, 178.66, 
176.62, 174.57, 172.51, 170.44, 168.35, 166.25, 164.13, 162.01, 159.87, 157.72, 155.57, 153.40, 151.23, 149.05, 
146.87, 144.67, 142.48, 140.27, 138.07, 135.86, 133.65, 131.43, 129.22, 127.00, 124.78, 122.57, 120.35, 118.14, 
115.93, 113.72, 111.52, 109.32, 107.13, 104.95, 102.77, 100.60, 98.43, 96.28, 94.13, 91.99, 89.87, 87.75, 85.65, 
83.56, 81.49, 79.42, 77.38, 75.34, 73.33, 71.33, 69.34, 67.38, 65.43, 63.50, 61.59, 59.70, 57.83, 55.98, 54.16, 
52.35, 50.57, 48.81, 47.08, 45.37, 43.68, 42.02, 40.39, 38.78, 37.20, 35.64, 34.12, 32.62, 31.15, 29.71, 28.30, 
26.92, 25.57, 24.25, 22.97, 21.71, 20.49, 19.30, 18.14, 17.01, 15.92, 14.87, 13.84, 12.85, 11.90, 10.98, 10.10, 
9.25, 8.44, 7.66, 6.92, 6.22, 5.55, 4.92, 4.33, 3.77, 3.25, 2.78, 2.33, 1.93, 1.56, 1.24, 0.95, 0.70, 0.48, 0.31, 
0.17, 0.08, 0.02
};


// Set direction based on REVERSE_STEPPER variable
void setDestination(int pos) {
    if (REVERSE_STEPPER) { currentDestination = -pos; }
    else                 { currentDestination =  pos; }
}


// End stop function
void setHome() {
    if (fillerState == MOVE_HOME) {
        fillerState = HOME;
        stepper.setCurrentPosition(0);
    }
}


// User button interrupt function
void userButton() {
    if ((millis() - previousPress) > BUTTON_DEBOUNCE) {
        // Move to pre purge if at home position while user button pressed
        if ( fillerState == HOME) { fillerState = MOVE_PRE_PURGE; }

        // Activate emergency stop is user button is pressed while not at home position
        else {
            servo.write(SERVO_POS_IDLE);       // Move servo to idle position
            digitalWrite(PURGE_SOLENOID, LOW); // Disable solenoid
            fillerState = MOVE_HOME;           // Change back to default state

            HAL_NVIC_SystemReset();            // Reset the device (Nasty but it works)
        }
    }

    previousPress = millis();
}


// LED filling timer function
void ledBreathe(void) {
    if (fillerState == FILLING) {
        ledTime++;

        if (ledTime == ledPeriod) {

            if      (ledValue == 0)   { ledValue++;             ledPrevious = 0; }
            else if (ledValue == 360) { ledValue = 0;                            }
            else                      { ledPrevious = ledValue; ledValue++;      }

            analogWrite(USER_LED, ledArray[ledValue]);
            ledTime = 0;
        }
    }

    else { analogWrite(USER_LED, 255); }
}


void setup() {
    servo.attach(SERVO_SIGNAL);  // Attach servo
    servo.write(SERVO_POS_IDLE); // Move servo to idle position

    // Setup IO
    pinMode(END_STOP,       INPUT);
    pinMode(USER_BUTTON,    INPUT);
    pinMode(FILL_SENSOR,    INPUT);
    pinMode(USER_LED,       OUTPUT);
    pinMode(STEPPER_ENABLE, OUTPUT);
    pinMode(PURGE_SOLENOID, OUTPUT);

    digitalWrite(PURGE_SOLENOID, LOW); // Disable solenoid
    digitalWrite(STEPPER_ENABLE, LOW); // Enable stepper motor

    // Set stepper speeds
    stepper.setMaxSpeed(STEPPER_MAX_SPEED);
    stepper.setAcceleration(STEPPER_ACCELERATION);

    // Setup and attach User button timer interrupt
    TIM_TypeDef   *userInstance = TIM1;
    uint32_t       userChannel  = 3;
    HardwareTimer *userTimer    = new HardwareTimer(userInstance);

    userTimer->setMode(userChannel, TIMER_INPUT_CAPTURE_FALLING, USER_BUTTON);
    userTimer->attachInterrupt(userChannel, userButton);
    userTimer->resume();

    // Setup and attach LED timer
    TIM_TypeDef   *ledInstance = TIM2;
    HardwareTimer *ledTimer    = new HardwareTimer(ledInstance);

    ledTimer->setOverflow(10, HERTZ_FORMAT);
    ledTimer->attachInterrupt(ledBreathe);
    ledTimer->resume();

}


void loop() {
    switch(fillerState) {
        case MOVE_HOME:
            if (!stepper.run()) {
                stepper.setCurrentPosition(FILL_POSITION - 750); // Assume machine starts at its limit (fill position - a little bit)
                setDestination(50);                              // Set destination just a little past home
                stepper.moveTo(currentDestination);              // Start moving home
            }

            if (digitalRead(END_STOP) == END_STOP_TRIGGER) { setHome();     }
            else                                           { stepper.run(); }

            break;

        case HOME:
            break;

        case MOVE_PRE_PURGE:
            // If Idle, start moving
            if (!stepper.run()) {
                setDestination(PRE_PURGE_POSITION);
                stepper.moveTo(currentDestination);
            }

            // When destination reached, change state to pre purge
            if (stepper.currentPosition() == currentDestination) { fillerState = PRE_PURGE; }

            stepper.run();
            break;

        case PRE_PURGE:
            digitalWrite(PURGE_SOLENOID, HIGH); // Open Solenoid
            delay(PRE_PURGE_DURATION);          // Wait for pre purge
            digitalWrite(PURGE_SOLENOID, LOW);  // Close solenoid

            fillerState = MOVE_FILL;            // Change state to move fill
            break;

        case MOVE_FILL:
            // If Idle, start moving
            if (!stepper.run()) {
                setDestination(FILL_POSITION);
                stepper.moveTo(currentDestination);
            }

            // When destination reached, change state to filling
            if (stepper.currentPosition() == currentDestination) { fillerState = FILLING; }

            stepper.run();
            break;

        case FILLING:
            // While filling continuously poll sensor
            if (servo.read() >= SERVO_POS_FILL) {

                // When full
                if (analogRead(FILL_SENSOR) < SENSOR_TRIGGER) {
                    servo.write(SERVO_POS_IDLE);  // Return servo to idle position

                    if (POST_PURGE_DURATION > 0) { fillerState = MOVE_POST_PURGE; }
                    else                         {
                        fillerState = MOVE_HOME;
                        setDestination(50);                 // Set destination just a little past home
                        stepper.moveTo(currentDestination); // Start moving home
                        }
                }
            }

            else { servo.write(SERVO_POS_FILL); } // Move servo to fill position and start filling

            break;
    
        case MOVE_POST_PURGE:
            // If Idle, start moving
            if (!stepper.run()) {
                setDestination(POST_PURGE_POSITION);
                stepper.moveTo(currentDestination);
            }

            // When destination reached, change state to post purge
            if (stepper.currentPosition() == currentDestination) { fillerState = POST_PURGE; }

            stepper.run();
            break;

        case POST_PURGE:
            digitalWrite(PURGE_SOLENOID, HIGH); // Open solenoid
            delay(POST_PURGE_DURATION);         // Wait for post purge
            digitalWrite(PURGE_SOLENOID, LOW);  // Close solenoid

            fillerState = MOVE_HOME;            // Change state to move home
            setDestination(50);                 // Set destination just a little past home
            stepper.moveTo(currentDestination); // Start moving home
            break;

    }
}