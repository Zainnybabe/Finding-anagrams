# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

ram = str(input("enter a word: "))
arm = str(input("enter the second word: "))

def find_anagram(word, anagram):
    # [assignment] Add your code here
  sortedword = sorted(word)
  sortedanagram = sorted(anagram)
  if sortedword == sortedanagram:
    return True
  else:
    return False

    print(find_anagram(ram, arm))     