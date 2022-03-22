from data_cleaning import seperator

   
# bracket, off, division, multiplication, (addition, subtraction) same level

class Calculate:
    def __init__(self):
        self.inputs = seperator()
        
    def calculation(self):
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


                