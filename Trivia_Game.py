import random

questions = {
    "What is the keyword used to define a function in Python?": "def",
    "What data type is used to store a sequence of characters?": "string",
    "What symbol is used for comments in Python?": "#",
    "What is the built-in function to get the length of a list?": "len",
    "What keyword is used to create a class in Python?": "class",
    "What is the name of the Python package manager?": "pip",
    "What keyword is used to handle exceptions in Python?": "try",
    "What is the default return value of a function that does not explicitly return a value?": "None",
    "What is the term for a variable that is defined outside of a function?": "global",
    "What is the method used to add an element to the end of a list?": "append"
}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0
    
    selected_questions = random.sample(questions_list, total_questions)

    for index, question in enumerate(selected_questions):
        print(f"{index + 1}.{question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]
        
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {correct_answer}.\n")

    print(f"Game over! Your Final Score is: {score}/{total_questions}")

python_trivia_game()


