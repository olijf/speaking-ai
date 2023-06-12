import json
from RogueAIStateMachine import RogueAIStateMachine

# Load the conversation script from a JSON file
with open("conversation-dutch.json", "r") as file:
    conversation_script = json.load(file)

# Create an instance of the rogue AI state machine with the conversation script
rogue_ai = RogueAIStateMachine(conversation_script)

# Start the conversation loop
rogue_ai.start()
while True:
    # Display the current prompt and available options
    print("Keuze:")
    for i, option in enumerate(rogue_ai.get_options(), start=1):
        print(f"{i}. {option['text']}")

    # Get user input
    user_input = input("(1, 2, etc.): ")
    print()
    # Check if the user's input is a valid option
    valid_option = False
    for i, option in enumerate(rogue_ai.get_options(), start=1):
        if int(user_input) == i:
            valid_option = True
            next_state = option["transition"]
            break

    # If the input is valid, transition to the next state
    if valid_option:
        rogue_ai.transition(next_state)
        rogue_ai.display_prompt(next_state)
    else:
        print("Onjuiste keuze!")
