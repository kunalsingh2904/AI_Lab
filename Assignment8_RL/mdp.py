import numpy as np
import gym
import time

# gamma value
gamma = 0.999

# action mapping for display the final result
action_mapping = {
    3: '\u2191',  # UP
    2: '\u2192',  # RIGHT
    1: '\u2193',  # DOWN
    0: '\u2190'  # LEFT
}
# print(' '.join([action_mapping[i] for i in range(4)]))


def play_episodes(enviorment, n_episodes, policy, random=False):
    """
    This fucntion plays the given number of episodes given by following a policy or sample randomly from action_space.

    Parameters:
        enviorment: openAI GYM object
        n_episodes: number of episodes to run
        policy: Policy to follow while playing an episode
        random: Flag for taking random actions. if True no policy would be followed and action will be taken randomly

    Return:
        wins: Total number of wins playing n_episodes
        total_reward: Total reward of n_episodes
        avg_reward: Average reward of n_episodes

    """
    # intialize wins and total reward
    wins = 0
    total_reward = 0

    # loop over number of episodes to play
    for episode in range(n_episodes):

        # flag to check if the game is finished
        terminated = False

        # reset the enviorment every time when playing a new episode
        state = enviorment.reset()

        while not terminated:

            # check if the random flag is not true then follow the given policy other wise take random action
            if random:
                action = enviorment.action_space.sample()
            else:
                action = policy[state]
            # action = policy[state]
            # take the next step
            next_state, reward,  terminated, prob = enviorment.step(action)

            # show states
            # enviorment.render()

            # accumalate total reward
            total_reward += reward

            # change the state
            state = next_state

            # if game is over with positive reward then add 1.0 in wins
            if terminated and reward == 1.0:
                wins += 1

    # calculate average reward
    average_reward = total_reward / n_episodes
    return wins, total_reward, average_reward


def one_step_lookahead(env, state, V, gamma):
    """
    Helper function to  calculate state-value function

    Arguments:
        env: openAI GYM Enviorment object
        state: state to consider
        V: Estimated Value for each state. Vector of length nS
        gamma: MDP discount factor

    Return:
        action_values: Expected value of each action in a state. Vector of length nA
    """

    # initialize vector of action values
    action_values = np.zeros(env.nA)

    # loop over the actions we can take in an enviorment
    for action in range(env.nA):
        # loop over the P_sa distribution.
        for probablity, next_state, reward, info in env.P[state][action]:
             # if we are in state s and take action a. then sum over all the possible states we can land into.
            action_values[action] += probablity * \
                (reward + (gamma * V[next_state]))

    return action_values


def update_policy(env, policy, V, gamma):
    """
    Helper function to update a given policy based on given value function.

    Arguments:
        env: openAI GYM Enviorment object.
        policy: policy to update.
        V: Estimated Value for each state. Vector of length nS.
        gamma: MDP discount factor.
    Return:
        policy: Updated policy based on the given state-Value function 'V'.
    """
    real_transition_value = list()
    for state in range(env.nS):
        # for a given state compute state-action value.
        action_values = one_step_lookahead(env, state, V, gamma)
        real_transition_value.append(action_values)
        # choose the action which maximizez the state-action value.
        policy[state] = np.argmax(action_values)

    return policy, real_transition_value


def value_iteration(env, gamma, max_iteration=1000):
    """
    Algorithm to solve MPD.

    Arguments:
        env: openAI GYM Enviorment object.
        gamma: MDP discount factor.
        max_iteration: Maximum No.  of iterations to run.

    Return:
        V: Optimal state-Value function. Vector of lenth nS.
        optimal_policy: Optimal policy. Vector of length nS.

    """
    # intialize value fucntion
    V = np.zeros(env.nS)
    # real_transition_value = list()
    # iterate over max_iterations
    for i in range(max_iteration):

        #  keep track of change with previous value function
        prev_v = np.copy(V)

        # loop over all states
        for state in range(env.nS):

            # Asynchronously update the state-action value
            #action_values = one_step_lookahead(env, state, V, gamma)

            # Synchronously update the state-action value
            action_values = one_step_lookahead(
                env, state, prev_v, gamma)

            # select best action to perform based on highest state-action value
            best_action_value = np.max(action_values)
            # real_transition_value.append(action_values)
            # update the current state-value fucntion
            V[state] = best_action_value

        # if policy not changed over 10 iterations it converged.
        if i % 10 == 0:
            # if values of 'V' not changing after one iteration
            if (np.all(np.isclose(V, prev_v))):
                print('Value converged at iteration %d' % (i+1))
                break

    # intialize optimal policy
    optimal_policy = np.zeros(env.nS, dtype='int8')

    # update the optimal polciy according to optimal value function 'V'
    optimal_policy, real_transition_value = update_policy(
        env, optimal_policy, V, gamma)

    return V, optimal_policy, real_transition_value


def policy_eval(env, policy, V, gamma):
    """
    Helper function to evaluate a policy.

    Arguments:
        env: openAI GYM Enviorment object.
        policy: policy to evaluate.
        V: Estimated Value for each state. Vector of length nS.
        gamma: MDP discount factor.
    Return:
        policy_value: Estimated value of each state following a given policy and state-value 'V'. 

    """
    policy_value = np.zeros(env.nS)
    for state, action in enumerate(policy):
        for probablity, next_state, reward, info in env.P[state][action]:
            policy_value[state] += probablity * \
                (reward + (gamma * V[next_state]))

    return policy_value


def policy_iteration(env, gamma, max_iteration=1000):
    """
    Algorithm to solve MPD.

    Arguments:
        env: openAI GYM Enviorment object.
        gamma: MDP discount factor.
        max_iteration: Maximum No.  of iterations to run.

    Return:
        V: Optimal state-Value function. Vector of lenth nS.
        new_policy: Optimal policy. Vector of length nS.

    """
    # intialize the state-Value function
    V = np.zeros(env.nS)

    # intialize a random policy
    policy = np.random.randint(0, 4, env.nS)
    policy_prev = np.copy(policy)

    for i in range(max_iteration):

        # evaluate given policy
        V = policy_eval(env, policy, V, gamma)

        # improve policy
        policy, real_transition_value = update_policy(env, policy, V, gamma)

        # if policy not changed over 10 iterations it converged.
        if i % 10 == 0:
            if (np.all(np.equal(policy, policy_prev))):
                print('policy converged at iteration %d' % (i+1))
                break
            policy_prev = np.copy(policy)

    return V, policy, real_transition_value


if __name__ == "__main__":
    enviorment = gym.make('FrozenLake-v0')
    print("\nValue iteration")
    # enviorment.render()
    print()
    tic = time.time()
    opt_V, opt_Policy, real_transition_value = value_iteration(
        enviorment.env, gamma, max_iteration=1000)
    toc = time.time()
    elapsed_time = (toc - tic) * 1000

    print(f"Time to converge: {elapsed_time: 0.3} ms")
    # print('Optimal Value function: ')
    # print(opt_V.reshape((4, 4)))
    # print(real_transition_value)
    print('\n\nFinal Policy: ')
    print(opt_Policy)
    print(' '.join([action_mapping[int(action)] for action in opt_Policy]))
    n_episode = 100
    wins, total_reward, avg_reward = play_episodes(
        enviorment, n_episode, opt_Policy, random=False)
    print(f'\nTotal wins with value iteration: {wins}')
    print(f"Average rewards with value iteration: {avg_reward}")

    enviorment2 = gym.make('FrozenLake-v0')
    print("\n\n\npolicy iteration")
    # enviorment2.render()
    print()
    tic = time.time()
    opt_V2, opt_policy2, real_transition_value = policy_iteration(
        enviorment2.env, gamma, max_iteration=10000)
    toc = time.time()
    elapsed_time = (toc - tic) * 1000
    print(f"Time to converge: {elapsed_time: 0.3} ms")
    # print('Optimal Value function: ')
    # print(opt_V2.reshape((4, 4)))
    # print(real_transition_value)
    print('\nFinal Policy: ')
    print(opt_policy2)
    print(' '.join([action_mapping[(action)] for action in opt_policy2]))
    n_episode = 100
    wins, total_reward, avg_reward = play_episodes(
        enviorment2, n_episode, opt_policy2, random=False)
    print(f'\nTotal wins with Policy iteration: {wins}')
    print(f"Average rewards with Policy iteration: {avg_reward}")
