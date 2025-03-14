class Dog:
    def __init__(self, name):
        self.name = name 

    def sit(self):
        return f'"Sit, {self.name}."'
    
    def stay(self):
        return f'"Stay, {self.name}."'
    
dog1 = Dog("Cyrano")
dog1.sit(), dog1.stay()

class Fox:
    def __init__(self, name):
        self.name = name
       
    def say(self):
        return f"'What does {self.name} say? Ring-ding-ding-ding-dingeringeding! Gering-ding-ding-ding-dingeringeding! Gering-ding-ding-ding-dingeringeding!'"

fox1 = Fox("Orange")
fox1.say()