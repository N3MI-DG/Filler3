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

def makeIdleStop():
    idle_stop_assm = (
        cq.Assembly(name="Idle_Stop")

        .add(
            # https://www.aliexpress.com/item/4000029868541.html
            cq.Workplane().microswitch(),
            name="Endstop_Switch",
            color=cq.Color('coral')
        )

        .add(
            # https://www.aliexpress.com/item/32796878074.html
            cq.Workplane().pulley(),
            name="Idle_Pulley",
            color=cq.Color('gray')
        )

        .add(
            cq.Workplane().idle_stop(),
            name="Idle_Stop_Print",
            color=cq.Color(print_color)
        )

        .add(
            cq.Workplane().M5_button_screw(10).translate((0, 0, extrusion_z_offset+extrusion_length+5)),
            name="Idle_Stop_M5x10_Button_Head_Screw",
            color=cq.Color(fastener_color)
        )

        .add((
            cq.Workplane().M2_pan_screw(10)
            .rotate((0, 0, 0), (0, 1, 0), 90)
            .translate((12.3, 21.8, extrusion_z_offset+extrusion_length-4.8))
            ),
            name="Endstop_Switch_M2x10_Pan_Head_Self_Tapper_Screw0",
            color=cq.Color(fastener_color)
        )

        .add((
            cq.Workplane().M2_pan_screw(10)
            .rotate((0, 0, 0), (0, 1, 0), 90)
            .translate((12.3, 15.3, extrusion_z_offset+extrusion_length-4.8))
            ),
            name="Endstop_Switch_M2x10_Pan_Head_Self_Tapper_Screw1",
            color=cq.Color(fastener_color)
        )

        .add((
            cq.Workplane().M3_cap_screw(20)
            .rotate((0, 0, 0), (1, 0, 0), -90)
            .translate((0, 44, extrusion_z_offset+extrusion_length-abs(pulley_z_offset)))
            ),
            name="Idler_M3x20_Cap_Head_Screw",
            color=cq.Color(fastener_color)
        )
    )

    return(idle_stop_assm)