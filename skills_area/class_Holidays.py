class Holidays:
    def __init__(self, destination, duration, budget):
        self.destination = destination
        self.duration = duration
        self._budget = budget  # Приватный атрибут

    def get_budget(self):
        return self._budget

    def set_budget(self, budget):
        self._budget = budget

    def display_info(self):
        print(f"Destination: {self.destination}, Duration: {self.duration}, Budget: {self._budget}")

# Создаем экземпляры класса
holidays1 = Holidays("Paris", "1 week", "$1000")
holidays2 = Holidays("Tokyo", "10 days", "$3000")

# Выводим информацию о поездках
holidays1.display_info()
holidays2.display_info()

# Изменяем приватный атрибут с помощью метода set
holidays1.set_budget("$1500")
holidays1.display_info()

# Получаем значение приватного атрибута с помощью метода get
print("New budget:", holidays1.get_budget())


# Выводим информацию о каждом празднике
print("Праздник 1:")
print("Место назначения:", holidays1.destination)
print("Продолжительность:", holidays1.duration)
print("Бюджет:", holidays1._budget)

print("\nПраздник 2:")
print("Место назначения:", holidays2.destination)
print("Продолжительность:", holidays2.duration)
print("Бюджет:", holidays2._budget)

