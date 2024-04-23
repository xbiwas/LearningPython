quiz = [
    {
       "Question":"What is the capital of Nepal?",
        "Answer": "Kathmandu"
    },
    {
       "Question":"What is the capital of India?",
        "Answer": "Delhi"
    },
]

# answer = input()

# if answer != quiz[0]["Answer"]:
#     print("Wrong")
# else:
#     print("Right")

def check_answer(question, user_answer):
    if user_answer != question["Answer"]:
        return "WRONG"
    else:
        return "RIGHT"

for question in quiz:
    print(question["Question"])
    userInput = input()
    result = check_answer(question, userInput)
    print(result)

