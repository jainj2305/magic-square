def magic_square(n):
    square=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        square.append(l)
    i=n//2
    j=n-1
    num=n*n
    count=1
    
    while(count<=num):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(square[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            square[i][j]=count
            count+=1
        i=i-1
        j=j+1
        
    for i in range(n):
        for j in range(n):
            print(square[i][j],end=" ")
        print()

def run():
    while True:
        x=int(input("Enter any number: "))
        if(x%2==0):
            print("Unable to create magic square for even numbers!!\nPlease enter a odd number:")
        else:
            magic_square(x)
            break


if __name__ == '__main__' :
    run()
