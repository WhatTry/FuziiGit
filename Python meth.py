import random
import time

def generate_problem():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    
    # Ensure that the division has the higher number as the numerator
    if num1 < num2:
        num1, num2 = num2, num1
    
    operator = random.choice(['+', '-', '*', '/'])
    expression = f"{num1} {operator} {num2}"
    result = eval(expression)
    return expression, result, operator

def countdown(count):
    for i in range(count, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)

def is_valid_number(user_input):
    try:
        float(user_input)
        return True
    except ValueError:
        return False

def play_game():
    print("Welcome to the 30 seconds minigame!")
    print("You will have exactly 30 seconds to solve as many problems as you can.")
    
    headstart_duration = 5
    countdown(headstart_duration)

    score = 0
    start_time = time.time()
    end_time = start_time + 30

    while time.time() < end_time:
        problem, correct_answer, operator = generate_problem()
        print(f"Solve: {problem}")

        user_answer = input("Your answer: ")

        # Check if the user answer is a valid number
        if is_valid_number(user_answer):
            if round(float(user_answer), 2) == round(correct_answer, 2):
                print("Correct!\n")
                score += 1
            else:
                formatted_correct_answer = '{:.2f}'.format(correct_answer).rstrip('0').rstrip('.')
                print(f"Wrong! The correct answer was {formatted_correct_answer}\n")
        else:
            print("Invalid input! Please enter a valid number.\n")

    print(f"Time's up! Your score: {score}")

# Run the game
play_game()