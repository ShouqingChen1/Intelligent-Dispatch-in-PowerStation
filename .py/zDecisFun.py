
def zDecisFun(k,i,x):
    xs = x[~np.isnan(x[:,k]),k]
    u = x[i,k-1] - xs