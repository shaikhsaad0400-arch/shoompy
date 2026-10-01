# num1 = 100

# answer = num1 + 10.5

# print(answer)

# answer2 = int(110.5)

# print(answer2)



# print(type(num1))





#boolean function
# b1 = True
# print(b1)

# b2 = False

# b3 = num1 - b1
# print(b3)

# b4 = num1 - b2
# print(b4)






#typecasting
# res = bool(103)

# print(res)





#indexing
#s = "testing"

# print(s)

# print(s[0]) #t
# print(s[2]) #s
# #print(s[7]) #error
# print(s[0:5])  #t[start:stop]

# print(s[2:5])  #sti

# print(s[1:])  #till end

# print(s[1:5:1])  #esti

# print(s[1:5:2])  #et

# print(s[4:2:-1])   #for reversing

# print(s[-3])

# print(s[-3:-5:-1])



# #3 arguments of string 
# #start, stop, 




#string functions

# s = "testing"

# print(s.capitalize())   #Testing

# print(s.upper())   #TESTING

# print(s)   #testing

# print(dir(s))    #shows all string methods

#print(len(s))

# print(help(s.strip))  #helping function

# s = "   testing   "  






#list
# l1 = [10,20,30,40,50]

# l1[0] = 100  #value changing



# print(type(l1))

# print(l1[0])   #10
# print(l1[1])   #20
# print(l1[2])   #30

# print(l1[0:3])



#list are iterable



# print(dir(l1))

# print(help(l1.count))

# print(help(l1.count.append))

# l1.append([100,200,300])
# l1.extend([100,200,300])   #extend the list

# l1.extend("Testing")


# print(l1)


#l1 = [10,20,30,40]

#l2 = l1


# l2 = l1.copy()   #making the changes in the 2nd list


# print(l1)
# print(l2)

# l2[0] = 101

# print(l1)
# print(l2)



# a = 100
# b = 200

# print(f'value of b : {b}')     #f string

# msg = f'value of a : {a}'       #f string
# print(msg)



# NESTED LIST

# import copy

# l1 = [[10,20,30,40],[50,60,70],80,90]   # the proper copy is been made only for the outer element for nested list only shallow copy is made

# # l2 = l1.copy()   #shallow copy of the list 1 (reference ) the shallow copy only makes the copy of main list not the nested list

# l2 = copy.deepcopy(l1)    #this is opposite to shallow copy which is deep copy  

# l1[1][0] = 55   #does not create =s copy it jus pass the reference to the other list

# l1[2] = 800     #works because 80 is top element or outer element of nested list

# print(f"l1: {l1}")
# print(f"l2: {l2}")



# print(l1)

# print(l1[0][2])

# print(l1[1][0])

# make the example for shallow copy


# Tupple

# t1 = (10,20,30)


#t1[0] = 100      #will not work becoz tupple are immutable

# t1 = (11,12)

# print(t1)

# print(dir(t1))

#print(help(t1.count))  #  count is method of tupple

#print(t1.count(10))


# print(t1.index(10))


# creating a tuple

# a = 10,20

# print(a)

# print(type(a))


# t2 = (100)

# print(t2)

# print(type(t2))



# t2 = (100,)

# print(t2)

# print(type(t2))


# t1 = (100,200,300,400,500,600)

# # a,b,c = t1   # If there are 3 values then 3 variables are required

# a, *b, c, d = t1

# print(a)
# print(b)
# print(c)
# print(d)



# Dictionary is a key value pair

# d1 = {key: value}    #syntax

# d1 = {"name": "Shoom", "city": "Pune", "age": 22}    #key are immutable coz they are string



# d1["state"] = "Maharashtra"

# d1["name"] = "Shoom patil " 

# print(d1)

# print(d1["city"])

# print(d1["state"])

# print(d1["name"])


# print(d1.get("country"))   # Get function




# While Loop

# i = 1

# while i<=10:
#     print(f"value of : {i}")
#     if i == 5:
#         break

#     i = i + 1


# i = 0
# lst = [10,20,30,40,50]
# n = len(lst)

# while i < n:
#     print(lst[i])
#     i = i + 1






# dictionary

#d1 = {"name": "Shoom", "city": "Pune", "age": 22}

# result = d1.keys()


# print(result)

# # print(type(result))

# result2 = list(result)

# print(result2)

# print(type(result2))
 
# values = d1.values()
# print(values)
# print(type(values))

# lst = list(values)      #Typecasting
# print(lst)

# items = d1.items()
# print(items)

# items2 = list(items)    # Typecasting
# print(items2)

# print(items2[0])
# print(items2[1])

