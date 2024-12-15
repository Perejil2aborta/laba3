class Cone:
    def __init__(self, radius1, radius2, height):
        self._radius1 = radius1
        self._radius2 = radius2
        self._height = height

    @staticmethod
    def about():
        print("Программа расчета объема усеченного конуса. Разработано командой TopilMubil.")
    
class TruncatedCone(Cone):
    def __init__(self, radius1, radius2, height):
        super().__init__(radius1, radius2, height)

    def volume(self):
        return (1 / 3) * 3.14159 * self._height * (
                    self._radius1 ** 2 + self._radius1 * self._radius2 + self._radius2 ** 2)


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка: пожалуйста, введите числовое значение.")


if __name__ == "__main__":
    Cone.about()

    radius1 = get_float_input("Введите верхний радиус усеченного конуса: ")
    radius2 = get_float_input("Введите нижний радиус усеченного конуса: ")
    height = get_float_input("Введите высоту усеченного конуса: ")

    truncated_cone = TruncatedCone(radius1, radius2, height)

    print(f"Объем усеченного конуса: {truncated_cone.volume()} кубических единиц.")
