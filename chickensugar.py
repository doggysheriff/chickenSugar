import os
from openai import OpenAI

client = OpenAI(
api_key=os.environ['sk-proj-dUZHNvaG5pzaWDWsVgEbT3BlbkFJ6nDOdHrNLldUZOAYnnRM'], # this is also the default, it can be omitted
)

def get_ai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Using Davinci as the model
        prompt=prompt,
        max_tokens=150,
        temperature=0.9  # Adjust for more varied outputs
    )
    return response.choices[0].text.strip()

def main():
    # Initial scenario setup
    print("You are a partially transformed zombie approaching the gates of a small town.")
    print("Your goal is to convince the gate guard to let you in so you can infect the town")
    print("What will you say to the guard?")

    # Loop to continue the conversation
    while True:
        player_input = input("You say: ")
        if player_input.lower() in ['exit', 'quit']:  # Allowing the player to exit the conversation
            print("Exiting game.")
            break
        
        # Create a prompt for the AI based on the player's input
        prompt = f"A partially transformed zombie at the town gates says: '{player_input}' The guard, wary but unaware of the transformation, responds:"
        
        # Get the AI response and print it
        ai_response = get_ai_response(prompt)
        print(f"Guard says: {ai_response}")

if __name__ == "__main__":
    main()