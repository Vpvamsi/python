 
test_list1 = [1,2,3,]
test_list2 = [2,3,5,6]
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))
res = sorted(test_list1 + test_list2)
print ("The combined sorted list is : " + str(res))

OUT PUT>>>>>
The original list 1 is : [1, 2, 3]
The original list 2 is : [2, 3, 5, 6]
The combined sorted list is : [1, 2, 2, 3, 3, 5, 6]
