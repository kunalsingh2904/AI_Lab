1. No input required
2. Please install Gym package using command "pip install gym==0.7.4" on terminal. OpenAI Gym is a toolkit for developing and comparing reinforcement learning algorithms. I used this package to create environment.
3. Run code as "python3 mdp.py" or run script as "./run.sh".

4. Output format:

   Value iteration

   Value converged at iteration 341
   Time to converge: 50.0 ms


    Final Policy:
    [0 3 3 3 0 0 0 0 3 1 0 0 0 2 1 0]
    ← ↑ ↑ ↑ ← ← ← ← ↑ ↓ ← ← ← → ↓ ←

    Total wins with value iteration: 85
    Average rewards with value iteration: 0.85



    policy iteration

    policy converged at iteration 31
    Time to converge:  4.61 ms

    Final Policy:
    [0 3 0 3 0 0 0 0 3 1 0 0 0 2 1 0]
    ← ↑ ← ↑ ← ← ← ← ↑ ↓ ← ← ← → ↓ ←

    Total wins with Policy iteration: 68
    Average rewards with Policy iteration: 0.68
