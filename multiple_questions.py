from question_class import Questions

question_prompt = [
    "what colour is the sky? A.blue\n B.Red\n C.Yellow\\n",
    "what colour is Danger? A.blue\n B.Red\n C.Yellow\\n",
    "what colour is Banana? A.blue\n B.Red\n C.Yellow\\n"
]

question = [
    Questions(question_prompt[0], "A"),
    Questions(question_prompt[1], "B"),
    Questions(question_prompt[2], "C"),

]


def run_test():
    score = 0
    for index in question_prompt:
        answer = input(question.prompt)
        if question == question.answer:
            score += 1
        return score
    print("you scored" + str(score) + "/" + str(len(question_prompt)) + "correct")







