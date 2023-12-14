#import Model.model_exam

class Grades:
    def __init__(self, name, lName):
        self.name = name
        self.lName = lName

        self.math = []
        self.biology = []
        self.physics = []
        self.chemistry = []
        self.geology = []
        self.arabic = []
        self.history = []
        self.english = []
        self.dini = []

    def get_math(self):
        return self.math

    def get_biology(self):
        return self.biology

    def get_physics(self):
        return self.physics

    def get_chemistry(self):
        return self.chemistry

    def get_geology(self):
        return self.chemistry

    def get_arabic(self):
        return self.arabic

    def get_history(self):
        return self.history

    def get_english(self):
        return self.english

    def get_dini(self):
        return self.dini

    def set_math(self, math):
        self.math = math

    def set_biology(self, biology):
        self.biology = biology

    def set_physics(self, physics):
        self.physics = physics

    def set_chemistry(self, chemistry):
        self.chemistry = chemistry

    def set_geology(self, geology):
        self.geology = geology

    def set_arabic(self, arabic):
        self.arabic = arabic

    def set_history(self, history):
        self.history = history

    def set_english(self, english):
        self.english = english


def set_dini(self, dini):
    self.dini = dini


def add_exam_result(self, examRes):
    self.examResults.append(examRes)