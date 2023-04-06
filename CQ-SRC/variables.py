# Filler3 open source can filler
# Copyright (C) 2023  David Gray https://github.com/N3MI-DG
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

extrusion_xy           = 20
extrusion_z_offset     = 20    # 0 to bottom of extrusion
extrusion_length       = 500
car_z_offset           = 285   # 0 to center of MGN12H carriage
car_mount_z            = 45.4
car_mount_x            = 27
car_mount_y            = 11.5+6
filler_mount_car_y     = 7.5
filler_mount_car_x_pos = 30
filler_mount_car_x_neg = -27
can_dia                = 66.3
can_dia_small          = 51
can_small_height       = 7
can_height             = 170
can_y_offset           = -60   # 0 to center of can
can_side_wall          = 5
can_front_wall         = 15
filler_car_z_offset    = 22.5  # Bottom of trigger to top of MGN12H carriage
servo_x_offset         = 11.5  # Center of filler to center of servo
servo_y_offset         = 47.25 #46.25 # Center of filler to bottom/back of servo
servo_z_offset         = -10.5 # Bottom of trigger to center of servo shaft
rail_length            = 400   # Overall length of rail
rail_y_offset          = 15.5  # 0 to center of rail
rail_z_offset          = 90    # 0 to bottom of rail
motor_thick            = 20
motor_width            = 42.3
motor_y_offset         = 30    # 0 to face of motor
motor_z_offset         = (motor_width/2) + 5    # 0 to center of motor shaft
motor_counter_bore     = 4.5
solenoid_x_offset      = 45
solenoid_y_offset      = motor_thick + 10
solenoid_z_offset      = 55
solenoid_x_thick       = 22.2
solenoid_y_thick       = 30.2
solenoid_wall_thick    = 12
liquid_nut_correction  = 1.5
pcb_x_offset           = -43
pcb_y_offset           = (42/2)-12
pcb_z_offset           = motor_z_offset
big_hole_dia           = 5.6
big_screw_head_dia     = 10.5
small_hole_dia         = 3.4
small_screw_head_dia   = 6.5
thread_insert_dia      = 4.6
mount_tol              = 0.1
mount_pcb_s            = 6
mount_b_x              = motor_width
mount_b_y              = 20 + (mount_tol*2)
mount_s_x              = mount_b_x/2 - 10
mount_s_z              = motor_width+(motor_z_offset-(motor_width/2))
mount_f_y              = 3 + 4
mount_f_x              = mount_b_x+(mount_tol*2)+mount_pcb_s

mount_motor_points     = [
    ( 31/2, motor_z_offset+31/2),
    ( 31/2, motor_z_offset-31/2),
    (-31/2, motor_z_offset+31/2),
    (-31/2, motor_z_offset-31/2)
]

base_wall_thick  = 2
power_x_offset   = (motor_width/2)+((solenoid_x_offset-(solenoid_x_thick/2)-(motor_width/2))/2)
button_x_offset  = solenoid_x_offset + (solenoid_x_thick/2) + base_wall_thick
button_y_offset  = -2
button_z_offset  = 35
estop_x_offset   = 10
estop_y_offset   = 18.5
estop_z_offset   = -3.35
pulley_y_offset  = 33
pulley_z_offset  = -3

car_mount_points = [
    ( 10,  10),
    ( 10, -10),
    (-10,  10),
    (-10, -10)
]

servo_screw_points = [
    (25.5,  (car_mount_z/2)-10.25+5),
    (25.5,  (car_mount_z/2)-10.25-5),
    (-22.5, (car_mount_z/2)-10.25+5),
    (-22.5, (car_mount_z/2)-10.25-5)
        ]

filler_dia       = 9.7
filler_bodge     = 2.5
filler_y_offset  = -(abs(can_y_offset)+filler_bodge)
sensor_x_offset  = 20
sensor_length    = 132
foot_height      = 7
print_color      = "gray20"
print_flex_color = "gray30"
fastener_color   = "lightgray"
nutsert_color    = "lightgoldenrod"
tube_cut_length  = 70
