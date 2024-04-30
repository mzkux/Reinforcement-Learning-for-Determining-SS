class qState:
    def __init__(self, value):
        self.value = value
        self.transitions = []
        self.accepting = False
        self.action = []

    def add_transition(self, transition):
        self.transitions.append(transition)

    def get_transitions(self):
        self.set_actions()
        return self.transitions

    def set_actions(self):
        actions = set()
        for transition in self.transitions:
            actions.add(transition[1])
        self.action = actions

    def get_actions(self):
        return self.action

    def get_value(self):
        return self.value

    def __str__(self):
        return self.value