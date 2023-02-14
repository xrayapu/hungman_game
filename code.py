# hangman game !
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6
sample=['word', 'mind','look']
import random
word = random.choice(sample) 
# print(word)
it= len(word)
dispay=[]
#  _ use hoise cause here , ja use korba oita loop e kuno kaj nai 
for _ in range(it):  
    dispay+='-'
# print(dispay)
# '-' joto somoy display te thakbe oi time porjnto 
end_of_game =False
while not end_of_game :
    user =input('give a letter ').lower()

    for i in range(it):
        letter = word[i]

        if user == letter:
            dispay[i] =letter

    if user not in word:
        lives-=1
        if lives == 0 :
            end_of_game =True
            print('you lose.')
                        
    print(dispay)
    if '-' not in dispay:
        end_of_game =True
        print('you won !')
    
    print(stages[lives])


