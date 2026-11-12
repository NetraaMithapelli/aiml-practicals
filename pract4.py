#Practical 4 : Rule based Car TroubleShooting Expert Systems

"""
Steps:
1)Create rules : knowledge base
2)Ask the user questions and store known facts
3)Create facts set
4)Forward Chaining
5)Backward Chaining
6)Display facts using FC
7)Check the goal using BC

""" 

#Knowledge base : If conditions are true then conclude a result
rules = [
    ({"battery_weak"}, "battery_problem"),
    ({"fuel_empty"}, "fuel_problem"),
    ({"battery_problem"}, "car_starting_issue"),
    ({"fuel_problem"}, "car_starting_issue")
]

battery = input("Is battery weak? (yes/no) : ").strip().lower()
fuel = input("Is fuel empty? (yes/no) : ").strip().lower()

facts = set()

if battery == "yes":
    facts.add("battery_weak")

if fuel == "yes":
    facts.add("fuel_empty")

#Forward Chaining : Start with known facts and repeatedly check against existing rules
def forward(facts):
    facts = facts.copy()

    while True:
        new_fact = False

        for conditions, result in rules:
            if conditions.issubset(facts) and result not in facts:
                facts.add(result)
                new_fact = True

        if not new_fact:
            break

    return facts

#Backward Chaining : start with a goal and check whether facts and rules can prove it
def backward(goal, facts, checked=None):
    if goal in facts:
        return True

    if checked is None:
        checked = set()

    if goal in checked:
        return False

    checked = checked | {goal}

    for conditions , result in rules:
        if result == goal:
            if all(backward(condition, facts, checked) for condition in conditions):
                return True
            
    return False

#Display facts using Forward Chaining
print("----FORWARD CHAINING------")
derived_facts = forward(facts)

if derived_facts:
    print("Derived facts : ", ",".join(sorted(derived_facts)))
else:
    print("No facts were provided or derived")

#Check the goal using Backward Chaining
print("----BACKWARD CHAINING----------")
goal = "car_starting_issue"

if backward(goal, facts) :
    print("Conclusion : ", goal, " is True")
else:
    print("Conclusion : ", goal, " is False")


