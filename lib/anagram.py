# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word
    
    def match(self, annas):
        word = self.word
        result = []

        for entry in annas:
            if sorted([letter for letter in word]) == sorted([letter for letter in entry]):
                result.append(entry) 
        return result
            

