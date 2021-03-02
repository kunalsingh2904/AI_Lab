# Importing Libraries
import sys


# creating superclass Action
class Action:
    pass


class Stack(Action):
    """
    Action Stack
    """

    def __init__(self, arg1, arg2):
        self.type_ = 'stack'
        self.arg1 = arg1
        self.arg2 = arg2

    @property
    def preconditions(self):
        # preconditions for Action
        return [Predicate('AE'), Predicate('clear', self.arg2), Predicate('clear', self.arg1)]

    @property
    def positive_effects(self):
        return [Predicate('AE'), Predicate('on', self.arg1, self.arg2), Predicate('clear', self.arg1)]

    @property
    def negative_effects(self):
        return [Predicate('clear', self.arg2), Predicate('hold', self.arg1)]

    def __str__(self):
        return '({} {} {})'.format(self.type_, self.arg1, self.arg2)


class Unstack(Action):
    """
    Action Untack
    """

    def __init__(self, arg1, arg2):
        self.type_ = 'unstack'
        self.arg1 = arg1
        self.arg2 = arg2

    @property
    def preconditions(self):
        # preconditions for Action
        return [Predicate('AE'), Predicate('clear', self.arg1), Predicate('on', self.arg1, self.arg2)]

    @property
    def positive_effects(self):
        return [Predicate('clear', self.arg2), Predicate('hold', self.arg1)]

    @property
    def negative_effects(self):
        return [Predicate('AE'), Predicate('on', self.arg1, self.arg2), Predicate('clear', self.arg1)]

    def __str__(self):
        return '({} {} {})'.format(self.type_, self.arg1, self.arg2)


class Pick(Action):
    """
    Action Pick
    """

    def __init__(self, arg1):
        self.type_ = 'pick'
        self.arg1 = arg1

    @property
    def preconditions(self):
        # preconditions for Action
        return [Predicate('AE'), Predicate('clear', self.arg1), Predicate('ontable', self.arg1)]

    @property
    def positive_effects(self):
        return [Predicate('hold', self.arg1)]

    @property
    def negative_effects(self):
        return [Predicate('AE'), Predicate('ontable', self.arg1), Predicate('clear', self.arg1)]

    def __str__(self):
        return '({} {})'.format(self.type_, self.arg1)


class Putdown(Action):
    """
    Action Putdown
    """

    def __init__(self, arg1):
        self.type_ = 'putdown'
        self.arg1 = arg1

    @property
    def preconditions(self):
        # preconditions for Action
        return [Predicate('hold', self.arg1)]

    @property
    def positive_effects(self):
        return [Predicate('AE'), Predicate('ontable', self.arg1), Predicate('clear', self.arg1)]

    @property
    def negative_effects(self):
        return [Predicate('hold', self.arg1)]

    def __str__(self):
        return '({} {})'.format(self.type_, self.arg1)


class Predicate:
    """
    Defines a Predicate
    """

    def __init__(self, type_: str, *args):
        self.type_ = type_.strip()
        self.args = list(args)

    def __str__(self):
        # for printing
        if self.args:
            return '({} {})'.format(self.type_, ' '.join(self.args))
        return '(' + self.type_ + ')'

    def __eq__(self, value):
        # check equality
        return (self.type_ == value.type_) and (self.args == value.args)


# Finds the block on top of a given block in the given state
# If no block is on top returns False
def find_top(x, state):
    for predicate in state:
        if predicate.type_ == 'on' and predicate.args[1] == x.args[0]:
            return predicate.args[0]
    return False


# Finds if arm is holding a block in given state or not
# returns False if arm is empty the
def find_hold(state):
    for predicate in state:
        if predicate.type_ == 'hold':
            return predicate.args[0]
    return False


# Main Algorithm
# start_state: Represents start state. List of Predicates
# goal: Represents goal state. List of Predicates
# return:      Plan to achieve goal state. List of Actions
def goal_stack_planning(start_state, goal):
    stack = []      # stack for gsp
    plan = []       # list of action
    state = start_state
    stack.append(goal)
    stack.extend(goal)
    while stack:
        # taking top sentence
        temp = stack.pop()
        if isinstance(temp, Action):
            plan.append(temp)   # putting in plan
            state.extend(temp.positive_effects)
            # Changes the state after an action is performed
            # new_state = old_state + action.positive_effects - action.negative_effects
            state = [s for s in state if s not in temp.negative_effects]
        elif isinstance(temp, list):
            solved = True
            # Checks if a conjunct of predicates is satisfied in given state
            for predicate in temp:
                if not satisfy(predicate, state):
                    solved = False
            if not solved:
                stack.append(temp)
                stack.extend(temp)
        elif isinstance(temp, Predicate) and not satisfy(temp, state):
            # choses an action to satisfy that predicate and state
            if temp.type_ == 'on':
                action = Stack(temp.args[0], temp.args[1])
            elif temp.type_ == 'ontable':
                action = Putdown(temp.args[0])
            elif temp.type_ == 'clear':
                if Predicate('hold', temp.args[0]) in state:
                    action = Putdown(temp.args[0])
                else:
                    action = Unstack(find_top(temp, state), temp.args[0])
            elif temp.type_ == 'hold':
                if Predicate('ontable', temp.args[0]) in state:
                    action = Pick(temp.args[0])
                else:
                    action = Unstack(find_top(temp, state), temp.args[0])
            elif temp.type_ == 'AE':
                action = Putdown(find_hold(state))
            # put action in stack
            stack.append(action)
            stack.append(action.preconditions)
            stack.extend(action.preconditions)
    return plan


# Checks if a predicate is satisfied in given state or not
def satisfy(predicate, state):
    if predicate.type_ == 'clear':
        return not find_top(predicate, state)
    else:
        return predicate in state


# return list of sentence
def make_state(states):
    states = states.replace('(', '')
    states = states.replace(')', '')
    states = states.split('^')
    sentences = []
    for state in states:
        predicate = state.split(' ')
        sentences.append(Predicate(predicate[0], *predicate[1:]))
    return sentences


# input file
fp = open(sys.argv[1], 'r')
# Reading number of block
total = int(fp.readline().strip())
# start state
start = make_state(fp.readline().strip())
# Appending "AE" if not hold
if not find_hold(start):
    start.append(Predicate('AE'))
# Goal state
goal = make_state(fp.readline().strip())
fp.close()
goal.reverse()
# plan: Lit of action
plan = goal_stack_planning(start, goal)
# Output file
output_file = open("output.txt", "w")
for i in plan:
    # writing in file
    output_file.write(str(i))
    output_file.write("\n")
output_file.close()
