

word1 = input("enter word1 ")#ABCDE

word2 = input("enter word2 ")#PQR

# word1=>ABCDRF
    #    01234
# word2=>PQR

if len(word1) > len(word2):

    print(word1[len(word2):])

elif len(word2)>len(word1):

    print(word2[len(word1):])


# 
#indexing
#sequence[start:stop]
#sequence[:stop]
#sequence[start:]
#copy=sequence[:]

