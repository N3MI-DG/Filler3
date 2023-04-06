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

def makeMotorMount(extrusion=extrusion_length, cover=True):
    motor_mount_assm = (
        cq.Assembly(name="Motor_Mount")

        .add(
            cq.Workplane().motor_mount(),
            name="Motor_Mount_Print",
            color=cq.Color(print_color)
        )

        .add(
            cq.Workplane().pcb_spacer(),
            name="PCB_Spacer_Print",
            color=cq.Color(print_color)
        )

        .add(
            cq.Workplane().dfu_helper(),
            name="DFU_Helper_Print",
            color=cq.Color(print_color)
        )

        .add(
            # https://www.aliexpress.com/item/32585429251.html
            cq.Workplane().nema_17(),
            name="17HS08-1004S",
            color=cq.Color('ivory4')
        )

        .add(
            # https://www.aliexpress.com/item/1005002226516848.html
            # 16 Teeth Bore 5mm
            # 6mm Width
            cq.Workplane().motor_pulley(),
            name="Motor_Pulley",
            color=cq.Color('ivory3')
        )

        .add(
            # https://www.aliexpress.com/item/1005004242828520.html
            # EBB42 CAN
            cq.Workplane().ebb42(),
            name="PCB",
            color=cq.Color('yellowgreen')
        )

        .add(
            # https://www.aliexpress.com/item/1005002755168110.html
            # Elbow Typec F to M
            cq.Workplane().usb_elbow(),
            name="USB_Elbow",
            color=cq.Color('gray40')
        )
    )

    # Extrusion
    if extrusion:
        motor_mount_assm.add(
            # https://www.makerstore.com.au/product/black-v-slot-20-x-20mm/
            cq.Workplane().extrusion(extrusion),
            name="Extrusion",
            color=cq.Color('lightgray')
        )

    # Condensation Cover
    if cover:
        motor_mount_assm.add(
            cq.Workplane().condensation_cover(),
            name="Condensation_Cover",
            color=cq.Color(print_color)
        )

    # Extrusion Screw
    motor_mount_assm.add(
        (
            cq.Workplane().M5_button_screw(10)
            .rotate((0, 0, 0), (1, 0, 0), 180)
            .translate((0, 0, extrusion_z_offset-5))
        ), 
        name="Extrusion_M5x10_Button_Head", 
        color=cq.Color(fastener_color)
    )


    # Motor Screws
    for i, p in enumerate(mount_motor_points[1:]):
        motor_mount_assm.add(
            (
                cq.Workplane().M3_pan_screw(40)
                .rotate((0, 0, 0), (1, 0, 0), 90)
                .translate((p[0], -17.1+motor_counter_bore, p[1]))
            ), 
            name=f"Motor_M3x40_Pan_Head{i}", 
            color=cq.Color(fastener_color)
        )

    # PCB Nutserts
    for i, p in enumerate(mount_motor_points):
        motor_mount_assm.add(
            (
                cq.Workplane().M3_nutsert()
                .rotate((0, 0, 0), (0, 1, 0), 90)
                .translate((-27, p[0]+4, p[1]))
            ), 
            name=f"PCB_Nutsert{i}", 
            color=cq.Color(nutsert_color)
        )

    # PCB M3x10 Screws
    for i, p in enumerate(mount_motor_points):
        if i in [0, 2, 3]:
            motor_mount_assm.add(
                (
                    cq.Workplane().M3_cap_screw(10)
                    .rotate((0, 0, 0), (0, 1, 0), -90)
                    .translate((-31.5, p[0]+4, p[1]))
                ), 
                name=f"PCB_M3X10_Cap_Head{i}", 
                color=cq.Color(fastener_color)
            )

    # PCB M3x16 Screw
    motor_mount_assm.add(
        (
            cq.Workplane().M3_cap_screw(16)
            .rotate((0, 0, 0), (0, 1, 0), -90)
            .translate((-37.5, mount_motor_points[1][0]+4, mount_motor_points[1][1]))
        ), 
        name=f"PCB_M3X16_Cap_Head{1}", 
        color=cq.Color(fastener_color)
    )

    return(motor_mount_assm)