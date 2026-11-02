# ============ БАЗОВЫЙ КЛАСС ============
class Transport:
    """Базовый класс — транспортное средство."""
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        print(f"[Transport.__init__] Создан объект: {self.name}, скорость = {self.speed} км/ч")
    
    def move(self):
        """Метод базового класса."""
        print(f"[Transport.move] {self.name} движется со скоростью {self.speed} км/ч")
    
    def info(self):
        """Метод, который будет переопределён в производном классе."""
        return f"Транспорт: {self.name}, скорость: {self.speed} км/ч"
    
    def __str__(self):
        return self.info()


# ============ ПРОИЗВОДНЫЙ КЛАСС ============
class Car(Transport):
    """Производный класс — автомобиль."""
    
    def __init__(self, name, speed, fuel):
        # Вызов конструктора базового класса
        super().__init__(name, speed)
        self.fuel = fuel
        print(f"[Car.__init__] Доп. параметр: топливо = {self.fuel}")
    
    def move(self):
        """Переопределённый метод (полиморфизм)."""
        print(f"[Car.move] {self.name} едет на {self.fuel} со скоростью {self.speed} км/ч")
    
    def info(self):
        """Переопределённый метод — расширяет базовый."""
        base_info = super().info()
        return f"{base_info}, топливо: {self.fuel}"
    
    def honk(self):
        """Собственный метод производного класса (нет в базовом)."""
        print(f"[Car.honk] {self.name}: Би-бип!")


# ============ ТЕСТОВАЯ ПРОГРАММА ============
def main():
    print("=" * 60)
    print("1. Создание объектов")
    print("=" * 60)
    
    t = Transport("Велосипед", 20)
    c = Car("Лада", 120, "бензин")
    
    print("\n" + "=" * 60)
    print("2. Вызов переопределённого метода move()")
    print("=" * 60)
    t.move()   # метод базового класса
    c.move()   # метод производного класса (переопределён)
    
    print("\n" + "=" * 60)
    print("3. Вызов метода info()")
    print("=" * 60)
    print(t.info())
    print(c.info())          # расширенная версия
    print(f"str(c) -> {c}")  # через __str__
    
    print("\n" + "=" * 60)
    print("4. Собственный метод производного класса")
    print("=" * 60)
    c.honk()  # доступен только у Car
    
    print("\n" + "=" * 60)
    print("5. Полиморфизм: список объектов разных типов")
    print("=" * 60)
    vehicles = [Transport("Самокат", 15), Car("BMW", 200, "дизель"), Car("Tesla", 250, "электро")]
    for v in vehicles:
        v.move()   # у каждого вызовется своя версия метода
    
    print("\n" + "=" * 60)
    print("6. Проверка наследования (isinstance / issubclass)")
    print("=" * 60)
    print("isinstance(c, Transport):", isinstance(c, Transport))  # True
    print("isinstance(c, Car):      ", isinstance(c, Car))        # True
    print("isinstance(t, Car):      ", isinstance(t, Car))        # False
    print("issubclass(Car, Transport):", issubclass(Car, Transport))  # True


if __name__ == "__main__":
    main()