import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, "../")

import particle.particle as pt
import forces.forces as fr

#Function Definitions

def analytic_solution(tf, v0, a0):
    #This assumes x0 = 0, y0 = 0, m = 1
    v0x = v0 * np.cos(np.radians(a0))
    v0y = v0 * np.sin(np.radians(a0))
    xa = v0x * (1. - np.exp(-pt.DRAG * tf)) / pt.DRAG
    ya = (v0y + pt.G / pt.DRAG) * (1. - np.exp(-pt.DRAG * tf)) \
       - pt.G * tf
    return xa, ya / pt.DRAG

def resistive_falling(state, params):
    xp, yp, vxp, vyp, _ = state
    mass, grav, drag = params
    axp = -drag * vxp / mass
    ayp = -grav - drag * vyp / mass
    return vxp, vyp, axp, ayp, 1.

def euler(ball, xpos, ypos, tpos):
    while True:
        xc, yc, _, _, tc = ball.get_state()
        if yc < 0: break
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        ball.euler_step(deltat)

def euler_cromer(ball, xpos, ypos, tpos):
    while True:
        xc, yc, _, _, tc = ball.get_state()
        if yc < 0: break
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        ball.euler_cromer_step(deltat)

def midpoint(ball, xpos, ypos, tpos):
    while True:
        xc, yc, _, _, tc = ball.get_state()
        if yc < 0: break
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        ball.midpoint_step(deltat)

def exact(ball, xpos, ypos, tposReference):
    for t in tposReference:
        x, y = analytic_solution(t, ball.v0, ball.a0)
        xpos.append(x)
        ypos.append(y)

#Initial Variables and Lists

m, x0, y0, v0, a0 = 1., 0., 0., 1., 45
deltat = 0.01
sim_params = m, pt.G, pt.DRAG

ball = pt.Particle("Pelota 1", x0, y0, v0, a0, m)
ball_force = fr.Forces(resistive_falling, sim_params)
ball.set_force(ball_force)

ball2 = pt.Particle("Pelota 2", x0, y0, v0, a0, m)
ball2.set_force(ball_force)

ball3 = pt.Particle("Pelota 3", x0, y0, v0, a0, m)
ball3.set_force(ball_force)

ball4 = pt.Particle("Pelota 4", x0, y0, v0, a0, m)
ball4.set_force(ball_force)

xposEuler = []
yposEuler = []
tposEuler = []

xposEulerCromer = []
yposEulerCromer = []
tposEulerCromer = []

xposMidpoint = []
yposMidpoint = []
tposMidpoint = []

xposNum = []
yposNum = []

euler(ball, xposEuler, yposEuler, tposEuler)
euler_cromer(ball2, xposEulerCromer, yposEulerCromer, tposEulerCromer)
midpoint(ball3, xposMidpoint, yposMidpoint, tposMidpoint)
exact(ball4, xposNum, yposNum, tposEuler)

#Generate Plots
fig, ax = plt.subplots()
ax.plot(xposEuler, yposEuler, '--', label='Euler')
ax.plot(xposEulerCromer, yposEulerCromer, '--', label='Euler-Cromer')
ax.plot(xposMidpoint, yposMidpoint, '--', label='Midpoint')
ax.plot(xposNum, yposNum, '-', label ='Exact')

ax.set(xlabel='x (a.u.)', ylabel='y (a.u.)',
       title='Projectile motion with drag')
ax.grid()

plt.legend()
plt.show()
