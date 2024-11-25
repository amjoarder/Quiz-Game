def quiz_game():
    print("Welcome to the Quiz Game!")
    
    # Define questions and answers
    questions = [
        {"question": "What is the capital of France?", "answer": "paris"},
        {"question": "What is 5 + 7?", "answer": "12"},
        {"question": "Which programming language is known as 'Python'?", "answer": "python"},
        {"question": "What is the color of the sky on a clear day?", "answer": "blue"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "shakespeare"}
    ]

    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was '{q['answer']}'.")

    print(f"\nGame Over! Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
