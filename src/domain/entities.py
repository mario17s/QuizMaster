class Question:
    def __init__(self, id, text, first_answer, second_answer, third_answer, correct_answer, difficulty):
        self.__id = id
        self.__text = text
        self.__first_answer = first_answer
        self.__second_answer = second_answer
        self.__third_answer = third_answer
        self.__correct_answer = correct_answer
        self.__difficulty = difficulty

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    @property
    def first_answer(self):
        return self.__first_answer

    @first_answer.setter
    def first_answer(self, value):
        self.__first_answer = value

    @property
    def second_answer(self):
        return self.__second_answer

    @second_answer.setter
    def second_answer(self, value):
        self.__second_answer = value

    @property
    def third_answer(self):
        return self.__third_answer

    @third_answer.setter
    def third_answer(self, value):
        self.__third_answer = value

    @property
    def correct_answer(self):
        return self.__correct_answer

    @correct_answer.setter
    def correct_answer(self, value):
        self.__correct_answer = value

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, value):
        self.__difficulty = value

    def __str__(self):
        return str(self.__id) + " " + self.__text + " " + str(self.__first_answer) + " " + str(self.__second_answer) + " " + str(self.__third_answer) + " -> " + self.__difficulty