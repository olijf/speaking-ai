import json
from RogueAIStateMachine import RogueAIStateMachine

# Load the conversation script from a JSON file
with open("conversation.json", "r") as file:
    conversation_script = json.load(file)

# Create an instance of the rogue AI state machine with the conversation script
rogue_ai = RogueAIStateMachine(conversation_script)

# Start the conversation loop
print(rogue_ai.start())
while True:
    # Display the current prompt and available options
    print("Options:")
    for i, option in enumerate(rogue_ai.get_options(), start=1):
        print(f"{i}. {option['text']}")

    # Get user input
    user_input = input("Enter your choice (1, 2, etc.): ")

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
    else:
        print("Invalid option. Please try again.")
