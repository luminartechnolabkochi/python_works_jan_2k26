

# lst1=["listen","earth","moon","dad","madam","race"]

# lst2=["silent","angel","heart","test","dam","care"]

# anagram_words={"listen"}


word="racecarfast"

# print non recursive character
# print recursive character whose count >= 2

non_recursive = [ch for ch in word if word.count(ch)==1]
recursive = {ch:word.count(ch) for ch in word if word.count(ch)>=2}

print("non recursive",non_recursive)

print("recursive",recursive)