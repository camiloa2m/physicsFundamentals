import numpy as np

GM = 4*(np.pi**2)
DRAG = 4.

class Particle:

    def __init__(self, label, x0, y0, v0, alpha0, m0 = 1., t0 = 0.):
        self.lb = label
        self.m, self.t = m0, t0
        self.x, self.y = x0, y0
        self.vx = v0 * np.cos(np.radians(alpha0))
        self.vy = v0 * np.sin(np.radians(alpha0))
        self.force = None

    def __str__(self):
        strng = self.lb + "\n"
        strng += "mass = {}, time = {}\n".format(self.m, self.t)
        strng += "position = ({:.4f}, {:.4f})\n".format(self.x, self.y)
        strng += "velocity = ({:.4f}, {:.4f})\n".format(self.vx, self.vy)
        return strng

    def get_state(self):
        return self.x, self.y, self.vx, self.vy, self.t

    def set_state(self, x, y, vx, vy, t):
        self.x, self.y, self.vx, self.vy, self.t = x, y, vx, vy, t

    def set_force(self, netforce):
        self.force = netforce

    def get_energy(self):
        return .5*self.m*(self.vx**2 + self.vy**2) - (GM*self.m)/np.sqrt(self.x**2 + self.y**2)

    def get_angle(self):
        if self.x >= 0 and self.y >= 0:
            return abs(np.arctan(self.y / self.x))
        elif self.x < 0 and self.y >= 0:
            return np.pi/2 + abs(np.arctan(self.x / self.y))
        elif self.x < 0 and self.y < 0 :
            return np.pi + abs(np.arctan(self.y / self.x))
        else:
            return 2*np.pi - abs(np.arctan(self.y / self.x))
