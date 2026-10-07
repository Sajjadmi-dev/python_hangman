import random


words_list = ["apple" , "python" , "student" , "television" , "university" , "computer"]
max_eror = 5


def choose_word() :
    return random.choice(words_list)


def display_word(secret_word , guessed_letters) :
    
    displayed = []
    
    for letter in secret_word :
        if (letter) in guessed_letters :
            displayed.append(letter)  
        else :
            displayed.append("_")     
            
    print("\nWord : " , "".join(displayed))
    

def get_guess() :
    
    while True :
        
        guess = input("enter your guess letter : ")
        
        if len(guess) != 1 or not guess.isalpha() or not guess.isascii() :
            print("please enter one english letter")
        
        else :
            return guess
        

def check_guess(guess , secret_word , guessed_letters , wrong_guesses) :
    
    if guess in guessed_letters :
        print("you already guessed that letter!")
        return wrong_guesses
    
    guessed_letters.append(guess)
    
    if guess in secret_word :
        print("correct")
    else : 
        print("wrong guess!")
        wrong_guesses += 1
        
    return wrong_guesses


def has_won(secret_word , guessed_letters) :
    
    return all( letter in guessed_letters for letter in secret_word) 

def play_round() :
    secret_word = choose_word()
    guessed_letters = []
    wrong_guess = 0
    
    
    print("\nWwlcome to Hangman game!")
    print(f"you can make up to {max_eror} wrong guesses")
    
    
    while wrong_guess < max_eror and not has_won(secret_word , guessed_letters) :
        
        display_word(secret_word , guessed_letters) 
        
        print("Guessed letter : " , "".join(sorted(guessed_letters)) or "None")
        print(f"Wrong guesses : {wrong_guess} / {max_eror}")
        
        guess = get_guess()
        
        wrong_guess = check_guess(guess , secret_word , guessed_letters , wrong_guess) 
        
        display_word(secret_word , guessed_letters)
    
    if has_won(secret_word , guessed_letters) :
        print("Congratulation you won!!")
        
    else :
        print("GAME OVER!")
        print(f"the word was : {secret_word} ")
            
            
def main() :
    
    while True :
        
        play_round()
        
        while True :
            
          answer = input("Do you want play again? (yes or no)").strip().lower()
        
          if answer == "yes" :
             break
          elif answer == "no" :
             print("Thanks for playing")
             return
          else :
             print("Please enter yes or no")
            

if __name__ == "__main__" :
    main()        
            