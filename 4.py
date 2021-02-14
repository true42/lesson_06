from my_class import WorkCar, PoliceCar, SportCar, TownCar


work_car = WorkCar(80, 'red', 'camry')
print(work_car)
work_car.show_speed()
work_car.go()
work_car.turn('налево')

police_car = PoliceCar(25, 'чёрная', 'ока', True)
print(police_car)
police_car.go()
police_car.turn('назад')
police_car.stop()

sport_car = SportCar(1000, 'синяя', 'Ока')
print(sport_car)

town_car = TownCar(61, 'зелёная', 'самоходка')
print(town_car)
town_car.go()
town_car.show_speed()
town_car.stop()