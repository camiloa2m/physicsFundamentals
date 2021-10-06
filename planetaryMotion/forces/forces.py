# forces.py

class Forces:
    def __init__(self, user_force, params):
        self.force = user_force
        self.params = params
        self.state = None

    def get_state(self):
        return self.state

    def get_force(self, state):
        self.state = state
        return self.force(state, self.params)
