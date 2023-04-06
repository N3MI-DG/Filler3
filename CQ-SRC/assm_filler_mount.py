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

import cadquery as cq
from parts import *

def makeFillerMount():
    filler_mount_assm = (
        cq.Assembly(name="Filler Mount")

        .add(
            cq.Workplane().filler_mount(front=True, left=False, right=False),
            name="Filler_Mount_Front_Print",
            color=cq.Color(print_color)
        )

        .add(
            cq.Workplane().filler_mount(front=False, left=True, right=False),
            name="Filler_Mount_left_Print",
            color=cq.Color(print_color)
        )

        .add(
            cq.Workplane().filler_mount(front=False, left=False, right=True),
            name="Filler_Mount_right_Print",
            color=cq.Color(print_color)
        )

        .add(
            cq.Workplane().carriage(),
            name="Carriage_Print",
            color=cq.Color(print_color)
        )

        .add(
            # https://www.aliexpress.com/item/1005004556540857.html
            # MG996R - 180 Degrees
            # All Metal
            cq.Workplane().MG996R_servo(arm=False),
            name="MG996R_Servo",
            color=cq.Color('cadetblue3')
        )

        .add(
            cq.Workplane().MG996R_servo(body=True),
            name="Servo_Arm",
            color=cq.Color('tomato2')
        )

        .add(
            cq.Workplane().belt(),
            name="Belt",
            color=cq.Color('wheat4')
        )

        .add(
            (
                cq.Workplane().M3_cap_screw(10)
                .rotate((0, 0, 0), (1, 0, 0), -90)
                .translate((0, filler_y_offset+14, car_z_offset-(car_mount_z/2)+7.8))
            ), 
            name=f"Filler_Tube_M3X10_Cap_Head",
            color=cq.Color(fastener_color)
        )

        .add(
            (
                cq.Workplane().M3_square_nut()
                .rotate((0, 0, 0), (1, 0, 0), 90)
                .translate((0, filler_y_offset+10, car_z_offset-(car_mount_z/2)+7.8))
            ), 
            name=f"Filler_Tube_M3_Square_Nut",
            color=cq.Color(fastener_color)
        )

        .add(
            (
                cq.Workplane().M3_cap_screw(20)
                .rotate((0, 0, 0), (1, 0, 0), -90)
                .translate((sensor_x_offset, filler_y_offset+20, car_z_offset-(car_mount_z/2)+7.8))
            ), 
            name=f"Filler_Tube_M3X20_Cap_Head",
            color=cq.Color(fastener_color)
        )

        .add(
            (
                cq.Workplane().M3_square_nut()
                .rotate((0, 0, 0), (1, 0, 0), 90)
                .translate((sensor_x_offset, filler_y_offset+10, car_z_offset-(car_mount_z/2)+7.8))
            ), 
            name=f"Sensor_M3_Square_Nut",
            color=cq.Color(fastener_color)
        )
    )

    # Carriage Screws
    for i, x in enumerate(car_mount_points):
        filler_mount_assm.add(
            (
                cq.Workplane().M3_cap_screw(20)
                .rotate((0, 0, 0), (1, 0, 0), -90)
                .translate((x[0], rail_y_offset+(car_mount_y/2+filler_mount_car_y/2)+10.2, x[1]+car_z_offset))
            ), 
            name=f"Carriage_M3X20_Cap_Head{i}",
            color=cq.Color(fastener_color)
        )
    
    # Front Mount
    for i, x in enumerate(filler_mount(0, True)):
        # M3x10 Cap Screws
        filler_mount_assm.add(
            (
                cq.Workplane().M3_cap_screw(10)
                .rotate((0, 0, 0), (1, 0, 0), 90)
                .translate((x[0], -66, x[1]))
            ), 
            name=f"Filler_Mount_M3X10_Cap_Head{i}",
            color=cq.Color(fastener_color)
        )

        # M3 Square Nuts
        filler_mount_assm.add(
            (
                cq.Workplane().M3_square_nut()
                .rotate((0, 0, 0), (1, 0, 0), 90)
                .translate((x[0], -66+7.1, x[1]))
            ), 
            name=f"Filler_Mount_M3_Square_Nut{i}",
            color=cq.Color(fastener_color)
        )

    # Servo Mount
    for i, x in enumerate(servo_screw_points):
        # M3x10 Cap Screws
        filler_mount_assm.add(
            (
                cq.Workplane().M3_cap_screw(10)
                .rotate((0, 0, 0), (1, 0, 0), 90)
                .translate((x[0], -48.4, x[1]+car_z_offset))
            ), 
            name=f"Servo_Mount_M3X10_Cap_Head{i}",
            color=cq.Color(fastener_color)
        )

        # M3 Washers
        filler_mount_assm.add(
            (
                cq.Workplane().M3_washer()
                .rotate((0, 0, 0), (1, 0, 0), 90)
                .translate((x[0], -47.8, x[1]+car_z_offset))
            ), 
            name=f"Servo_Mount_M3_Washer{i}",
            color=cq.Color(fastener_color)
        )

        # M3 Square Nuts
        filler_mount_assm.add(
            (
                cq.Workplane().M3_square_nut()
                .rotate((0, 0, 0), (1, 0, 0), 90)
                .translate((x[0], -47.8+6.25, x[1]+car_z_offset))
            ), 
            name=f"Servo_Mount_M3_Square_Nut{i}",
            color=cq.Color(fastener_color)
        )

    return(filler_mount_assm)