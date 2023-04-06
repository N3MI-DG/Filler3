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
from assm_motor_mount import *
from assm_base import *
from assm_extrusion import *
from assm_idle_stop import *
from assm_filler_mount import *
from assm_filler import *

def makeFiller3(): 
    return(
        cq.Assembly(name="Filler3")

        .add(makeMotorMount())
        .add(makeBase())
        .add(makeExtrusion())
        .add(makeIdleStop())
        .add(makeFillerMount())
        .add(makeFiller())
    )

filler3 = makeFiller3()
# filler3.save('Filler3.step')
show_object(filler3)

# Exprt STL files
# parts = [
#     (cq.Workplane().carriage(), "Carriage"),
#     (cq.Workplane().motor_mount(), "Motor Mount"),
#     (cq.Workplane().pcb_spacer(), "PCB Spacer"),
#     (cq.Workplane().dfu_helper(), "DFU Helper"),
#     (cq.Workplane().base(), "Base"),
#     (cq.Workplane().idle_stop(), "Idle Stop"),
#     (cq.Workplane().filler_mount(front=False, left=False), "Filler Mount Right"),
#     (cq.Workplane().filler_mount(front=False, right=False), "Filler Mount Left"),
#     (cq.Workplane().filler_mount(right=False, left=False), "Filler Mount Front"),
#     (cq.Workplane().purge_cap(), "Purge Cap"),
#     (cq.Workplane().handle_stop(), "Handle Stop"),
#     (cq.Workplane().foot(), "Foot"),
#     (cq.Workplane().condensation_cover(), "Condensation Cover"),
#     (cq.Workplane().tube_section(extrude=238, rail=False).rotate((0, 0, 0), (1, 0, 0), 180), "Car Stop"),
#     (cq.Workplane().tube_section(z=238, extrude=136), "Tube Section")
# ]

# for x in parts:
#     fn = f"STL/{x[1]}.stl"
#     print('Exporting', fn)
#     cq.exporters.export(x[0], fn)



# show_object(cq.Workplane().carriage(), "Carriage")
# show_object(cq.Workplane().motor_mount(), "Motor Mount")
# show_object(cq.Workplane().pcb_spacer(), "PCB Spacer")
# show_object(cq.Workplane().dfu_helper(), "DFU Helper")
# show_object(cq.Workplane().base(), "Base")
# show_object(cq.Workplane().idle_stop(), "Idle Stop")
# show_object(cq.Workplane().filler_mount(front=False, left=False), "Filler Mount Right")
# show_object(cq.Workplane().filler_mount(front=False, right=False), "Filler Mount Left")
# show_object(cq.Workplane().filler_mount(right=False, left=False), "Filler Mount Front")
# show_object(cq.Workplane().purge_cap(), "Purge Cap")
# show_object(cq.Workplane().handle_stop(), "Handle Stop")
# show_object(cq.Workplane().foot(), "Foot")
# show_object(cq.Workplane().condensation_cover(), "Condensation Cover")
# show_object(cq.Workplane().tube_section(extrude=238, rail=False).rotate((0, 0, 0), (1, 0, 0), 180), "Car Stop")
# show_object(cq.Workplane().tube_section(z=238, extrude=136), "Tube Section")
