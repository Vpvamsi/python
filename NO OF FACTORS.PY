    i=1
    count=0
    a=[]
    while(i<=n):
        if (n%i==0):
            count+=1
            a.append(i)
        i+=1
    print("Number of factors:",count)
    print("1*",o,"factor is:",a[0:o])
a=int(input("Enter number:"))
o=int(input("Enter N:"))
factor(a,o)

OUT PUT>>>>>>
Enter number:90
Enter N:8
('Number of factors:', 12)
('1*', 8, 'factor is:', [1, 2, 3, 5, 6, 9, 10, 15])
