
import random

class HangMan :
    

    WORDS = [
        "PYTHON" ,
        "APPLE" ,
        "ORANGE" ,
        "COMPUTER" ,
        "PROGRAM" ,
        "HANGMAN" ,
    ]        
    
    max_eror = 5
    
    def __init__(self):
        self.__secret_word = random.choice(self.WORDS)
        
        self.guessed_letters = []
        
        self.wrong_guesses = 0
        
    def display_word(self) :
        
        displayed = []
        
        for letter in self.__secret_word :
            if letter in self.guessed_letters :
                displayed.append(letter)
            
            else :
                displayed.append("_")
                
        print("\nThe word : ","".join(displayed))
            
            
    def get_guesses(self) :
        
        while True :
            guess = input("Enter your guess letter : ").strip().upper()
            
            if len(guess) != 1 or not guess.isalpha() or not guess.isascii() :
                print("Please enter one letter!")
                
            else :
                return guess
            
            
    
    def check_guess(self , guess) :
        
        if guess in self.guessed_letters :
            print("you already guess that letter!")
            return 
        
        self.guessed_letters.append(guess)
        
        if guess in self.__secret_word :
            print("Correct!")
            
        else :
            print("Wrong guess")
            self.wrong_guesses += 1
            
            
    
    def has_won(self) :
        for letter in self.__secret_word :
            if letter not in self.guessed_letters :
                return False
    
        return True
            
            
    def play(self) :
        
        print("\nWelcome to HangMan")
        print(f"you can make up to {self.max_eror} wrong guesses. ")
        
        while self.wrong_guesses < self.max_eror and not self.has_won() :
            
            self.display_word()
            
            print("guessed letter : " , "".join(self.guessed_letters) or "none")
            print(f"Wrong guesses : {self.wrong_guesses}/{self.max_eror}")
            
            guess = self.get_guesses()
            
            self.check_guess(guess)
            
        self.display_word()
            
        if self.has_won() :
            print("Congratulation , you won!")
        else :
            print("GAME OVER")
            print(f"The word was : {self.__secret_word}")


def main() :
    
    while True :
        
        game = HangMan()
        
        game.play()
        
        while True :
            
            answer = input("Do you want to play again ? (yes/no)")
            
            if answer == "yes" :
                break
            if answer == "no" :
                print("thanks for playing")
                return
            
            else :
                print("choose yes or no")
                
                
                
if __name__  == "__main__" :
    main()