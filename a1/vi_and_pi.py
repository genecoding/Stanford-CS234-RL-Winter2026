### MDP Value Iteration and Policy Iteration

import argparse
import numpy as np
from riverswim import RiverSwim

np.set_printoptions(precision=3)

def bellman_backup(state, action, R, T, gamma, V):
    """
    Perform a single Bellman backup.

    Parameters
    ----------
    state: int
    action: int
    R: np.array (num_states, num_actions)
    T: np.array (num_states, num_actions, num_states)
    gamma: float
    V: np.array (num_states)

    Returns
    -------
    backup_val: float
    """
    backup_val = 0.
    ############################
    # YOUR IMPLEMENTATION HERE #
    backup_val = R[state, action] + gamma * np.sum(T[state, action] * V)
    ############################

    return backup_val

def policy_evaluation(policy, R, T, gamma, tol=1e-3):
    """
    Compute the value function induced by a given policy for the input MDP
    Parameters
    ----------
    policy: np.array (num_states)
    R: np.array (num_states, num_actions)
    T: np.array (num_states, num_actions, num_states)
    gamma: float
    tol: float

    Returns
    -------
    value_function: np.array (num_states)
    """
    num_states, num_actions = R.shape
    value_function = np.zeros(num_states)

    ############################
    # YOUR IMPLEMENTATION HERE #
    while True:
        value_old = np.copy(value_function)
        # for all s in S
        for state, action in enumerate(policy):
            value_function[state] = bellman_backup(state, action, R, T, gamma, value_old)

        # stop condition: max_s|V_new(s) - V_old(s)| < tol
        if np.max(np.abs(value_function - value_old)) < tol:
            break
    ############################
    return value_function


def policy_improvement(policy, R, T, V_policy, gamma):
    """
    Given the value function induced by a given policy, perform policy improvement
    Parameters
    ----------
    policy: np.array (num_states)
    R: np.array (num_states, num_actions)
    T: np.array (num_states, num_actions, num_states)
    V_policy: np.array (num_states)
    gamma: float

    Returns
    -------
    new_policy: np.array (num_states)
    """
    num_states, num_actions = R.shape
    new_policy = np.zeros(num_states, dtype=int)

    ############################
    # YOUR IMPLEMENTATION HERE #
    new_policy = (R + gamma * (T * V_policy).sum(axis=2)).argmax(axis=1)
    ############################
    return new_policy


def policy_iteration(R, T, gamma, tol=1e-3):
    """Runs policy iteration.

    You should call the policy_evaluation() and policy_improvement() methods to
    implement this method.
    Parameters
    ----------
    R: np.array (num_states, num_actions)
    T: np.array (num_states, num_actions, num_states)
    gamma: float
    tol: float

    Returns
    -------
    V_policy: np.array (num_states)
    policy: np.array (num_states)
    """
    num_states, num_actions = R.shape
    V_policy = np.zeros(num_states)
    policy = np.zeros(num_states, dtype=int)
    ############################
    # YOUR IMPLEMENTATION HERE #
    # policy = np.random.randint(num_actions, size=num_states)  # initialize π0(s) randomly
    while True:
        V_policy = policy_evaluation(policy, R, T, gamma, tol)
        policy_old = np.copy(policy)
        policy = policy_improvement(policy, R, T, V_policy, gamma)

        # stop condition: |πi − πi−1| = 0
        if np.sum(np.abs(policy - policy_old)) == 0:
            break
    ############################
    return V_policy, policy


def value_iteration(R, T, gamma, tol=1e-3):
    """Runs value iteration.
    Parameters
    ----------
    R: np.array (num_states, num_actions)
    T: np.array (num_states, num_actions, num_states)
    gamma: float
    tol: float

    Returns
    -------
    value_function: np.array (num_states)
    policy: np.array (num_states)
    """
    num_states, num_actions = R.shape
    value_function = np.zeros(num_states)
    policy = np.zeros(num_states, dtype=int)
    ############################
    # YOUR IMPLEMENTATION HERE #
    while True:
        value_old = np.copy(value_function)
        # for all s in S and all a in A
        q_function = R + gamma * (T * value_function).sum(axis=2)

        # extract new value_function and policy
        value_function = q_function.max(axis=1)
        policy = q_function.argmax(axis=1)
        
        # stop condition: max_s|V_new(s) - V_old(s)| < tol
        if np.max(np.abs(value_function - value_old)) < tol:
            break
    ############################
    return value_function, policy


# Edit below to run policy and value iteration on different configurations
# You may change the parameters in the functions below
if __name__ == "__main__":
    # add this
    parser = argparse.ArgumentParser()
    parser.add_argument('--current', type=str, default='WEAK')
    parser.add_argument('--discount_factor', type=float, default=0.99)
    args = parser.parse_args()
    print(args)  # show hyperparameters
    
    SEED = 1234

    RIVER_CURRENT = args.current
    assert RIVER_CURRENT in ['WEAK', 'MEDIUM', 'STRONG']
    env = RiverSwim(RIVER_CURRENT, SEED)

    R, T = env.get_model()
    discount_factor = args.discount_factor

    print("\n" + "-" * 25 + "\nBeginning Policy Iteration\n" + "-" * 25)

    V_pi, policy_pi = policy_iteration(R, T, gamma=discount_factor, tol=1e-3)
    print(V_pi)
    print([['L', 'R'][a] for a in policy_pi])

    print("\n" + "-" * 25 + "\nBeginning Value Iteration\n" + "-" * 25)

    V_vi, policy_vi = value_iteration(R, T, gamma=discount_factor, tol=1e-3)
    print(V_vi)
    print([['L', 'R'][a] for a in policy_vi])
