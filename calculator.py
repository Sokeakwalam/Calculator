from re import U
from data_cleaning import clean_data

   
# bracket, off, division, multiplication, (addition, subtraction) same level

class Calculate:
    
    def calculation(self, user_input):
        self.inputs = clean_data(user_input)
        while '*' in self.inputs:
            for i, x in enumerate(self.inputs):
                if x == '*':
                    mult = float(self.inputs[i-1]) * float(self.inputs[i+1])
                    del self.inputs[i-1:i+2]
                    self.inputs.insert(i-1, mult) 
                    break

        while '/' in self.inputs:
            for i, x in enumerate(self.inputs):
                if x == '/':
                    div = float(self.inputs[i-1]) / float(self.inputs[i+1])
                    del self.inputs[i-1:i+2]
                    self.inputs.insert(i-1, div)
                    break

        while '+' in self.inputs:
            for i, x in enumerate(self.inputs):
                if x == '+':
                    addition = float(self.inputs[i-1]) + float(self.inputs[i+1])
                    del self.inputs[i-1:i+2]
                    self.inputs.insert(i-1, addition)
                    break
        while '-' in self.inputs:
            for i, x in enumerate(self.inputs):
                if x == '-':
                    minus = float(self.inputs[i-1]) - float(self.inputs[i+1])
                    del self.inputs[i-1:i+2]
                    self.inputs.insert(i-1, minus)
                    break

        
        return self.inputs


                