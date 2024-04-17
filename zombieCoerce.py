# Imports the operating system the user will interact with on python
import os
# Imports the AI API that will stream responses to the user
import openai

# Set your OpenAI API key here
openai.api_key = os.getenv('sk-proj-dUZHNvaG5pzaWDWsVgEbT3BlbkFJ6nDOdHrNLldUZOAYnnRM')

# The defined function is the response the user will recieve from the AI depending on the user input
def get_ai_response(prompt):
    # The response is equated with whatever the OprnAI responds with
    response = openai.Completion.create(
        # Davinci is the model the AI relies on to actually generate the responses
        engine="text-davinci-003",  # Using Davinci as the model
        # Ensuring the prompt is the response from the AI
        prompt=prompt,
        # Amount of max characters the AI responds with 
        max_tokens=150,
        # Gauges how much the the ai is similar to another response it has already made
        temperature=0.9  # Adjust for more varied outputs
    )
    # Returns the response with the given limitations
    return response.choices[0].text.strip()
# The function that the game will start with and build off of
def main():
    # Initial scenario setup
    print("You are a partially transformed zombie approaching the gates of a small town.")
    print("Your goal is to convince the gate guard to let you in so you can infect the town.")
    print("What will you say to the guard?")

    # Loop to continue the conversation until the condition is reached or the player has exited the game 
    while True:
        # The user input that will determine what the ai responds with
        player_input = input("You say: ")
        # Gives the player the option to exit the conversation and by extension, the game
        if player_input.lower() in ['exit', 'quit']:  # Allowing the player to exit the conversation
            # The text that will inform the user of their exiting
            print("Exiting game.")
            break

        # Creates a prompt for the AI based on the player's input
        prompt = f"A partially transformed zombie at the town gates says: '{player_input}' The guard, wary but unaware of the transformation, responds:"

        # Get the AI response and print it
        ai_response = get_ai_response(prompt)
        print(f"Guard says: {ai_response}")

# Letting the computer know that if this script is placed somewhere else, it won't be the same function - this modual wont be the same unless it is runned in this script
if __name__ == "__main__":
    main()
