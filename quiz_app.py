questions = [
    {
        "question": "What is the output of 3 + 2 * 2?",
        "options": ["10", "7", "9", "None"],
        "answer": "7"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": "Tuple"
    }
]

score = 0

for i, q in enumerate(questions):
    print(f"\nQ{i+1}: {q['question']}")
    for idx, opt in enumerate(q['options'], start=1):
        print(f"{idx}. {opt}")

    try:
        user_input = int(input("Your answer (1-4): "))
        if q['options'][user_input - 1] == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
    except:
        print("❌ Invalid input!")

print(f"\n🎯 Your final score: {score}/{len(questions)}")
