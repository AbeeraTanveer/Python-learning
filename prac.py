#variable declaration
num1 : int
num2 : int
num3: int
name : str 

# taking input from user
name = input("Enter your name: ")
num1 = int(input("Enter your first favourite number : "))
num2 = int(input("Enter your second favourite number : "))
num3 = int(input("Enter your third favourite number : "))

print(f"Hello , {name} ! Let's explore your first favourite number: ")

# making the list of user's favourite numbers
favNum =  [num1,num2,num3]
tuple_list : list= []

# check if the number is even or odd
for i in favNum:
    if(i%2 == 0):
       print(f"The number {i} is even.")
       tuple = (i,'even')
    elif (i%2 !=0):
        print(f"The number {i} is odd.")
        tuple = (i,'odd')
        tuple_list.append(tuple)

#finding the square
for i in favNum:
    print(f"The number {i} and it's square is : ({i} , {i**2}")
    totalSum = sum(favNum)
    print(f"The sum of your favourite number is :{totalSum}")

#checking if the total sum is prime or not
is_prime =  True
if totalSum > 1:
  for j in range(2, int(totalSum**0.5)+1):
     if totalSum % j == 0:
        is_prime = False
else:
   is_prime = False
if is_prime:
    print(f"WOW , {totalSum} is a prime number!")
else:
    print(f"WOW , {totalSum} is not a prime number!")