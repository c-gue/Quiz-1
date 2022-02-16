import random

'''
Create a Weapon Class definition according to the following specs:

Attributes:

name - user supplied
bullets - random number between 10 and 100000
speed - user supplied
range - user supplied
status - 'Active' (this attribute should be changed to 'Inactive' if bullets 
                    run out.)

Methods:

Create accessor methods for each attribute.

Create a method named 'fire_bullet' that will simulate
firing a bullet. This is accomplished by decreasing the number of bullets by 1 
every time the method is called. When the bullet count reaches zero, it should change
the attribute 'status' to 'Inactive'

'''
class Weapon():
    def __init__(self,name,mph,distance):
        self.__Name = name
        self.__Bullets = random.randint(10,10000)
        self.__Speed = mph
        self.__Range = distance
        self.__Status = "Active"


    def fire_bullet(self):
        self.__Bullets -= 1

    def status(self):
        if self.__Bullets == 0:
            self.__Status = 'Inactive'

    def get_name(self):
        return self.__Name

    def get_bullets(self):
        return self.__Bullets

    def get_speed(self):
        return self.__Speed

    def get_range(self):
        return self.__Range

    def get_status(self):
        return self.__Status










