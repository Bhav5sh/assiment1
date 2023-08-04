l1=[]
l2=[]
sizelist=int(input('please mentaion the size of list:'))
for i in range(sizelist):
    l1.append(int(input('enter number for l1: ')))
    l1.append(input('enter names for l1: '))
    l2.append(int(input('enter number for l2: ')))
    l2.append(input('enter names for l2: '))


d={'number':'names'}

for i in range(sizelist):
        d['number']=l1[i]
        d['names']=l1[i+1]
        d['number']=l2[i]
        d['names']=l2[i+1]
    
        

print(d)