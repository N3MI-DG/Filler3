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

def makeBase(t=0):
    feet_locations = [
        (52.1, 51.1),
        (-52.1, 51.1),
        (39, -50),
        (-39, -50),
    ]

    base_assm = (
        cq.Assembly(name="Base")

        .add(
            cq.Workplane().base().translate((0, 0, t)),
            name="Base_Print",
            color=cq.Color(print_color)
        )

        .add(
            # https://www.aliexpress.com/item/1005003862203895.html 
            # 12-24V LED Momentary
            # 19mm
            cq.Workplane().button().translate((0, 0, t)),
            name="Button",
            color=cq.Color("skyblue3")
        )

        .add(
            # https://www.kegland.com.au/ball-lock-post-with-1-4-inch-bulkhead-assembly-liquid.html
            # https://www.kegland.com.au/stainless-keg-dip-tube-long-liquid.html
            (
                cq.Workplane().ball_lock()
                .translate((-solenoid_x_offset, solenoid_y_offset+15+solenoid_wall_thick, solenoid_z_offset))
                .translate((0, 0, t))
            ),
            name="Ball_Lock_Liquid",
            color=cq.Color('lightgray')
        )

        .add((
                cq.Workplane().quater_bsp_nut()
                .translate((-solenoid_x_offset, solenoid_y_offset+15, solenoid_z_offset))
                .translate((0, 0, t))
            ),
            name="Ball_Lock_Liquid_Nut",
            color=cq.Color(fastener_color)
        )

        .add((
                cq.Workplane("XZ").cylinder(31, 4)
                .translate((-solenoid_x_offset, solenoid_y_offset-8.5, solenoid_z_offset))
                .translate((0, 0, t))
            ),
            name="Ball_Lock_Liquid_Tube",
            color=cq.Color(fastener_color)
        )

        .add(
            # https://www.kegland.com.au/duotight-8mm-push-in-tee-piece-double-oring-897.html
            (
                cq.Workplane().duo_elbow()
                .translate((-solenoid_x_offset, solenoid_y_offset-3.5, solenoid_z_offset))
                .translate((0, 0, t))
            ),
            name="Liquid_Elbow",
            color=cq.Color("gray60")
        )

        .add((
                cq.Workplane()
                .circle(1.25)
                .revolve(360, (-7,0,0),(-7,-1,0))
                .translate((-solenoid_x_offset+7, solenoid_y_offset+15+solenoid_wall_thick+32.2, solenoid_z_offset))
                .translate((0, 0, t))
            ),
            name="Ball_Lock_Liquid_O_Ring",
            color=cq.Color('gray30')
        )

        .add(
            # https://www.kegland.com.au/ball-lock-post-with-1-4-inch-bulkhead-assembly-gas.html
            (
                cq.Workplane().ball_lock()
                .translate((solenoid_x_offset, solenoid_y_offset+15+solenoid_wall_thick, solenoid_z_offset))
                .translate((0, 0, t))
            ),
            name="Ball_Lock_Gas",
            color=cq.Color('lightgray')
        )

        .add((
                cq.Workplane()
                .circle(1.25)
                .revolve(360, (-7,0,0),(-7,-1,0))
                .translate((solenoid_x_offset+7, solenoid_y_offset+15+solenoid_wall_thick+32.2, solenoid_z_offset))
                .translate((0, 0, t))
            ),
            name="Ball_Lock_Gas_O_Ring",
            color=cq.Color('gray30')
        )

        .add(
            # https://www.aliexpress.com/item/1005003324287626.html
            cq.Workplane().gas_solenoid().translate((0, 0, t)),
            name="Gas Solenoid",
            color=cq.Color('lightblue')
        )

        .add(
            # https://www.aliexpress.com/item/1005001357072469.html
            # PL8-02
            (
                cq.Workplane().threaded_elbow()
                .translate((solenoid_x_offset, solenoid_y_offset-6.5, solenoid_z_offset))
                .translate((0, 0, t))
            ),
            name="Gas_Elbow",
            color=cq.Color("gray60")
        )

        .add(
            # https://www.aliexpress.com/item/4000053061172.html
            cq.Workplane().power_socket().translate((0, 0, t)),
            name="Power_Socket",
            color=cq.Color('lightgray')
        )
    )


    for i, p in enumerate(feet_locations):
        # Feet
        base_assm.add(
            (
                cq.Workplane().foot()
                .rotate((0, 0, 0), (0, 1, 0), 180)
                .translate((p[0], p[1], 0))
                .translate((0, 0, t))
            ), 
            name=f"Foot{i}", 
            color=cq.Color(print_flex_color)
        )

        # Feet Nutserts
        base_assm.add(
            (
                cq.Workplane().M3_nutsert()
                .translate((p[0], p[1], 0))
                .translate((0, 0, t))
            ), 
            name=f"Foot_Nutsert{i}", 
            color=cq.Color(nutsert_color)
        )

        # Feet washers
        base_assm.add(
            (
                cq.Workplane().M3_washer()
                .translate((p[0], p[1], -2.6))
                .translate((0, 0, t))
            ), 
            name=f"Foot_M3_Washer{i}", 
            color=cq.Color(fastener_color)
        )

        # Feet Screws
        base_assm.add(
            (
                cq.Workplane().M3_cap_screw(6)
                .rotate((0, 0, 0), (0, 1, 0), 180)
                .translate((p[0], p[1], -2.6))
                .translate((0, 0, t))
            ), 
            name=f"Foot_M3X6_Cap_Head{i}",
            color=cq.Color(fastener_color)
        )


    for i, p in enumerate(mount_motor_points):
        # Motor Screws
        base_assm.add(
            (
                cq.Workplane().M3_cap_screw(6)
                .rotate((0, 0, 0), (0, 1, 0), -90)
                .rotate((0, 0, 0), (0, 0, 1), -90)
                .translate((p[0], 33.5, p[1]))
                .translate((0, 0, t))
            ), 
            name=f"Motor_M3X6_Cap_Head{i}",
            color=cq.Color(fastener_color)
        )

    return(base_assm)