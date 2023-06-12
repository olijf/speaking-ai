import json
from transitions.extensions import GraphMachine

from RogueAIStateMachine import RogueAIStateMachine

# Load the conversation script from a JSON file
with open("conversation.json", "r") as file:
    conversation_script = json.load(file)

# Create an instance of the rogue AI state machine with the conversation script
rogue_ai = RogueAIStateMachine(conversation_script)

# Create a GraphMachine instance and generate the graph
graph = GraphMachine(rogue_ai)
graph.get_graph().draw("conversation_graph.png", prog="dot", format="png")
