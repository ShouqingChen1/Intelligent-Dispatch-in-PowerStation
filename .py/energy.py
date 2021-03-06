from out_find import out_find
import numpy as np
from zbianjie_cal ,zDecisFun,zdyprog,sZubObjFun, TransFun,ObjFun,out_find import zbianjie_cal,zDecisF,zdyprog，zSubObjF,TransF1,ObjF1,out_find


def energy(QHT,L,R,Tur,A,U):
    n = A[1]
    H = QHT[1]
    if H >= A[3] & H <= A[2]:
        Q = QHT[0]
        q_lr = zbianjie_cal(L,R,Tur,A,H,U) # 边界流量
        q_jizu_max = sum(q_lr[:2]) # 机组最大提水流量
        q_max = min(q_jizu_max,A(1))
        if min(q_max,Q) < min(q_lr[:,1]):
            out = np.nan*np.ones(A[1])
            qout =  np.nan*np.ones(A[1])
            hout =  np.nan*np.ones(A[1])
            fout =  np.nan*np.ones(A[1])
            return out,qout,hout,fout

        else:
            # 流量动态规划
            m = min(q_max,Q)
            step = 0.2
            x2 = np.arange(0,m,step)
            x2 = np.transpose(x2)
            hangshu = len(x2)
            rest_x = np.empty(hangshu-1)
            rest_x.fill(np.nan)
            x1 =[m]+list(rest_x)
            indr = x2
            xx =[list(x2) for i in range(n-1) ]
            xk1 =[0]+list(rest_x)
            x = np.transpose(np.array([x1]+xx+[xk1]))

            p_opt = zdyprog( x,zDecisF,zSubObjF,TransF1,ObjF1,L,R,Tur,A,H,U)

    else:
        out = np.nan*np.ones(A[1])
        qout =  np.nan*np.ones(A[1])
        hout =  np.nan*np.ones(A[1])
        fout =  np.nan*np.ones(A[1])
        return out,qout,hout,fout

    QX = p_opt[2,:]
    out = np.nan*np.ones(A[1])
    qout =  np.nan*np.ones(A[1])
    hout =  np.nan*np.ones(A[1])
    fout =  np.nan*np.ones(A[1])
    for k in range(A[1]):
        out[:,k],qout[:,k],hout[:,k],fout[:,k] = out_find(L,R,Tur,H,QX[k],k) # 转化到模型计算

    return out,qout,hout,fout

        

            



