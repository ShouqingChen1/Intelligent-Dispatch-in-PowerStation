import numpy as np

def out_find(L,R,Tur,HX,QX,net_box,k):

    DR = Tur[k,0] #水泵真机直径
    NR = Tur[k,2]#水泵真机额定转速
    S = Tur[k,5]
    hsun =0.5 # S*QX**2
    HX = HX-hsun

    #转化为模型工况点
    n11=NR*DR/HX**0.5
    q11=1000*QX/DR**2/HX**0.5

    if q11 <= 0:
        n11 = []
        q11 = []


    if len(q11) == 0:
        out=np.zeros(1)
        qout=np.zeros(1)
        hout=np.zeros(1)
        fout=np.zeros(1)

        return out,qout,hout,fout

    eta = 0.8
    p=9.81*QX*HX*eta*Tur(k,5)
    out=p
    qout=QX
    hout=HX
    fout=eta
    return out,qout,hout,fout

