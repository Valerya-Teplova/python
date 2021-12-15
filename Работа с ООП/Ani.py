"""
Написать класс "Животные", который вкл в себя общие признаки и поведения животных.
Наследовать от "Животные" класс "Млекопитающие", который вкл в себя общие признаки и поведения млекопитающих.
Наследовать от "Млекопитающие" класс "Человек", "Кот", "Собака", у каждого свои признаки и поведения.
"""

class animals:
    def __init__(self, name, gender, age, 
    height, weight): 
        self.name = name
        self.gender = gender        
        self.age = age
        self.height = height
        self.weight = weight

class mammals(animals):
    def __init__(self, name, gender, age,
     height, weight, breed, color): 
        
        self.name = name
        self.gender = gender
        self.age = age        
        self.height = height
        self.weight = weight
        self.breed = breed
        self.color = color

class human(mammals):
    def __init__(self, name, gender, age, 
    height, weight, income, workstag, 
    company, breed=0, color=0): 
        super().__init__(name, gender, age,  
        height, weight, breed, color)
        self.income = income
        self.workstage = workstag
        self.company = company

class Cat(mammals):
    def __init__(self, name, eyescolor, human, 
    gender, age,  height, weight,
     breed, color): 
        super().__init__( name, gender, age, 
         height, weight, breed, color)
        self.eyescolor = eyescolor
        self.human = human
        self.color = color


class Dog(mammals):
    def __init__(self, name, gender, age,
     height, weight, breed, 
     color, human):
        super().__init__( name, gender, age, 
        height, weight, breed, color)
        self.human = human
        self.color = color