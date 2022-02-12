A=[[1,1,1,1,1],[2,4,-3,2,8],[-1,-1,0,-3,5],[1,-1,4,9,7],[5,7,0,7,2]]

def fx(A):

    coefs = []


    for p in range(len(A)-1):
        damned=[]

        x = A[p][p]     #this is the coeficient of the diagonal, the one we have to compare every line with

        for i in range(len(A)): #no [p] because it's a square matrix !!!!!!!change it if its not a square matrix!!!!!!!!!!!!!!

            if i in range(0,p+1): #we only take the coeficient of the new line (we pass the already done ones)
                pass
            else:
                c=A[i][p]/x     #this is the coeficient of how many times i have to substract the 'pivot' line to the new line
                damned.append(c)  #store this value


                for j in range(len(A[i])):
                    A[i][j]-=c*A[p][j]      #compute every new coefficient and replace it

        coefs.append(damned)
    return A,coefs

A,coefs=fx(A)

print("Your new matrices are: \n U=",A,"\n and the lower triangular matrix: \n L=",coefs)