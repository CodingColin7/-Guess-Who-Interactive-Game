print("Welcome to 'Guess What I Am' game!")
print("_" * 25)
print("Do you wish to play?")

players_input = input("Yes or No? ")

if players_input.lower() != "yes":
    print("Come on, play it. I put it on my resume :)")
    quit()

print("_" * 25)
print("Awesome! Let's get straight to it!")
print(" - Before we start, you get 3 guesses, and 10 total hints. If you guess wrong, we'll take a life away!")
print("_" * 25)

lives = 3  # Initialize player's lives
hints_remaining = 10  # Initialize hints counter

# List of questions and hints based on a "mouse"
questions_hints = [
    ("I am something that you can use to get stuff done", "I'm a pointing device for computers"),
    ("I am used by businesses every day", "I process information digitally"),
    ("I am not an expensive item/thing", "You use me to navigate on a screen"),
    ("I can be moved around a lot", "You slide me across a surface"),
    ("I am not hard to control", "You click and scroll with me"),
    ("I am something you often hold in your hand", "I have buttons and a scroll wheel"),
    ("I am an essential tool for computer work", "You use me alongside a keyboard"),
    ("I am often seen with a computer", "I'm part of a computer setup"),
    ("I am a common input device", "I help you interact with your computer"),
    ("I am a small device", "I fit in the palm of your hand")  # Add more questions and hints here
]

def ask_question(question, hint):
    print(question)
    players_input = input("Do you wish to guess what I am? (Yes or No) ")
    
    if players_input.lower() == "yes":
        guess = input("What do you think I am? ").lower()
        if guess == "mouse":
            print("Congrats! You guessed it!")
            quit()
        else:
            global lives, hints_remaining
            lives -= 1
            print(f"Wrong answer! You have {lives} lives left.")
            if lives == 0:
                print("You lost. Play again!")
                quit()
            else:
                print("_" * 25)
                print(f"Question {len(questions_hints) - lives + 1}.")
                ask_question(*questions_hints[len(questions_hints) - lives])

for question, hint in questions_hints:
    ask_question(question, hint)
