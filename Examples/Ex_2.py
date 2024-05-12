import json

with open("file\Ex_2.json","r") as f:
    content = f.read()
data = json.loads(content)

for question in data:
    print(question["Question_text"])
    for index,alternative in enumerate(question["alternative"]):
        print(index+1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_ans"] = user_choice

score = 0
for index,question in enumerate(data):
    if question["user_ans"] == question["correct_ans"]:
        score+=1
        result = "correct answer"
    else:
        result = "incorrect answer"
    massage = (f"{index+1} {result} your answer: {question['user_ans']}, "
               f"correct answer: {question['correct_ans']}")
    print(massage)

print(score,"/",len(data))