import pandas as pd
# 机组运行工况须在模型曲线范围内
def get_para_fcn(A,Tur):
    L = []
    R = []
    xls = pd.ExcelFile(r"zz680.xlsx")
    left = xls.parse(2)[['N11', 'Q11',]]
    right= xls.parse(3)[['N11', 'Q11',]]
    L.append(left)
    R.append(right)
        
    L.append(left)
    R.append(right)

    xls_1=xlsread('ZDK400_5.xls')
    left = xls.parse(2)[['N11', 'Q11',]]
    right= xls.parse(3)[['N11', 'Q11',]]
    L.append(left)
    R.append(right)
    return L, R 







