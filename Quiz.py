class Quiz:
    Score = 0
    
    QuestionBank = [
        {"q" : "Name of Indian PM?", "a" : "a"},
        {"q" : "Speed of sound in air (in m/s)?", "a" : "c"},
        {"q" : "Major General is a rank in _____", "a" : "b"},
        {"q" : "Country with heighest military budget?", "a" : "b"}
        ]

    options = [
        ["a.Modi", "b.Ram", "c.Shah", "d.Anna"],
        ["a.1", "b.1234", "c.330", "d.infinite"],
        ["a.RAW", "b.Army", "c.Pilot", "d.Police"],
        ["a.India", "b.USA", "c.Russia", "d.Australia"]
        ]

    def display(self):
            for i in range (0,4):
                print("************************")
                print("************************")

                print ("Your Sorce is ", self.Score)
                print(self.QuestionBank[i]["q"])

                for j in self.options[i]:
                    print (j)
                    
                print()
                Choice = input ("Enter your Choice :")

                if (Choice == self.QuestionBank[i]["a"]):
                    self.Score += 1
                else :
                    print ("Oops you missed it")
                    print ("Your Sorce is ", self.Score)
                    break

q1 = Quiz()
q1.display()
z = input()
