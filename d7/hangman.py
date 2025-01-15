from random_word import Wordnik
wordnik_service = Wordnik()
lives = 6
word = ""
#status control
def status():
    if lives == 6:
      return hangmansok()
    elif lives == 5:
      return head()
    elif lives == 4:
      return body()
    elif lives == 3:
      return left()
    elif lives == 2:
      return right()
    elif lives == 1:
       return leg()
    else:
       return ded()
def hangmansok():
    print('  +---+')
    print('  |   |')
    print('      |')
    print('      |')
    print('      |')
    print('      |')
    print('=========')
def head():
    print('  +---+')
    print('  |   |')
    print('  o   |')
    print('      |')
    print('      |')
    print('      |')
    print('=========')
def body():
    print('  +---+')
    print('  |   |')
    print('  o   |')
    print('  |   |')
    print('      |')
    print('      |')
    print('=========')
def left():
    print('  +---+')
    print('  |   |')
    print('  o   |')
    print(' /|   |')
    print('      |')
    print('      |')
    print('=========')
def right():
    print('  +---+')
    print('  |   |')
    print('  o   |')
    print(' /|\  |')
    print('      |')
    print('      |')
    print('=========')
def leg():
    print('  +---+')
    print('  |   |')
    print('  o   |')
    print(' /|\  |')
    print(' /    |')
    print('      |')
    print('=========')
def ded():
    print('  +---+')
    print('  |   |')
    print('  o   |')
    print(' /|\  |')
    print(' / \  |')
    print('      |')
    print('=========')
    print(f"the word is {word}")
#setting up the game
def setup():
  global display
  global letters
  global word
  global length_word
  display = []
  word = wordnik_service.get_random_word().lower()
  length_word = len(word)
  for _ in range(length_word):
     display += "_"
  print(display)
  #print(word)
  print(f"there is {len(word)} characters in this word")

#intro pretty cute
def intro():
    print('========================================================')
    print("welcome to the hangman by lynn, please guess the word!")
    print("before the little man dies, or you will carry the guilt")
    print('       / _| ___  _ __ _____   _____ _ __ ')
    print('      | |_ / _ \|  __/ _ \ \ / / _ \  __|')
    print('      |  _| (_) | | |  __/\ V /  __/ |   ')
    print('      |_|  \___/|_|  \___| \_/ \___|_|   ')
    print('========================================================')


intro()
setup()
end = False
while not end:
  guess = input("guess a letter\n").lower()
  #check for repeated letters
  if guess in display:
     print(f"you have already tried {guess}")
  #check that position baby
  for position in range(length_word):
    letter = word[position]
    if guess == letter:
      #print('right')
      display[position] = letter
      status()
    # else:
    #   print(display)
    #   print("wrong")
  if guess not in word:
    lives -= 1
    print(f"the letter {guess} is not in the word")
    status()
    if lives == 0:
       end = True
       print("you lose")
  print(display)
  if "_" not in display:
    end = True
    print("you win")
    status()
  if lives == 0:
    end = True
    print("you lose")
    status()
