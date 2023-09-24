A=[63 ,70, 80, 33, 33, 47 ,20]

l=[]
flag=0
i,j=0,0
while (i<=len(A)):
    if A[i]>=A[j]:
        flag=1
        j+=1
    else:
        flag=0
        i+=1
if flag:
    l.append(A[i])


# author-- Divyansh Raj Gupta    

