#Creating a class and initializing variable lyrics
class Songs():
    def __init__(self,lyrics):
        "Initializing variable lyrics"
        self.lyrics=lyrics

    def sing_me_a_song(self):
        "printing lyrics and happy_bday song in form of list"
        print(self.lyrics)
        print(type(self.lyrics))
        happy_bday= ["May god bless you, ", "Have a sunshine on you,", "Happy Birthday to you !"]
        print(*happy_bday)
        print(type(happy_bday))

Songs_object1=Songs(['I believe i can fly, I believe i can touch the sky'])
Songs_object1.sing_me_a_song()