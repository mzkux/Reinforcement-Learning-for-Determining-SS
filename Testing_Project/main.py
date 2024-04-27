from qNode import qNode
from qState import qState
from qTree import qTree
import random


# Function to calculate the reward based on the state size reduction
def calculate_states(node, initial_node) -> int:
    size_difference = initial_node.getSize() - node.getSize()
    return size_difference * 100


# Function to calculate the reward based on the state size
def calculate_reward(node, initial_node) -> float:
    if node.getSize() == 1:
        return 1_000_000
    else:
        return calculate_states(node, initial_node)


# Initialize the states and transitions
#states = ['A', 'B', 'C',]
#actions = [0, 1]
#transitions = [['A', 0, 'A'], ['A', 1, 'B'], ['A', 1, 'C'], ['B', 0, 'C'], ['C', 1, 'C'], ]

#states = ['A', 'B', 'C', 'D']
#transitions = [['A', 0, 'A'], ['A', 1, 'B'], ['B', 0, 'A'], ['B', 1, 'C'],
#              ['C', 0, 'B'], ['C', 1, 'D'], ['D', 0, 'D'], ['D', 1, 'C']]


# Define the file's name.
filename = r"C:\Users\mzkux\Documents\Software Testing\fsms.txt"
transitions = []
states = set()
actions = set()

# Open the file and read its content.
with open(filename) as f:
    content = f.readlines()

print(content[0].split())
sm_id, gg, num_states, num_inputs, num_outputs = content[0].split()

# Display the file's content line by line.
for line in content[1:-1]:
    transition = line.split()
    #print(transition)
    transitions.append(transition)
    states.add(transition[0])  # Add the state to the set
    actions.add(transition[1])  # Add the action to the set

# Convert the set to a list
states = list(states)
actions = list(actions)
print(len(actions))

# Initialize the States
for i, state in enumerate(states):
    states[i] = qState(state)

# Initialize the Transitions
for transition in transitions:
    for state in states:
        if transition[0] == state.get_value():
            state.add_transition(transition)
            state.set_actions()
            break

# Initialize the root node and the tree
initial_node = qNode(states, transitions, [], actions, None, states)
tree = qTree()
tree.add_node(initial_node)

# Set the exploration factor
epsilon = 0.2

# Flag to control the main loop
cont = True
iterations = 1000
iteration = 0


# Main loop
while cont and iteration < iterations:
    # Traverse the tree
    current_node = tree.get_root()
    all_nodes = list(tree.all_nodes())

    for current_node in all_nodes:
        if not current_node.getLeaf():
            # Choose an action
            if random.random() < epsilon:
                action = random.choice(actions)  # Choose a random action
            else:
                action = max(actions, key=lambda action: current_node.getReward(action))  # Choose the action with the highest reward

            # Apply the chosen action if it's applicable
            if current_node.applicableAction(action):
                current_node = current_node.applyOldAction(action)

        else:
            # Process leaf nodes
            for action in actions:
                if current_node.applicableAction(action):
                    current_node.setLeaf(False)
                    node = current_node.applyNewAction(action)

                    # Add the new node to the tree if it doesn't exist already
                    if not tree.existing_node(node):
                        tree.add_node(node, current_node)
                        current_node.setReward(calculate_reward(node, current_node), action)

                        # Check if the new node is a goal state
                        if node.getSize() == 1:
                            node.printStates()
                            ss = node.get_actions()
                            print(ss)
                            cont = False  # Terminate the loop if a goal state is reached
            break
    iteration += 1
