class Palyercontrol:
    def __init__(self,butkick,butleft,butright,butsit):  #THIS class is for the controls of player
        self.butkick=butkick
        self.butleft=butleft
        self.butright=butright
        self.butsit=butsit

    def printcontrol(self):
       print(f"button for kick={self.butkick},button for left look={self.butleft},button for right look{self.butright},button for sit={self.butsit}")

    buttonfire="enter"

    @classmethod
    def changefire(cls,butfire):
        cls.buttonfire=butfire

    @staticmethod
    def playerhealth():
        print("the health of the player is ",100)

class Playerapp:      #this class is for apperance for palyer
    def __init__(self,haircol,skincol):
        self.haircol=haircol
        self.skincol=skincol
    eyecol="blue"
    def printapp(self):
        print(f"hair colour of player={self.haircol},skin colour of player ={self.skincol}")

    @classmethod
    def changeeyecol(cls, eyecol):
        cls.eyecol = eyecol

    @staticmethod
    def playerstate():
        print("the state of the player is  awesome")


class Palyerlook(Palyercontrol,Playerapp):
    def __init__(self,butkick,butleft,butright,butsit,haircol,skincol):  #THIS class is for the controls of for both
        self.butkick=butkick
        self.butleft=butleft
        self.butright=butright
        self.butsit=butsit
        self.haircol = haircol
        self.skincol = skincol

    def printlook(self):
        print(
            f"button for kick={self.butkick},button for left looh={self.butleft},button for right look{self.butright},button for sit={self.butsit},hair colour of player={self.haircol},skin colour of player ={self.skincol}")


if __name__ == '__main__':

   samrat=Palyerlook("k","l","r","s","black","light brown")
   #now i can use the func of both palyercontrol and playerapp
   samrat.changeeyecol("black")
   print(samrat.eyecol)



   print(samrat.printlook())
   print(samrat.eyecol)