class Eagle:
    def __init__(self, species, wingspan, diet):
        self.species = species
        self.wingspan = wingspan
        self.diet = diet

    def fly(self):
        return f"The {self.species} eagle flies high with its {self.wingspan}-inch wingspan."


    def hunt(self):
        return f"The {self.species} eagle hunts for {self.diet}"

eagle1 = Eagle("Bald Eagle", "80", "fish")

print(eagle1.fly())
print(eagle1.hunt())