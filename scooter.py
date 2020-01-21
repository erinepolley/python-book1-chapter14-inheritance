from vehicle import Vehicle

class Scooter(Vehicle):
    def __init__(self):
        self.grip_pad = ""
        self.foot_plate_material = ""
    def drive(self):
        print(f"The {self} goes rawr.")