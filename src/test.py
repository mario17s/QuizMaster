import unittest

from src.repo.repository import Repository
from src.serv.service import Service


class TestCreateQuiz(unittest.TestCase):
    def test_1(self):
        r = Repository()
        s = Service(r)
        questions = s.create_quiz("easy", 5, "test.txt")
        for q in questions:
            self.assertEqual(q.difficulty, "easy")

    def test_2(self):
        r = Repository()
        s = Service(r)
        questions = s.create_quiz("medium", 6, "test.txt")
        count = 0
        for q in questions:
            if q.difficulty == "medium":
                count += 1
        self.assertGreater(count, 3)

    def test_3(self):
        r = Repository()
        s = Service(r)
        try:
            questions = s.create_quiz("hey", 6, "test.txt")
        except ValueError as ve:
            pass

    def test_4(self):
        r = Repository()
        s = Service(r)
        questions = s.create_quiz("medium", 6, "test.txt")
        self.assertEqual(len(questions), 6)
