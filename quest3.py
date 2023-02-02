lst=[]
n=int(input('enter the number of element in list'))
for i in range(n):
    ele=int(input('enter the element:'))
    lst.append(ele)
n=int(input('enter the position'))
# import pdb;pdb.set_trace()
if n>len(lst):
    n=n-len(lst)
elif n==len(lst):
    print('enter position is equal to length of list ')
else:
     n
print('enter list is :',lst)
a=lst[len(lst)-n:len(lst)] + lst[0:len(lst)-n]
print(a)
# # Rly

# 1:27
# sum equal to element:-
# n=int(input('enter the number of element in list'))
# list=[]
# l1=[]
# for i in range(0,n):
#     ele=int(input('enter the element:'))
#     list.append(ele)
# print('enter list is :',list)
# k=int(input('enter the number '))
# if k  in list:
#     for i in range(0,len(list)):
#         for j in range(1,len(list)):
#             if list[i]+list[j]==k  :
#                 c=(list[i],list[j])
#                 l1.append(c)
#                 if (list[j],list[i]) in l1:
#                   l1.remove((list[j],list[i]))
#     print(l1)
# else:
#     print('enter number not in list')