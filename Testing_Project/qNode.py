from qState import qState
class qNode:
    def __init__(self, states, transitions, actions, possible_actions, parent_node, possible_states) -> None:
        #self.current_states = states
        self.states = set(states)
        self.actions = actions
        self.possible_actions = possible_actions
        self.transitions = transitions
        self.reward = {action: 0 for action in self.possible_actions}  # Initialize Q-values with zeros
        self.neighbors = [-1]  # Initialize neighbors with -1 (invalid ID)
        self.action_is_valid = True
        self.parent_node = parent_node
        self.isLeaf = True
        self.children = []
        self.possible_states = possible_states

    def applyOldAction(self, action):
        # Find the transition rule for the current state and the given action
        new_states = []

        for transition in self.transitions:
            if transition[0] in [state.get_value() for state in self.states] and transition[1] == action:
                for state in self.possible_states:
                    if transition[2] == state.get_value():
                        new_states.append(state)
        return qNode(new_states, self.transitions, self.actions, self.possible_actions, self, self.possible_states)

    def applyNewAction(self, action):
        # Find the transition rule for the current state and the given action
        #print(self.actions)
        new_states = []
        actions = list(self.actions)
        actions.append(action)
        for transition in self.transitions:
            if transition[0] in [state.get_value() for state in self.states] and transition[1] == action:
                for state in self.possible_states:
                    if transition[2] == state.get_value():
                        new_states.append(state)
        return qNode(new_states, self.transitions, actions, self.possible_actions, self, self.possible_states)

    def getSize(self):
        return len(self.states)

    def get_current_states(self):
        return self.states

    def get_previous_states(self):
        return self.states

    def setReward(self, reward, action):
        if self.parent_node is not None:
            self.parent_node.setReward(self.parent_node.getReward(self.actions[-1])+reward, self.actions[-1])
        self.reward[action] = reward

    def getReward(self, action):
        return self.reward[action]

    def get_actions(self):
        return self.actions

    def printStates(self):
        for state in self.states:
            print(state.get_value(), end=" ")
        print()

    def applicableAction(self, action):
        self.action_is_valid = True
        for state in self.states:
            if action not in state.get_actions():
                self.action_is_valid = False
                #print("application not applicable", action, state.get_actions())
        return self.action_is_valid

    def setLeaf(self, leaf):
        self.isLeaf = leaf

    def getLeaf(self):
        return self.isLeaf

    def get_value(self):
        states = []
        for state in self.states:
            states.append(state.get_value())


