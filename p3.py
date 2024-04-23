quiz = [
    {
       "Question":"What is the capital of Nepal?",
        "Answer": "Nepal"
    },
    {
       "Question":"What is the capital of India?",
        "Answer": "Delhi"
    },
]

print("What is the capital of nepal")
answer = input()

if answer != quiz[0].Answer:
    print("Wrong")
else:
    print("Right")