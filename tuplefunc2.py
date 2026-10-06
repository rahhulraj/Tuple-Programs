#1. Given a tuple containing student names and marks as nested tuples, find the student who scored the highest mark.
students=(("Rahul Raj",100),("Neymar",90),("Messi",82))
highest=students[0]
for student in students:
    if student[1]>highest[1]:
        highest=student

print("Student:",highest[0])
print("Mark:",highest[1])

#2. Given a tuple of employee details (name, department, salary), find the employee with the highest salary.
employees=(("Rahul Raj", "IT",25000),("ABCD","HR",30000),("QWERT","Sales",28000))
highest=employees[0]
for employee in employees:
    if employee[2] > highest[2]:
        highest = employee
print("Name:", highest[0])
print("Department:", highest[1])
print("Salary:", highest[2])


#3. Given a nested tuple containing product names and prices, calculate the total price of all products.
products=(("Pen", 10),("Book", 50),("Bag", 500))
total=0
for product in products:
    total=total+product[1]
print("TOTAL PRICE =", total)

#4. Given a tuple containing repeated elements, create a new tuple containing only the unique elements without using a set.
numbers=(10,20,10,30,20,40,30)
unique=()
for n in numbers:
    if n not in unique:
        unique=unique + (n,)
print(unique)

#5. Given two tuples, find the common elements between them and store the result in a new tuple
t1=(10,20,30,40)
t2=(30, 40, 50, 60)
common=()
for n in t1:
    if n in t2:
        common = common + (n,)
print(common)