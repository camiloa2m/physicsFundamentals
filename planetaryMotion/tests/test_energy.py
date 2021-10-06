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
    for i in range(500001):
        xc, yc, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        energy.append(planet.get_energy())
        numeric.euler_step(deltat)

def euler_cromer(planet, numeric, xpos, ypos, tpos, energy):
    for i in range(5000001):
        xc, yc, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        energy.append(planet.get_energy())
        numeric.euler_cromer_step(deltat)

def midpoint(planet, numeric, xpos, ypos, tpos, energy):
    for i in range(500001):
        xc, yc, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        energy.append(planet.get_energy())
        numeric.midpoint_step(deltat)

m1, x01, y01, v01, a01 = 1., 3., 0., 2., 90
m2, x02, y02, v02, a02 = 1., 1., 0., 8., 90
deltat = 0.00001

########################################################

planet1 = pt.Particle("Planet 1", x02, y02, v02, a02, m2)
planet1.set_force(fr.Forces(grav_force, pt.GM))

planet2 = pt.Particle("Planet 2", x02, y02, v02, a02, m2)
planet2.set_force(fr.Forces(grav_force, pt.GM))

planet3 = pt.Particle("Planet 3", x02, y02, v02, a02, m2)
planet3.set_force(fr.Forces(grav_force, pt.GM))

xpos1, ypos1, tpos1, energy1 = [], [], [], []
xpos2, ypos2, tpos2, energy2= [], [], [], []
xpos3, ypos3, tpos3, energy3= [], [], [], []

numeric1 = sv.Solver(planet1, "Euler", deltat)
numeric2 = sv.Solver(planet2, "Euler-Cromer", deltat)
numeric3 = sv.Solver(planet3, "Midpoint", deltat)

#euler(planet1, numeric1, xpos1, ypos1, tpos1, energy1)
euler_cromer(planet2, numeric2, xpos2, ypos2, tpos2, energy2)
#midpoint(planet3, numeric3, xpos3, ypos3, tpos3, energy3)

#########################################################

planet1p = pt.Particle("Planet 1p", x01, y01, v01, a01, m1)
planet1p.set_force(fr.Forces(grav_force, pt.GM))

planet2p = pt.Particle("Planet 2p", x01, y01, v01, a01, m1)
planet2p.set_force(fr.Forces(grav_force, pt.GM))

planet3p = pt.Particle("Planet 3p", x01, y01, v01, a01, m1)
planet3p.set_force(fr.Forces(grav_force, pt.GM))

xpos1p, ypos1p, tpos1p, energy1p = [], [], [], []
xpos2p, ypos2p, tpos2p, energy2p = [], [], [], []
xpos3p, ypos3p, tpos3p, energy3p = [], [], [], []

numeric1p = sv.Solver(planet1p, "Euler", deltat)
numeric2p = sv.Solver(planet2p, "Euler-Cromer", deltat)
numeric3p = sv.Solver(planet3p, "Midpoint", deltat)

#euler(planet1p, numeric1p, xpos1p, ypos1p, tpos1p, energy1p)
euler_cromer(planet2p, numeric2p, xpos2p, ypos2p, tpos2p, energy2p)
#midpoint(planet3p, numeric3p, xpos3p, ypos3p, tpos3p, energy3p)

energyEuler, energyEuler_Cromer, energyMidpoint = [], [], []

for i in range(len(energy2)):
    #energyEuler.append(energy1[i]+energy1p[i])
    energyEuler_Cromer.append(energy2[i]+energy2p[i])
    #energyMidpoint.append(energy3[i]+energy3p[i])

#Generate Plots -------------------------------------------------

fig, ax = plt.subplots()
# ax.plot(xpos1, ypos1, '-', label='Euler')
# ax.plot(xpos2, ypos2, '-', label='Euler-Cromer')
# ax.plot(xpos3, ypos3, '-', label='Midpoint')

#print(energyEuler)
#ax.plot(tpos1, energyEuler, '-', label='Euler')
ax.plot(tpos2, energyEuler_Cromer, '-', label='Euler-Cromer')
#ax.plot(tpos3, energyMidpoint, '-', label='Midpoint')

ax.set(xlabel='t (yr)', ylabel='energy (earths*AU^2/yr^2)',
       title='Total energy with dt = 0.00001 and 5000000 iterations')
ax.grid()

plt.legend()
plt.show()
