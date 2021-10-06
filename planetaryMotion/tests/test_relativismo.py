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
    GM, delta_sim = params
    r = np.sqrt(xp**2 + yp**2)
    r_delta = r**(3+delta_sim)
    axp = -((GM*xp)/(r_delta))
    ayp = -((GM*yp)/(r_delta))
    return vxp, vyp, axp, ayp, 1.

def euler_cromer(planet, numeric, angles):
    for i in range(6260):
        xc, yc, _, _, tc = planet.get_state()
        t.append(tc)
        ang = planet.get_angle()/np.pi
        angles.append(ang)
        numeric.euler_cromer_step(deltat)


#Initial Variables and lists
deltat = 0.001
m, x0, y0, v0, a0 = 1., 1., 0., 5, 90

delta_sim_1 = 0.001
delta_sim_2 = 0.005
delta_sim_3 = 0.01
delta_sim_4 = 0.05
delta_sim_5 = 0.1


sim_params_1 = pt.GM, delta_sim_1
sim_params_2 = pt.GM, delta_sim_2
sim_params_3 = pt.GM, delta_sim_3
sim_params_4 = pt.GM, delta_sim_4
sim_params_5 = pt.GM, delta_sim_5

planet_1 = pt.Particle("Planet Y", x0, y0, v0, a0, m)
planet_1.set_force(fr.Forces(grav_force, sim_params_1))

planet_2 = pt.Particle("Planet Y", x0, y0, v0, a0, m)
planet_2.set_force(fr.Forces(grav_force, sim_params_2))

planet_3 = pt.Particle("Planet Y", x0, y0, v0, a0, m)
planet_3.set_force(fr.Forces(grav_force, sim_params_3))

planet_4 = pt.Particle("Planet Y", x0, y0, v0, a0, m)
planet_4.set_force(fr.Forces(grav_force, sim_params_4))

planet_5 = pt.Particle("Planet Y", x0, y0, v0, a0, m)
planet_5.set_force(fr.Forces(grav_force, sim_params_5))

t = []
angles_1, angles_2, angles_3, angles_4, angles_5 = [], [], [], [], []
graph_angles_1, graph_angles_2, graph_angles_3, graph_angles_4, graph_angles_5 = [], [], [], [], []
graph_time = []

numeric_1 = sv.Solver(planet_1, "Euler-Cromer", deltat)
euler_cromer(planet_1, numeric_1, angles_1)

numeric_2 = sv.Solver(planet_2, "Euler-Cromer", deltat)
euler_cromer(planet_2, numeric_2, angles_2)

numeric_3 = sv.Solver(planet_3, "Euler-Cromer", deltat)
euler_cromer(planet_3, numeric_3, angles_3)

numeric_4 = sv.Solver(planet_4, "Euler-Cromer", deltat)
euler_cromer(planet_4, numeric_4, angles_4)

numeric_5 = sv.Solver(planet_5, "Euler-Cromer", deltat)
euler_cromer(planet_5, numeric_5, angles_5)

val = True
cont = 0
time = 0
for i in range(len(angles_1)):
    if(val == True):
        graph_angles_1.append(angles_1[i])
        graph_angles_2.append(angles_2[i])
        graph_angles_3.append(angles_3[i])
        graph_angles_4.append(angles_4[i])
        graph_angles_5.append(angles_5[i])
        graph_time.append(time)
        val = False
    else:
        if(cont == 626):
            time += 1
            graph_angles_1.append(angles_1[i])
            graph_angles_2.append(angles_2[i])
            graph_angles_3.append(angles_3[i])
            graph_angles_4.append(angles_4[i])
            graph_angles_5.append(angles_5[i])
            graph_time.append(time)
            cont = 0
        cont += 1
#Generate Plots

fig, ax = plt.subplots()

ax.plot(graph_time, graph_angles_1, 'ro', label='0.001')
ax.plot(graph_time, graph_angles_2, 'bo', label='0.005')
ax.plot(graph_time, graph_angles_3, 'go', label ='0.01')
ax.plot(graph_time, graph_angles_4, 'co', label='0.05')
ax.plot(graph_time, graph_angles_5, 'yo', label ='0.1')
#ax.plot(xposEulerCromer, yposEulerCromer, '-')

ax.set(xlabel='time (yr)', ylabel='Angle per revolution',
       title='Angles per revolution with different deltas.')
ax.grid()

plt.legend()
plt.show()
