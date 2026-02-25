# Create a program capable of displaying questions to user like KBC (Kaun Banega Crorepati) and accepting answers.Use List data type to store questions and their correct answers.Display the final amount the person is taking home after playing the game.

def kbc_game():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
            "answer": "A"
        },
        {
            "question": "Who is known as the Father of the Nation?",
            "options": ["A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. Subhas Chandra Bose", "D. Bhagat Singh"],
            "answer": "B"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Mars", "C. Saturn", "D. Jupiter"],
            "answer": "D"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["A. Oxygen", "B. Gold", "C. Silver", "D. Iron"],
            "answer": "A"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Jane Austen"],
            "answer": "C"
        },
        {
            "question": "What is the currency of Japan?",
            "options": ["A. Rupee", "B. Dollar", "C. Yen", "D. Pound"],
            "answer": "C"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["A. China", "B. Japan", "C. South Korea", "D. Thailand"],
            "answer": "B"
        }
    ]

    prize_money = [1000,2000,3000,5000,6000,7000,8000]
    total_amount = 0

    print("Welcome to Kaun Banega Crorepati!")
    
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Please enter your answer (A/B/C/D): ").strip().upper()
        
        if answer == q['answer']:
            total_amount += prize_money[i]
            print(f"Correct! You have won Rs. {prize_money[i]}. Total amount: Rs. {total_amount}")
        else:
            print(f"Wrong answer! The correct answer was {q['answer']}. You are taking home Rs. {total_amount}.")
            break
    else:
        print(f"Congratulations! You have answered all questions correctly and are taking home Rs. {total_amount}.")


if __name__ == "__main__":
    kbc_game()

