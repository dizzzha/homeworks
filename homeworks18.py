class Buiding:

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


first_buiding = Buiding(1, 'hello')
second_buiding = Buiding(1, 'hello')
print(first_buiding.__eq__(second_buiding))
