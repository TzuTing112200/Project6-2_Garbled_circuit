import random
import json

def circuit():
    # 讀電路檔案
    infile = open('circuit.json', 'r')
    r = infile.readline()
    infile.close()
    dic = json.loads(r)
    C_in = dic['input']
    C_mid = dic['mid']
    C_out = dic['output']
    return C_in, C_mid, C_out

def getValue(Coz):
    re = int(Coz[-1])
    if re % 2:
        re = int(Coz[1])%2
    else:
        re = int(Coz[0])%2
    return re

def decide(index, a, b):
    for j in index:
        if j == 0:
            if a == 0 and b == 0:
                return 1
        if j == 1:
            if a == 0 and b == 1:
                return 1
        if j == 2:
            if a == 1 and b == 0:
                return 1
        if j == 3:
            if a == 1 and b == 1:
                return 1
    return 0
    
def calculate(values):
    C_in, C_mid, C_out = circuit()

    # input數量
    size = len(values)
    # 輸入的值加上gate輸出的值
    values = values + ([0] * (len(C_in) + len(C_mid) + len(C_out)))
    
    # 完成 IN
    for i in range(len(C_in)):
        
        # 找出上面的值
        a = getValue(values[C_in[i][1][0]])
            
        # 找出下面的值
        b = getValue(values[C_in[i][1][1]])

        # 算出輸出值
        temp = decide(C_in[i][2], a, b)

        # 放回去values
        values[size + C_in[i][0]] = enc(str(temp) + str(random.randint(0,1)), '10')
    
    # 完成 MID
    for i in range(len(C_mid)):
        
        # 找出上面的值
        a = getValue(values[C_mid[i][1][0]])
            
        # 找出下面的值
        b = getValue(values[C_mid[i][1][1]])

        # 算出輸出值
        temp = decide(C_mid[i][2], a, b)

        # 放回去values
        values[size + C_mid[i][0]] = enc(str(random.randint(0,1)) + str(temp), '01')
