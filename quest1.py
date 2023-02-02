# lst=[1,2,3,4,5,6,7,8,9,10]
# # #o/p=c
# ls1=[]


# # if k<=len(lst):
    
# for i in lst:
#     for p in lst:
#         if i+p==10:
#             # import pdb;pdb.set_trace()
#             z=tuple((i,p))
#         ls1.append(z)            
# print(ls1)        
        



# ls2=[]
# for i in range(0,len(ls)):
   
#     x=ls[0]
#     ls1=[]
#     if x+i==10:
#         z=tuple((x,i))
#         ls1.append(z)
#         ls=ls.remove(x)
     
   
        

# print(ls1)        

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

# from captcha.image import ImageCaptcha

# image =ImageCaptcha()
# data=image.generate('abcd')
# image.write('abcd','1.png')

# 
# ls=[5,10,5,20,10,5]
# c=0
# for i in ls:
#     if i == 5:
#         c+=i
#     elif (i-c)+5 == 0:


# ls=["abc","123","xyz"]
# st=""
# for i,k in enumerate(ls):
#     import pdb;pdb.set_trace()
    
#     for x in k:
#         st+=x[i]

# print(st)        
    

# x=int(input("enter no one "))
# y=int(input("enter no two "))

# t=y-x
# v=t//10
# print(v)
  #        0 1 2 3 4 5 
# test_list=[2,3,2,1,5,6]
# # out =4
# n=len(test_list)
# count =0
# res = {}
# res1={}   
# for idx in range(0, len(test_list)):
#     x=idx
#     count =0
#     for k in range((idx+1), len(test_list)):
#         if test_list[idx] <= test_list[k]:
#             count+=1
#             if  test_list[idx] not in res:
#                 res[test_list[x]]=count
#             else:
#                 if test_list[idx]  in res:
#                     res[test_list[x]]=count
#             idx=k         
#         else:
#             break  
# # print(res)  
# dict3={}   
# dict={}
# for idx in range(len(test_list)-1,0,-1):
#     count=0
#     x=idx
#     for k in range(len(test_list)-1, 0, -1):
#         k=idx-1
#         if test_list[idx] <= test_list[k]:
#             count+=1
#             if  test_list[idx] not in res1:
#                 res1[test_list[x]]=count
#             else:
#                 if test_list[idx]  in res1:
#                     res1[test_list[x]]=count
#             idx=k         
#         else:
#             break
# dict={}
# dict['val']=res,res1 
# print(dict)        



#sort dict according key
# dict= {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# dic={}
# myKeys = list(dict.keys())
# import pdb;pdb.set_trace()
# # myKeys.sort()
# for i in range(len(myKeys)-1):
#     for j in range(i+1,len(myKeys)):
#         if myKeys[i]> myKeys[j]:
#             temp = myKeys[i]
#             myKeys[i] = myKeys[j]
#             myKeys[j] = temp
# for i in myKeys:
#     dic[i]=dict[i]
# print(dic)

# u = ["B", "D", "A", "E", "C"]
# y=[]
# count=65
# while len(y)<len(u):
#     import pdb;pdb.set_trace()
#     for i in u:
#         if ord(i)==count:
#             y.append(i)
#             count+=1
# print(y)
        
# example of python json dumps and loads
# import json  
# x = """{
#     "Name": "Jennifer Smith",
#     "Contact Number": 7867567898,
#     "Email": "jen123@gmail.com",
#     "Hobbies":["Reading", "Sketching", "Horse Riding"]
#     }"""
# y = json.loads(x)
# print(y)

# Dictionary ={(1, 2, 3):'Welcome', 2:'to',
#             3:'Geeks', 4:'for',
#             5:'Geeks', 6:float('nan')}
# json_string = json.dumps(Dictionary,skipkeys = True,allow_nan = True)
# print(json_string)

# dict ={'a': 100, 'b':200, 'c':300}

# for k, v in dict.items():
#     v=v+v
# print(v)
#------------------------------------------------------
# ls = ["abc", "123", "xyz"]
# ls=["abc", "1"]
ls=["abcd", "12", "x"]
# ls=["ab", "1234"]
# output=  "a1xb2yc3z"
# "a1b c "
# "a1xb2 c  d  "
# "a1b2 3 4"

# ln=len(ls)
# print(ln)
# str=""
# for i in ls:
#     if i=='':
#         str+=' '
#         # ls.append(i[1:])
#     for k in i[:1]:
#         # import pdb;pdb.set_trace()
#         str+=k
#         ls.append(i[1:])
#         # break
# print(str)        
#----------------------------------------------------------
# from collections import Counter
# inpt = "tna magenta magnate tan gnamate"
# inp= inpt.split(" ")  
# for i in range(0, len(inp)):
#   # import pdb;pdb.set_trace()
#   inp[i]=''.join(sorted(inp[i]))
# print(inp)
# x=Counter(inp)

# print(max(x.values()))
# ........................................................
# n= [19, 15, 15, 5, 3, 3, 5, 2]

# for i in n :
#   x = n.count(i)
#   # if i == 19    and x == 2 or i == 5 and x == 3:
#   if n.count(i)>=2:
#     print("true", i) 
#   # print("false")  
# .......................................................
# n = [19, 15, 5, 7, 5, 5, 2]
# # ln = len(n)
# for i in range(len(n)):
#   x= n.count(i)
#   if n[i]==5 or  x == 3 and len(n) == 8:
#     print("true")

# .........................................................
# n = 922

# x = n % 34
# y = pow(4, 4)
# if y<=n and x == 4:
#   print("true")
# else:
#   print('False')
# .........................................................
# no = 17
# x = no//2
# l =[]
# # import pdb;pdb.set_trace()
# if no%2 == 0:
#   for i in range(0,2):
#     l.append(no)
#     b = no+2
#     no=b
# else:
#     for i in range(0,17):
#       l.append(no)
#       b = no+2
#       no=b
# print(l)
# ...............................................................
# from itertools import combinations 
# # ni  = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
# ni = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
# new=[]
# st=ni[-1]
# for p in combinations(st, 5):
#     new.append(''.join(p))
#     if ni[-2] in new:
#       print("True")

# # print(new)
# ...................................................................
strs = ['palindrome', 'nadamimadam', '', 'foo', 'eyes']
'''
i[::-1] minus value use for reverse data
'''
for i in strs:
  import pdb;pdb.set_trace()
  if i[::-1] == i:
    print("True")
  else:
    print("False")   

# ........................................................................
# import re
# ls=[]
# strs = "W3resource Python, Exercises asddds adsa sddaa"
# s = re.split(r"([ ,]+)", strs)
# ls.append([s[::2],s[1::2]])
# print(ls)
