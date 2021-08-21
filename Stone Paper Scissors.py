import random

#selectors
roles = ["stone", "paper", "scissor"]
command = ["start", "help"]
yes = ["Yes", "yes", "Y", "y"]
no = ["No", "no", "N", "n"]
leave = ["quit", "exit"]
#instructions
help = """In this game, you will play Stone, Paper & Scissors with your imaginary friend.
Here's a bit help (commands)~
help - to see this message.
start - to start playing
stone - to select Stone.
paper - to select Paper.
scissor - to select Scissors.
quit / exit - to leave the game.

Type 'start' to start playing. """

#values
m_score = 0
p_score = 0
start = '''
Welcome to Stone, Paper & Scissors!
Type "help" for more info!
'''
print(start)
#inputs
go = True
run = False
while go:
    you = input(">> ")
    if you == "help":
        print(help)
    elif you == "start":
        print("Alright! Lets Go... \nChoose from stone, paper or scissor!")
        run = True
        while run:
            mac = random.choice(roles)
            you = input(">> ")
            if you == "help":
                print(help)
            elif you == mac:
                print("Oh Its a Tie.")
                print(f"You: {you} \nFriend: {mac} \n")
                print(f"Score: You = {p_score} | Friend: {m_score}")
            elif you == "paper":
                if mac == "stone":
                    print("You Won!")
                    p_score += 1
                else:
                    print("Friend Won!")
                    m_score += 1
                print(f"You: {you} \nFriend: {mac} \n")
                print(f"Score: You = {p_score} | Friend: {m_score}")
            elif you == "stone":
                if mac == "scissor":
                    print("You Won!")
                    p_score += 1
                else:
                    print("Friend Won!")
                    m_score += 1
                print(f"You: {you} \nFriend: {mac} \n")
                print(f"Score: You = {p_score} | Friend: {m_score}")
            elif you == "scissor":
                if mac == "paper":
                    print("You Won!")
                    p_score += 1
                else:
                    print("Friend Won!")
                    m_score += 1
                print(f"You: {you} \nFriend: {mac} \n")
                print(f"Score: You = {p_score} | Friend: {m_score}")
            elif you in leave:
                print("Are you sure? Y/N")
                run = False
                break
            else:
                print("Invalid Command!")
    elif you in no:
        print("Oh, another round? \nPlease type 'start' to continue")
    elif you in yes:
        print("Good Game! See ya soon!")
        break
    elif you in leave:
        print("Sad to see you go...")
        break
    else:
        print("Invalid Command!")

