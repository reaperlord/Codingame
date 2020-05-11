import numpy
import typing
import collections

class Cell:

    
    def __init__(self, operationStr:str, arg1:str, arg2:str, worksheet, unevalDeque:collections.deque):
        self.operationStr = operationStr    
        self.arg1Str = arg1
        self.arg2Str = arg2
        self.worksheet = worksheet
        self.unevalDeque = unevalDeque
        
        #assign prorper operation
        if self.operationStr == "VALUE":
            self.outerOperation = self._valueOperation
        else:
            self.outerOperation = self._nonValueOperation

        #try operation evaluation
        self.outerOperation()
    
        
    def evaluateArgString(self, argStr:str) -> typing.Optional[int]:
        if "$" in argStr:
            referencedCell = self.worksheet[int(argStr[1:])]
            if referencedCell != None and referencedCell.value != None:
                return referencedCell.value
            else: return None
        else:
            return int(argStr)

    #operation dictionary
    _opDict = {
        "ADD" : lambda a, b : a + b, 
        "SUB" : lambda a, b : a - b,
        "MULT" : lambda a, b : a * b, 
        }

    def _valueOperation(self):
        self.arg1 = self.evaluateArgString(self.arg1Str)
        if self.arg1 != None: #if arg1 string can already be evaluated
            self.value = self.arg1
        else:
            self.value = None
            self.unevalDeque.append(self)

    def _nonValueOperation(self):
        self.arg1 = self.evaluateArgString(self.arg1Str) #first try to evaluate both args
        self.arg2 = self.evaluateArgString(self.arg2Str)
        if self.arg1 != None and self.arg2 != None:
            self.value = self._opDict[self.operationStr](self.arg1, self.arg2) #evaluate operation
        else:
            self.value = None
            self.unevalDeque.append(self)

    def outerOperation(self): pass #to be overwritten per instance


n = int(input())

worksheet = numpy.full(n, None, Cell)
unevalDeque = collections.deque()

for i in range(n):
    operation, arg_1, arg_2 = input().split()
    worksheet[i] = Cell(operation, arg_1, arg_2, worksheet, unevalDeque)

while unevalDeque: # while there are still elements in unevalDeque
    unevalDeque.popleft().outerOperation() #gets next uneval and tries to use operation

#all elements are evald, therefore print the worksheet
for cell in worksheet:
    print(cell.value)
