print("Welcome to my Mad Libs game. Add the corect word to below sentences.")
print('1. I hear _________(noun) barking.\n2. I can _________(verb) in swimmingpool. \n3. I would like to _________(verb) a car.')

print("\n1. Write 'OK' to continue")
sentence = input()
sentence = sentence.lower()
if sentence != 'ok':
    print(str(sentence) + 'buy buy')
    
else:
    print("Lets start. ")


print("1. I hear _________(noun) barking.")
sentence = input('Noun: ')
sentence = sentence.lower()
if sentence != 'dog':
    print(str(sentence) + '- incorrect, try again')
else:
    print("1. I hear " + str(sentence) + " barking. - correct ")
    score = 1
    
print("2. I can _________(verb) in swimmingpool.")
sentence1 = input('Verb: ')
sentence1 = sentence1.lower()
if sentence1 != 'swim':
    print(str(sentence1) +'- incorrect, try again')
else:
    print("2. I can " + str(sentence1) + " in swimmingpool. - correct")
    score = score+1
    
print("3. I would like to _________(verb) a car.")
sentence2 = input('Verb: ')
sentence2 = sentence2.lower()
if sentence2 != 'have':
    print(str(sentence2) +'- incorrect, try again')
else:
    print("3. I would like to " + str(sentence2) + " a car. - correct")
    score = score+1

print('Your score: ' + str(score) + 'points. \n Thnak you' )
