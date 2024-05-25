class House:

    def __init__(self):
        self.numberOfFloors = 0

    def set_new_number_of_floors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


main_home = House()
main_home.set_new_number_of_floors(floors=3)


