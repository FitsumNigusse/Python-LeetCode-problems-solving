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

# [27] Given an array of integers, find the most frequent number.
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

#[28] Find the smallest number that appears exactly 3 times.
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

#[30] a sorted array, remove duplicates in-place so each unique element appears once, then return the number of unique elements k
"""nums = [0, 0, 1, 1, 2, 2, 3, 4, 5]

k = 1

for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        nums[k] = nums[i]
        k += 1

print(k)
print(nums)"""

#[31] Given an integer x, reverse its digits and return the reversed number.
"""x = -123
reverse = 0
negative = x < 0
x = abs(x)
while x != 0:
  last_digit = x % 10
  x = x // 10
  reverse = reverse * 10 + last_digit
if negative:
  reverse = -reverse
print(reverse)"""
#[32] find the length of the last word in the string.
"""s = "hello world"
word = s.split()
last_word = len(word[-1])
print(last_word)"""
#For example if n = 1, then his feeling is "I hate it" or 
# if n = 2 it's "I hate that I love it", 
# and if n = 3 it's "I hate that I love that I hate it" and so on
"""n = int(input())
answer = ""
for i in range(1, n + 1):
  if i % 2 == 1:
    if i == n:
      answer += "I hate it"
    else:
      answer += "I hate that "
  else:
    if i == n:
      answer += "I love it"
    else:
      answer += "I love that "
print(answer)
  """
#Given three distinct integers a, b, and c, find the medium number between all of them.
"""n = int(input())
for i in range(n):
  a, b, c  = map(int, input().split())
  if a < b < c or c < b < a:
    print(b)
  elif b < a < c or c < a < b:
    print(a)
  elif a < c < b or b < c < a:
    print(c)"""

#You are given three integers a, b, and c such that exactly one of these two equations is true:
# a + b = c
# a − b = c
#Output + if the first equation is true, and - otherwise.
"""n = int(input())
for i in range(n):
  a, b, c = map(int, input().split())
  if a + b == c:
    print("+")
  elif a - b == c:
    print("-")"""

# An elephant decided to visit his friend. 
# It turned out that the elephant's house is located at point 0 
# and his friend's house is located at point x(x > 0) of the coordinate line. 
# In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. 
# Determine, what is the minimum number of steps he need to make in order to get to his friend's house.
"""x = int(input())
steps = x // 5
if x % 5 != 0:
  steps += 1
print(steps)"""

# Codeforces separates its users into 4
#  divisions by their rating:

# For Division 1: 1900≤rating
# For Division 2: 1600≤rating≤1899
# For Division 3: 1400≤rating≤1599
# For Division 4: rating≤1399

"""x = int(input())
for i in range(x):
  rating = int(input())
  if rating <= 1399:
    print("Division 4")
  elif 1400<= rating <= 1599:
    print("Division 3")
  elif 1600 <= rating <= 1899:
    print("Division 2")
  elif 1900 <= rating:
     print("Division 1")"""

# she can't calculate sum 1+3+2+1 but she can calculate sums 1+1+2 and 3+3.
# You've got the sum that was written on the board. 
# Rearrange the summans and print the sum in such a way that Xenia can calculate the sum.
"""s = str(input())  
numbers = s.split("+")
numbers.sort()
result = "+".join(numbers)
print(result)"""

# Bear Limak wants to become the largest of bears, or at least to become larger than his brother Bob.
# Right now, Limak and Bob weigh a and b respectively.
#  It's guaranteed that Limak's weight is smaller than or equal to his brother's weight.
# Limak eats a lot and his weight is tripled after every year, while Bob's weight is doubled after every year.
# After how many full years will Limak become strictly larger (strictly heavier) than Bob?

"""count = 0
a, b = map(int, input().split())
while True:
  if a <= b:
    a = a * 3
    b = b * 2
    count += 1
  elif a > b:
    break
print(count)"""

# A soldier wants to buy w bananas in the shop. 
# He has to pay k dollars for the first banana, 2k dollars for the second one and so on 
# (in other words, he has to pay i·k dollars for the i-th banana).
# He has n dollars. How many dollars does he have to borrow from his friend soldier to buy w bananas?

"""k, n, w = map(int, input().split())

total = 0

for i in range(1, w + 1):
    price = i * k
    total += price

borrow = total - n

if borrow < 0:
    borrow = 0

print(borrow)"""

#There are n stones on the table in a row,
#  each of them can be red, green or blue. 
# Count the minimum number of stones to take from the table 
# so that any two neighboring stones had different colors. 
# Stones in a row are considered neighboring if there are no other stones between them.

"""n = int(input())
s = str(input())
count = 0
for i in range(n - 1):
  if s[i] == s[i + 1]:
    count += 1
print(count)"""

# Little girl Tanya is learning how to decrease a number by one,
#  but she does it wrong with a number consisting of two or more digits. 
# Tanya subtracts one from a number by the following algorithm:
# if the last digit of the number is non-zero, she decreases the number by one;
# if the last digit of the number is zero, she divides the number by 10 (i.e. removes the last digit).

"""n, k = map(int, input().split())

for i in range(k):
    if n % 10 == 0:
        n = n // 10
    else:
        n = n - 1

print(n)"""

# Petya loves lucky numbers. We all know that lucky numbers are the positive 
# integers whose decimal representations contain only the lucky digits 4 and 7. 
# For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.
# Unfortunately, not all numbers are lucky. 
# Petya calls a number nearly lucky if the number of lucky digits in it is a lucky number. 
# He wonders whether number n is a nearly lucky number.
# Print on the single line "YES" if n is a nearly lucky number. Otherwise, print "NO" (without the quotes).

"""n = int(input())

count = 0

while n > 0:
    digit = n % 10

    if digit == 4 or digit == 7:
        count += 1

    n = n // 10

if count == 4 or count == 7:
    print("YES")
else:
    print("NO")"""

# Petya started to attend programming lessons. 
# On the first lesson his task was to write a simple program. 
# The program was supposed to do the following: in the given string, 
# consisting if uppercase and lowercase Latin letters, it:
# deletes all the vowels,
# inserts a character "." before each consonant,
# replaces all uppercase consonants with corresponding lowercase ones.

"""vowels = ["a", "e", "i", "o", "u", "y"]

s = input()
s = s.lower()

final = ""

for char in s:
    if char not in vowels:
        final += "." + char

print(final)"""

# Petya wants to compare those two strings lexicographically. 
# If the first string is less than the second one, print "-1". 
# If the second string is less than the first one, print "1". 
# If the strings are equal, print "0". 
# Note that the letters' case is not taken into consideration when the strings are compared.

"""s1 = input().lower()
s2 = input().lower()
if s1 < s2 :
  print(-1)
elif s2 < s1:
  print(1)
else:
  print(0)
"""

# Input
# The first line contains a positive integer n (1 ≤ n ≤ 100), then follow n lines containing three integers each: the xi coordinate, the yi coordinate and the zi coordinate of the force vector, 
# applied to the body ( - 100 ≤ xi, yi, zi ≤ 100).
# Output
# Print the word "YES" if the body is in equilibrium, or the word "NO" if it is not.

"""n = int(input())

x_sum = 0
y_sum = 0
z_sum = 0

for i in range(n):
    x, y, z = map(int, input().split())

    x_sum += x
    y_sum += y
    z_sum += z

if x_sum == 0 and y_sum == 0 and z_sum == 0:
    print("YES")
else:
    print("NO")
"""

# Given a two-digit positive integer n
# , find the sum of its digits.

"""t = int(input())
for i in range(t):
    num = int(input())
    x = num % 10
    y = num // 10
    print(x + y)"""


"""x = int(input())

if x < 0:
    print("False")
else:
    original = x
    reverse = 0

    while x != 0:
        reman = x % 10
        x = x // 10
        reverse = reverse * 10 + reman

    if original == reverse:
        print("True")
    else:
        print("False")"""

# It seems like the year of 2013 came only yesterday. 
# Do you know a curious fact? The year of 2013 is the first year after the old 1987 with only distinct digits.
# Now you are suggested to solve the following problem: 
# given a year number, find the minimum year number which is strictly larger than the given one
#  and has only distinct digits.

"""y = int(input())
y += 1
while len(set(str(y))) != 4:
  y += 1
print(y)"""

# If the word t is a word s, written reversely, print YES, otherwise print NO.
"""s = input()
t = input()

s = s[::-1]

if s == t:
    print("YES")
else:
    print("NO")"""

# If Anton won more games than Danik, print "Anton" (without quotes) in the only line of the output.
# If Danik won more games than Anton, print "Danik" (without quotes) in the only line of the output.
# If Anton and Danik won the same number of games, print "Friendship" (without quotes).
"""n = input()
winer = str(input())
dani = 0
anto = 0
for i in winer:
  if i == "D":
    dani += 1
  else:
    anto += 1
if dani > anto:
  print("Danik")
elif dani == anto:
  print("Friendship")
else:
  print("Anton")"""

# Input
# The first line of the input contains two integers n and h (1 ≤ n ≤ 1000, 1 ≤ h ≤ 1000) — the number of friends and the height of the fence, respectively.
# The second line contains n integers ai (1 ≤ ai ≤ 2h), the i-th of them is equal to the height of the i-th person.
# Output
# Print a single integer — the minimum possible valid width of the road.

"""n,h = map(int, input().split())
height = list(map(int, input().split()))
width =  0
for i in height:
    if i <= h:
        width += 1
    else:
        width += 2
print(width)"""

#  If there are at least 7 players of some team standing one after another, 
# then the situation is considered dangerous. 
# For example, the situation 00100110111111101 is dangerous 
# and 11110111011101 is not. You are given the current situation. 
# Determine whether it is dangerous or not.
# Print "YES" if the situation is dangerous. Otherwise, print "NO".
"""player = input()

dangerous = False

for i in range(len(player)):
    if player[i:i+7] == "1111111" or player[i:i+7] == "0000000":
        dangerous = True
        break

if dangerous:
    print("YES")
else:
    print("NO")"""

# At the first stop, the number of passengers inside the tram before arriving is 0. Then, 3 passengers enter the tram, and the number of passengers inside the tram becomes 3.
# At the second stop, 2 passengers exit the tram (1 passenger remains inside). Then, 5 passengers enter the tram. There are 6 passengers inside the tram now.
# At the third stop, 4 passengers exit the tram (2 passengers remain inside). Then, 2 passengers enter the tram. There are 4 passengers inside the tram now.
# Finally, all the remaining passengers inside the tram exit the tram at the last stop. There are no passenger inside the tram now, which is in line with the constraints.

"""n = int(input())
people = 0
max = 0
for i in range(n):
    a, b = map(int,input().split())
    people = people - a + b
    if people > max:
        max = people
print(max)"""
# The second line contains nintegers, each integer is either 0 or 1
# If i-th integer is 0, then i-th person thinks that the problem is easy; if it is 1, then i-th person thinks that the problem is hard.

"""n = int(input())
rate = list(map(int, input().split()))
if 1 in rate:
    print("HARD")
else:
    print("EASY")"""

"""n = int(input())
count = 0
for i in range(n):
  a, b = map(int, input().split())
  if b - a >= 2:
    count += 1
print(count)"""

# For a positive integer n let's define a function f:
# f(n) =  - 1 + 2 - 3 + .. + ( - 1)nn
# Your task is to calculate f(n) for a given integer n.
#  solution : even = n // 2     odd = - (n + 1)// 2

"""n = int(input())

if n % 2 == 0:
    print(n // 2)
else:
    print(-(n + 1) // 2)"""

#[266B] The first line contains two integers n and t (1 ≤ n, t ≤ 50), which represent the number of children in the queue and the time after which the queue will transform into the arrangement you need to find.
# The next line contains string s, which represents the schoolchildren's initial arrangement. If the i-th position in the queue contains a boy, then the i-th character of string s equals "B", otherwise the i-th character equals "G".
# Output
# Print string a, which describes the arrangement after t seconds. If the i-th position has a boy after the needed time, then the i-th character a must equal "B", otherwise it must equal "G".

"""n, t = map(int, input().split())
s = input()
for _ in range(t):
    s = s.replace('BG', 'GB')
print(s)
"""

# The first line of the input contains an integer n (1 ≤ n ≤ 100000) — the number of magnets.
#  Then n lines follow. The i-th line (1 ≤ i ≤ n) contains either characters "01", if Mike put the i-th magnet in the "plus-minus" position, or characters "10", 
# if Mike put the magnet in the "minus-plus" position.
# Output
# On the single line of the output print the number of groups of magnets.

"""n = int(input())

previous = input()
groups = 1
same = 0

for i in range(1, n):
    current = input()

    if current == previous:
        same += 1

    previous = current

print(n - same)"""

# [200B] find average
"""n = int(input())
p = list(map(int, input().split()))

total = sum(p)
answer = total / n

print(answer)"""

# [136A] cood force problems
"""n = int(input())
p = list(map(int, input().split()))

answer = [0] * n

for i in range(n):
    answer[p[i] - 1] = i + 1

print(*answer)"""

# Read the four numbers: x, y, z, and n.
# For the first coordinate, try every number from 0 to x:
# For the second coordinate, try every number from 0 to y:
# For the third coordinate, try every number from 0 to z:
# For every combination, make a list:[i, j, k]

"""x = int(input())
y = int(input())
z = int(input())
n = int(input())

answer = [[i, j, k]
          for i in range(x + 1)
          for j in range(y + 1)
          for k in range(z + 1)
          if i + j + k != n]

print(answer)"""

# You are given a 2D integer array ranges and two integers left and right. 
# Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.
# Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. 
# Return false otherwise.

"""class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        for number in range(left, right + 1):
            covered = False

            for r in ranges:
                if r[0] <= number <= r[1]:
                    covered = True
                    break

            if not covered:
                return False

        return True"""

# find the missing number from array
"""def missingNumber(a):
    n = len(a)

    expected = n * (n + 1) // 2
    actual = sum(a)

    return expected - actual"""

# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
# Example 2:
# Input: matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]
# Explanation:
# Players 1, 2, 5, and 6 have not lost any matches.
# Players 3 and 4 each have lost two matches.
# Thus, answer[0] = [1,2,5,6] and answer[1] = [].

"""class Solution:
    def findWinners(self, matches):
        losses = {}
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)

            if loser not in losses:
                losses[loser] = 0

            losses[loser] += 1

        no_loss = []
        one_loss = []

        for player in players:
            if player not in losses:
                no_loss.append(player)
            elif losses[player] == 1:
                one_loss.append(player)

        no_loss.sort()
        one_loss.sort()

        return [no_loss, one_loss]"""


# finding from the dectionery some values
"""n = int(input())

phone_book = {}

for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

while True:
    try:
        name = input()

        if name in phone_book:
            print(name + "=" + phone_book[name])
        else:
            print("Not found")

    except EOFError:
        break"""

#  this is how to change string by it index number
"""def mutate_string(string, position, character):
    length  = list(string)
    length[position] = character
    string = ''.join(length)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)"""

# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]"""
"""
n = int(input())
seen = []
for i in range(1, n+1):
  if i % 3 == 0 and i % 5 == 0:
    seen.append("FizzBuzz")
  elif i % 3 == 0:
    seen.append("Fizz")
  elif i % 5 == 0:
    seen.append("Buzz")
  else:
    seen.append(str(i))
print(seen) """


# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.
# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]

"""nums = [6,5,4,8]
count = 0
seen = []
for i in range(len(nums)):
  count = 0
  for j in range(len(nums)):
    if nums[i] > nums[j]:
       count +=1
  
  seen.append(count)
  
print(seen)"""

# There is a programming language with only four operations and one variable X:
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
# Example 1:
# Input: operations = ["--X","X++","X++"]
# Output: 1
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# --X: X is decremented by 1, X =  0 - 1 = -1.
# X++: X is incremented by 1, X = -1 + 1 =  0.
# X++: X is incremented by 1, X =  0 + 1 =  1.
# Example 2:

# Input: operations = ["++X","++X","X++"]
# Output: 3
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# ++X: X is incremented by 1, X = 0 + 1 = 1.
# ++X: X is incremented by 1, X = 1 + 1 = 2.
# X++: X is incremented by 1, X = 2 + 1 = 3.
# Example 3:

# Input: operations = ["X++","++X","--X","X--"]
# Output: 0
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# X++: X is incremented by 1, X = 0 + 1 = 1.
# ++X: X is incremented by 1, X = 1 + 1 = 2.
# --X: X is decremented by 1, X = 2 - 1 = 1.
# X--: X is decremented by 1, X = 1 - 1 = 0.

# x = 0
# for i in operations:
#   if i == "X++" or i == "++X":
#     x+=1
#   else:
#     x-=1
# print(x)"""

# """Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
"""class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = {}

        # Count characters in the first word
        for ch in words[0]:
            if ch not in common:
                common[ch] = 1
            else:
                common[ch] += 1

        # Compare with the other words
        for word in words[1:]:
            count = {}

            for ch in word:
                if ch not in count:
                    count[ch] = 1
                else:
                    count[ch] += 1

            # Keep the smaller count
            for ch in list(common):
                if ch in count:
                    common[ch] = min(common[ch], count[ch])
                else:
                    common[ch] = 0

        # Build the answer
        answer = []

        for ch in common:
            for _ in range(common[ch]):
                answer.append(ch)

        return answer"""

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.
# Example 1:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]
"""
nums = [1,3,2,1]
con = []
for i in nums:
  con.append(i)
for x in con:
  nums.append(x)
print(nums)"""

# Example 1:
# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: The array ans is built as follows: 
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]
# Example 2:
# Input: nums = [5,0,1,2,3,4]
# Output: [4,5,0,1,2,3]
# Explanation: The array ans is built as follows:
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
#     = [4,5,0,1,2,3]
"""class Solution:
    def buildArray(self, nums):
        ans = []

        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans"""

# """Example 1:
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
# Example 2:

# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false
# Example 3:

# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true"""
"""class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        commen1 = ''.join(word2)
        commen = ''.join(word1)
        if commen == commen1:
           return True
        else:
            return False
        """

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
# xample 1:
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Explanation:
# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.
# Example 2:
# Input: words = ["omk"]
# Output: []
# Example 3:
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]
"""
class Solution:
    def findWords(self, words: list[str]) -> list[str]:

        ans = []
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

for word in words:
    lower_words = set(word.lower())

    if (lower_words.issubset(row1) or
        lower_words.issubset(row2) or
        lower_words.issubset(row3)):

        ans.append(word)

return ans"""

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]"""
# s = ["H","a","n","n","a","h"]
"""s.reverse()
print(s)"""


# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.
# Example 1:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".
# Example 2:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
# Example 3:
# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".

"""class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        smallest = float("inf")
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    index_sum = i + j
                    if index_sum < smallest:
                        smallest = index_sum
                        ans = []
                        ans.append(list1[i])
                    elif index_sum == smallest:
                        ans.append(list1[i])
        return ans"""


# escape ghost
"""class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:

        my_distance = abs(target[0]) + abs(target[1])

        for ghost in ghosts:
            ghost_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])

            if ghost_distance <= my_distance:
                return False

        return True     """

# Input: nums = [1, 2, 3, 3]
# Output: true
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

"""class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        if not nums:
            found = False
        else:
            for i in nums:
                if i not in seen:
                    seen[i] = 1
                else:
                    seen[i] = seen[i] + 1
            for x in seen:
                if seen[x] > 1:
                    found = True
                    break
                else:
                    found = False
        if found:
            return True
        else:
            return False
"""

# this all above solution can replaced by one line code
"""return len(nums) != len(set(nums))"""

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true
# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

"""class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        else:
            return sorted(s) == sorted(t)"""

# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]
# Example 3:
# Input: strs = [""]
# Output: [[""]]
"""strs = ["act","pots","tops","cat","stop","hat"]
group = {}
for word in strs:
  i = ''.join(sorted(word))
  if i not in group:
    group[i] = [word]
  else:
    group[i].append(word) 
out_put = list(group.values())
print(out_put)
 """

# Given an integer array `nums` and 
# an integer `k`, return the `k` most frequent elements within the array.
# The test cases are generated such that the answer is always **unique**.
# You may return the output in **any order**.
# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]

"""class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        # Count how many times each number appears
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        # Sort numbers by their frequency
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Get the first k numbers
        answer = []

        for i in range(k):
            answer.append(sorted_freq[i][0])

        return answer"""


"""class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top_element = stack[len(stack) - 1]
                if char == ')' and top_element == '(':
                    stack.pop()
                    
                elif char == '}' and top_element == '{':
                    stack.pop()
                    
                elif char == ']' and top_element == '[':
                    stack.pop()
                    
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
"""
# The idea is simple: count consecutive 0s, and keep the biggest count.
# For example:
# 1 0 0 1 0 → zero groups are 00 and 0 → answer is 2.
  
"""t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    current = 0
    longest = 0

    for x in arr:
        if x == 0:
            current += 1
            longest = max(longest, current)
        else:
            current = 0

    print(longest)"""
  
# Allen has a LOT of money. He has n dollars in the bank. For security reasons, 
# he wants to withdraw it in cash (we will not disclose the reasons here). 
# The denominations for dollar bills are 1
# , 5,10,20,100
# . What is the minimum number of bills Allen could receive after withdrawing his entire balance?
# Examples
# InputCopy
# 125
# OutputCopy
# 3
# InputCopy
# 43
# OutputCopy
# 5
# InputCopy
# 1000000000
# OutputCopy
# 10000000

"""n = int(input())

coins = [100, 20, 10, 5, 1]
ans = 0

for coin in coins:
    ans += n // coin
    n %= coin

print(ans)"""

# Input
# You will be given in the first line an integer T (1 ≤ T ≤ 20) the number of test cases.
# Each test case begins with one integer N the count of the numbers given (1 ≤ N ≤ 104).
# The next line contains N integers a1,a2,...,an (1 ≤ ai ≤ 105).
# Output
# For each test case print a single line, containing a single integer, the minimum number that has the
# maximum number of digits among the other numbers
"""T = int(input())
max_digit = 0
ans = 0
for i in range(T):
  N = int(input())
  numbers = list(map(int , input().split()))
  for x in numbers:
    digit = len(str(x))
    if digit > max_digit:
      max_digit = digit
      ans = x
    elif len(str(x)) == max_digit and x < ans:
      ans = x
  print(ans)
  
"""

# Input
# The first line of the input contains an integer t (1 ≤ t ≤ 10) the number of test cases.
# The first line of each test case contains an integer n (1 ≤ n ≤ 104) the number of elements in the array.
# The second line of each test case contains n integers (1 ≤ ai ≤ 109). The elements of the array a.
# Output
# For each test case, print a single line containing n elements, The lexicographically largest array by making
# the operation any number of times as you want.

"""even = []
odd = []
a = [4,8,3,5]
for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.sort(reverse=True)
odd.sort(reverse=True)

answer = []

for i in a:
    if i % 2 == 0:
        answer.append(even.pop(0))
    else:
        answer.append(odd.pop(0))

print(answer)"""


    
  




  
