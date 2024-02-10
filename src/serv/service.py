import unittest

from src.repo.repository import Repository


class Service:
    def __init__(self, repo):
        self.__repository = repo

    def add_question(self, id, text, first_answer, second_answer, third_answer, correct_answer, difficulty):
        if len(text) < 5:
            raise ValueError("Question too short")
        if correct_answer != first_answer and correct_answer != second_answer and correct_answer != third_answer:
            raise ValueError("invalid correct answer")
        if difficulty not in ["easy", "medium", "hard"]:
            raise ValueError("invalid difficulty")
        self.__repository.add_question(id, text, first_answer, second_answer, third_answer, correct_answer, difficulty)

    def create_quiz(self, difficulty, nb_of_questions, file_name):
        '''

        :param difficulty: the difficulty of the question is provided, but it has to be verified
        :param nb_of_questions: the number of questions we want to have in the quiz
        :param file_name: the name of the file where we want the quiz to be saved
        :return:

        questions are added in an array until we exceed the number of questions
        we validate and write the questions in the file
        '''
        if difficulty not in ["easy", "medium", "hard"]:
            raise ValueError("invalid difficulty")
        quiz_questions = []
        index = 0
        for question in self.__repository.get_all():
            if question.difficulty == difficulty:
                index += 1
                quiz_questions.append(question)
                if index >= nb_of_questions:
                    break
        if index < nb_of_questions // 2:
            raise ValueError(f'not enough {difficulty} questions')
        if index < nb_of_questions:
            for question in self.__repository.get_all():
                if question.difficulty != difficulty:
                    index += 1
                    quiz_questions.append(question)
                    if index >= nb_of_questions:
                        break
        fout = open(file_name, "wt")
        for question in quiz_questions:
            question_string = str(question.id) + ";" + question.text + ";" + str(question.first_answer) + ";" + str(question.second_answer) + ";" + str(question.third_answer)  + ";" + str(question.correct_answer) + ";" + question.difficulty + "\n"
            fout.write(question_string)
        fout.close()
        return quiz_questions

    def get_all(self):
        return self.__repository.get_all()

