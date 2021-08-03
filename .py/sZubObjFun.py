
import numpy as np
def zSubObjF(k,q_lr,u,Tur,H,L,R):
    S = Tur[k-1,5]
    price = 1 #惩罚因子
    pf = -10000000 # 惩罚因子
    
    qmin=q_lr[k-1,0] #k台机的最小提水流量
    qmax=q_lr[k-1,1] #k台机的最大提水流量
    n=len(u)
    qd=np.nan*np.ones(n)#k台机的提水流量
    qd[:]=0
    for index in range(n):
        if qmin <= u[index] < qmax:
            qd[index] = u[index]
        elif qmax <= u[index]:
            qd[index] = u[index]
    Hd=H*np.ones(n,1)
    hsun=0.5 #%S*qd.^2;
    HHB=Hd-hsun #净水头

    n11=Tur[k-1,1]*Tur[k,0]/HHB**0.5
    q11=1000*qd/HHB**0.5/Tur(k,1)**2

    etax = 0.8
    eta=etax+Tur[k-1,3]
    b=0.931
    if eta>b:
        eta = b


    etag=Tur[k-1,4]*np.ones(n) # 发电机效率
    N=9.81*qd*HHB*eta*etag
    v=price*N+pf*np.absolute(u-qd)

    return v,eta