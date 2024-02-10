from src.domain.entities import Question


class Repository:
    def __init__(self, file_name = "questions.txt"):
        self.__list_of_questions = []
        self.__file_name = file_name
        self.load_file()

    def add_question(self, id, text, first_answer, second_answer, third_answer, correct_answer, difficulty):
        for question in self.__list_of_questions:
            if question.id == id:
                raise ValueError("duplicated id")
        new_question = Question(id, text, first_answer, second_answer, third_answer, correct_answer, difficulty)
        self.__list_of_questions.append(new_question)
        self.save_file()

    def load_file(self):
        fin = open(self.__file_name, "rt")
        lines = []
        lines = fin.readlines()
        for line in lines:
            current_line = line.split(";")
            new_question = Question(current_line[0].strip(), current_line[1].strip(), current_line[2].strip(), current_line[3].strip(), current_line[4].strip(), current_line[5].strip(), current_line[6].strip())
            self.__list_of_questions.append(new_question)
        fin.close()

    def save_file(self):
        fout = open(self.__file_name, "wt")
        for question in self.__list_of_questions:
            question_string = str(question.id) + ";" + question.text + ";" + str(question.first_answer) + ";" + str(question.second_answer) + ";" + str(question.third_answer)  + ";" + str(question.correct_answer) + ";" + question.difficulty + "\n"
            fout.write(question_string)
        fout.close()
    def get_all(self):
        return self.__list_of_questions

