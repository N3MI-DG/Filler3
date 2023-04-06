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

import math

def polygon_long_side(dia, sides=6): return((dia * math.sin(math.pi / sides) / math.cos(math.pi / sides))*2)

def solveOppHyp(opposite, hypotenuse):
    # solve for Adjacent
    adjacent = (hypotenuse * hypotenuse) - (opposite * opposite)
    adjacent = math.sqrt(adjacent)

    # solve for angle x
    tanx = opposite / adjacent
    atanx = math.atan(tanx) # result in radians
    anglex = atanx * 180 / math.pi # converted to degrees

    return({'opposite': opposite, 'adjacent': adjacent, 'hypotenuse': hypotenuse, 'anglex': anglex})

def solveHypAng(hypotenuse, anglex):
	# convert degrees to radians
	anglexinradians = anglex * math.pi / 180

	# solve for Opposite
	opposite = math.sin(anglexinradians) * hypotenuse

	# solve for Adjacent
	adjacent = math.cos(anglexinradians) * hypotenuse
   
	return {'opposite': opposite, 'adjacent': adjacent, 'hypotenuse': hypotenuse, 'anglex': anglex}