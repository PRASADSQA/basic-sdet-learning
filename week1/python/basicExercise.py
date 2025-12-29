# #Exercise 1
# weight = float(input("Enter your weight: "))
# unit = input("(K)g or (L)bs: ")
# if unit.upper() == "K":
#     convert = weight / 0.45
#     print("weight in lbs: " + str(convert))
# else:
#     convert = weight * 0.45
#     print("weight in kg: " + str(convert))


#Reverse a String
s = "python"
print(s[::-1])

#Check Palindrome
s = "madam"
print(s == s[::-1])

#Find Largest and smallest Number in a List
nums = [10, 20, 3, 90]
print(max(nums))
print(min(nums))

#Find Duplicate Elements in a List
lst = [1, 2, 3, 2, 4, 1]
duplicates = set([x for x in lst if lst.count(x) > 1])
print(duplicates)

# Remove Duplicates
lst = [1, 2, 2, 3, 1]
result = []

for i in lst:
    if i not in result:
        result.append(i)

print(result)

#Count Character Frequency
text = "automation"
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

# Find Second Largest Number
nums = [10, 5, 20, 8]
nums = list(set(nums))
nums.sort()
print(nums[-2])


# Reverse Words in a Sentence
sentence = "I love Python"
print(" ".join(sentence.split()[::-1]))

# Find Missing Number (1 to n)
nums = [1, 2, 4, 5]
n = 5
missing = n * (n + 1) // 2 - sum(nums)
print(missing)

# Swap Two Variables
a, b = 5, 10
a, b = b, a
print(a, b)
