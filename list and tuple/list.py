marks=91.4
marks2=87.4
list1=[marks,marks2]
print("lists of marks:",list1)


#tuple
marks1=list1[1:4]
print("this is slicing:",marks1)
#example
list=[2,1,3,4]
list.append(7)
print("this is appended one",list)
#ascend
list.sort()
print("ascending order:",list)
#descend
list.sort(reverse=True)
print("descending order:",list)
#reverse
list.reverse()
print("this is reversed list:",list)
#insert====list.insert(index,element)
list.insert(2,5)
print("this is inserted list:",list)
#remove
list.append(3)
list.remove(3)
print("this is removed list:",list)
