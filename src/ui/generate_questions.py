import random

def find(id, list_of_questions):
    if len(list_of_questions) > 0:
        for question in list_of_questions:
            if question[0] == id:
                return True
    return False

def generate_questions():
    number = 100
    index = 0
    list_of_questions = []
    while index < number:

        index += 1
        id = random.randint(1, 100)
        while find(id, list_of_questions) == True:
            id = random.randint(1, 100)
        q = ["Which number is the smallest?", "Which number is the largest"]
        question = q[random.randint(0, 1)]
        first_answer = random.randint(1, 1000)
        second_answer = random.randint(1, 1000)
        third_answer = random.randint(1, 1000)
        if question == "Which number is the smallest?":
            correct_answer = first_answer
            if correct_answer > second_answer:
                correct_answer = second_answer
            if correct_answer > third_answer:
                correct_answer = third_answer
        else:
            correct_answer = first_answer
            if correct_answer < second_answer:
                correct_answer = second_answer
            if correct_answer < third_answer:
                correct_answer = third_answer
        diff = ["easy", "medium", "hard"]
        difficulty = diff[random.randint(0, 2)]
        list_of_questions.append([id,question, first_answer, second_answer, third_answer,correct_answer,difficulty])
    return list_of_questions

def put_in_file(list_of_questions):
    fout = open("../questions.txt", "wt")
    for question in list_of_questions:
        question_string = str(question[0]) + ";" + question[1] + ";" + str(question[2]) + ";" + str(question[3]) + ";" + str(question[4]) + ";" + str(question[5]) + ";" + question[6] + "\n"
        fout.write(question_string)
    fout.close()

array = generate_questions()
put_in_file(array)