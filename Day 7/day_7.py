import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letter = []
lives = 6
    
while game_over == False:

    print(f"****************************<???>/{lives} LIVES LEFT****************************")
   
    guess = input("Guess a letter: ").lower()
   
    display = ""
    
    if guess in correct_letter:
        print(f"You've already guessed a letter {guess}")
        
    if guess not in chosen_word:       
        print(f"You guessed a letter {guess}, that's not in the word. You lose a life") 
        lives -= 1
        
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display+=letter
        else:
            display += "_"
    
    
            
   
    
    if lives == 0:
        game_over = True
        print(stages[lives])
        print(display)
        print(f"IT WAS {chosen_word}! YOU LOSE")    
    elif "_" in display:
        game_over = False
    else:
        game_over = True
        print(stages[lives])
        print(display)        
        print("You win!")

    print(stages[lives])
    print(display)   
    
