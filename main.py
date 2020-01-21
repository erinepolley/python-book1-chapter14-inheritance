from scooter import Scooter
from golf_cart import GolfCart

hot_wheelz = Scooter()
hot_wheelz.grip_pad = "stretch"
print(hot_wheelz.grip_pad)
print(hot_wheelz.drive())
barret = GolfCart()
barret.driver_type = "drunk"
print(barret.driver_type)