import sys
sys.path.insert(0, "../")

import particle.particle as pt
import forces.forces as fr
import solver.solver as sv
import matplotlib.pyplot as plt
import numpy as np

def grav_force(state, params):
    xp, yp, vxp, vyp, _ = state
    GM = params
    r2 = xp**2 + yp**2
    r3 = r2*np.sqrt(r2)
    axp = -((GM*xp)/r3)
    ayp = -((GM*yp)/r3)
    return vxp, vyp, axp, ayp, 1.

def euler(planet, numeric, xpos, ypos, tpos, energy):
    for i in range(101):
        xc, yc, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        energy.append(planet.get_energy())
        numeric.euler_step(deltat)

def euler_cromer(planet, numeric, xpos, ypos, tpos, energy):
    for i in range(10001):
        xc, yc, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        energy.append(planet.get_energy())
        numeric.euler_cromer_step(deltat)

def midpoint(planet, numeric, xpos, ypos, tpos):
    for i in range(101):
        xc, yc, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        energy.append(planet.get_energy())
        numeric.midpoint_step(deltat)

m1, x01, y01, v01, a01 = 1., 2., 0., 4.442882938, 90
m2, x02, y02, v02, a02 = 1., 1., 0., 8., 90
deltat = 0.001

planet1 = pt.Particle("Planet X", x01, y01, v01, a01, m1)
planet1.set_force(fr.Forces(grav_force, pt.GM))

planet2 = pt.Particle("Planet Y", x02, y02, v02, a02, m2)
planet2.set_force(fr.Forces(grav_force, pt.GM))

xpos1, ypos1, tpos1, energy1 = [], [], [], []
xpos2, ypos2, tpos2, energy2= [], [], [], []

numeric1 = sv.Solver(planet1, "Euler-Cromer", deltat)
numeric2 = sv.Solver(planet2, "Euler-Cromer", deltat)

euler_cromer(planet1, numeric1, xpos1, ypos1, tpos1, energy1)
euler_cromer(planet2, numeric2, xpos2, ypos2, tpos2, energy2)

#Generate Plots -------------------------------------------------

fig, ax = plt.subplots()
ax.plot(xpos1, ypos1, '-', label='Planet X')
ax.plot(xpos2, ypos2, '-', label='Planet Y')

#ax.plot(tpos1, energy1, '-', label='Energy Planet X')
#ax.plot(tpos2, energy2, '--', label='Energy Planet Y')

ax.set(xlabel='x (a.u.)', ylabel='y (a.u.)',
       title='Two planets')
ax.grid()

plt.legend()
plt.show()
