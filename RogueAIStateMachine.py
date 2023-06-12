import json
from transitions import Machine


class RogueAIStateMachine(object):
    def __init__(self, conversation):
        self.states = conversation["states"]
        self.machine = Machine(model=self, states=list(self.states.keys()), initial='intro')

        for state, state_data in self.states.items():
            self.machine.add_transition('answer', state, state_data["options"][0]["transition"])

    def start(self):
        self.display_prompt("intro")
        self.answer()

    def on_enter_state(self, state):
        self.display_prompt(state)

    def display_prompt(self, state):
        state_data = self.states[state]
        prompt = state_data["prompt"]
        print(prompt)

    def answer(self):
        current_state = self

    def get_options(self):
        return self.states[self.state]["options"]

    def transition(self, next_state):
        next_state = getattr(self, f'to_{next_state}')
        next_state()
