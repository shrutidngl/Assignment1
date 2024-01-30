# 1. “Python + is + an + awesome + language”. 
    # Split the given string to get a list and join to get another string “Python is an awesome language” 
# 2. Write a Python program to create a dictionary from a string. Track the count of the letters from the string.
    # Input = “broadway”
    # Output = {“b”: 1, “r”: 1, “o”: 1, “a”: 2, “d”: 1, “w”: 1, “y”: 1} 
# 3. Write a Python program to combine two dictionaries by adding values for common keys. 
# 4. Write a program to check whether a string is anagram or not. 
    # An anagram of a string is another string that contains the same characters, only the order of characters can be different. 
    # For example, “silent” and “listen” are an anagram of each other.
# 5. Check whether a number is palindrome or not. Palindrome numbers are those which remain same even on reversing. 
    # Examples – 111, 131, 222, 212 etc.
    # Input: 121 => The number is palindrome
    # Input: 321 => The number is not palindrome


# 1)
words = "Python is an awesome language"
result = words.split("n")
result = words.split("s")
result = words.split("n")
result = words.split("e")
result = words.split(" ")
print(result)

word1 = "Python"
word2 = "is"
word3 = "an"
word4 = "awesome"
word5 = "language"
wordsS = f"{word1} {word2} {word3} {word4} {word5}"
print(words)


# 2)
str = input("Enter a String: ")
my_dict = {}
my_dict = my_dict.get(str, 0) + 1
print(my_dict)


# 3)
d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
#d = d1 + d2
#print(d)

# 4)
str1 = input("Enter string 1:")
str2 = input("Enter string 2:")
if sorted(str1) == sorted(str2):
    print("Two Strings are Anagrams.")
else:
    print("Two Strings are not Anagrams.")



# 5)
n = int(input("Enter number:"))
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if temp == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")