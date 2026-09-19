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

#Find the length of the longest consecutive increasing run.
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

#This is inspired by 2020 Ethiopian Collegiate Programming Contest Problem D — Good Arrays
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