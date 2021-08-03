from sZubObjFun, zbianjie_cal import zbianjie_cal,sZubObjFun
import numpy as np
#https://blog.csdn.net/u013527937/article/details/53140686
def zdynprog( x,zDecisFun,zSubObjFun,TransFun,ObjFun,L,R,Tur,A,H,U ):
    #  x状态变量，一列代表一个阶段状态
    #  DecisFun(k,x)决策变量
    #  SubObjFun(k,x,u)是阶段指标函数
    #  TransFun(k,x,u)是状态转移函数
    #  ObjFun(v,f)是第k阶段至最后阶段指标函数
    #  p_opt=[序号组；最优策略组；最优轨线组；指标函数值组]；
    #  fval是一个列向量，各元素分别表示p_opt各最优策略组对应始端状态x的最优函数值

    q_lr = zbianjie_cal(L,R,Tur,A,H,U) # 边界流量
    M,N = x.shape
    k=N-1
    t_vubm = -np.inf*np.ones([M,k])#最优阶段指标
    f_opt = -np.inf*np.ones([M,k]) #累积指标
    d_opt = -inf*ones(M,k) # 最优决策变量
    eta_opt = np.nan * np.ones([M,k]) # 水轮机效率
    
    #从最后一段开始计算，由后向前逐步推移至开始阶段：
    # 最后阶段
    tmp1 = x[:,k-1][~np.isnan(x[:,k-1])] 
    tmp2 = len(tmp1)
    for i in range(tmp2):
        u = zDecisFun(k,i,x)
        tmp, eta = sZubObjFun(k,q_lr,u,Tur,H,L,R)
        f_opt[i,k-1] = tmp
        d_opt[i,k-1] = U
        t_vubm[i,k-1] = tmp
        eta_opt[i,k-1] = eta

    # 最后第二阶段 至 开始阶段
    for ii in range(k-2,0,-1):
        tmp20 = len(x[:,ii][~np.isnan(x[:,ii])])
        for i in range(tmp20):
            u = zDecisFun(k,i,x)
            tmp0, eta = sZubObjFun(k,q_lr,u,Tur,H,L,R) # 效益计算
            tmp00 = ObjFun(tmp0,f_opt[:,ii+1])
            maxv= max(tmp00)
            index = np.argmax(tmp00)
            f_opt[i,ii] = maxv
            d_opt[i,ii] = u[index]
            t_vubm[i,ii] = tmp0[index]
            eta_opt[i,ii] = eta[index]
    

    # 求解方向： 与上述行进方向是相反
    tmpx = np.nan*np.ones(k)
    tmpd = np.nan*np.ones(k)
    tmpf = np.nan*np.ones(k)
    tmpe = np.nan*np.ones(k)
    p_opt = np.nan*np.ones([5,k])
    #开始阶段
    Emax = max(f_opt[:,0])
    index = np.argmax(f_opt[:,0])
    p_opt[0,0] = Emax
    p_opt[1,0] = x[index,0]
    p_opt[2,0] = d_opt[index,0]
    p_opt[3,0] = t_vubm[index,0]
    p_opt[4,0] = eta_opt[index,0]

    tmpd[0] = d_opt[index,0]
    tmpx[0] = x[index,0]
    tmpf[0] = t_vubm[index,0]
    tmpe[0] = eta_opt[index,0]

    # 第二阶段至最后阶段
    for ii in range(1,k):
        tmpx[ii] = TransFun(ii,tmpx[ii-1],tmpd[ii-1])
        tmp1 = np.absolute(x[:,ii]-tmpx[ii])
        tmp2 = np.argmin(tmp1)
        tmpd[ii] = d_opt[tmp2,ii]

        tmp[ii]=t_vubm[tmp2,ii]
        tmpe[ii]=eta_opt[tmp2,ii]
        p_opt[0,ii]=f_opt[tmp2,ii]
        p_opt[1,ii]=tmpx[ii]
        p_opt[2,ii]=tmpd[ii]
        p_opt[3,ii]=tmpf[ii]
        p_opt[4,ii]=tmpe[ii]


    return p_opt






            










