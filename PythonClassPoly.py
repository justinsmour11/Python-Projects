
class Person:
    def __init__(self,arms,legs,gender,origin):
        self.arms = arms
        self.legs = legs
        self.gender = gender
        self.origin = origin

    def identity(self):
        msg = ("I'm a {} from {} with {} arms and {} legs.".format(\
            self.gender,self.origin,self.arms,self.legs))
        return msg

class PeoplePerson(Person):
    peopleSkills = True
    charismaLvl = 10
    
    def identity(self):
        msg = ("I'm a {} from {} with {} arms and {} legs, who is good with people!".format(\
            self.gender,self.origin,self.arms,self.legs))
        return msg     

class NotPeoplePerson(Person):
    peopleSkills = False
    deductionLvl = 10
    
    def identity(self):
        msg = ("\nI'm a {} from {} with {} arms and {} legs, who is NOT good with people!".format(\
            self.gender,self.origin,self.arms,self.legs))
        return msg



if __name__ == "__main__":
    people = PeoplePerson(2,2,'Male','Oklahoma')
    print(people.identity())
    print(people.peopleSkills)
    print(people.charismaLvl)

    notpeople = NotPeoplePerson(2,1,'Female','Oregon')
    print(notpeople.identity())
    print(notpeople.peopleSkills)
    print(notpeople.deductionLvl)
