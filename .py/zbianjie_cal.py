from scipy import interpolate
import numpy as np

# 计算边界流量
def zbianjie_cal(L,R,Tur,A,H,U):
    q_lr = np.empty((A[1],2))
    q_lr[:]= np.NaN
    for i in range(A[1]):
        n11 = Tur[i,1]*Tur[i,0]/H**0.5
        if len(L[i]) >=2:
            q_lr(i,0) = interpolate.interp1d(L[0][:,0],L[0][:,1],kind='linear',fill_value='extrapolate',)(n11)

        else:
            q_lr[i,0] = 0

        if len(R[i]) >=2:
            q_lr(i,1) = interpolate.interp1d(R[0][:,0],R[0][:,1],kind='linear',fill_value='extrapolate',)(n11)

        else:
            q_lr[i,1] = 0

        if q_lr[i,0]*q_lr[i,1] == 0:
            q_lr[i,1] = max(q_lr[i,0],q_lr[i,1])
            q_lr[i,0] = q_lr[i,1]


    # 流量口径变换
    DR = Tur[:,0]
    ri = DR**2 * H**0.5 /1000
    RI = [ri,ri]
    Q_LR = q_lr
    Q_LR = np.multiply(q_lr,RI)

    qmax = np.divide(Tur[:,2],T[:7])/9.81/H # 最大功率对应流量
    Q_LR[:,2] = np.transpose(min(np.transpose([Q_LR[:2],qmax])))
    Q_LR = np.multiply(Q_LR,np.transpose([U,U]))

    return Q_LR




    
