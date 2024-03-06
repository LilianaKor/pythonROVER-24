class Sport:
    def __init__(self, team, size, budget):
        self.team = team  # Количество команд
        self.size = size  # Размер поля/площадки
        self.__budget = budget  # Бюджет на спортивные мероприятия
        self.__type = "Sport"  # Private attribute

    def get_team(self):
        return self.team

    def get_size(self):
        return self.size

    def get_budget(self):
        return self.__budget

    def set_budget(self, new_budget):
        self.__budget = new_budget

    def get_type(self):
        return self.__type
    def set_type(self, new_type):
        self.__type = new_type

    # def play(self):
    #     print(f"Playing {self.__type}")

    def display_info(self):
        print(f"Team: {self.team}, Size: {self.size}, Budget: {self.__budget}, Type: {self.__type}")

class TennisLesson(Sport):
    def __init__(self, team, size, budget):
        super().__init__(team, size, budget)
        self.set_type("Tennis Lesson")

class TennisGeneral(Sport):
    def __init__(self, team, size, budget):
        super().__init__(team, size, budget)
        self.set_type("Tennis General")

class Swimming(Sport):
    def __init__(self, team, size, budget):
        super().__init__(team, size, budget)
        self.set_type("Swimming")


tennis_lesson = TennisLesson(team=5, size="small", budget=10000)
# print("Количество команд:", tennis_lesson.get_team())
# print("Размер поля:", tennis_lesson.get_size())
# print("Бюджет:", tennis_lesson.get_budget())
#print("Тип:", tennis_lesson.get_type())

tennis_gen = TennisGeneral(team=20, size="big", budget=5000)
# print("Количество команд:", tennis_gen.get_team())
# print("Размер поля:", tennis_gen.get_size())
# print("Бюджет:", tennis_gen.get_budget())
#print("Тип:", tennis_gen.get_type())

swim = Swimming(team=7, size="standart", budget=12000)
# print("Количество команд:", swim.get_team())
# print("Размер поля:", swim.get_size())
# print("Бюджет:", swim.get_budget())
#print("Тип:", swim.get_type())

tennis_lesson.display_info()
tennis_gen.display_info()
swim.display_info()
