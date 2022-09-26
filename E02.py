import random


class Dog:
    """A simple attempt to model a dog."""
    
    
    def __init__(self, name, age, color):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.color = color
        

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

    def dog_color(self):
        """Tells the dogs color"""
        print(f"{self.name} is {self.color}")


class Band:

    def __init__(self, band_name, music_genre):
        self.band_name = band_name
        self.music_genre = music_genre
        self.active_state = "Not active"
        self.home_awards = 0
        self.international_awards = 0

    def describe_band(self):
        print(f"{self.band_name} plays {self.music_genre}")

    def is_active(self):
        print(f"{self.band_name} is {self.active_state}")

    def set_status(self,boolean):

        if (boolean == True):
            self.active_state = "Active"
        
        elif(boolean == False):
            self.active_state = "Not Active"
        
        else:
            self.active_state = "Use ("'True'") or ("'False'") as a parameter"

    def set_home_awards(self,number):
        self.home_awards = number

    def set_international_awards(self,number):
        self.international_awards = number
        
class RockBand(Band):

    def __init__(self,band_name,music_genre,rock_concert_movements):
        super().__init__(band_name,music_genre)
        self.rock_concert_movements = rock_concert_movements

    def moves(self):
        print("moves seen in",self.band_name, "concert = ",*self.rock_concert_movements)

class Choir(Band):
    def __init__(self,band_name,music_genre,size):
        super().__init__(band_name,music_genre)
        self.size = size

    def choir_size(self):
        print(f"size of {self.band_name} is {self.size}")

    def change_size(self,number):
        self.size = number

class Coin():

    sides = 1     

    def toss_coin():
        sides = random.randint(0,1)
        if sides == 1:
            print ("Head")
        if sides == 0:
            print ("Tail")

dog = Dog("testi",8,"Brown")
dog.dog_color()

band = Band("Nickelback","Rock")
print(band.band_name,band.music_genre)
band.describe_band()

band.is_active()
band.set_status(True)
band.is_active()

band1 = Band("band1","Rock")
band1.describe_band()
band2 = Band("band2","Techno")
band2.describe_band()
band3 = Band("band3","Metal")
band3.describe_band()

band.set_home_awards(2)
band.set_international_awards(4)
print (f"Home awards = {band.home_awards},international awards = {band.international_awards}")


rockband = RockBand("Rock'n'Rolla","Rock",list(("head bobbing","Devil horns","Jumping")))
rockband.moves()


choir = Choir("zingers","Choir",8)
choir.choir_size()
choir.change_size(10)
choir.choir_size()

for i in range(0,50):
    Coin.toss_coin()