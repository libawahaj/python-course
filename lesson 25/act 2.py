#zip function

s1 = {2, 3,1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1,s2))
print(s3)

#reverse elements

list1 = [1,2,3,4]
list2 = [10,20,30,40]

for x,y in zip(list1,list2[::-1]):
    print (x,y)
