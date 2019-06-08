def solution(A):
    # write your code in Python 3.6
    if len(A)<3: return(0)
    B=A[:]
    B.sort()
    C=[]
    i=0
    while i<len(B)-1:
        C.append(B[i+1]-B[i])
        i+=1
    j=0
    while j<len(B)-2:
        if B[j]>C[j+1]:
            #print(j)
            return(1)
        j+=1
    return(0)
    pass
