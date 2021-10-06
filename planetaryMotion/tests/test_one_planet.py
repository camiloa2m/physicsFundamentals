import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, "../")

import particle.particle as pt
import forces.forces as fr
import solver.solver as sv

#Function Definitions

def grav_force(state, params):
    xp, yp, vxp, vyp, _ = state
    GM = params
    r2 = xp**2 + yp**2
    r3 = r2*np.sqrt(r2)
    axp = -((GM*xp)/r3)
    ayp = -((GM*yp)/r3)
    return vxp, vyp, axp, ayp, 1.

def euler(planet, numeric, xpos, ypos, tpos):
    for i in range(1000001):
        xc, yc, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        numeric.euler_step(deltat)

def euler_cromer(planet, numeric, xpos, ypos, tpos):
    for i in range(10002):
        xc, yc, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        numeric.euler_cromer_step(deltat)

def midpoint(planet, numeric, xpos, ypos, tpos):
    for i in range(5002):
        xc, yc, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        numeric.midpoint_step(deltat)

#Initial Variables and lists

m, x0, y0, v0, a0 = 1., 3., 0., 2., 90
deltat = 0.001
sim_params = pt.GM

planet = pt.Particle("Planet X", x0, y0, v0, a0, m)
planet_force = fr.Forces(grav_force, sim_params)
planet.set_force(planet_force)

planet2 = pt.Particle("Planet Y", x0, y0, v0, a0, m)
planet2.set_force(planet_force)

planet3 = pt.Particle("Planet Z", x0, y0, v0, a0, m)
planet3.set_force(planet_force)

xposEuler = []
yposEuler = []
tposEuler = []

xposEulerCromer = []
yposEulerCromer = []
tposEulerCromer = []

xposMidpoint = []
yposMidpoint = []
tposMidpoint = []

numeric1 = sv.Solver(planet, "Euler", deltat)
numeric2 = sv.Solver(planet2, "Euler-Cromer", deltat)
numeric3 = sv.Solver(planet3, "Midpoint", deltat)

#euler(planet, numeric1, xposEuler, yposEuler, tposEuler)
euler_cromer(planet2, numeric2, xposEulerCromer, yposEulerCromer, tposEulerCromer)
#midpoint(planet3, numeric3, xposMidpoint, yposMidpoint, tposMidpoint)

#Generate Plots

fig, ax = plt.subplots()
#ax.plot(xposEuler, yposEuler, '-', label='Euler')
ax.plot(xposEulerCromer, yposEulerCromer, '-', label='Euler-Cromer')
#ax.plot(xposMidpoint, yposMidpoint, '-', label='Midpoint')

ax.set(xlabel='x (AU)', ylabel='y (AU)',
       title='Planet :D')
ax.grid()

plt.legend()
plt.show()
