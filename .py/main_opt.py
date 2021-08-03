import get_para_fcn
import energy

def main_opt(Q,hup,hdown,A,Tur,U,QH):
    H = hup - hdown
    QHT = [Q,H,1]
    A,net_box,Tur,L,R = get_para_fcn(A,Tur)
    out,qout,hout,fout = energy(QHT,net_box,L,R,Tur,A,U)

    return out,qout,hout,fout    
