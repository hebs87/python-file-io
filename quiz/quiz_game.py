'''
Our game will store questions and answers in a file
When you run it, it will ask the questions and check your answers against those in the file.
At the end of the quiz, it will tell you how many questions you got right.
It will also allow us to add new questions and answers to our quiz file.
When we run the game, we will be presented with a menu with the following options:
the first option to ask questions;
the second to add a question;
and the third to exit the game.
If you select option 1 to ask questions, the game will display each quiz question in turn, asking for the answer to each one.
When you give an answer, the game will indicate whether it's right or wrong before moving to the next question.
After all of the questions have been answered, the game will display how many out of the total number of questions asked that you got right.
It will then return to the main menu.
If we select option 2 to add a question, the game will prompt the user for the question and the answer,
and it will append these to the questions file. It will then return to the main menu.
Finally, if we choose option 3 then the game will simply shut down
'''

'''
Function to create simple game menu
Lists 3 options and asks user to choose an option
This then returns the option that the user has chosen
'''
def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")
    
    option = input("Enter option: ")
    return option

'''
Function to ask questions
The user's input will then be verified and checked to see if it is true
The user's score will be tracked
'''
def ask_questions():
    questions = []
    answers = []
    
    # Handy alternative, as at the end of the with block, it will be closed, so we don't have to use the close() method
    with open('questions.txt', 'r') as file:
        # Create a variable in which we read our file in and split the lines
        lines = file.read().splitlines()
    
    # The enumerate() function turns each list into a tuple, with the line number stored in i and the text in text
    for i, text in enumerate(lines):
        # If the line number is even, that is a question, if not, then it's an answer
        if i % 2 == 0:
            # We append the text to the questions list
            questions.append(text)
        else:
            # We append the text to the answers list
            answers.append(text)
    
    # The zip() function puts the questions and answers together
    for question, answer in zip(questions, answers):
        # We zip the question and answers together, and we add in our guess here
        guess = input(question + "> ")
    
'''
Function to allow user to add a question and answer
The input will then be appended to the questions.txt file
'''
def add_question():
    # Print a blank line
    print("")
    question = input("Enter a question\n> ")
    
    print("")
    print("OK then, tell me the answer")
    # We take the question that we've already asked and parse it into the input string, so user will be asked question again when they come to answer it
    answer = input("{0}\n> ".format(question))
    
    # Now we add it to the questions.txt file
    file = open('questions.txt', 'a')
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

'''
Function to loop the game while the condition is true
We want to loop the function infinitely, unless there is a break in the statement
'''
def game_loop():
    while True:
        # Call our show_menu() function and store whatever option was chosen
        option = show_menu()
        if int(option) == 1:
            # Run the ask_question() function, which allows the user to add a question and answer
            ask_questions()
        elif int(option) == 2:
            # Run the add_question() function, which allows the user to add a question and answer
            add_question()
        elif int(option) == 3:
            break
        else:
            print("Invalid option")
        # Finally, we print a blank line for presentation purposes
        print("")

game_loop()