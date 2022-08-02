"""Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence. The function should return True if the sentence has any word with duplicate letters, else return False. """

def StringDuplicate(s):
    duplicates = {}

    for word in s:
        if word in duplicates:
            duplicates[word] +=1

        else:
            duplicates[word] = 1


    for k,v in duplicates.items():
        if v > 1:
            return True
        return False



c = StringDuplicate(input("Please Enter String"))
print(c)
