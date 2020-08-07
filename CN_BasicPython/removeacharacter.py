def removecharacter(sentence, character):
    result = ''
    for i in sentence:
        if i != character:
            result +=i
    print(result)


sentence = "welcome to coding ninjas"
character = "o"
removecharacter(sentence, character)