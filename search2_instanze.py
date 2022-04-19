#ROBOT MULTIPLE OBJECT INSTANCES
problema1 = Robot_MultipleObj({"robot":{"room":"A", "hand":["obj10/5"], "currentLoad":5}, "rooms":{"A":["obj1/10"], "B":["obj2/10"], "C":["obj3/5", "obj4/5"], "D":["obj5/5", "obj6/10","obj7/5"], "E":["obj8/5", "obj9/10"]}},{"robot":{"room":"A", "hand":[]}})
soluzione1 = breadth_first_tree_search(problema1)
soluzione1 = depth_first_tree_search(problema1)
soluzione1 = iterative_deepening_search(problema1)

problema1 = Robot_MultipleObj({"robot":{"room":"B", "hand":["obj10/5"], "currentLoad":5}, "rooms":{"A":["obj1/10"], "B":["obj2/10"], "C":["obj3/5", "obj4/5"], "D":["obj5/5", "obj6/10","obj7/5"], "E":["obj8/5", "obj9/10"]}},{"robot":{"room":"C", "hand":["obj3/5","obj4/5"]}})

problema1 = Robot_MultipleObj({"robot":{"room":"A", "hand":[], "currentLoad":0}, "rooms":{"A":["obj1/10"], "B":["obj2/10"], "C":["obj3/5", "obj4/5"], "D":["obj5/5", "obj6/10","obj7/5"], "E":["obj8/5", "obj9/10"]}},{"robot":{"room":"A", "hand":[]},"rooms":{"A":["obj2/10"], "B":["obj1/10"], "C":["obj3/5", "obj4/5"], "D":["obj5/5", "obj6/10","obj7/5"], "E":["obj8/5", "obj9/10"]}})