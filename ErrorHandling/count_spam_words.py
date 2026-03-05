

def count_spam_words(message):

    count = 0

    fr = open("ErrorHandling\\spam_words.txt")

    spam_words = [line.rstrip("\n") for line in fr]

    spam_words_in_msg = [w for w in message.split(" ") if w in spam_words]

    count = len(spam_words_in_msg)

    print(len(spam_words_in_msg)/len(message.split(" "))*100)

    return count


print(count_spam_words("you win free cash"))
print(count_spam_words("win free cash lottery"))


# ObjectOrientedProgramming
# 