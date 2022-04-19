from search import *

class Giare(Problem):

    def __init__(self, initial, goal):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)


    def actions(self, state):
        """ Return the actions that can be executed in the given state."""

        possible_actions = []
        A = state[0]
        B = state[1]

        if A < 3:
            possible_actions.append('FILL_A')
        if B < 4:
            possible_actions.append('FILL_B')
        if A > 0:
            possible_actions.append('EMPTY_A')
        if B > 0:
            possible_actions.append('EMPTY_B')
        if A > 0 and B < 4:
            possible_actions.append('MOVE_A_B')
        if B > 0 and A < 3: 
            possible_actions.append('MOVE_B_A')

        return possible_actions


    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        new_state = list(state)
        A = state[0]
        B = state[1]

        if action == 'FILL_A':
            new_state[0] = 3
        if action == 'FILL_B':
            new_state[1] = 4
        if action == 'EMPTY_A':
            new_state[0] = 0
        if action == 'EMPTY_B':
            new_state[1] = 0

        if action == 'MOVE_A_B':
            if A < (4 - B):
                new_state[0] = 0
                new_state[1] = A + B
            else:
                new_state[0] = A - (4 - B)
                new_state[1] = 4
        if action == 'MOVE_B_A':
            if B < (3 - A):
                new_state[1] = 0
                new_state[0] = A + B
            else:
                new_state[1] = B - (3 - A)
                new_state[0] = 3

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal


"""
    Esempi di esecuzioni (instanziamenti di problemi):
    - problema1 = Giare((0,0),(3,0))
    - soluzione1 = breadth_first_tree_search(problema1)
    - soluzione1.solution()

    - problema2 = Giare((3,0),(0,4))
    - soluzione2 = breadth_first_tree_search(problema2)
    - soluzione2.solution()
"""