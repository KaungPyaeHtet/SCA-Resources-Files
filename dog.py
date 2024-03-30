class Dog:
    "A simple attempt to model a dog"
    
    def __init__(self, name, age):
        "Initialize name and age attributes"
        self.name = name
        self.age = age
    
    def roll_over(self):
        "Stimulates the dog to roll over"
        print(self.name, 'is rolling over to you')
        
    def sit(self):
        "Stimulates the dog to sit"
        print(self.name, 'is sitting down')
        
# __init__() Runs automatically when you created the instance