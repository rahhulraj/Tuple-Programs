#1. Create a tuple of five numbers and print the first and last elements.
num=(10,20,30,40,50)
print(num)
print("first element",num[0])
print("last element",num[4])

#2. Create a tuple of student names and access the third student.
students=("Rahul Raj","Messi","Neymar","Ronaldo","Yamal")
print(students)
print("3rd STUDENT IS",students[2])

#3. Given a tuple of numbers, find the number of elements using len().
numbers=(10,20,30,40,50)
print(numbers)
print("LENGTH IS",len(numbers))

#4. Create a tuple containing repeated numbers and count how many times a given number occurs using a variable.
numbers=(10,20,10,30,10,40)
print(numbers)
n=10
count=numbers.count(n)
print(count)

#5. Given a tuple of numbers, find the index of a given number stored in a variable.
num1=(10,20,30,40,50)
print(num1)
n=30
index=num1.index(n)
print(index)

#6.Create a tuple of fruits and check whether a particular fruit exists in the tuple.
fruits=("apple","banana","orange","mango")
fruit="mango"
if fruit in fruits:
    print("YES IT EXIST")
else:
    print("NOT IT EXIST")

#7. Given a tuple of marks, count how many students scored a particular mark stored in a variable.
marks=(50, 75, 80, 50, 90, 50, 65)
mark=50
count=marks.count(mark)
print(count)

#8. Create two tuples and concatenate them into a single tuple.
tuple1=(10,20,30)
tuple2=(40,50,60)
tuple3=tuple1+tuple2
print(tuple3)

#9. Given a tuple of numbers, find the maximum and minimum values.
num2=(10,50,20,80,30)
maximum=max(num2)
minimum=min(num2)
print("MAXIMUM =",maximum)
print("MINIMUM =",minimum)

#10. Create a tuple containing different data types and print each element using indexing.
data = ("Rahul Raj",22,172.5,True)
print(data)
print(data[0])
print(data[1])
print(data[2])
print(data[3])
