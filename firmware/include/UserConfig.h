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

/* Pins */
// EBB42 https://raw.githubusercontent.com/bigtreetech/EBB/master/EBB%20CAN%20V1.1%20(STM32G0B1)/EBB42%20CAN%20V1.1/Hardware/EBB42%20CAN%20V1.1%26V1.2-PIN.png
// EBB36 https://raw.githubusercontent.com/bigtreetech/EBB/master/EBB%20CAN%20V1.1%20(STM32G0B1)/EBB36%20CAN%20V1.1/Hardware/EBB36%20CAN%20V1.1%26V1.2-PIN.png

#define END_STOP             PB8
#define USER_BUTTON          PB6
#define USER_LED             PA1 // FAN1 PA0, FAN2 PA1
#define FILL_SENSOR          PA3

#define PURGE_SOLENOID       PA2 // EBB V1.1 PA2, EBBV1.2 PB13
#define SERVO_SIGNAL         PB9
#define STEPPER_STEP         PD0
#define STEPPER_DIR          PD1
#define STEPPER_ENABLE       PD2


/* Variables */
#define BUTTON_DEBOUNCE      200    // Debounce in ms
#define SENSOR_TRIGGER       400    // Analog trigger between 0 to 4095 (lower is more sensitive)
#define PRE_PURGE_DURATION   3000   // Pre purge duration in ms
#define POST_PURGE_DURATION  0      // Post purge duration in ms
#define PRE_PURGE_POSITION   -10550 // Relative steps from end stop to pre purge position
#define POST_PURGE_POSITION  -3000  // Relative steps from end stop to post purge position
#define FILL_POSITION        -10800 // Relative steps from end stop to filling position
#define SERVO_POS_IDLE       0      // Servo position while idle
#define SERVO_POS_FILL       60     // Servo position while filling
#define STEPPER_MAX_SPEED    10000  // Stepper max speed in steps per second
#define STEPPER_ACCELERATION 24000  // Stepper acceleration in steps per second per second
#define REVERSE_STEPPER      false  // Reverse stepper direction
#define END_STOP_TRIGGER     HIGH   // End stop trigger state (NO = HIGH, NC = LOW)
#define PURGE_TRAVEL_MOVES   true   // Continue to purge while moving to the next position after purge position
#define POSITIVE_PRESSURE    false  // After filling the gantry will stay at the fill position until user button is pressed
