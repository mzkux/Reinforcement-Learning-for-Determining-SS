import random
import qGraph
import qNode

def calculate_states(s: int, d: int, q: qGraph) -> int:
    # Check for state size reduction (potentially reaching a goal state)
    size_difference = q.nodeatIndex(s).get_set().size() - q.nodeatIndex(d).get_set().size()
    if size_difference > 0:
        return size_difference * 100  # Reward for reducing state size

    return -1



def calculate_reward(s: int, d: int, q: qGraph) -> float:
    if q.nodeatIndex(d).is_singleton_set():
        return 10000  # High reward for reaching a singleton set (goal state)
    else:
        # Assuming calculateStates is implemented to handle state transition costs
        return calculate_states(s, d, q)



ss = []


while cont:
    iterations += 1

    # Epsilon-greedy action selection
    epsilon = random.randint(0, 99)  # Inclusive range for epsilon (0-100)
    if epsilon < 20:
        a = random.randint(0, q.get_actions() - 1)  # Random action selection within valid range
    else:
        a = q.max_next_action(n)  # Exploit action with maximum Q-value

    ss.append(a)

    if a == -1:
        print("Error: Invalid action selected!")  # Informative error message

    next_node_id = n.get_reach_node_id(a)
    if next_node_id == -1:
        # Handle case where no neighbors exist for the chosen action
        temp = generate_node(fdd, n, a)
        if temp.get_actions() > 0:
            next_node_id = q.add_node(n, a, temp)
        else:
            next_node_id = -1

    # Update Q-values
    max_expected_future_reward = q.get_mefr(node_id, a)
    reward = -10000000
    if next_node_id >= 0:
        max_expected_future_reward = q.get_mefr(next_node_id, a)
        reward = calculate_reward(node_id, next_node_id, q)

    current_q_value = q.nodeatIndex(node_id).get_q_value(a)
    q.nodeatIndex(node_id).set_new_q_value(current_q_value + (alpha * (reward + (gamma * max_expected_future_reward) - current_q_value)), a)

    # Update node and check for termination
    if next_node_id >= 0:
        n = q.nodeatIndex(next_node_id)
        node_id = n.get_id()
        cont = not n.is_singleton_set()
    else:
        n = q.nodeatIndex(0)  # Reset to initial node
        node_id = 0
        cont = False  # Terminate after episode
        ss.clear()
        episodes += 1

    # Check for exceeding episode length
    if ss.size() > FSMStates * 100:
        cont = False
        q.clear()
        iterations = 0
        ss.clear()
