import random
import HangManArt
import words

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

hangmanWord = getRandomWord(words.words)

print(r"""
 _                                              
| |                                             
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __    
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \   
| | | | (_| | | | | (_| | | | | | | (_| | | | |  
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  
                    __/ |                       
                   |___/                        
""")

#print("Psst, the solution is " + hangmanWord)

lives = 0
display = []

for _ in range(len(hangmanWord)):
    display.append("-")

while lives < 6:
    index = 0
    guess = input("guess a letter: ").lower()
    if guess in display:
        print("you have already guessed " + guess)
        continue

    for letter in hangmanWord:
        if guess == letter:
            display[index] = guess
        index+=1

    if guess not in hangmanWord:
        lives+=1
        print(guess + " not in word")

    print("".join(display))
    print(HangManArt.HANGMANPICS[lives])

    if "".join(display) == hangmanWord:
        print("you won.")
        break

if lives == 6:
    print("you lose")