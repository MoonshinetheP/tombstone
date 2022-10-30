import datetime as dt

class Person:
    def __init__(self,name,birthdate,deathdate,occupation):

        self.name = name
        self.birthdate = birthdate
        self.deathdate = deathdate
        self.occupation = occupation
    
    def age(self):
        age = self.deathdate - self.birthdate
        return age

    def tombstone(self):
        print('In memory of')
        print(self.name)
        print(f'who died at the age of {self.age()}')
        print(f'{self.birthdate} - {self.deathdate}')
        print(self.occupation)
    
        
thislife = Person(name = 'Steven Linfield', birthdate = dt.datetime(1992,8,30,10,16), deathdate = None, occupation = 'Scientist, coder, goat enthusiast')
setattr(thislife, 'deathdate', dt.datetime(2093,3,15,14,50))
thislife.tombstone()