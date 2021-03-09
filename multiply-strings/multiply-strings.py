class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a , b = 0,0;
        num = {'0':0,
                    '1':1,
                    '2':2,
                    '3':3,
                    '4':4,
                    '5':5,
                    '6':6,
                    '7':7,
                    '8':8,
                    '9':9
                   }
        for i in num1:
            a = a*10 + num[i]
        for i in num2:
            b = b*10 + num[i]
            
        return (f'{a*b}')