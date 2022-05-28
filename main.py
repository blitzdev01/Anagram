# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    return word[::-1] == anagram


print(find_anagram("now", "won"))
print(find_anagram("now", "woo"))

