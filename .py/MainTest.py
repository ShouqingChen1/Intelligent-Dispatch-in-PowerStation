import numpy as np
from numpy.lib.function_base import quantile
from scipy import interpolate
from main_opt import main_opt


# 电站基本参数
A = np.nan*np.ones(5)
A[0]=504 #最大过水流量
A[1]=3 #装机台数
A[2]=9.51 #最大水头
A[3]=3.35 #最小水头
A[4]=0.5 #水头损失

# 机组基本参数
Tur = np.nan*np.ones([int(A[1]),8])
Tur[0,0]=2.0;#直径
Tur[0,1]=214.3;#额定转速
Tur[0,2]=1100;#最大功率
Tur[0,3]=0.01;#水轮机效率修正
Tur[0,4]=0.95;#发电机效率
Tur[0,5]=1.2500e-06;#管道阻力系数S
Tur[0,6]=250;#最小出力
Tur[0,7]=0.8;#效率

Tur[1,:] = Tur[0,:]

Tur[2,0]=2.0;#直径
Tur[2,1]=214.3;#额定转速
Tur[2,2]=1100;#最大功率
Tur[2,3]=0.01;#水轮机效率修正
Tur[2,4]=0.95;#发电机效率
Tur[2,5]=1.2500e-06;#管道阻力系数S
Tur[2,6]=250;#最小出力
Tur[2,7]=0.85;#效率

U = [1,1,1] 
hup = 186 # 最大水头

# 水位流量关系
xls = pd.ExcelFile(r"D:\Documents\Projects\Water-Energy-Calculation\水文.xlsx")
QH =  xls.parse(5)[['流量', '水位',]]

# 流量保证率
QT = xls.parse(2)[['Q', 't',]]


MM = len(QT[:,1])
# 功率、流量、净水头、效率
out = np.nan*np.ones([MM,A[1]])
qout = np.nan*np.ones([MM,A[1]])
hout = np.nan*np.ones([MM,A[1]])
fout =  np.nan*np.ones([MM,A[1]])

for i in range(MM):
    print(i)
    Q = QT[i,1]
    T = QT[i,2]
    if 1%T != 0:
        hdown = interpolate.interp1d(QH[:0],QH[:1],kind='linear',fill_value='extrapolate',)(Q) # https://www.codenong.com/8215419/
        out[i,:],qout[i,:],hout[i,:],fout[i,:] = main_opt( Q,hup,hdown,A,Tur,U,QH)


P = np.nansum(out,1) # 功率
e=P*QT[:,1] # 发电能量
E = np.nansum(e)
HQUAN=np.nansum(np.nansum(out*hout,1)*QT[:,1])/E # 加权水头
FQUAN=np.nansum(np.nansum(out*fout,1)*QT[:,1])/E # 加权出力
maxp = max(P) # 最大功率

