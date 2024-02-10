from src.domain.entities import Question


class Console:
    def __init__(self, serv):
        self.__service = serv

    def print_options(self):
        print("WELCOME TO QUIZ!")
        print("add")
        print("create quiz")
        print("start an existing quiz")

    def read_command(self, command):
        position = command.find(" ")
        if position == -1 and command == "exit":
            return command, []
        given_command = command[:position]
        if given_command == "add":
            arguments = command[position + 1:]
            arguments = arguments.split(";")
            return given_command, arguments
        if given_command == "create":
            arguments = command[position + 1:]
            arguments = arguments.split(" ")
            return given_command, arguments
        if given_command == "start":
            arguments = command[position + 1:]
            arguments = arguments.split(" ")
            return given_command, arguments
        raise ValueError("not ok")

    def add_question(self, id, text, first_answer, second_answer, third_answer, correct_answer, difficulty):
        id = int(id)
        first_answer = int(first_answer)
        second_answer = int(second_answer)
        third_answer = int(third_answer)
        correct_answer = int(correct_answer)
        self.__service.add_question(id, text, first_answer, second_answer, third_answer, correct_answer, difficulty)

    def create_quiz(self, difficulty, nb_of_questions, file_name):
        nb_of_questions = int(nb_of_questions)
        quiz = self.__service.create_quiz(difficulty, nb_of_questions, file_name)

    def start_quiz(self, file_name):
        fin = open(file_name, "rt")
        lines = []
        lines = fin.readlines()
        quiz = []
        for line in lines:
            current_line = line.split(";")
            new_question = Question(current_line[0].strip(), current_line[1].strip(), current_line[2].strip(), current_line[3].strip(), current_line[4].strip(), current_line[5].strip(), current_line[6].strip())
            quiz.append(new_question)
        fin.close()

        official_quiz = []
        for question in quiz:
            if question.difficulty == "easy":
                official_quiz.append(question)
        for question in quiz:
            if question.difficulty != "easy":
                official_quiz.append(question)

        player_score = 0
        for question in official_quiz:
            print(question)
            choice = input("your choice: ")
            while choice != question.first_answer and choice != question.second_answer and choice != question.third_answer:
                print("choice is not in list")
                choice = input("your choice: ")
            if choice == question.correct_answer:
                if question.difficulty == "easy":
                    player_score += 1
                if question.difficulty == "medium":
                    player_score += 2
                if question.difficulty == "hard":
                    player_score += 3
        print(f' your score is {player_score}')



    def run_console(self):
        questions = self.__service.get_all()
        for q in questions:
            print(q)
        commands = {
            "add": self.add_question,
            "create": self.create_quiz,
            "start": self.start_quiz
        }
        max_parameters = {
            "add": 7,
            "create": 3,
            "start": 1
        }
        while True:
            self.print_options()
            command = input(">")
            try:
                given_command, arguments = self.read_command(command)
                if given_command == "exit":
                    break
                if len(arguments) != max_parameters[given_command]:
                    raise ValueError("invalid nb of arguments")
                commands[given_command](*arguments)
            except ValueError as ve:
                print(ve)
            except KeyError as ke:
                print(ke)
            except IOError as ioe:
                print(ioe)