def S(seq, i=0):
    if i == len(seq): return 0
    return S(seq, i+1) + seq[i]

seq = range(1,1001)
S(seq)