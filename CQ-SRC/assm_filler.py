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

def makeFiller():
    filler_assm = (
        cq.Assembly(name="Filler")
        .add(
            cq.Workplane().purge_cap(),
            name="Purge_Cap_Print",
            color=cq.Color(print_color)
        )

        .add(
            cq.Workplane().handle_stop()
            .rotate((0, 0, 0), (1, 0, 0), -180)
            .rotate((0, 0, 0), (0, 0, 1), -90)
            .translate((-2.25, filler_y_offset, car_z_offset+104))
            ,
            name="Handle_Stop_Print",
            color=cq.Color(print_color)
        )

        .add(
            # https://www.kegland.com.au/bottle-filler-beer-gun.html
            cq.Workplane().filler_tube(),
            name="Filler_Tube",
            color=cq.Color('gray80')
        )

        .add(
            # https://www.aliexpress.com/item/33011074542.html
            # 8mm OD Hose
            # 1/4"
            (
                cq.Workplane().threaded_elbow(male=False)
                .translate((12, filler_y_offset, car_z_offset+80))
            ),
            name="Gas_Elbow_Filler",
            color=cq.Color("gray60")
        )

        .add(
            # https://www.kegland.com.au/duotight-6-5mm-1-4-x-8mm-5-16-reducer.html
            (
                cq.Workplane().duo_reducer()
                .translate((0, filler_y_offset, car_z_offset+120))
            ),
            name="Liquid_Duo_Reducer",
            color=cq.Color("gray60")
        )

        .add(
            cq.Workplane().cylinder(sensor_length, 1.2)
            .translate((sensor_x_offset, filler_y_offset, car_z_offset-(sensor_length/2)))
            ,
            name="Sensor",
            color=cq.Color(fastener_color)
        )

    )

    return(filler_assm)