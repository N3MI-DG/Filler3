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

def makeExtrusion():
    ext_assm = (
        cq.Assembly(name="Extrusion_Rail")

        .add(
            # https://www.aliexpress.com/item/4000264234020.html
            # 400mm
            # MGN12H
            cq.Workplane().MGN12_rail(),
            name="MGN12_Rail",
            color=cq.Color('lightgray')
        )

        .add(
            cq.Workplane().MGN12H_car(),
            name="MGN12_Car",
            color=cq.Color('firebrick2')
        )

        .add(
            cq.Workplane().tube_section(extrude=238, rail=False),
            name="Carriage_Stop_Print",
            color=cq.Color(print_color)
        )

        .add(
            cq.Workplane().tube_section(z=238, extrude=136),
            name="Tube_Section_1_Print",
            color=cq.Color(print_color)
        )

        .add(
            cq.Workplane().tube_section(z=238+136, extrude=136),
            name="Tube_Section_2_Print",
            color=cq.Color(print_color)
        )
    )

    for i in [0, 4, 8, 14]:

        # M3x10 Cap Screws
        ext_assm.add(
            (
                cq.Workplane().M3_cap_screw(10)
                .rotate((0, 0, 0), (0, 1, 0), -90)
                .rotate((0, 0, 0), (0, 0, 1), -90)
                .translate((0, 14, extrusion_z_offset+rail_z_offset+10+(i*25)))
            ), 
            name=f"Rail_M3X10_Cap_Head{i}",
            color=cq.Color(fastener_color)
        )

        # M3 T Nuts
        ext_assm.add(
            (
                cq.Workplane().M3_T_nut()
                .translate((0, 6.8, extrusion_z_offset+rail_z_offset+10+(i*25)))
            ), 
            name=f"Rail_M3T_nut{i}",
            color=cq.Color(fastener_color)
        )

    return(ext_assm)

