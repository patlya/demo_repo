
ls=[1,2,3,4,5,6,7,8,9,10]
# import pdb;pdb.set_trace()
# k=3
k=1
# k=12
if k>len(ls):
    k=k-len(ls)
# elif k==len(ls):
#     print(ls)
else:
     pass
new_ls=ls[len(ls)-k:len(ls)] + ls[0:len(ls)-k]
print(new_ls)

# ls.append(ls.pop(0))
# print(ls)
# ls+=[ls.pop(2)]
# ls=[ls[len(ls)-k:len(ls)]] + ls[0:len(ls)-k]
# print(ls)    
    

# ls1=[]   
# for i in ls:
#     for j in range(i,k):
#         ls1.insert(j,i)

# #shifted forward (to right)
#     # ls.insert(0,ls.pop())
# print(ls) 



