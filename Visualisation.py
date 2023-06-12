import json
from transitions.extensions import GraphMachine

from RogueAIStateMachine import RogueAIStateMachine

# Load the conversation script from a JSON file
with open("conversation-dutch.json", "r") as file:
    conversation_script = json.load(file)

# Create an instance of the rogue AI state machine with the conversation script
rogue_ai = RogueAIStateMachine(conversation_script)

# Create a GraphMachine instance and generate the graph
graph = GraphMachine(model=rogue_ai, states=list(rogue_ai.states.keys()), initial='intro', auto_transitions=True, title="Rogue AI State Machine", show_conditions=True)
for state, state_data in rogue_ai.states.items():
    for option in state_data["options"]:
        graph.add_transition(trigger="answer", source=state, dest=option["transition"], label=option["text"])

graph.get_graph().draw("conversation_graph.png", prog="dot", format="png")
