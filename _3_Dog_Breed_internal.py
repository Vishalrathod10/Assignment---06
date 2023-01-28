class dog:
    def description(self):
        self.name = input("\nPLESE ENTER THE NAME OF YOUR DOG : ")
        self.age = (input("\nPLEASE ENTER THE AGE OF YOUR DOG : "))

    def getinfo(self):
        self.coat_color = input("\nPLEASE ENTER THE COAT COLOR OF YOUR DOG : ")

    def display(self):
        print('\nNAME : ',self.name)
        print('AGE : ',self.age)
        print('COAT COLOR : ',self.coat_color)

class jackRusselTerrier(dog):
    def inteligence(self):
       self.intel_rank = (input("\nINTELIGENCY RANK OF YOUR DOG : "))

    def popularity(self):
        self.popular_rank = (input('\nPOPULARITY RANK OF YOUR DOG : '))

    def display1(self):
        print('POPULARITY RANK : ',self.popular_rank)
        print('INTELLIGENCY RANK : ',self.intel_rank)

class Bulldog(dog):
    def inteligence(self):
       self.intel_rank = int(input("\nINTELIGENCY RANK OF YOUR DOG : "))
       return f"\nINTELLIGENCE RANK : {self.intel_rank}"

    def popularity(self):
        self.popular_rank = int(input('\nPOPULARITY RANK OF YOUR DOG : '))
        return f"\nPOPULARITY RANK : {self.popular_rank}"

    def display2(self):
        print('POPULARITY RANK : ',self.popular_rank)
        print('INTELLIGENCY RANK : ',self.intel_rank) 


jackRusselTerrier_obj = jackRusselTerrier()
jackRusselTerrier_obj.description()
jackRusselTerrier_obj.getinfo()
jackRusselTerrier_obj.inteligence()
jackRusselTerrier_obj.popularity()
jackRusselTerrier_obj.display()
jackRusselTerrier_obj.display1()

Bulldog_obj = Bulldog()
Bulldog_obj.description()
Bulldog_obj.getinfo()
Bulldog_obj.inteligence()
Bulldog_obj.popularity()
Bulldog_obj.display()
Bulldog_obj.display2()






