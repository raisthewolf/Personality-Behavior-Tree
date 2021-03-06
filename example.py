from tree import *

setVariable("a", True)
setVariable("b", False)
setVariable("c", False)

addAgent("Agent 2")
addPersonalityAgent("Agent 1", 0, 0, 0, 0, 0)

def action1Precond():
    return getVariable("a")

def action1Effects():
    setVariable("b", True)
    setVariable("a", False)

action1 = ActionNode(action1Precond,
                    action1Effects,
                    effectText = "Action 1. ")

def action2Precond():
    return getVariable("b")

def action2Effects():
    setVariable("c", True)

action2 = ActionNode(action2Precond,
                    action2Effects,
                    effectText = "Action 2. ")

def action3Precond():
    return getVariable("b") and getVariable("c")

def action3Effects():
    setVariable("a", True)
    setVariable("b", False)
    setVariable("c", False)

action3 = ActionNode(action3Precond,
                    action3Effects,
                    effectText = "Action 3. ")

sequence1 = SequenceNode([action1, action3])
sequence2 = SequenceNode([action2, action3])
selector1 = SelectorNode([sequence1, sequence2])
selector2 = SelectorUtilityNode([action2, selector1])

tree1 = attachTreeToAgent("Agent 1", selector2)
tree2 = attachTreeToAgent("Agent 2", selector1)

turn()
inp = input("continue? (y/n): ")
quit = False
while (not quit):
    if inp == "y":
        turn()
        inp = input("continue? (y/n): ")
    elif inp == "n":
        quit = True
    else:
        print("not recognized\n")
        inp = input("continue? (y/n): ")
print("goodbye")
