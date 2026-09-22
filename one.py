# [1] find the largest number in the list
"""
num = [3, 7, 2, 9, 4]
largest = num[0]
for numbers in num:
    if numbers > largest:
        largest = numbers
print(largest)
"""
#[2] find how many even numbers are in the list.
"""numbers = [3, 8, 5, 12, 7, 10, 4]
event_count = sum(1 for even in numbers if even % 2 == 0)
print(event_count)
"""
# or 
"""
numbers = [3, 8, 5, 12, 7, 10, 4]
event_count = 0
for even in numbers:
  if even % 2 == 0:
    event_count = event_count + 1
print(event_count)
"""
#[3] Find the smallest number.
"""
numbers = [12, 5, 8, 2, 15, 7]
small = numbers[0]
for smaller in numbers:
  if smaller < small:
    small = smaller
print(small)
"""
#[4] calculate the sum of all positive num
"""numbers = [-3, 5, -2, 8, 0, 4, -1]
result = 0
for positive in numbers:
  if positive > 0:
    result = result + positive
print(result)
"""
#[5] calculate the average of all the numbers.
#Then count how many numbers are greater than the average.
"""numbers = [2, 4, 6, 8, 10]
total = 0
ave_count  = 0
large_count = 0
for ave in numbers:
  total += ave
  ave_count +=1
average = total / ave_count
for greater in numbers:
  if greater > average:
    large_count = large_count + 1
print(large_count)"""

#[6] Find the second largest number.
"""numbers = [10, 5, 8, 20, 15, 3]
first_larger = numbers[0]
second_larger = numbers[0]
for largest in numbers:
  if largest > first_larger:
    second_larger = first_larger
    first_larger = largest
  elif largest > second_larger and largest != first_larger:
        second_larger = largest
print(second_larger)"""

#[7] Find the first number that appears more than once.
"""numbers = [4, 7, 2, 9, 7, 5]
seen = []
for number in numbers:
  if number in seen:
    print(number)
  else:
    seen.append(number)"""

#[8] You are given numbers from 1 to 10, but one number is missing:
"""numbers = [1, 2, 4, 5, 6, 7, 8, 9, 10]
addition_list = 0
total_addition =  sum(range(1,11))
for num in numbers:
  addition_list += num
total_result = total_addition - addition_list
print(total_result)"""

#[9] Find two numbers whose sum is equal to target.
"""numbers = [2, 7, 11, 15]
target = 9
for i in range(len(numbers)):
  for j in range(i+1,len(numbers)):
    if numbers[i] + numbers[j] == target :
      print(numbers[i] , numbers[j])"""

#[10] Find how many times target appears in the list.
"""numbers = [2, 5, 2, 8, 2, 7, 5]
target = 2
count = 0
for i in numbers:
  if i == target:
    count +=1
print(count)"""

#[11] Find the difference between the largest and smallest numbers.
"""numbers = [3, 10, 6, 2, 15, 8]
smallest = numbers[0]
largest = numbers[0]
for num in numbers:
  if num > largest:
    largest = num
  elif num < smallest:
    smallest = num
total = largest - smallest
print(total)"""

#[12] Find the second smallest number.
"""numbers = [8, 3, 10, 5, 1, 7]
first_smallest = numbers[0]
second_smallest = numbers[0]
for small in numbers:
  if small < first_smallest:
    second_smallest = first_smallest
    first_smallest = small
  elif small < second_smallest and small != first_smallest:
    second_smallest = small
print(second_smallest)"""

#[13] Find the largest number that appears only once.
"""numbers = [4, 7, 2, 7, 9, 2, 5]
largest = numbers[0]
for num in numbers:
    count = 0
    for other in numbers:
        if num == other:
            count += 1
    if count == 1 and num > largest:
        largest = num
print(largest)"""

#[14] Find the first number that appears exactly once.
"""numbers = [3, 5, 3, 7, 8, 5, 9]
for num in numbers:
    count = 0
    for first in numbers:
        if num == first:
            count += 1
    if count == 1:
        once = num
        break

print(once)"""

#[15] first pair of different numbers whose sum is equal to target
"""numbers = [4, 7, 2, 9, 5, 1]
target = 10
found = False
for i in range(len(numbers)):
  for j in range(i + 1 ,len(numbers)):
    if numbers[i] + numbers[j] == target:
      print(numbers[i] , numbers[j])
      found = True
      break
  if found:
     break"""

# [15] Find all numbers that appear more than once, but print each repeated number only once.
"""numbers = [2, 2, 2, 4]
seen = []
for i in range(len(numbers)):
  for j in range(i+1,len(numbers)):
      if numbers[i] == numbers[j] and numbers[i] not in seen:
        print(numbers[i])
        seen.append(numbers[i])
        break"""

# [16] Move all 0s to the end while keeping the order of the other numbers.
"""numbers = [0, 5, 0, 3, 8, 0, 2]

result = []

for i in range(len(numbers)):
    if numbers[i] != 0:
        result.append(numbers[i])

for i in range(len(numbers) - len(result)):
    result.append(0)

print(result)"""

#[17] Find the length of the longest consecutive increasing run.
"""numbers = [2, 4, 6, 3, 5, 7, 8, 2, 10]

current = 1
longest = 1

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        current += 1
    else:
        current = 1

    if current > longest:
        longest = current

print(longest)"""

#[18] This is inspired by 2020 Ethiopian Collegiate Programming Contest Problem D — Good Arrays
"""s = "abca"
count = 0
for i in range(len(s)):
    seen = set()
    for j in range(i, len(s)):
        if s[j] in seen:
            break
        seen.add(s[j])
        count += 1
print(count)"""

#[19] Find the number that appears the most times.
"""numbers = [2, 5, 2, 7, 5, 2, 9, 7]
frequency = {}
# Count each number
for x in numbers:
    if x not in frequency:
        frequency[x] = 1
    else:
        frequency[x] = frequency[x] + 1

# Find the number with the largest frequency
most_common = None
largest_count = 0

for number in frequency:
    if frequency[number] > largest_count:
        largest_count = frequency[number]
        most_common = number
print(most_common)"""

# [20] Find their GCD (Greatest Common Divisor).
"""a = 24
b = 36
largest = 0
for x in range(1,25):
   if a % x ==0 and b % x == 0 and x > largest:
      largest = x
print(largest) """
# OR best way for ICPC
"""a = 36
b = 24

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print(a)"""

#[21] is a prime number.
"""a = int(input("write what evere number you need and i will tell you if the number is prime "))
prime_num = True
for x in range(2,a):
  if a % x == 0:
    prime_num = False
    break
if prime_num:
  print("prime")
else:
  print("not prime")"""

#[22]Find how many of these numbers are prime in ICPC approach.
"""import math
numbers = [17, 20, 23, 25, 31]
count = 0
for x in numbers:
  prime_num = True
  for p in range(2,math.isqrt(x) + 1):
    if x % p == 0:
      prime_num = False
      break
  if prime_num:
    count+=1
print(count)"""

#[23] Find its prime factorization.
"""n = 60
q = 2
while q <= n:
  while n % q == 0:
    print(q)
    n = n // q
  
  q += 1 """

# [24] find LCM and GCD
"""a = 24
b = 36
x = a
y = b
while y != 0:
  remainder = x % y
  x = y
  y = remainder
lcm = a * b // x
print("LCM =", lcm)
print("GCD =", x)"""

#[25] Count how many numbers are divisible by 5.
"""numbers = [12, 17, 20, 25, 31, 40]
count = 0
for num in numbers:
  if num % 5 == 0:
    count+=1
print(count)"""

#[26] Count how many numbers are divisible by both 3 AND 5.
"""numbers = [12, 15, 18, 20, 24, 30, 35, 40]
count = 0
for num in numbers:
  if num % 3 == 0 or num % 5 == 0:
    count+=1
print(count)"""

# Given an array of integers, find the most frequent number.
#If two numbers have the same frequency, choose the smaller number.
"""numbers = [4, 2, 4, 3, 2, 4, 2]
num = {}
for x in numbers:
  if x not in num:
    num[x] = 1
  else:
    num[x] = num[x] + 1
print(num)
largest = 0
most_common = None

for number in num:
  if num[number] > largest or (num[number] == largest and number < most_common):
    largest = num[number]
    most_common = number
print(most_common)"""

#Find the smallest number that appears exactly 3 times.
"""numbers = [4, 2, 7, 4, 2, 7, 9, 4, 2, 5]
seen ={}
for num in numbers:
  if num not in seen:
    seen[num] = 1
  else:
    seen[num] +=1
print(seen)
smallest = None
for number in seen:
  if seen[number] == 3:
     if smallest is None or number < smallest:
        smallest = number
print(smallest)"""

#a sorted array, remove duplicates in-place so each unique element appears once, then return the number of unique elements k
"""nums = [0, 0, 1, 1, 2, 2, 3, 4, 5]

k = 1

for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        nums[k] = nums[i]
        k += 1

print(k)
print(nums)"""