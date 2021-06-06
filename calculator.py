import tkinter as tk
import tkinter.font as tkFont
import math


class Calculator:
    def __init__(self):
        #UI elements
        self.formulaLbl = None
        self.resultLbl = None
        self.sinBtn = None
        self.cosBtn = None
        self.tanBtn = None
        self.backBtn = None
        self.leftParentheseBtn = None
        self.rightParentheseBtn = None
        self.clearBtn = None
        self.divideBtn = None
        self.sevenBtn = None
        self.eightBtn = None
        self.NineBtn = None
        self.minusBtn = None
        self.fourBtn = None
        self.fiveBtn = None
        self.sixBtn = None
        self.minusBtn = None
        self.oneBtn = None
        self.twoBtn = None
        self.threeBtn = None
        self.plusBtn = None
        self.negBtn = None
        self.zeroBtn = None
        self.pointBtn = None
        self.equalBtn = None

        #input list
        self.input = []

        
    def createUI(self):
        root = tk.Tk()
        root.title("Calculator_Shunting Yard Algorithm")
        #root.resizable(width=False, height=False)
        root.geometry('437x400+100+20')

        largeFont = tkFont.Font(family="Lucida Grande", size=18)

        self.formulaLbl = tk.Label(text="", bg='lavender', font=largeFont, anchor="w")
        self.formulaLbl.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipady=8, sticky="NESW")

        self.resultLbl = tk.Label(text="", bg='lavender', font=largeFont, anchor="w")
        self.resultLbl.grid(row=1, column=0, columnspan=4, padx=5, pady=0, ipady=8, sticky="NESW")

        emptyLbl = tk.Label(text="", width=60)
        emptyLbl.grid(row=2, column=0, columnspan=4, padx=5, pady=0)

        mediumPlusFont = tkFont.Font(family="Lucida Grande", size=12)
        mediumFont = tkFont.Font(family="Lucida Grande", size=10)
        smallFont = tkFont.Font(family="Lucida Grande", size=8)

        # sin cos tan back
        self.sinBtn = tk.Button(root, text="sin", font=mediumFont)
        self.sinBtn.grid(row=3, column=0, padx=5, pady=5, sticky="NESW")
        self.sinBtn.bind('<Button-1>', self.sinBtnHandler)

        self.cosBtn = tk.Button(root, text="cos", font=mediumFont)
        self.cosBtn.grid(row=3, column=1, padx=5, pady=5, sticky="NESW")
        self.cosBtn.bind('<Button-1>', self.cosBtnHandler)

        self.tanBtn = tk.Button(root, text="tan", font=mediumFont)
        self.tanBtn.grid(row=3, column=2, padx=5, pady=5, sticky="NESW")
        self.tanBtn.bind('<Button-1>', self.tanBtnHandler)

        self.backBtn = tk.Button(root, text="<<", font=mediumFont)
        self.backBtn.grid(row=3, column=3, padx=5, pady=5, sticky="NESW")
        self.backBtn.bind('<Button-1>', self.backBtnHandler)

        # parentheses clear divide
        self.leftParentheseBtn = tk.Button(root, text="(", font=mediumFont)
        self.leftParentheseBtn.grid(row=4, column=0, padx=5, pady=5, sticky="NESW")
        self.leftParentheseBtn.bind('<Button-1>', self.leftParentheseBtnHandler)

        self.rightParentheseBtn = tk.Button(root, text=")", font=mediumFont)
        self.rightParentheseBtn.grid(row=4, column=1, padx=5, pady=5, sticky="NESW")
        self.rightParentheseBtn.bind('<Button-1>', self.rightParentheseBtnHandler)

        self.clearBtn = tk.Button(root, text="CE", font=smallFont)
        self.clearBtn.grid(row=4, column=2, padx=5, pady=5, sticky="NESW")
        self.clearBtn.bind('<Button-1>', self.clearBtnHandler)

        self.divideBtn = tk.Button(root, text="÷", font=mediumPlusFont)
        self.divideBtn.grid(row=4, column=3, padx=5, pady=5, sticky="NESW")
        self.divideBtn.bind('<Button-1>', self.divideBtnHandler)

        # set up button on 7, 8, 9, and multiply
        self.sevenBtn = tk.Button(root, text="7", font=mediumFont)
        self.sevenBtn.grid(row=5, column=0, padx=5, pady=5, sticky="NESW")
        self.sevenBtn.bind('<Button-1>', self.sevenBtnHandler)

        self.eightBtn = tk.Button(root, text="8", font=mediumFont)
        self.eightBtn.grid(row=5, column=1, padx=5, pady=5, sticky="NESW")
        self.eightBtn.bind('<Button-1>', self.eightBtnHandler)
        
        self.nineBtn = tk.Button(root, text="9", font=mediumFont)
        self.nineBtn.grid(row=5, column=2, padx=5, pady=5, sticky="NESW")
        self.nineBtn.bind('<Button-1>', self.nineBtnHandler)

        self.multiplyBtn = tk.Button(root, text="×", font=mediumPlusFont)
        self.multiplyBtn.grid(row=5, column=3, padx=5, pady=5, sticky="NESW")
        self.multiplyBtn.bind('<Button-1>', self.multiplyBtnHandler)
        
        # set up button on 4, 5, 6 and minus
        self.fourBtn = tk.Button(root, text="4", font=mediumFont)
        self.fourBtn.grid(row=6, column=0, padx=5, pady=5, sticky="NESW")
        self.fourBtn.bind('<Button-1>', self.fourBtnHandler)

        self.fiveBtn = tk.Button(root, text="5", font=mediumFont)
        self.fiveBtn.grid(row=6, column=1, padx=5, pady=5, sticky="NESW")
        self.fiveBtn.bind('<Button-1>', self.fiveBtnHandler)


        self.sixBtn = tk.Button(root, text="6", font=mediumFont)
        self.sixBtn.grid(row=6, column=2, padx=5, pady=5, sticky="NESW")
        self.sixBtn.bind('<Button-1>', self.sixBtnHandler)

        self.minusBtn = tk.Button(root, text="-", font=mediumPlusFont)
        self.minusBtn.grid(row=6, column=3, padx=5, pady=5, sticky="NESW")
        self.minusBtn.bind('<Button-1>', self.minusBtnHandler)

        # set up button on 1, 2, 3, and plus
        self.oneBtn = tk.Button(root, text="1", font=mediumFont)
        self.oneBtn.grid(row=7, column=0, padx=5, pady=5, sticky="NESW")
        self.oneBtn.bind('<Button-1>', self.oneBtnHandler)

        self.twoBtn = tk.Button(root, text="2", font=mediumFont)
        self.twoBtn.grid(row=7, column=1, padx=5, pady=5, sticky="NESW")
        self.twoBtn.bind('<Button-1>', self.twoBtnHandler)

        self.threeBtn = tk.Button(root, text="3", font=mediumFont)
        self.threeBtn.grid(row=7, column=2, padx=5, pady=5, sticky="NESW")
        self.threeBtn.bind('<Button-1>', self.threeBtnHandler)

        self.plusBtn = tk.Button(root, text="+", font=mediumPlusFont)
        self.plusBtn.grid(row=7, column=3, padx=5, pady=5, sticky="NESW")
        self.plusBtn.bind('<Button-1>', self.plusBtnHandler)

        #set up button on neg, 0, point and equal
        self.negBtn = tk.Button(root, text="+/-", font=mediumFont)
        self.negBtn.grid(row=8, column=0, padx=5, pady=5, sticky="NESW")
        self.negBtn.bind('<Button-1>', self.negBtnHandler)

        self.zeroBtn = tk.Button(root, text="0", font=mediumFont)
        self.zeroBtn.grid(row=8, column=1, padx=5, pady=5, sticky="NESW")
        self.zeroBtn.bind('<Button-1>', self.zeroBtnHandler)

        self.pointBtn = tk.Button(root, text=".", font=mediumPlusFont)
        self.pointBtn.grid(row=8, column=2, padx=5, pady=5, sticky="NESW")
        self.pointBtn.bind('<Button-1>', self.pointBtnHandler)

        self.equalBtn = tk.Button(root, text="=", font=mediumPlusFont)
        self.equalBtn.grid(row=8, column=3, padx=5, pady=5, sticky="NESW")
        self.equalBtn.bind('<Button-1>', self.equalBtnHandler)
        
        tk.mainloop()

    def displayInput(self):
        text = ""
        for token in self.input:
            text += token["display"]
        self.formulaLbl.config(text=text)
        self.resultLbl.config(text="")

    def sinBtnHandler(self, event):
        self.input.append({
            "is_operator": True,
            "display": "sin",
            "operant_count": 1,
            "precedence": 4,
            "associativity": "",
            "is_function": True,
            "operator": self.dsin})
        self.displayInput()

    def dsin(self, op1):
        return math.sin(math.radians(op1))

    def cosBtnHandler(self, event):
        self.input.append({
            "is_operator": True,
            "display": "cos",
            "operant_count": 1,
            "precedence": 4,
            "associativity": "",
            "is_function": True,
            "operator": self.dcos})
        self.displayInput()

    def dcos(self, op1):
        return math.cos(math.radians(op1))

    def tanBtnHandler(self, event):
        self.input.append({
            "is_operator": True,
            "display": "tan",
            "operant_count": 1,
            "precedence": 4,
            "associativity": "",
            "is_function": True,
            "operator": self.dtan})
        self.displayInput()

    def dtan(self, op1):
        return math.tan(math.radians(op1))

    def backBtnHandler(self, event):
        if len(self.input) > 0:
            if self.input[-1]["is_operator"] or len(self.input[-1]["display"]) == 1:
                self.input.pop()
            else:
                self.input[-1]["display"] = self.input[-1]["display"][:-1]
                
            self.displayInput()

    def leftParentheseBtnHandler(self, event):
        self.input.append({
            "is_operator": True,
            "display": "(",
            "operant_count": 0,
            "precedence": 4,
            "associativity": "",
            "is_function": False,
            "operator": None})
        self.displayInput()

    def rightParentheseBtnHandler(self, event):
        self.input.append({
            "is_operator": True,
            "display": ")",
            "operant_count": 0,
            "precedence": 4,
            "associativity": "",
            "is_function": False,
            "operator": None})
        self.displayInput()

    def clearBtnHandler(self, event):
        if len(self.input) > 0:
            self.input.clear()
            self.displayInput()

    def divideBtnHandler(self, event):
        self.input.append({
            "is_operator": True,
            "display": "÷",
            "operant_count": 2,
            "precedence": 3,
            "associativity": "L",
            "is_function": False,
            "operator": self.divide})
        self.displayInput()

    def divide(self, op1, op2):
        return op1 / op2

    # define a dictionary on 7, 8 ,9 and *
    def sevenBtnHandler(self,event):
        if len(self.input) > 0 and not self.input[-1]["is_operator"]:
            self.input[-1]["display"] += "7"
        else:
            self.input.append({
                "is_operator": False,
                "display": "7",
                "operant_count": 0,
                "precedence": 0,
                "associativity": "",
                "is_function": False,
                "operator": None})
        self.displayInput()

    def eightBtnHandler(self,event):
        if len(self.input) > 0 and not self.input[-1]["is_operator"]:
            self.input[-1]["display"] += "8"
        else:
            self.input.append({
                "is_operator": False,
                "display": "8",
                "operant_count": 0,
                "precedence": 0,
                "associativity": "",
                "is_function": False,
                "operator": None})
        self.displayInput()
             
    def nineBtnHandler(self,event):
        if len(self.input) > 0 and not self.input[-1]["is_operator"]:
            self.input[-1]["display"] += "9"
        else:
            self.input.append({
                "is_operator": False,
                "display": "9",
                "operant_count": 0,
                "precedence": 0,
                "associativity": "",
                "is_function": False,
                "operator": None})
        self.displayInput()
         
    def multiplyBtnHandler(self,event):
         self.input.append({
             "is_operator": True,
             "display": "×",
             "operant_count": 2,
             "precedence": 3,
             "associativity": "L",
             "is_function": False,
             "operator": self.multiply})
         self.displayInput()
         
    def multiply(self, op1, op2):
        return op1 * op2

    # define a dictionary on 4, 5, 6 and -
    def fourBtnHandler(self,event):
        if len(self.input) > 0 and not self.input[-1]["is_operator"]:
            self.input[-1]["display"] += "4"
        else:
            self.input.append({
                "is_operator": False,
                "display": "4",
                "operant_count": 0,
                "precedence": 0,
                "associativity": "",
                "is_function": False,
                "operator": None})
        self.displayInput()

    def fiveBtnHandler(self,event):
        if len(self.input) > 0 and not self.input[-1]["is_operator"]:
            self.input[-1]["display"] += "5"
        else:
            self.input.append({
                "is_operator": False,
                "display": "5",
                "operant_count": 0,
                "precedence": 0,
                "associativity": "",
                "is_function": False,
                "operator": None})
        self.displayInput()
             
    def sixBtnHandler(self,event):
        if len(self.input) > 0 and not self.input[-1]["is_operator"]:
            self.input[-1]["display"] += "6"
        else:
            self.input.append({
                "is_operator": False,
                "display": "6",
                "operant_count": 0,
                "precedence": 0,
                "associativity": "",
                "is_function": False,
                "operator": None})
        self.displayInput()
         
    def minusBtnHandler(self,event):
         self.input.append({
             "is_operator": True,
             "display": "-",
             "operant_count": 2,
             "precedence": 2,
             "associativity": "L",
             "is_function": False,
             "operator": self.minus})
         self.displayInput()
         
    def minus(self, op1, op2):
        return op1 - op2

    def oneBtnHandler(self,event):
        if len(self.input) > 0 and not self.input[-1]["is_operator"]:
            self.input[len(self.input) - 1]["display"] += "1"
        else:
            self.input.append({
                "is_operator": False,
                "display": "1",
                "operant_count": 0,
                "precedence": 0,
                "associativity": "",
                "is_function": False,
                "operator": None})
        self.displayInput()

    def twoBtnHandler(self,event):
        if len(self.input) > 0 and not self.input[len(self.input) - 1]["is_operator"]:
            self.input[len(self.input) - 1]["display"] += "2"
        else:
            self.input.append({
                "is_operator": False,
                "display": "2",
                "operant_count": 0,
                "precedence": 0,
                "associativity": "",
                "is_function": False,
                "operator": None})
        self.displayInput()

    def threeBtnHandler(self,event):
        if len(self.input) > 0 and not self.input[len(self.input) - 1]["is_operator"]:
            self.input[len(self.input) - 1]["display"] += "3"
        else:
            self.input.append({
                "is_operator": False,
                "display": "3",
                "operant_count": 0,
                "precedence": 0,
                "associativity": "",
                "is_function": False,
                "operator": None})
        self.displayInput()

    def plusBtnHandler(self,event):
         self.input.append({
             "is_operator": True,
             "display": "+",
             "operant_count": 2,
             "precedence": 2,
             "associativity": "L",
             "is_function": False,
             "operator": self.plus})
         self.displayInput()
         
    def plus(self, op1, op2):
        return op1 + op2

    def negBtnHandler(self,event):
         self.input.append({
             "is_operator": True,
             "display": "-",
             "operant_count": 1,
             "precedence": 4,
             "associativity": "",
             "is_function": True,
             "operator": self.neg})
         self.displayInput()
         
    def neg(self, op1):
        return -op1

    def zeroBtnHandler(self,event):
        if len(self.input) > 0 and not self.input[-1]["is_operator"]:
            self.input[len(self.input) - 1]["display"] += "0"
        else:
            self.input.append({
                "is_operator": False,
                "display": "0",
                "operant_count": 0,
                "precedence": 0,
                "associativity": "",
                "is_function": False,
                "operator": None})
        self.displayInput()

    def pointBtnHandler(self,event):
        if len(self.input) > 0 and not self.input[-1]["is_operator"]:
            if "." in self.input[len(self.input) - 1]["display"]:
                return
            self.input[len(self.input) - 1]["display"] += "."
        else:
            self.input.append({
                "is_operator": False,
                "display": ".",
                "operant_count": 0,
                "precedence": 0,
                "associativity": "",
                "is_function": False,
                "operator": None})
        self.displayInput()

    def equalBtnHandler(self,event):
        postfix = self.infixToPostfix()
        if postfix != None:
            text = ""
            for token in postfix:
                text += token["display"]
            self.resultLbl.config(text=text)
        result = self.evaluatePostfix(postfix)
        self.resultLbl.config(text=result[0]["display"])

    # transfer infix expression to postfix expression by implementing shunting yard algorithm
    def infixToPostfix(self):
        postfix = []
        length = len(self.input)
        index = 0
        operatorStack = []
        token = None

        while index < length:
            token = self.input[index]
            if not token["is_operator"]:
                postfix.append(token)
            elif token["is_function"]:
                operatorStack.append(token)
            elif token["is_operator"] and token["display"] != "(" and token["display"] != ")":
                while len(operatorStack) > 0 and \
                        (operatorStack[-1]["precedence"] > token["precedence"] or \
                        (operatorStack[-1]["precedence"] == token["precedence"] and \
                        token["associativity"] == "L")) and \
                        operatorStack[-1]["display"] != "(":
                    postfix.append(operatorStack[-1])
                    operatorStack.pop()
                operatorStack.append(token)
            elif token["display"] == "(":
                operatorStack.append(token)
            elif token["display"] == ")":
                while len(operatorStack) > 0 and operatorStack[-1]["display"] != "(":
                    postfix.append(operatorStack[-1])
                    operatorStack.pop()
                if len(operatorStack) == 0 or operatorStack[-1]["display"] != "(":
                    self.resultLbl.config(text="parenthesis mismatch")
                    return None
                operatorStack.pop()
            index += 1

        while len(operatorStack) > 0:
            postfix.append(operatorStack[-1])
            operatorStack.pop()

        return postfix

    # do calculation on the postfix expression
    def evaluatePostfix(self, postfix):
        tmp = []
        index = 0

        while len(postfix) > 1:
            index = 0
            tmp = []
            while index < len(postfix):
                if not postfix[index]["is_operator"]:
                    if "value" not in postfix[index]:
                        postfix[index]["value"] = float(postfix[index]["display"])
                    index += 1
                    continue

                operantCount = postfix[index]["operant_count"]
                if index < operantCount:
                    self.resultLbl.config(text="invalid expression")
                    return None

                if index > operantCount:
                    tmp.extend(postfix[0:index-operantCount])

                func = postfix[index]["operator"]
                params = self.tokenListToFloatList(postfix[index-operantCount:index])
                result = func(*params)

                tmp.append({
                    "is_operator": False,
                    "display": str(result),
                    "value": result,
                    "operant_count": 0,
                    "precedence": 0,
                    "associativity": "",
                    "is_function": False,
                    "operator": None})

                if index < len(postfix) - 1:
                    tmp.extend(postfix[index+1:])

                postfix = tmp
                break
        return postfix

    def tokenListToFloatList(self, tokenList):
        floatList = []
        for token in tokenList:
            if "value" not in token:
                token["value"] = float(token["display"])
            floatList.append(token["value"])
        return floatList








