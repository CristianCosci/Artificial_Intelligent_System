from search import *
import copy

class Robot(Problem):
    """State is defined as a dict:
    {
        "robot":{room, hand}
        "rooms":{room:[objects]}
    }
    """
    def __init__(self, initial, goal):
        """ Degine goal state and initialize a problem """
        self.goal = goal
        Problem.__init__(self, initial, goal)
        self.rooms = ["A", "B", "C", "D", "E"]

    
    def actions(self, state):
        possible_actions = []
        room = state["robot"]["room"]
        hand = state["robot"]["hand"]

        if hand is None:
            for obj in state["rooms"][room]:
                possible_actions.append("GET_"+obj)
        if hand is not None:
            possible_actions.append("PUT_"+hand)
        roomIndex = self.rooms.index(room) #restituisce l'indice in cui si trova
        if roomIndex > 0:
            possible_actions.append("MOVE_"+room+"_"+self.rooms[roomIndex-1])
        if roomIndex < len(self.rooms) - 1:
            possible_actions.append("MOVE_"+room+"_"+self.rooms[roomIndex+1])

        return possible_actions

    def result(self, state, action):
        """Given state and action, return a new state that is the result
        Action is assumed to be a valid action in the state"""
        newstate = copy.deepcopy(state) #serve per fare una copia dello stato corrente, perchè usiamo un dizionario
        act = action.split("_") #split permette di separe le parole in cui di mezzo c'è il carattere '_' ---> MOVE_A_A restituisce MOVE,A,B
        room = state["robot"]["room"]
        hand = state["robot"]["hand"]
        #print(newstate["rooms"][room])

        if act[0] == "MOVE":
            current_room = act[1]
            next_room = act[2]
            newstate["robot"]["room"] = next_room
        elif act[0] == "PUT":
            newstate["rooms"][room].append(hand)
            newstate["robot"]["hand"] = None
        elif act[0] == "GET":
            obj = act[1]
            newstate["rooms"][room].remove(obj)
            newstate["robot"]["hand"] = obj
            
        return newstate

    
    def goal_test(self, state):
        if state["robot"]["room"] == self.goal["robot"]["room"] and state["robot"]["hand"] == self.goal["robot"]["hand"]:
            return True
        return False    


"""
robot_1 = Robot({"robot":{"room":"A", "hand":None}, "rooms":{"A":["obj1"], "B":["obj2"], "C":["obj3", "obj4"], "D":["obj5", "obj6", "obj7"], "E":["obj8", "obj9"]}}, {"robot":{"room":"A", "hand":"obj1"}}) 
robot_1 = Robot({"robot":{"room":"A", "hand":None}, "rooms":{"A":["obj1"], "B":["obj2"], "C":["obj3", "obj4"], "D":["obj5", "obj6", "obj7"], "E":["obj8", "obj9"]}}, {"robot":{"room":"E", "hand":None}}) 
robot_2 = Robot({"robot":{"room":"A", "hand":"obj10"}, "rooms":{"A":["obj1"], "B":["obj2"], "C":["obj3", "obj4"], "D":["obj5", "obj6", "obj7"], "E":["obj8", "obj9"]}}, {"robot":{"room":"E", "hand":None}})
s2 = breadth_first_tree_search(robot_2)
print(s2.solution())
"""
robot = Robot({"robot":{"room":"A", "hand":None}, "rooms":{"A":["obj1"], "B":["obj2"], "C":["obj3", "obj4"], "D":["obj5", "obj6", "obj7"], "E":["obj8", "obj9"]}}, {"robot":{"room":"E", "hand":None}}) 
s1 = breadth_first_tree_search(robot)
print(s1.solution())
