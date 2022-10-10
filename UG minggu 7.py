class PrefixConverter: 
    def __init__(self): 
        self.stackList = ['?'] 
        
    # method untuk menambahkan data baru 
    def push(self,data): 
        self.stackList.append(data) 
        
    # method untuk melihat data paling atas 
    def peek(self): 
        if self.stackList: 
            return self.stackList[-1] 
        else: 
            return "Isi Stack Kosong" 
    
    # method untuk menghapus data palin atas 
    def pop(self): 
        if self.stackList: 
            data = self.stackList.pop(-1) 
            return data 
        else: 
            return "Isi Stack Kosong"

    def isEmpty(self):
        return self.stackList == []  

    def size(self):
        return len(self)

    def showList(self):
          return self.items
    # def cekValidExpression(self,expression): 
        # tuliskan code anda disini 
    
    def infixToPrefix(self,expression): 
        # Tuliskan code anda disini
        prec = {'*':3, '/':3 , '+':2, '-':2 , '(':1}
        opStack = PrefixConverter()
        prefixList = []
        tokenList = expression.split()
        tokenList.reverse()
        for i in range(len(tokenList)):
            if tokenList[i] == '(':
                tokenList[i]=')'
            elif tokenList[i] == ')':
                tokenList[i]='('
        for token in tokenList:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                prefixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                
                while topToken != '(':
                    prefixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                   (prec[opStack.peek()] >= prec[token]):
                    prefixList.append(opStack.pop())
                opStack.push(token)

        while not opStack.isEmpty():
            prefixList.append(opStack.pop())
        prefixList = prefixList[::-1]
        return " ".join(prefixList)



if __name__ == '__main__': 
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1")) 
    # print(expresi1.infixToPrefix("A * (B + C) / D")) 
    # print(expresi1.infixToPrefix("(1+2)*3")) 
    # print(expresi1.infixToPrefix("20 * 3 - 10 + 289")) 
    # print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))