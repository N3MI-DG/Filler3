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

from variables import *
from funcs import *
import cadquery as cq
from cadquery import selectors


def M5_button_screw(self, length=10):
    thing = (
        cq.Workplane()
        .circle(2.5)
        .extrude(-length)
        .union(
            cq.Workplane()
            .sphere(4.98)
            .translate((0, 0, -1.5))
            .cut(
                cq.Workplane()
                .circle(10)
                .extrude(-10)
            )
            .cut(
                cq.Workplane()
                .circle(10)
                .extrude(10)
                .translate((0, 0, 2.8))
            )
            .faces(">Z").polygon(6, 3, False, True).extrude(-2.38, combine="cut")
        )
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def M3_cap_screw(self, length=10):
    thing = (
        cq.Workplane()
        .circle(1.5)
        .extrude(-length)
        .union(
            cq.Workplane()
            .circle(2.85)
            .extrude(3)
            .faces(">Z").fillet(0.24)
            .faces(">Z").polygon(6, 2.5, False, True).extrude(-2.38, combine="cut")
        )
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def M3_pan_screw(self, length=10):
    thing = (
        cq.Workplane()
        .circle(1.5)
        .extrude(-length)
        .union(
            cq.Workplane()
            .circle(2.73)
            .extrude(2.4)
            .faces(">Z").fillet(1)
            .cut(
                cq.Workplane()
                .box(3, 0.6, 2)
                .translate((0, 0, 2))
                .faces("<Z").edges("Y").chamfer(1.2)
            )
            .cut(
                cq.Workplane()
                .box(0.6, 3, 2)
                .translate((0, 0, 2))
                .faces("<Z").edges("X").chamfer(1.2)
            )
        )
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def M3_nutsert(self):
    thing = (
        cq.Workplane()
        .circle(2.1)
        .extrude(4)

        .union(
            cq.Workplane()
            .polygon(8, 5)
            .twistExtrude(-1.2,60)

            .union(
                cq.Workplane()
                .polygon(8, 5)
                .twistExtrude(1.2,-60)
                .translate((0, 0, 0.4))
                .rotateAboutCenter((0, 0, 1), 30)
            )
            .translate((0, 0, 1.2))
        )
        .faces(">Z")
        .workplane()
        .hole(3)
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def M3_washer(self):
    thing = (
        cq.Workplane()
        .circle(3.45)
        .extrude(0.6)

        .faces(">Z")
        .workplane()
        .hole(3.2)
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def M3_T_nut(self):
    thing = (
        cq.Workplane()
        .box(10.35, 4.95, 11.2)
        .faces(">Y")
        .workplane()
        .hole(3)
        .pushPoints([(4, 0), (-4, 0)])
        .rect(3, 11.2)
        .extrude(-1.25, combine="cut")
        .faces("<Y").edges("|Z").chamfer(3)

    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def M3_square_nut(self):
    thing = (
        cq.Workplane()
        .rect(5.5, 5.5)
        .extrude(-2)
        .faces(">Z")
        .hole(3)
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def M2_pan_screw(self, length=10):
    thing = (
        cq.Workplane()
        .circle(1)
        .extrude(-length)
        .union(
            cq.Workplane()
            .circle(1.5)
            .extrude(1.24)
            .faces(">Z").fillet(1)
            .cut(
                cq.Workplane()
                .box(3, 0.6, 2)
                .translate((0, 0, 1))
                .faces("<Z").edges("Y").chamfer(1.2)
            )
            .cut(
                cq.Workplane()
                .box(0.6, 3, 2)
                .translate((0, 0, 1))
                .faces("<Z").edges("X").chamfer(1.2)
            )
        )
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def quater_bsp_nut(self):
    thing = (
        cq.Workplane("XZ")
        .polygon(6, 21.5)
        .extrude(5.6)
        .rotate((0, 0, 0), (0 ,1 ,0), 30)
        .faces("<Y").hole(13)
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def extrusion(self, length=500):
    thing = (
        cq.importers.importDXF('imports/V-Slot 20x20.dxf')
        .wires().toPending()
        .extrude(length)
        .translate((0, 0, extrusion_z_offset))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def MGN12_rail(self):
    thing = (
        cq.importers.importStep(f'imports/MGN12_RAIL_{rail_length}.step')
        .translate((
            0, 
            rail_y_offset, 
            extrusion_z_offset+(rail_length/2)+rail_z_offset
        ))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def MGN12H_car(self):
    zero = 3.325+(45/2)

    thing = (
        cq.importers.importStep('imports/MGN12H_CAR.step')
        .translate((0, rail_y_offset, zero+car_z_offset))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def MG996R_servo(self, body=True, arm=True):

    _body = cq.importers.importStep('imports/MG996R.step')
    _arm  = (
        cq.importers.importStep('imports/servo_arm.step')
        .rotate((0, 0, 0), (1, 0, 0), 90)
        .rotate((0, 0, 0), (0, 1, 0), 270)
        .translate((-10.5, 47.5+1.55, 0))
    )

    if body and arm:
        thing = _body.union(_arm)

    elif body and not arm:
        thing = _body

    elif arm and not body:
        thing = _arm
    
    thing = (
        thing
        .rotate((0, 0, 0), (1, 0, 0), 180)
        .rotate((0, 0, 0), (0, 1, 0), 180)

        .translate((
                servo_x_offset-10, 
                filler_y_offset+servo_y_offset,
                (car_z_offset+filler_car_z_offset)-10.25
        ))

    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def gas_solenoid(self, post=False):
    thing = (
        cq.importers.importStep('imports/Solenoid_Valve_1_4.stp')
        .rotate((0, 0, 0), (0, 0, 1), -90)
        .translate((0, 0, 3.175))
        .rotate((0, 0, 0), (1, 0, 0), 180)
        .translate((solenoid_x_offset, solenoid_y_offset, solenoid_z_offset))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def filler_tube(self):
    thing = (
        cq.importers.importStep('imports/filler_tube.step')
        .rotate((0, 0, 0), (0, 0, 1), 270)
        .translate((
            0, 
            filler_y_offset, 
            (-134)+car_z_offset+filler_car_z_offset
        ))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def ball_lock(self):
    thing = (
        cq.importers.importDXF('imports/ball_lock.dxf')
        .wires().toPending()
        .revolve(360, (-0, 0, 0), (-0, -1, 0))
    )
    
    # Ball Lock Hex
    thing = thing.union(
        cq.Workplane("ZX")
        .polygon(6, 19.35)
        .extrude(9.5)
        .translate((0, 5, 0))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def duo_elbow(self):
    thing = (
        cq.Workplane()
        .circle(12.4/2)
        .extrude(32.7)

        .union(
            cq.Workplane()
            .circle(12.75/2)
            .extrude(1.2)
            .faces(">Z")
            .workplane()
            .circle(16.6/2)
            .extrude(3)
            .faces(">Z")
            .workplane()
            .circle(18.4/2)
            .extrude(8.5)
            .faces(">Z")
            .workplane()
            .circle(16.35/2)
            .extrude(5.5)
        )
    )

    thing = (
        thing
        .union(
            thing
            .rotate((0, 0, 0), (1, 0, 0), -90)
            .rotate((0, 0, 0), (0, 0, 1), 180)
            .translate((0, 26.5, 26.5))
        )
        .cut(
            cq.Workplane()
            .circle(20).extrude(20)
            .faces("<Z").workplane()
            .hole(12.4)
            .cut(
                cq.Workplane()
                .box(50, 50, 50)
                .translate((0, 25, 0))
            )
            .translate((0, 0, 19))
        )
        .cut(
            cq.Workplane()
            .circle(20).extrude(20)
            .faces("<Z").workplane()
            .hole(12.4)
            .cut(
                cq.Workplane()
                .box(50, 50, 50)
                .translate((0, 25, 0))
            )
            .rotate((0, 0, 0), (1, 0, 0), -90)
            .translate((0, -12, 26.5))
        )
    )

    thing = (
        thing
        .rotate((0, 0, 0), (1, 0, 0), 90)
        .rotate((0, 0, 0), (0, 1, 0), 45)
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def threaded_elbow(self, male=True):
    thing = (
        cq.Workplane()
        .circle(11.75/2)
        .extrude(29.5)

        .cut(
            cq.Workplane()
            .box(10, 10, 30)
            .translate((10, 0, 19))
        )

        .cut(
            cq.Workplane()
            .box(10, 10, 30)
            .translate((-10, 0, 19))
        )
    )

    thing = (
        thing
        .union(
            thing
            .union(
                cq.Workplane()
                .circle(13.8/2)
                .extrude(2)
                .faces(">Z")
                .workplane(1.5)
                .circle(13.8/2)
                .extrude(11.65)
                .faces(">Z")
                .chamfer(1)
            )
            .rotate((0, 0, 0), (1, 0, 0), -90)
            .rotate((0, 0, 0), (0, 0, 1), 180)
            .translate((0, 23.63, 23.63))
        )

    )


    if male:
        thing = (
            thing
            .union(
                cq.Workplane()
                .circle(13.36/2)
                .extrude(9.6)
                .faces(">Z")
                .workplane()
                .polygon(6, 14, circumscribed=True)
                .extrude(7.2)
            )
        )

    else:
        thing = (
            thing
            .union(
                cq.Workplane().transformed(offset=(0, 0, -1))
                .circle(16.55/2)
                .extrude(17.7)
                .faces("<Z")
                .workplane()
                .polygon(6, 17, circumscribed=True)
                .extrude(-10)
            )
        )

    thing = (
        thing
        .cut(
            cq.Workplane()
            .circle(20).extrude(20)
            .faces("<Z").workplane()
            .hole(11.75)
            .cut(
                cq.Workplane()
                .box(50, 50, 50)
                .translate((0, 25, 0))
            )
            .translate((0, 0, 17))
        )

        .cut(
            cq.Workplane()
            .circle(20).extrude(20)
            .faces("<Z").workplane()
            .hole(11.75)
            .cut(
                cq.Workplane()
                .box(50, 50, 50)
                .translate((0, 25, 0))
            )
            .rotate((0, 0, 0), (1, 0, 0), -90)
            .translate((0, -14, 23.63))
        )
    )

    if male:
        thing = (
            thing
            .rotate((0, 0, 0), (1, 0, 0), 90)
            .rotate((0, 0, 0), (0, 1, 0), -45)
        )
    
    else:
        thing = (
            thing
            .rotate((0, 0, 0), (1, 0, 0), 90)
            .rotate((0, 0, 0), (0, 0, 1), 90)
        )
    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def duo_reducer(self):
    thing = (
        cq.Workplane()
        .circle(9.88/2).extrude(1.5)
        .faces(">Z").workplane()
        .circle(14.38/2).extrude(3.5)
        .faces(">Z").workplane()
        .circle(15.88/2).extrude(12)
        .faces(">Z").workplane()
        .circle(9.5/2).extrude(3.5)
        .faces(">Z").workplane()
        .circle(12.3/2).extrude(3)
        .faces(">Z").workplane()
        .circle(16.4/2).extrude(6)
        .faces(">Z").workplane()
        .circle(18.2/2).extrude(8.1)
        .faces(">Z").workplane()
        .circle(16.5/2).extrude(3)
        .faces(">Z").workplane()
        .circle(12.75/2).extrude(1.5)
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def power_socket(self):
    thing = (
        cq.Workplane()
        .circle(7.72/2)
        .extrude(5.5)
        .faces(">Z")
        .workplane()
        .circle(10.9/2)
        .extrude(3)
        .faces(">Z")
        .workplane()
        .circle(8.65/2)
        .extrude(6.5)
        .faces("<Z")
        .workplane()
        .hole(5.73, depth=10)

        .union(
            cq.Workplane()
            .circle(1.25)
            .extrude(7)
            .translate((0, 0, 3))
            .faces("<Z")
            .fillet(1.24)
        )

        .union(
            cq.Workplane()
            .polygon(6, 10, circumscribed=True)
            .extrude(2.24)
            .faces(">Z")
            .hole(7.72)
            .translate((0, 0, 5.5-2.24-2))
        )

    )

    tab = (
        cq.Workplane()
        .box(2.75, 0.45, 6)
        .translate((0, 0, 18))
        .faces(">Z").edges(">X").fillet(1.3)
        .faces(">Z").edges("<X").fillet(1.3)
    )

    thing = (
        thing
        .union(tab.translate((0,  3, 0)))
        .union(tab.translate((0, -3.8, 0)))
        .union(tab.rotate((0, 0, 0), (0, 0, 1), 90).translate((3.8, 0, 0)))
    )

    thing = (
        thing
        .rotate((0, 0, 0), (1, 0, 0), 90)
        .rotate((0, 0, 0), (0, 1, 0), 180)
        .translate((power_x_offset, 50.5, motor_z_offset))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def button(self):
    points = [
        (22/2,   0),
        (17.5/2, 1.7),
        (0,      1.7),
        (0,      0)
    ]

    face = (
        cq.Workplane("XZ")
        .lineTo(points[0][0], points[0][1])
        .lineTo(points[1][0], points[1][1])
        .lineTo(points[2][0], points[2][1])
        .lineTo(points[3][0], points[3][1])
        .close()
        .revolve()
    )

    thread = (
        cq.Workplane()
        .circle(19/2)
        .extrude(-(14-1.7))
    )

    nut = (
        cq.Workplane().transformed(offset=(0, 0, -(2.8+base_wall_thick)))
        .polygon(6, 25)
        .extrude(2.8)
    )

    thing = (
        face
        .union(thread)
        .union(nut)
    )

    thing = (
        thing
        .rotate((0, 0, 0), (0, 1, 0), 90)
        .translate((button_x_offset, button_y_offset, button_z_offset))
    )



    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def motor_pulley(self):
    thing = (
        cq.importers.importDXF('imports/pulley.dxf')
        .wires().toPending()
        .revolve(360, (-0, 0, 0), (-0, -1, 0))
        .rotate((0, 0, 0), (0, 0, 1), 180)
        .translate((0, motor_y_offset+17, motor_z_offset))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def nema_17(self):
    thing = (
        cq.importers.importStep('imports/17HS08-1004S.stp')
        .rotate((0, 0, 0), (0, 1, 0), 90)
        .translate((0, -65.5745, 0))
    )

    thing = (
        thing
        .rotate((0, 0, 0), (0, 0, 1), 180)
        .translate((0, motor_y_offset, motor_z_offset))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def motor_mount(self):
    bottom = (
        cq.Workplane().transformed(offset=(0, 0, extrusion_z_offset/2))
        .box(mount_b_x, mount_b_y, extrusion_z_offset)
    )

    r_side = (
        cq.Workplane().transformed(offset=(10+(mount_s_x/2)+mount_tol, 0, mount_s_z/2))
        .box(mount_s_x, mount_b_y, mount_s_z)
    )

    l_side = (
        cq.Workplane().transformed(offset=(-(10+(mount_s_x/2)+mount_tol+(mount_pcb_s/2)), motor_thick/2-mount_f_y/2, mount_s_z/2))
        .box(mount_s_x+mount_pcb_s, mount_b_y + motor_thick-mount_f_y, mount_s_z)

    )

    f_side = (
        cq.Workplane().transformed(offset=(-(mount_pcb_s/2), -(10+(mount_f_y/2)+mount_tol), mount_s_z/2))
        .box(mount_f_x, mount_f_y, mount_s_z)
    )

    inner_a = (
        cq.importers.importDXF('imports/V_inner_a.dxf')
        .wires().toPending()
        .extrude(mount_s_z)
        
        .faces(">Z").edges("<X").chamfer(3)
        .faces(">Z").edges(">X").chamfer(3)
        .faces(">Z").edges(">Y").chamfer(1)
        .faces(">Y[-2]").edges(">Z").chamfer(1)
    )

    inner_b = (
        cq.importers.importDXF('imports/V_inner_b.dxf')
        .wires().toPending()
        .extrude(extrusion_z_offset+12)
    )


    thing = (
        bottom
        .union(r_side)
        .union(l_side)
        .union(f_side)
        .union(inner_a)
        .union(inner_b)
    )

    # Clean out the motor section
    thing = (
        thing
        .cut(
            cq.Workplane()
            .transformed(offset=(0, 10+(motor_thick/2), mount_s_z/2))
            .box(motor_width+(mount_tol*2), motor_thick+(mount_tol*2), mount_s_z)
        )
    )

    # Bottom Hole
    thing = (
        thing
        .faces("<Z")
        .workplane()
        .cboreHole(big_hole_dia, big_screw_head_dia, extrusion_z_offset-5)

        .cut(
            cq.Workplane()
            .box(solveOppHyp(big_hole_dia/2, big_screw_head_dia/2)['adjacent']*2, big_hole_dia, (extrusion_z_offset*2)-9.4)
            .box(big_hole_dia, big_hole_dia, (extrusion_z_offset*2)-8.8)
        )
    )

    # Motor Holes
    thing = (
        thing
        .faces("<Y")
        .workplane()
        .pushPoints(mount_motor_points[1:])
        .cboreHole(small_hole_dia, small_screw_head_dia, motor_counter_bore)
    )

    # PCB Holes
    thing = (
        thing
        .faces("<X")
        .workplane()

        .pushPoints([(x[0]-(motor_width/2), x[1]) for x in mount_motor_points])
        .hole(thread_insert_dia, 6)
    )

    # Wire Tunnels
    tunnel_r = (
        cq.Workplane()
        .circle(5)
        .revolve(90, (mount_s_z, 0, 0), (mount_s_z, -1, 0))
        .translate((7.5, 0, mount_s_z+1))
    )

    tunnel_r1 = (
        cq.Workplane()
        .polygon(6, 14)
        .extrude(extrusion_xy+(mount_f_y*2))
        .rotate((0, 0, 0), (0, 0, 1), 30)
        .rotate((0, 0, 0), (1, 0, 0), -90)
        .translate(((extrusion_xy/2)+mount_s_x+4, -(extrusion_xy+(mount_f_y*2))/2, motor_z_offset))
    )

    tunnel_l2 = (
        cq.Workplane("ZY")
        .rect(25, 9)
        .extrude(mount_s_z)
        .faces(">Y")
        .edges("#Z")
        .chamfer(4)
        .translate((10+mount_tol, 14.5-mount_tol, motor_z_offset))
    )

    tunnel_l3 = (
        cq.Workplane()
        .polygon(6, 14)
        .extrude(mount_s_z/2)
        .rotate((0, 0, 0), (0, 0, 1), 30)
        .translate((-((mount_f_x/2)+4), 1.5, mount_s_z/2))
    )

    tunnel_l4 = (
        cq.Workplane()
        .polygon(6, 14)
        .extrude(extrusion_xy+(mount_f_y*2))
        .rotate((0, 0, 0), (0, 0, 1), 30)
        .rotate((0, 0, 0), (1, 0, 0), -90)
        .translate((-((mount_f_x/2)+4), -(extrusion_xy+(mount_f_y*2))/2, motor_z_offset))
    )


    tunnel_l5 = (
        cq.Workplane()
        .rect(9.9, 7)
        .extrude(12) # 6
        .translate((-((mount_b_x/2)+mount_pcb_s), -4.5, motor_z_offset))
    )


    tunnel_b = (
        cq.Workplane()
        .polygon(6, 14)
        .extrude(mount_f_x)
        .rotate((0, 0, 0), (0, 1, 0), -90)
        .translate(((mount_f_x/2)-(mount_pcb_s/2), -((mount_b_y/2)+7), motor_z_offset))
    )


    # Cable Tie Tunnels
    ct_1 = (
        cq.Workplane()
        .rect(3, 1.8)
        .revolve(360, (0, 7, 0), (-1, 7, 0))
        .translate((-17, -(15+mount_f_y), motor_z_offset))
        .union(
            cq.Workplane()
            .rect(6, 11.8)
            .extrude(21)
            .translate((-17, -(mount_f_y+(extrusion_xy/2)), motor_z_offset-14+3.5))
        )
    )

    ct_2 = (
        cq.Workplane()
        .rect(3, 1.8)
        .revolve(360, (0, 7, 0), (-1, 7, 0))
        .translate((14.5, -(15+mount_f_y), motor_z_offset))
        .union(
            cq.Workplane()
            .rect(6, 11.8)
            .extrude(21)
            .translate((14.5, -(mount_f_y+(extrusion_xy/2)), motor_z_offset-14+3.5))
        )
    )

    ct_3 = (
        cq.Workplane()
        .circle(6.5)
        .extrude(3)
        .faces(">Z")
        .hole(10)
        .translate((-((mount_b_x/2)+(mount_pcb_s-3)), 1.5, motor_z_offset+7))
    )

    thing = (
        thing
        .cut(tunnel_r)
        .cut(tunnel_r1)
        .cut(tunnel_l2)
        .cut(tunnel_l3)
        .cut(tunnel_l4)
        .cut(tunnel_l5)
        .cut(tunnel_b)
        .cut(ct_1)
        .cut(ct_2)
        .cut(ct_3)

        # Trim the bottom
        .cut(
            cq.Workplane()
            .rect(200, 200)
            .extrude(mount_s_z-motor_width)
        )

        # PCB Chamfer
        .faces(">Y").edges("#Z").chamfer(4)

        # Front Chamfer
        .faces("<Y").edges("|Z").chamfer(1)

        # Bottom Chamfer
        .faces("<Z").chamfer(0.3)

        # top Chamfer
        .faces(">Z").chamfer(0.3)

    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def pcb_spacer(self):
    holes = [
        ( 31/2,  31/2),
        ( 31/2, -31/2),
        (-31/2,  31/2),
        (-31/2, -31/2)
    ]

    thing = (
        cq.Workplane()
        .box(37, 37, 1)
        .cut(
            cq.Workplane()
            .box(34, 24, 1)
        )
    )

    thing = thing.union(
        cq.Workplane()
        .pushPoints(holes)
        .circle(3)
        .extrude(3)
    )

    thing = (
        thing
        .edges("|Z")
        .fillet(3)
    )

    thing = (
        thing
        .faces(">Z")
        .workplane()
        .pushPoints(holes)
        .hole(small_hole_dia)

    )

    thing = (
        thing
        .union(
            cq.Workplane()
            .text(">", 8, 0.7)
            .translate((0, 14.5, 0))
        )
    )

    thing = (
        thing
        .rotate((0, 0, 0), (0, 1, 0), -90)
        .translate((-27.75, 4, motor_z_offset))

    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def tube_section(self, z=0, extrude=6, rail=True):
    thing = (
        cq.importers.importDXF(f'imports/V_tube_body.dxf')
        .wires().toPending()
        .extrude(extrude)
    )

    if rail:
        thing = thing.cut(
            cq.Workplane().box(12, 4, extrude*2)
            .translate((0, 12, 0))
        )
    
    else:
        thing = (
            thing
            .union(
                cq.Workplane().rect(26.14, 32, centered=True).extrude(extrude)
                .faces(">Y").edges(">X").chamfer(8, 6)
                .faces(">Y").edges("<X").chamfer(6, 8)
                .translate((0, 4, 0))
                .cut(cq.Workplane().rect(40, 24, centered=True).extrude(extrude))
            )
            .cut(cq.Workplane().base(profile=True))
            .cut(cq.Workplane().box(50, 50, 150))
            .cut(cq.Workplane().rect(12, 20, centered=True).extrude(extrude+1).translate((0, 15, 110)))
        )

    thing = thing.translate((0, 0, z))

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def carriage(self):
    pully_r = 4.75
    belt_depth = 7
    belt_pitch = 2
    belt_thick = 1.6

    mount = (
        cq.Workplane()
        .rect(car_mount_x, car_mount_y-filler_mount_car_y)
        .extrude(car_mount_z)
        .faces("<Y")
        .workplane()
        .center(0, car_mount_z/2)
        .pushPoints(car_mount_points)
        .hole(small_hole_dia)

        # Clamp A
        .faces(">Y")
        .workplane()
        .center(pully_r+(belt_thick/2), 0)
        .rarray(1, belt_pitch, 1, 25)
        .hole(belt_thick, belt_depth)

        .cut(
            cq.Workplane()
            .rect(belt_thick/2, belt_depth)
            .extrude(car_mount_z)
            .translate((-(pully_r+(belt_thick*0.75)), (car_mount_y/2-filler_mount_car_y/2)-((belt_depth)/2), 0))
        )

        .cut(
            cq.Workplane()
            .rect(1.1, 1.1)
            .extrude(car_mount_z)
            .edges("<Y and <X")
            .chamfer(1)
            .translate((-(pully_r+belt_thick+0.45), (car_mount_y/2-filler_mount_car_y/2)-0.4, 0))
        )

        # Clamp B
        .faces(">Y")
        .workplane()
        .center(-(pully_r+(belt_thick/2)), 0)
        .rarray(1, belt_pitch, 1, 25)
        .hole(belt_thick, belt_depth)

        .cut(
            cq.Workplane()
            .rect(belt_thick/2, belt_depth)
            .extrude(car_mount_z)
            .translate((belt_thick*0.25, (car_mount_y/2-filler_mount_car_y/2)-((belt_depth)/2), 0))
        )

        .cut(
            cq.Workplane()
            .rect(1.1, 1.1)
            .extrude(car_mount_z)
            .edges("<Y and >X")
            .chamfer(1)
            .translate((1.1, (car_mount_y/2-filler_mount_car_y/2)-0.4, 0))
        )

        # Clamp center
        .cut(
            cq.Workplane()
            .rect(car_mount_x/2, belt_depth)
            .extrude(car_mount_z/4)
            .translate((-(car_mount_x/4), (car_mount_y/2-filler_mount_car_y/2)-((belt_depth)/2), (car_mount_z/2)-(car_mount_z/8)))
        )

        # Belt Path
        .cut(
            cq.Workplane()
            .rect(belt_thick*3, belt_depth)
            .extrude(car_mount_z)
            .translate((pully_r+(belt_thick/2)-0.5, (car_mount_y/2-filler_mount_car_y/2)-((belt_depth)/2), 0))
        )
    )

    thing = (
        mount
        .faces(">Z").edges(">X or <X or >Y").chamfer(1)
        .faces("<Z").edges(">X or <X or >Y").chamfer(1)
        .faces(">Y").edges(">X or <X").chamfer(1)
        .faces("<Y").chamfer(0.3)

        .faces(">Y")
        .workplane()
        .pushPoints(car_mount_points)
        .hole(small_screw_head_dia+0.2, 2)
        
    ).translate((0, rail_y_offset+(car_mount_y/2+filler_mount_car_y/2)+7.1, car_z_offset-(car_mount_z/2)-0.2))


    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def filler_mount(self, get_points=False, front=True, left=True, right=True):
    mount_y = rail_y_offset+(filler_mount_car_y)/2+7.1
    mount_x = filler_mount_car_x_pos+abs(filler_mount_car_x_neg)
    mgn_to_can_offset = (mount_y + abs(can_y_offset)) - (filler_mount_car_y/2) + filler_bodge
    x_offset = ((mount_x)/2) + filler_mount_car_x_neg
    f_can_y_offset = -mgn_to_can_offset-(filler_mount_car_y/2)
    filler_front = 10

    if get_points: 
        return([
            (-30+filler_mount_car_x_pos+9.5+(x_offset*2), car_z_offset+6-10.5),
            (-30+filler_mount_car_x_pos+9.5+(x_offset*2), car_z_offset-6-10.5),
            (-30+filler_mount_car_x_pos-9.5,              car_z_offset+6-10.5),
            (-30+filler_mount_car_x_pos-9.5,              car_z_offset-6-10.5)
        ])

    f_mount_points = [
            (10-filler_mount_car_x_pos+9.5+(x_offset*2), ((car_mount_z-20.5)/2)+6),
            (10-filler_mount_car_x_pos+9.5+(x_offset*2), ((car_mount_z-20.5)/2)-6),
            (10-filler_mount_car_x_pos-9.5, ((car_mount_z-20.5)/2)+6),
            (10-filler_mount_car_x_pos-9.5, ((car_mount_z-20.5)/2)-6)
        ]

    # Carriage
    thing = (
        cq.Workplane()
        .rect(mount_x, filler_mount_car_y)
        .extrude(car_mount_z)
        .translate((x_offset, 0, 0))
        .faces(">Y")
        .workplane()
        .center(0, car_mount_z/2)
        .pushPoints(car_mount_points)
        .hole(small_hole_dia)
    )

    # Body
    thing = (
        thing
        .union(
            cq.Workplane().transformed(offset=(x_offset, -((mgn_to_can_offset/2)+filler_mount_car_y/2)-(filler_front/2), 0))
            .rect(mount_x, mgn_to_can_offset+filler_front)
            .extrude(car_mount_z)

            # Center Hole
            .cut(
                cq.Workplane().transformed(offset=(0, -((mgn_to_can_offset/2)+filler_mount_car_y/2)+10, 0))
                .rect(car_mount_x+0.5, mgn_to_can_offset-13.1)
                .extrude(car_mount_z)
                .faces("<Y").edges(">X").chamfer(10)
            )

            # Cable Path
            .cut(
                cq.Workplane().transformed(offset=(0.5, -((mgn_to_can_offset/2)+filler_mount_car_y/2)+2.75, 0))
                .rect((car_mount_x/2)+11.5, 34)
                .extrude(car_mount_z)
                .faces("<Y").edges(">X").chamfer(5)
                .faces("-Z or +Z or +Y or -X")
                .shell(7)
            )

            .cut(
                cq.Workplane().transformed(offset=(x_offset+21.5, -((mgn_to_can_offset/2)+filler_mount_car_y/2)-1.125, 0))
                .rect(10, 15.75)
                .extrude(car_mount_z)
                .faces("<Y").edges(">X").chamfer(9)
                .faces(">Y").edges(">X").chamfer(1)
            )

        )

        # Servo Body
        .cut(
            cq.Workplane().transformed(offset=(x_offset+3, -((mgn_to_can_offset/2)+filler_mount_car_y/2)-11.2, car_mount_z-20.5))
            .rect(47, 33)
            .extrude(20.5)
            .cut(
                cq.Workplane().transformed(offset=(filler_mount_car_x_pos, -((mgn_to_can_offset/2)+filler_mount_car_y/2)-11, car_mount_z-20.5))
                .rect(16, 30)
                .extrude(20.5)
                
            )
            .faces(">Y").edges("<X").chamfer(2)
        )

        # Servo Front
        .cut(
            cq.Workplane().transformed(offset=(x_offset, f_can_y_offset, car_mount_z-20.5))
            .rect(100, 34)
            .extrude(20.5)
        )

        # Servo Holes
        .faces("<Y")
        .workplane()
        .pushPoints(servo_screw_points)
        .hole(small_hole_dia, 44)

        .cut(
            cq.Workplane("ZX")
            .rect(5.6, 53.6).extrude(2.2)
            .translate((x_offset, -68, 35.15+5))
        )

        .cut(
            cq.Workplane("ZX")
            .rect(5.6, 53.6).extrude(2.2)
            .translate((x_offset, -68, 35.15-5))
        )

        # Filler Hole
        .faces("<Z")
        .workplane()
        .center(0, -filler_front)
        .cskHole(filler_dia, filler_dia+0.6, 45)

        # Channel Clearance
        .cut(
            cq.importers.importDXF('imports/filler_clearance.dxf')
            .wires().toPending()
            .extrude(car_mount_z)
            .translate((0, -mount_y, 0))
        )

        # Sensor Hole
        .faces("<Z")
        .workplane()
        .center(sensor_x_offset, 0)
        .cskHole(2.5, 3.1, 45)

        # Sensor cable
        .cut(
            cq.Workplane("ZX")
            .circle(1.25).extrude(40)
            .translate((sensor_x_offset, f_can_y_offset, 14))
        )

        # Sensor Screw
        .cut(
            cq.Workplane("ZX")
            .circle(small_hole_dia/2).extrude(40)
            .translate((sensor_x_offset, f_can_y_offset, 8))

            .union(
                cq.Workplane("ZX")
                .circle(small_screw_head_dia/2).extrude(20)
                .translate((sensor_x_offset, f_can_y_offset+20, 8))
            )

            .union(
                cq.Workplane()
                .rect(5.6, 2.2)
                .extrude(8+2.6)
                .translate((sensor_x_offset, f_can_y_offset+11, 0))
            )
            .union(
                cq.Workplane()
                .rect(2.5, 4)
                .extrude(14)
                .translate((sensor_x_offset, f_can_y_offset+2, 0))
            )
            
        )

        # Filler cable
        .cut(
            cq.Workplane("ZX")
            .circle(1.25).extrude(33)
            # .rotate((0, 0, 0), (0, 0, 1), -37)
            .translate((0, f_can_y_offset, 14))
        )

        # Filler Cable Screw
        .cut(
            cq.Workplane("ZX")
            .circle(small_hole_dia/2).extrude(40)
            .translate((0, f_can_y_offset, 8))

            .union(
                cq.Workplane("ZX")
                .circle(small_screw_head_dia/2).extrude(20)
                .translate((0, f_can_y_offset+14, 8))
            )

            .union(
                cq.Workplane()
                .rect(5.6, 2.2)
                .extrude(8+2.6)
                .translate((0, f_can_y_offset+11, 0))
            )
            .union(
                cq.Workplane()
                .rect(2.5, 5)
                .extrude(14)
                .translate((0, f_can_y_offset+5, 0))
            )
            
        )

        # Front Mount Screws
        .faces("<Y")
        .workplane()
        .pushPoints(f_mount_points)
        .circle(small_screw_head_dia/2).extrude(-6, combine="cut")
        .faces("<Y")
        .workplane()
        .pushPoints(f_mount_points)
        .circle(small_hole_dia/2).extrude(-19, combine="cut")

        # Nut Traps
        .cut(
            cq.Workplane("ZX")
            .rect(5.6, 5.6, True).extrude(2.2)
            .translate((f_mount_points[0][0]-2, f_can_y_offset+3, f_mount_points[0][1]+4))
            .union(
                cq.Workplane("ZX")
                .rect(5.6, 5.6, True).extrude(2.2)
                .translate((f_mount_points[0][0]-2, f_can_y_offset+3, f_mount_points[0][1]))
            )
        )

        .cut(
            cq.Workplane("ZX")
            .rect(5.6, 5.6, True).extrude(2.2)
            .translate((f_mount_points[1][0]-2, f_can_y_offset+3, f_mount_points[1][1]-4))
            .union(
                cq.Workplane("ZX")
                .rect(5.6, 5.6, True).extrude(2.2)
                .translate((f_mount_points[1][0]-2, f_can_y_offset+3, f_mount_points[1][1]))
            )
        )

        .cut(
            cq.Workplane("ZX")
            .rect(5.6, 5.6, True).extrude(2.2)
            .translate((f_mount_points[0][0]+(9.5*2)+1, f_can_y_offset+3, f_mount_points[0][1]+4))
            .union(
                cq.Workplane("ZX")
                .rect(5.6, 5.6, True).extrude(2.2)
                .translate((f_mount_points[0][0]+(9.5*2)+1, f_can_y_offset+3, f_mount_points[0][1]))
            )
        )

        .cut(
            cq.Workplane("ZX")
            .rect(5.6, 5.6, True).extrude(2.2)
            .translate((f_mount_points[1][0]+(9.5*2)+1, f_can_y_offset+3, f_mount_points[1][1]-4))
            .union(
                cq.Workplane("ZX")
                .rect(5.6, 5.6, True).extrude(2.2)
                .translate((f_mount_points[1][0]+(9.5*2)+1, f_can_y_offset+3, f_mount_points[1][1]))
            )
        )

        # Cable Tie
        .cut(
            cq.Workplane("ZX")
            .circle(5)
            .extrude(3)
            .faces(">Z")
            .hole(7)
            .translate((filler_mount_car_x_pos-9, -55, 16))
        )

        .cut(
            cq.Workplane()
            .rect(6, 9)
            .extrude(30)
            .translate((filler_mount_car_x_pos-11, -53, 0))

        )

        # Hop Cone
        .cut(
            cq.importers.importStep('imports/hop_cone.step')
            .rotate((0, 0, 0), (1, 0, 0), 90)
            .rotate((0, 0, 0), (0, 0, 1), 90)
            .translate((filler_mount_car_x_neg-0.8, -30, 3))
        )

        .cut(
            cq.importers.importStep('imports/hop_cone.step')
            .rotate((0, 0, 0), (1, 0, 0), 90)
            .rotate((0, 0, 0), (0, 0, 1), 90)
            .translate((filler_mount_car_x_pos-0.2, -30, 3))
        )


        # Rear Chamfers
        .faces(">Y").edges(">X").chamfer(16.5)
        .faces(">Y").edges("<X").chamfer(13.5)

        # Front Chamfer
        .faces("<Y").edges("|Z").chamfer(26, 9)
        .faces("<Y").edges("|Z").chamfer(4)

        # # Bottom Chamfer
        .faces("<Z").chamfer(0.5)


        # Front Cut
        .cut(
            cq.Workplane()
            .box(100, 0.2, 100)
            .translate((0, f_can_y_offset, 0))
        )

        # Split in half
        .cut( # Rear
            cq.Workplane()
            .rect(0.2, 20)
            .extrude(car_mount_z/4)
            .union(
                cq.Workplane().transformed(offset=(0, 0, (car_mount_z/4)*3))
                .rect(0.2, 20)
                .extrude(car_mount_z/4)
            )
            .union(
                cq.Workplane("ZX").transformed(offset=((car_mount_z/4)*2, 0, -10))
                .polygon(4, (car_mount_z/4)*2)
                .extrude(20)
                .edges("<X").chamfer(6)
                .faces("+Y and -Y").shell(0.2)
                .cut(
                    cq.Workplane().transformed(offset=(10, 0, 0))
                    .rect(20, 20)
                    .extrude(car_mount_z)
                )
            )
        )

        .cut( # Front Y Cut
            cq.Workplane().transformed(offset=(-(filler_dia/2)-1.1, f_can_y_offset+30, 0))
            .rect(0.2, 60)
            .extrude(car_mount_z)
        )
    )

    if not left:
        thing = (
            thing
            .cut(
                cq.Workplane().transformed(offset=(-(filler_dia/2)-1-25, f_can_y_offset+40, 0))
                .rect(50, 80)
                .extrude(car_mount_z)
            )
            .cut(
                cq.Workplane()
                .rect(50, 20)
                .extrude(car_mount_z)
                .translate((-25, 0, 0))
                .cut(
                    cq.Workplane("ZX").transformed(offset=((car_mount_z/4)*2, 0, -10))
                    .polygon(4, (car_mount_z/4)*2)
                    .extrude(20)
                    .edges("<X").chamfer(6)
                )

            )
        )

    if not right:
        thing = (
            thing
            .cut(
                cq.Workplane().transformed(offset=(-(filler_dia/2)-1+25, f_can_y_offset+40, 0))
                .rect(50, 80)
                .extrude(car_mount_z)
            )
            .cut(
                cq.Workplane()
                .rect(50, 20)
                .extrude(car_mount_z)
                .translate((25, 0, 0))
                .union(
                    cq.Workplane("ZX").transformed(offset=((car_mount_z/4)*2, 0, -10))
                    .polygon(4, (car_mount_z/4)*2)
                    .extrude(20)
                    .edges("<X").chamfer(6)
                )
            )
        )

    if not front:
        thing = (
            thing.cut(
                cq.Workplane().transformed(offset=(0, f_can_y_offset-10, 0))
                .rect(mount_x, 20)
                .extrude(car_mount_z)
            )
        )

    thing = thing.translate((0, mount_y, car_z_offset-(car_mount_z/2)-0.2))

    return(self.eachpoint(lambda loc: thing.val().located(loc), True)) 


def dfu_helper(self):
    thing = (
        cq.Workplane()
        .circle(3)
        .extrude(6) # 4.5
    )

    thing = (
        thing.union(
            cq.importers.importDXF('imports/dfu_a.dxf')
            .wires().toPending()
            .extrude(1)
        )
    )

    thing = (
        thing.union(
            cq.importers.importDXF('imports/dfu_b.dxf')
            .wires().toPending()
            .extrude(3) #2.5
        )
    )

    thing = thing.faces(">Z").hole(small_hole_dia)

    thing = (
        thing
        .rotate((0, 0, 0), (0, 1, 0), 90)
        .rotate((0, 0, 0), (1, 0, 0), 180)
        .translate((-37.4, 19.5, motor_z_offset-15.5))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def base(self, profile=False):

    mount_front     = (mount_f_y+(extrusion_xy/2))
    rear_x          = (solenoid_x_offset*2) + solenoid_x_thick + (base_wall_thick*2)
    rear_y          = (mount_f_y+(extrusion_xy/2)) + solenoid_y_offset + (solenoid_y_thick/2) + solenoid_wall_thick
    rear_z          = 66
    rear_motor_offset = rear_y - mount_front - motor_y_offset
    rear_poly_dim   = polygon_long_side((((rear_y - mount_front)-motor_y_offset))*2)-(base_wall_thick*2)-0.65-4

    poly_rad = rear_poly_dim/2
    motor_opening = solveHypAng(rear_poly_dim, 30)['opposite']
    front_offset = 5

    can = (
        cq.Workplane()
        .transformed(offset=(0, can_y_offset, 0))
        .placeSketch(
            cq.Sketch().circle(can_dia/2), 
            cq.Sketch().circle((can_dia/2)+3).moved(cq.Location(cq.Vector(0, 0, can_height)))
        )
        .loft()
    )

    # Main shell
    base_points = [
        # Rear +
        ((rear_x/2 , -(mount_front+front_offset)),              (rear_x/2, rear_y-mount_front)), 
        ((rear_x/2, rear_y-mount_front),                        (poly_rad , rear_y-mount_front)),
        # Poly
        ((poly_rad , rear_y-mount_front),                       (motor_opening/2, rear_y-mount_front-motor_opening+4)),
        ((motor_opening/2, rear_y-mount_front-motor_opening+4), (-motor_opening/2, rear_y-mount_front-motor_opening+4)),
        ((-motor_opening/2, rear_y-mount_front-motor_opening+4),(-poly_rad, rear_y-mount_front)),
        # Rear -
        ((-poly_rad, rear_y-mount_front),                       (-rear_x/2, rear_y-mount_front)),
        ((-rear_x/2, rear_y-mount_front),                       (-rear_x/2 , -(mount_front+front_offset))),
        # Front
        ((-rear_x/2 , -(mount_front+front_offset)),             (-can_dia/2-can_side_wall, can_y_offset-can_front_wall)),
        ((-can_dia/2-can_side_wall, can_y_offset-can_front_wall),(can_dia/2+can_side_wall, can_y_offset-can_front_wall)),
        ((can_dia/2+can_side_wall, can_y_offset-can_front_wall), (rear_x/2 , -(mount_front+front_offset))),


    ]

    base_sketch = (
        cq.Sketch()
        # Rear +
        .segment(base_points[0][0], base_points[0][1])
        .segment(base_points[1][0], base_points[1][1])
        # Rear Poly
        .segment(base_points[2][0], base_points[2][1])
        .segment(base_points[3][0], base_points[3][1])
        .segment(base_points[4][0], base_points[4][1])
        # Rear -
        .segment(base_points[5][0], base_points[5][1])
        .segment(base_points[6][0], base_points[6][1])
        # Front
        .segment(base_points[7][0], base_points[7][1])
        .segment(base_points[8][0], base_points[8][1])

        .close()
        .assemble()
    )

    rear_poly_sketch = (
        cq.Sketch()
        .segment(base_points[2][0], base_points[2][1])
        .segment(base_points[3][0], base_points[3][1])
        .segment(base_points[4][0], base_points[4][1])
        .close()
        .assemble()
    )

    front_base_sketch = (
        cq.Sketch()
        .segment(base_points[7][0], base_points[7][1])
        .segment(base_points[8][0], base_points[8][1])
        .segment(base_points[9][0], base_points[9][1])

        .close()
        .assemble()
    )

    front_slope = (
        cq.Workplane()
        .transformed(
            rotate=(65, 0, 0), 
            offset=(0, -(front_offset+mount_front+abs(can_y_offset)), 110)
        )
        .box(250, 250, 100)
    )
    corner_slope_l = (
        cq.Workplane()
        .transformed(
            rotate=(0, 35, 30), 
            offset=(-(rear_x+can_side_wall), can_y_offset, rear_z)
        )
        .box(140, 250, 250)
    )

    corner_slope_r = (
        cq.Workplane()
        .transformed(
            rotate=(0, -35, -30), 
            offset=((rear_x+can_side_wall), can_y_offset, rear_z)
        )
        .box(140, 250, 250)
    )

    # Main Body
    body = (
        cq.Workplane()
        .placeSketch(base_sketch)
        .extrude(rear_z)
    )

    # Front Cutouts
    body = (
        body
        .cut(front_slope)
        .faces("<Y").edges(">X").chamfer(5)
        .faces("<Y").edges("<X").chamfer(5)
    )

    body = (
        body
        .cut(can)
        .cut(corner_slope_l)
        .cut(corner_slope_r)
    )

    body = (
        body
        .faces("-Z or +Z")
        .shell(-base_wall_thick)
    )

    # Button
    body = (
        body
        .cut(
            cq.Workplane()
            .circle(9.75)
            .extrude(base_wall_thick+1)
            .rotate((0, 0, 0), (0, 1, 0), 90)
            .translate((button_x_offset-base_wall_thick, button_y_offset, button_z_offset))
        )
    )

    # Add the top
    top = (
        cq.Workplane()
        .placeSketch(
            base_sketch.moved(             cq.Location(cq.Vector(0, 0, rear_z))), 
            cq.Sketch().rect(21, 21).moved(cq.Location(cq.Vector(0, 0, rear_z+30)))
        )
        .loft()

        .cut(front_slope)
        .cut(can)
        .cut(corner_slope_l)
        .cut(corner_slope_r)
    )

    if profile:
        return(self.eachpoint(lambda loc: top.val().located(loc), True))

    top = (
        top
        .faces("-Z")
        .shell(-base_wall_thick)

        .cut(
            cq.Workplane()
            .rect(20.4, 20.4)
            .extrude(rear_z+30)

            .rect(24, 11)
            .extrude(rear_z+30)

            .pushPoints([(24/2, 0), (-24/2, 0)])
            .circle(5.5)
            .extrude(rear_z+30)
        )
        
    )

    body = body.union(top)

    # Thicken Rear Wall
    body = (
        body
        .union(
            cq.Workplane().transformed(offset=(-(liquid_nut_correction/2), motor_y_offset+(rear_motor_offset/2), 0))
            .rect(((solenoid_x_offset-(solenoid_x_thick/2))*2)+liquid_nut_correction, rear_motor_offset)
            .extrude(rear_z)
            .union(
                cq.Workplane().transformed(offset=(0, rear_y-mount_front-(solenoid_wall_thick/2), 0))
                .rect(rear_x, solenoid_wall_thick)
                .extrude(rear_z)
            )
            .cut(
                cq.Workplane()
                .placeSketch(rear_poly_sketch)
                .extrude(rear_z)
            )

        )
        .union(
            cq.Workplane().transformed(offset=(-((rear_x/2)-base_wall_thick-(liquid_nut_correction/2)), rear_y-mount_front-solenoid_wall_thick-2.5, solenoid_z_offset))
            .box(liquid_nut_correction, 5, 21.5)
            .faces("<Y")
            .edges("<Z")
            .chamfer(4.99)

        )
    )

    # Motor cutouts
    body = (
        body
        .faces(">Y")
        .workplane()
        .pushPoints([(x[0], x[1]) for x in mount_motor_points])
        .cboreHole(small_hole_dia, small_screw_head_dia, rear_motor_offset-3.5, depth=50)
    ) 

    body = (
        body
        .cut(
            cq.Workplane("ZX").transformed(offset=(motor_z_offset, 0, motor_y_offset))
            .circle(23/2)
            .extrude(50)

        )
        .cut(
            cq.Workplane("ZX").transformed(offset=(motor_z_offset/2, 0, motor_y_offset))
            .rect(motor_z_offset, 23)
            .extrude(50)
        )
    )

    # Power Cutout
    body = (
        body
        .cut(
            cq.Workplane("ZX").transformed(offset=(motor_z_offset, power_x_offset, 0))
            .circle(4)
            .extrude(50)
        )
        .cut(
            cq.Workplane("ZX").transformed(offset=(motor_z_offset+5, power_x_offset+(solveHypAng(15, 30)['adjacent']/2), 0))
            .polygon(6, 30)
            .extrude(rear_y-mount_front-solenoid_wall_thick)
            .union(
                cq.Workplane("ZX").transformed(offset=((motor_z_offset/2), power_x_offset, 0))
                .rect(motor_z_offset, solveHypAng(15, 30)['adjacent'])
                .extrude(rear_y-mount_front-solenoid_wall_thick)
            )
            .edges(">Y and <X")
            .chamfer(6.5, 11)
        )
        .cut(
            cq.Workplane("ZY").transformed(offset=(motor_z_offset, motor_y_offset+15+base_wall_thick, -power_x_offset))
            .lineTo(8.1, 0)
            .lineTo(60, 50) # 60
            .lineTo(0, 50)
            .lineTo(0, 0)
            .close()
            .revolve()
        )
        .cut(
            cq.Workplane("ZX").transformed(offset=(motor_z_offset, power_x_offset, 0))
            .circle(6.5)
            .extrude(rear_y-mount_front-solenoid_wall_thick)
        )
    )

    # PCB Power Cutout
    body = (
        body
        .cut(
            cq.Workplane("ZX").transformed(offset=(motor_z_offset+5-polygon_long_side(liquid_nut_correction), -(power_x_offset+(solveHypAng(15, 30)['adjacent']/2)+liquid_nut_correction), 0))
            .polygon(6, 30+polygon_long_side(liquid_nut_correction*2))
            .extrude(rear_y-mount_front-solenoid_wall_thick)
            .union(
                cq.Workplane("ZX").transformed(offset=(((motor_z_offset/2), -power_x_offset-(liquid_nut_correction/2), 0)))
                .rect(motor_z_offset, solveHypAng(15, 30)['adjacent']+liquid_nut_correction)
                .extrude(rear_y-mount_front-solenoid_wall_thick)
            )

            .edges(">Y and >X")
            .chamfer(11, 6.6)
        )
    )

    # Ball Lock Cutouts
    body = (
        body
        .cut(
            cq.Workplane("ZX").transformed(offset=(solenoid_z_offset, solenoid_x_offset, 0))
            .circle(6.75)
            .extrude(100)
        )

        .cut(
            cq.Workplane("ZX").transformed(offset=(solenoid_z_offset, -solenoid_x_offset, 0))
            .circle(6.75)
            .extrude(100)
        )
    )

    # Front Extrusion Mount
    f_ext_mount = (
            cq.importers.importDXF('imports/V_inner_a.dxf')
            .wires().toPending()
            .extrude(rear_z+30)
            .edges("<Y and >Z")
            .chamfer(1, 0.5)
        )

    f_ext_mount = (
        f_ext_mount
        .union(
            cq.Workplane().transformed(offset=(0, -(front_offset+mount_front-(extrusion_xy/2)/2)+(front_offset/4)-1.75, 0))
            .rect(6.05+6, front_offset+mount_front-(extrusion_xy/2)+3)
            .extrude(rear_z+28)
            .edges("<Y and >Z")
            .chamfer(6, front_offset+mount_front-(extrusion_xy/2)-0.01)
            .edges(">Y and |Z")
            .chamfer(3)
        )
        .cut(can)
    )

    # Rear Extrusion Mount
    r_ext_mount = (
        cq.importers.importDXF('imports/V_inner_c.dxf')
        .wires().toPending()
        .extrude(rear_z+30)
        .edges(">Y and >Z")
        .chamfer(1, 0.5)


        .union(
            cq.Workplane().transformed(offset=(0, motor_y_offset-(motor_thick/2)+2, 0))
            .rect(6.05+6, motor_thick+4)
            .extrude(rear_z+29)
            .edges(">Y and >Z")
            .chamfer(29, motor_thick+3.99)
            .edges("<Y and |Z")
            .chamfer(3)
        )
    )

    ext_mounts = (
        f_ext_mount.union(r_ext_mount)
        .cut(
        cq.Workplane().transformed(rotate=(45, 0, 0), offset=(0, 0, 0))
        .box(20, rear_z*1.8, rear_z*1.8)
        )

        # Safe Chamfer
        .cut(
            cq.Workplane().transformed(rotate=(0, 45, 0), offset=(7.25, 0, rear_z))
            .box(20, 16.25, 20)
        )
        .cut(
            cq.Workplane().transformed(rotate=(0, 45, 0), offset=(-7.25, 0, rear_z))
            .box(20, 16.25, 20)
        )

    )

    # Dodgy AF
    body = (
        body
        .union(
            cq.Workplane("XZ")
            .lineTo(base_wall_thick, 1)
            .lineTo(0, 1)
            .close()
            .extrude(-60)
            .translate((-(rear_x/2)+base_wall_thick, -11, rear_z-1))
        )
        .union(
            cq.Workplane("XZ")
            .lineTo(base_wall_thick, -1)
            .lineTo(base_wall_thick, 0)
            .close()
            .extrude(-60)
            .translate((rear_x/2-(base_wall_thick*2), -11, rear_z))
        )
    )

    # Feet Rear
    body = (
        body
        .faces("<Z")
        .workplane()
        .pushPoints([((rear_x/2)-6, 6), (-((rear_x/2)-6), 6)])
        .cskHole(thread_insert_dia, thread_insert_dia+1, 50, depth=6)
    )

    # Feet Front
    body = (
        body
        .union(
        cq.Workplane()
        .placeSketch(front_base_sketch)
        .extrude(base_wall_thick)
        .faces("<Y").edges(">X").chamfer(5)
        .faces("<Y").edges("<X").chamfer(5)
        .cut(
            cq.Workplane()
            .rect(rear_x-(base_wall_thick*2), front_offset+mount_front+abs(can_y_offset))
            .extrude(base_wall_thick)
            .edges("|Z").chamfer(front_offset)
        )
        .cut(can)
        )
        .union(
            cq.Workplane()
            .pushPoints([((can_dia/2)+6, can_y_offset+10), (-(can_dia/2)-6, can_y_offset+10)])
            .circle(5.5)
            .extrude(10)
        )
        .faces("<Z")
        .workplane()
        .pushPoints([
            ((can_dia/2)+6, rear_y-(mount_f_y+(extrusion_xy/2)+can_y_offset+10)), 
            (-(can_dia/2)-6, rear_y-(mount_f_y+(extrusion_xy/2)+can_y_offset+10))
        ])
        .cskHole(thread_insert_dia, thread_insert_dia+1, 50, depth=6)
    )

    thing = (
        body
        .union(ext_mounts)
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def microswitch(self):
    thing = (
        cq.importers.importStep('imports/SPDT.stp')
        .rotate((0, 0, 0), (1, 0, 0), 180)
        .rotate((0, 0, 0), (0, 0, 1), 270)
        .translate((estop_x_offset-0.6, estop_y_offset, extrusion_z_offset+extrusion_length+estop_z_offset))
    )
    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def pulley(self):
    thing = (
        cq.Workplane("ZX")
        .circle(9.5/2)
        .extrude(8.52)
        .union(
            cq.Workplane("ZX")
            .circle(13/2)
            .extrude(1)
        )
        .union(
            cq.Workplane("ZX").transformed(offset=(0, 0, 8.52))
            .circle(13/2)
            .extrude(-1)
        )
        .faces("<Z")
        .hole(3.2)
    )

    thing = thing.translate((0, pulley_y_offset, extrusion_z_offset+extrusion_length+pulley_z_offset))

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def belt(self):
    pulley_z = extrusion_z_offset+extrusion_length+pulley_z_offset
    pulley_y = pulley_y_offset+1.25

    belt_z              = pulley_z-motor_z_offset
    belt_z_short_bottom = car_z_offset-motor_z_offset-5
    belt_z_short_top    = pulley_z-car_z_offset-5
    belt_w = 6
    belt_offset = -0.2

    top = (
        cq.Workplane("ZX")
        .circle(13.5/2)
        .extrude(belt_w)

        .cut(
            cq.Workplane("ZX")
            .circle(9.5/2)
            .extrude(8.52)
        )

        .cut(
            cq.Workplane("ZX")
            .rect(14, 14, True)
            .extrude(14)
            .translate((0, 0, -7))
        )

        .translate((0, pulley_y, pulley_z))
    )

    bottom = (
        cq.Workplane("ZX")
        .circle(13.5/2)
        .extrude(belt_w)

        .cut(
            cq.Workplane("ZX")
            .circle(9.5/2)
            .extrude(8.52)
        )

        .cut(
            cq.Workplane("ZX")
            .rect(14, 14, True)
            .extrude(14)
            .translate((0, 0, 7))
        )

        .translate((0, pulley_y, motor_z_offset))
    )

    side_a = (
        cq.Workplane()
        .box(2, belt_w, belt_z)

        .translate(((13.5/2)-1, pulley_y+(belt_w/2), motor_z_offset+(belt_z/2)))
    )

    side_b = (
        # Bottom
        cq.Workplane()
        .box(2, belt_w, belt_z_short_bottom)
        .translate((-(13.5/2)+1, pulley_y+(belt_w/2), motor_z_offset+(belt_z_short_bottom/2)))

        # Bottom Loop
        .union(
            cq.Workplane("ZX")
            .circle(8/2)
            .extrude(belt_w)

            .cut(
                cq.Workplane("ZX")
                .circle(4/2)
                .extrude(belt_w)
            )

            .cut(
                cq.Workplane("ZX")
                .rect(14, 14, True)
                .extrude(14)
                .translate((0, 0, -7))
            )

            .translate((-2.75, pulley_y, car_z_offset-5))
        )

        # Bottom Clamped
        .union(
            cq.Workplane()
            .box(2, belt_w, 20)
            .translate((-(13.5/2)+1+6, pulley_y+(belt_w/2), motor_z_offset+(belt_z_short_bottom/2)+((belt_z_short_bottom/2-10))))
        )

        # Top
        .union(
            cq.Workplane()
            .box(2, belt_w, belt_z_short_top)
            .translate((-(13.5/2)+1, pulley_y+(belt_w/2), pulley_z-(belt_z_short_top/2)))
        )

        # Top Loop
        .union(
            cq.Workplane("ZX")
            .circle(8/2)
            .extrude(belt_w)

            .cut(
                cq.Workplane("ZX")
                .circle(4/2)
                .extrude(belt_w)
            )

            .cut(
                cq.Workplane("ZX")
                .rect(14, 14, True)
                .extrude(14)
                .translate((0, 0, 7))
            )

            .translate((-2.75, pulley_y, car_z_offset+5))
        )

        # Top Clamped
        .union(
            cq.Workplane()
            .box(2, belt_w, 20)
            .translate((-(13.5/2)+1+6, pulley_y+(belt_w/2), pulley_z-(belt_z_short_top/2)-((belt_z_short_top/2-10))))
        )
    )



    thing = top.union(bottom).union(side_a).union(side_b)
    thing = thing.translate((0, belt_offset, 0))

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def idle_stop(self):

    top_y  = 47
    stop_z = -10

    inner_a = (
        cq.importers.importDXF('imports/V_inner_a.dxf')
        .wires().toPending()
        .extrude(stop_z)
    )
    inner_c = (
        cq.importers.importDXF('imports/V_inner_c.dxf')
        .wires().toPending()
        .extrude(stop_z)
    )

    idler = (
        cq.Workplane()
        .polygon(6, 40)
        .extrude(stop_z)
        .union(
            cq.Workplane().transformed(offset=(0, top_y/2, 0))
            .rect(26, top_y)
            .extrude(stop_z)
            
        )

        .cut(
            cq.Workplane()
            .rect(20.3, 20.3)
            .extrude(stop_z)
        )

        .union(inner_a)
        .union(inner_c)

    )

    # Top
    top = (
        cq.Workplane()
        .polygon(6, 40)
        .extrude(15)
        .union(
            cq.Workplane().transformed(offset=(0, top_y/2, 0))
            .rect(26, top_y)
            .extrude(15)
        )
    )

    idler = (
        idler
        .union(top)
        .cut(
            cq.Workplane().transformed(offset=(0.5, -(extrusion_xy/2)-25-2, -25))
            .rect(50, 50)
            .extrude(50)
        )
        .faces(">Z").chamfer(3)
    )

    # Microswitch cutouts
    idler = (
        idler
        .cut(
            cq.Workplane().transformed(offset=(estop_x_offset, estop_y_offset, stop_z))
            .rect(7, 13)
            .extrude(6.7)
        )
        .cut(
            cq.Workplane().transformed(offset=(estop_x_offset-1, estop_y_offset, 0))
            .rect(5, 12)
            .extrude(stop_z)
        )

        # Holes
        .cut(
            cq.Workplane("YZ").transformed(offset=(estop_y_offset+3.25, stop_z+estop_z_offset+8.5, estop_x_offset-3))
            .circle(0.7)
            .extrude(-5)
        )
        .cut(
            cq.Workplane("YZ").transformed(offset=(estop_y_offset-3.25, stop_z+estop_z_offset+8.5, estop_x_offset-3))
            .circle(0.7)
            .extrude(-5)
        )

        # Channel
        .cut(
            cq.Workplane("YZ").transformed(offset=(estop_y_offset/2, stop_z+5.5, 4))
            .circle(estop_y_offset-2)
            .extrude(7.5)
            .cut(
                cq.Workplane("YZ").transformed(offset=(estop_y_offset/2, -25, 4))
                .rect(50, 50)
                .extrude(7.5)
            )
            .cut(
                cq.Workplane("YZ").transformed(offset=(-25-4.25, 0, 4))
                .rect(50, 50)
                .extrude(7.5)
            )
        )

    )

    # Pulley cutouts
    idler = (
        idler
        .cut(
            cq.Workplane("ZX")
            .circle(18/2)
            .extrude(10.5)
            .translate((0, pulley_y_offset-1, pulley_z_offset))
        )
        .cut(
            cq.Workplane()
            .rect(18, 10.5)
            .extrude(20)
            .translate((0, pulley_y_offset+5.25-1, pulley_z_offset-20))
        )
        .faces(">Y")
        .workplane()
        .center(0, pulley_z_offset)
        .hole(2.5, 30)

        .faces(">Y")
        .workplane()
        .cboreHole(small_hole_dia, small_screw_head_dia, 3, 10)
    )


    thing = (
        idler
        # Side Chamfers
        .edges(">X").chamfer(2)
        .edges("<X").chamfer(2)
        .faces(">Y").edges("|Z").chamfer(3)

        # Beer Line Clearance
        .faces(">Z").workplane()
        .pushPoints([(12, -top_y), (-12, -top_y)])
        .hole(11)

        .cut(
            cq.Workplane().transformed(offset=(0, 0, 5))
            .rect(24, 10)
            .extrude(20)
        )
        .cut(
            cq.Workplane().transformed(offset=(-8, 0, 0))
            .rect(8, 8.5)
            .extrude(5)
        )

        # Extrusion Mount
        .cut(
            cq.Workplane()
            .rect(big_hole_dia, 8)
            .extrude(0.3)
            .rect(big_hole_dia, big_hole_dia)
            .extrude(0.6)
            .circle(big_hole_dia/2)
            .extrude(20)

        )

        # Remove Sharp Points
        .faces(">X")
        .workplane()
        .pushPoints([(-top_y, 0)])
        .hole(big_screw_head_dia)

        # Add Wire Path
        .cut(
            cq.Workplane().transformed(offset=(estop_x_offset-0.35, 5, 0))
            .rect(3.7, 20)
            .extrude(stop_z)
        )

        # Bottom Chamfer
        .faces("<Z")
        .chamfer(0.3)
        .translate((0, 0, extrusion_z_offset+extrusion_length))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def purge_cap(self):
        thing = (
            cq.Workplane()
            .circle(56/2)
            .extrude(5)
            .faces("|Z").edges("<Z")
            .chamfer(4.3)
            .faces(">Z").workplane()
            .hole(9.5)
            .faces(">Z").workplane()
            .center(sensor_x_offset, 0)
            .hole(2.4)
            .translate((0, filler_y_offset, can_height-foot_height-3))

            .faces().chamfer(0.3)
        )

        return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def handle_stop(self):
        thing = (
            cq.Workplane()
            .rect(26, 21)
            .extrude(30)

            .faces(">Z")
            .workplane()
            .center(0, -2.25)
            .rect(20.5, 18.5)
            .extrude(-22, combine="cut")

            .faces("<Z").edges(">Y").chamfer(8)
            .faces("<Z").workplane()
            .hole(7)

            .faces().chamfer(0.3)

        )

        return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def foot(self):
    thing = (
        cq.Workplane()
        .circle(11.5/2)
        .extrude(foot_height)

        .faces(">Z")
        .cboreHole(small_hole_dia, 7, 5)

        .faces(">Z").edges().item(0).chamfer(4, 0.5)
        .faces("<Z").edges().item(1).chamfer(0.3)
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def condensation_cover(self):
    x_len = ((solenoid_x_offset*2)+solenoid_x_thick)-2
    y_len = (servo_y_offset*2)-4
    
    # Main Body
    thing = (
        cq.Workplane()
        .rect(x_len, y_len-2)
        .extrude(65)

        .faces("<X").edges(">Z").chamfer(25, solenoid_x_offset-3)
        .faces("<Y").edges(">Z").chamfer(30)
        .faces(">Y").edges(">Z").chamfer(22, 30)
        .faces("<Y").edges("<X").chamfer(23)

        .cut(
            cq.Workplane()
            .box(200, 200, 200)
            .translate((103.025, 0, 0))
        )

        .faces("-Z or #Z")
        .shell(-2)
    )

    thing = (
        thing
        # Front Clearance
        .cut(
            cq.Workplane()
            .box(200, 200, 200)
            .translate((0, -(100+(abs(can_y_offset)-20)), 0))
        )

        # V Slot Clearance
        .cut(
            cq.Workplane()
            .rect(20.2, 20.2)
            .extrude(65)
        )

        # Can Clearance
        .cut(
            cq.Workplane()
            .circle((can_dia/2)+4)
            .extrude(65)
            .translate((0, can_y_offset, 0))
        )

        # V Slot Interface
        .union(
            cq.importers.importDXF('imports/V_inner_d.dxf')
            .wires().toPending()
            .extrude(5)
            .translate((0, 0, 60))

            .faces(">Z").edges().item(4).chamfer(2.2)
            .faces(">Z").edges().item(9).chamfer(2.2)
        )

        # Rear Clearance
        .cut(
            cq.Workplane()
            .box((solenoid_x_offset*2)-solenoid_x_thick+4, 32, 200)
            .translate((0, y_len/2, 0))
        )

        # Make the v slot area easier to print
        .faces(">Z").chamfer(0.5)
        .faces("<Z[-1]").chamfer(0.5)

        # remove sharp edge on can curve
        .faces().edges(selectors.NearestToPointSelector((0, -20))).chamfer(0.5)
    
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def ebb42(self):
    thing = (
        cq.importers.importStep('imports/EBB42.step')
        .rotate((0, 0, 0), (0, 1, 0), -90)
        .translate((-31.4, -16, motor_z_offset-20))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))


def usb_elbow(self):
    thing = (
        cq.Workplane()
        .rect(16.4, 18.8, centered=False).extrude(6)
        .cut(
            cq.Workplane()
            .rect(10, 18.8-10.8, centered=False).extrude(6)
            .translate((10.8, 0, 0))
        )
        .edges().fillet(0.5)

        .union(
            cq.Workplane()
            .box(6.75, 8.3, 2.45)
            .edges("#Z and |X").fillet(1.22)
            .translate((16.4+(6.75/2), 18.8-5.1, 3))
        )

        .cut(
            cq.Workplane()
            .box(6.75, 8.3, 2.45)
            .edges("#Z and |X").fillet(1.22)
            
            .cut(
                cq.Workplane()
                .box(5.75, 7.3, 0.6)
                .edges("#Z and |X").fillet(0.275)
                .translate((0.5, 0, 0))

            )

            .rotate((0, 0, 0), (0, 0, 1), 90)
            .translate((5.4, 6.75/2, 3))
        )

        .rotate((0, 0, 0), (1, 0, 0), 90)
        .rotate((0, 0, 0), (0, 0, 1), -90)

        .translate((-30.05, 44.5, 4.8))
    )

    return(self.eachpoint(lambda loc: thing.val().located(loc), True))

cq.Workplane.M5_button_screw    = M5_button_screw
cq.Workplane.M3_cap_screw       = M3_cap_screw
cq.Workplane.M3_pan_screw       = M3_pan_screw
cq.Workplane.M3_nutsert         = M3_nutsert
cq.Workplane.M3_washer          = M3_washer
cq.Workplane.M3_T_nut           = M3_T_nut
cq.Workplane.M3_square_nut      = M3_square_nut
cq.Workplane.M2_pan_screw       = M2_pan_screw
cq.Workplane.quater_bsp_nut     = quater_bsp_nut
cq.Workplane.extrusion          = extrusion
cq.Workplane.MGN12_rail         = MGN12_rail
cq.Workplane.MGN12H_car         = MGN12H_car
cq.Workplane.MG996R_servo       = MG996R_servo
cq.Workplane.gas_solenoid       = gas_solenoid
cq.Workplane.filler_tube        = filler_tube
cq.Workplane.ball_lock          = ball_lock
cq.Workplane.duo_elbow          = duo_elbow
cq.Workplane.threaded_elbow     = threaded_elbow
cq.Workplane.duo_reducer        = duo_reducer
cq.Workplane.power_socket       = power_socket
cq.Workplane.button             = button
cq.Workplane.motor_pulley       = motor_pulley
cq.Workplane.nema_17            = nema_17
cq.Workplane.motor_mount        = motor_mount
cq.Workplane.pcb_spacer         = pcb_spacer
cq.Workplane.tube_section       = tube_section
cq.Workplane.carriage           = carriage
cq.Workplane.dfu_helper         = dfu_helper
cq.Workplane.base               = base
cq.Workplane.microswitch        = microswitch
cq.Workplane.pulley             = pulley
cq.Workplane.belt               = belt
cq.Workplane.idle_stop          = idle_stop
cq.Workplane.filler_mount       = filler_mount
cq.Workplane.purge_cap          = purge_cap
cq.Workplane.handle_stop        = handle_stop
cq.Workplane.foot               = foot
cq.Workplane.condensation_cover = condensation_cover
cq.Workplane.ebb42              = ebb42
cq.Workplane.usb_elbow          = usb_elbow
