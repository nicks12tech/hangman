from tkinter import * #imports the tkinter (window)
from tkinter import PhotoImage #imports photo into the tkinter
import random #imports random selection function


window = Tk()
window.title("Hangman")
window.state('zoomed')

is_dark_mode = False #sets the dark mode 
lbl2 = None #makes the lbl2 variable recognizable

def toggle_mode(): #sets a condition if the turn on/off button is clicked
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    if is_dark_mode:
        set_dark_mode() #sets the screen in dark mode if the is_dark_mode variable is False
    else:
        set_light_mode() #sets the screen in light mode if the is_dark_mode variable is True
    update_lbl2() #it updates the lbl2 screen to match is_dark_mode variable's value

def set_dark_mode(): #this command changes the color of the background of the following to dark color whenever the turn on/off is clicked
    window.config(bg="#2C2C2C")
    lbl.config(bg="#2C2C2C", fg="white")
    lbl_name.config(bg="#2C2C2C", fg="white")
    lbl_section.config(bg="#2C2C2C", fg="white")
    lbl_word.config(bg="#2C2C2C", fg="white")
    lbl_hangman.config(bg="#2C2C2C", fg="white")
    lbl_message.config(bg="#2C2C2C", fg="white")
    lbl_hint.config(bg="#2C2C2C", fg="white")
    btn_start.config(bg="green", fg="white")
    btn_guess.config(bg="#2C2C2C", fg="white")
    btn_reset.config(bg="blue", fg="white")
    btn_mode_toggle.config(bg="white", fg="black")
    entry_name.config(bg="#2C2C2C", fg="white")
    entry_section.config(bg="#2C2C2C", fg="white")
    entry_guess.config(bg="#2C2C2C", fg="white")
    lbl_message1.config(bg="#2C2C2C", fg="red")
    lbl_message2.config(bg="#2C2C2C", fg="white")
    lbl_message3.config(bg="#2C2C2C", fg="white")
    lbl_hangman2.config(bg="#2C2C2C", fg="red")
    lbl_sentence.config(bg="#2C2C2C", fg="white")
    btn_choice1.config(bg="light grey", fg="black")
    btn_choice2.config(bg="light grey", fg="black")
    btn_choice3.config(bg="light grey", fg="black")
    btn_choice4.config(bg="light grey", fg="black")
    lbl_result.config(bg="#2C2C2C", fg="white")
    lbl2.config(bg="#2C2C2C", fg="black")
    lbl3.config(bg="#2C2C2C", fg="white")

def set_light_mode(): #this command changes the color of the background of the following to light color whenever the turn on/off is clicked
    window.config(bg="white")
    lbl.config(bg="white", fg="black")
    lbl_name.config(bg="white", fg="black")
    lbl_section.config(bg="white", fg="black")
    lbl_word.config(bg="white", fg="black")
    lbl_hangman.config(bg="white", fg="black")
    lbl_message.config(bg="white", fg="black")
    lbl_hint.config(bg="white", fg="black")
    btn_start.config(bg="green", fg="white")
    btn_guess.config(bg="black", fg="white")
    btn_reset.config(bg="blue", fg="white")
    btn_mode_toggle.config(bg="black", fg="white")
    entry_name.config(bg="white", fg="black")
    entry_section.config(bg="white", fg="black")
    entry_guess.config(bg="white", fg="black")
    lbl_message1.config(bg="white", fg="black")
    lbl_message2.config(bg="white", fg="black")
    lbl_message3.config(bg="white", fg="black")
    lbl_hangman2.config(bg="white", fg="black")
    lbl_sentence.config(bg="white", fg="black")
    btn_choice1.config(bg="light grey", fg="black")
    btn_choice2.config(bg="light grey", fg="black")
    btn_choice3.config(bg="light grey", fg="black")
    btn_choice4.config(bg="light grey", fg="black")
    lbl_result.config(bg="white", fg="white")
    lbl2.config(bg="white", fg="black")
    lbl3.config(bg="white", fg="black")

word_hints = {
    "python": "A popular programming language.",
    "hangman": "A classic word-guessing game.",
    "for": "Entry controlled loops used to repeat a section of code known number of times.",
    "while": "Entry controlled loops used to repeat a specific block until a condition is met.",
    "monitor": "An output device that displays information in pictorial or textual form. ",
    "cpu": "Known as the brain of the computer. ",
    "and": "It is a Logical operator where it returns TRUE only if both operands are TRUE.",
    "or": "It is a Logical operator where it returns TRUE if either operand is TRUE.",
    "not": "It is a Logical operator where it changes TRUE to FALSE and FALSE to TRUE"
}   #this variable give hints to the random word selected

attempts = 6    #this variable sets the amount of times you can guess
rep = 5

def start_game(event=None): #this sets a condition if the start button is clicked (event = None is to enable using enter button function)
    global word, guessed_letters, attempts, word_completion, player_name, player_section, lbl2, rep
    update_lbl2()


    player_name = entry_name.get()  #this variable sets the player name into whatever you input
    player_section = entry_section.get()    #this variable sets the player section into whatever you input
    
    if not player_name or not player_section: #this displays a message to enter your name and section when there is no input
        lbl_message.config(text="Please enter your name and section.")
        return

    word_list = ["python", "hangman", "for", "while", "monitor", "cpu", "and", "or", "not"]    #this variable shows the list of word that the program will randomly get
    word = random.choice(word_list).lower() #this sets the word_list as the source of word that the program can get from
    hint = word_hints[word] #this variable sets the hint according to the random word is selected
    guessed_letters = [] #this variable set as empty and can store elements
    word_completion = "_ " * len(word) #this variable sets the amount of dash(_) the program will show according to the amount of words the randomly selected word will have

    lbl_word.config(text=word_completion) #this displays the word_completion variable
    lbl_hangman.config(text=display_hangman1(attempts))  #this displays and updates the hangman drawing whenever you guessed wrong
    lbl_message.config(text ="Guess the correct letter to win!!")    #this displays a text that tells you what to do
    lbl_message1.config(text = "")
    lbl_message2.config(text = "")
    lbl_message3.config(text = "")
    lbl_hint.config(text=f"Hint: {hint}", fg="black") #this command sets a color of the foreground of the hint
    
    lbl2.config(text=f"Welcome, {player_name} from {player_section}!")
    lbl2.place(relx=0.5, rely=0.05, anchor='center')    #this command sets the place of lbl2 variable

    #this command erases the location of the following after clicking the start button
    entry_name.place_forget()
    lbl_name.place_forget()
    entry_section.place_forget()
    lbl_section.place_forget()
    btn_start.place_forget()
    lbl.place_forget()
    lbl_message1.place_forget()
    lbl_message2.place_forget()
    lbl_message3.place_forget()

    #this command sets the location of the following after clicking the start button
    btn_guess.place(relx=0.5, rely=0.8, anchor='center')
    btn_reset.place(relx=0.5, rely=0.85, anchor='center')
    entry_guess.place(relx=0.5, rely=0.7, anchor='center')
    lbl_word.place(relx=0.5, rely=0.63, anchor='center')
    lbl_hint.place(relx=0.5, rely=0.75, anchor='center')
    lbl_hangman.place(relx=0.3, rely=0.1)
    btn_skip.place(relx = 0.2, rely = 0.8)

    entry_guess.bind("<Return>", guess_letter)  #this command processes the guessed letter

def validate_guess_input(char):     #this command sets the amount of letters you can input int the entry widget
    return len(char) == 0 or (len(char) == 1 and char.isalpha())

def guess_letter(event=None):   #this command sets an entry widget to input your guess
    global attempts, word_completion, rep
    guess = entry_guess.get().lower()
    entry_guess.delete(0, END)

    if guess in guessed_letters:    #this command displays a message if you already guessed the letter
        lbl_message.config(text="You've already guessed that letter.")
        return

    guessed_letters.append(guess)   #this command keeps track of the letter you already input and displays the letter if your guess is correct

    if guess in word:   #this command displays a message if you guessed wrong or right
        lbl_message.config(text=f"Good guess: {guess}")
        word_completion = "".join([letter if letter in guessed_letters else "_ " for letter in word])
    else:
        attempts -= 1
        lbl_message.config(text=f"Wrong guess: {guess}. You have {attempts} attempts left.")

    lbl_word.config(text=word_completion)   #this updates the amount of dash(_) that is displayed according to the amount of letter you guessed
    lbl_hangman.config(text=display_hangman1(attempts))  #this updates the attempts you have left

    if "_ " not in word_completion: #this command displays a message if the dash(_) is gone
        btn_guess.place_forget()
        rep -= 1
        reset()

    elif attempts == 0: #this displays a message if your attempts is at 0
        lbl_message1.config(text = "GAME OVER!!", font=("Bookman Old Style", 80), fg = "red")
        lbl_message1.place(relx = 0.5, rely = 0.45, anchor = 'center')
        lbl_message2.config(text = f"The word was: {word}")
        lbl_message2.place(relx = 0.5, rely = 0.55, anchor = 'center')
        lbl_message3.config(text = "Would you like to play again?")
        lbl_message3.place(relx = 0.5, rely = 0.10, anchor = 'center')
        btn_guess.place_forget()
        game_over()
        disable_enter()

    if rep == 0:
        attempts = 6    #this variable sets the amount of times you can guess
        rep = 5
        advance()

    entry_guess.bind("<Return>", guess_letter)

def game_over():

    btn_skip.place_forget()
    btn_guess.place_forget()
    btn_reset.place_forget()
    entry_guess.place_forget()
    lbl_word.place_forget()
    lbl_hint.place_forget()
    lbl_hangman.place_forget()
    lbl2.place_forget()
    disable_enter()
    attempts = 6    #this variable sets the amount of times you can guess
    rep = 5
    btn_reset()

def advance():
    global lbl2

    lbl_message1.config(text = f"Congratulations {player_name}!", font = ("Bookman Old Style", 50))
    lbl_message1.place(relx = 0.5, rely = 0.23, anchor = 'center')
    lbl_message2.config(text = f"You've guessed the word: {word}")
    lbl_message2.place(relx = 0.5, rely = 0.40, anchor = 'center')
    lbl_message3.config(text = "Would you like to play again? or Go to the next level?")
    lbl_message3.place(relx = 0.5, rely = 0.6, anchor = 'center')
    btn_next.place(relx = 0.8, rely = 0.85)

    btn_guess.place_forget()
    btn_reset.place_forget()
    btn_skip.place_forget()
    entry_guess.place_forget()
    lbl_word.place_forget()
    lbl_hint.place_forget()
    lbl_hangman.place_forget()
    lbl2.place_forget()
    lbl_message.place_forget()
    lbl.place_forget()
    disable_enter()
    btn_reset()
    btn_next()

def disable_enter():
    entry_guess.config(state="disabled")
    btn_guess.config(state="disabled")
    btn_reset.place(relx=0.5, rely=0.85, anchor='center')
    entry_guess.unbind("<Return>")

def reset_game():   
    global attempts, rep
    entry_guess.pack_forget()   #this hides the guess entry widget, removing it from the window
    btn_guess.pack_forget()     #this hides the guess button, removing it from the window
    btn_reset.place()   #The reset button (btn_reset) is made visible using .place(), allowing the user to start a new game or reset the current one.
    entry_guess.config(state="normal")
    btn_guess.config(state="normal")
    lbl_message.config(text="")
    entry_guess.bind("<Return>", guess_letter)
    attempts = 6    #this variable sets the amount of times you can guess
    rep = 5
    lbl_message1.place_forget()
    lbl_message2.place_forget()
    lbl_message3.place_forget()
    btn_restart_lvl.place_forget()
    lbl_result.place_forget()
    start_game()
    update_lbl2()

def update_lbl2():  #this updates the color of the lbl2 variable background according to the is_dark_mode variable's value
    if lbl2:
        if is_dark_mode:
            lbl2.config(bg="#2C2C2C", fg="white")
        else:
            lbl2.config(fg="black")

def skip():
    advance()

def display_hangman1(attempts):  #this displays the drawing and draws the hangman one by one if your guess is wrong
    stages1 = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """,
        """
           
           |    
           |    
           |    
           |   
           |
        """,
    ]
    return stages1[attempts]

def reset():
    global attempts
    entry_guess.pack_forget()   #this hides the guess entry widget, removing it from the window
    btn_guess.pack_forget()     #this hides the guess button, removing it from the window
    btn_reset.place()   #The reset button (btn_reset) is made visible using .place(), allowing the user to start a new game or reset the current one.
    entry_guess.config(state="normal")
    btn_guess.config(state="normal")
    lbl_message.config(text="")
    entry_guess.bind("<Return>", guess_letter)
    lbl_message1.place_forget()
    lbl_message2.place_forget()
    lbl_message3.place_forget()
    start_game()
    update_lbl2()

sentence_list = [
    {"sentence": "Python is a programming language known for its {word}.", "word": "simplicity", "word2": "complexity", "word3": "ice cream", "word4": "words"},
    {"sentence": "A monitor is an output device that displays {word}.", "word": "data", "word2": "shirt", "word3": "person", "word4": "feet"},
    {"sentence": "A loop is used to repeat a block of {word}.", "word": "code", "word2": "actions", "word3": "letters", "word4": "lol"},
    {"sentence": "A compiler translates code from high-level language to {word} language.", "word": "machine", "word2": "complicated", "word3": "sign", "word4": "alien"},
    {"sentence": "In a game of Hangman, players guess {word} to win.", "word": "letters", "word2": "numbers", "word3": "word", "word4": "pass"},
    {"sentence": "Name of our ITE 366 teacher: {word}", "word": "Rica", "word2": "Martin", "word3": "Alice Go", "word4": "Junel"},
    {"sentence": "Name of our leader: {word}", "word": "Nic", "word2": "Elmer", "word3": "Karl", "word4": "Mark"},
    {"sentence": "Known as the brain of a computer", "word": "CPU", "word2": "ILY", "word3": "IDGF", "word4": "UFO"}
]

attempts2 = 6
rep2 = 10
correct_ans = 0
total = 10

def next_lvl():
    global attempts2, correct_word, sentence_list
    lbl_message1.place_forget()
    lbl_message2.place_forget()
    lbl_message3.place_forget()
    btn_next.place_forget()
    btn_reset.place_forget()

    # Display the sentence label and choice buttons
    
    lbl_hangman2.config(text=display_hangman2(attempts2))  #this displays and updates the hangman drawing whenever you guessed wrong
    lbl3.config(text="Guess the correct answer to win!!")
    
    lbl_sentence.place(relx=0.5, rely=0.65, anchor='center')
    lbl_hangman2.place(relx = 0.3, rely = 0.1)
    btn_choice1.place(relx=0.3, rely=0.7, anchor='center')
    btn_choice2.place(relx=0.3, rely=0.75, anchor='center')
    btn_choice3.place(relx=0.7, rely=0.7, anchor='center')
    btn_choice4.place(relx=0.7, rely=0.75, anchor='center')
    lbl_result.place(relx=0.5, rely=0.7, anchor='center')
    lbl3.place(relx=0.5, rely=0.05, anchor='center')

    sentence_data = random.choice(sentence_list)  # Randomly select a sentence
    sentence = sentence_data["sentence"]
    correct_word = sentence_data["word"]

    # Generate three random incorrect words
    incorrect_words = [
        sentence_data["word2"], 
        sentence_data["word3"], 
        sentence_data["word4"]
    ]
    incorrect_choices = random.sample(incorrect_words, 3)

    # Create the final list of choices (1 correct + 3 incorrect)
    all_choices = incorrect_choices + [correct_word]
    random.shuffle(all_choices)  # Shuffle to randomize the position

    # Update the label to show the sentence with the missing word
    lbl_sentence.config(text=sentence.replace("{word}", "_____"))

    # Update button texts to show the words as options
    btn_choice1.config(text=all_choices[0], bg = "light grey", command=lambda: check_answer(all_choices[0]))
    btn_choice2.config(text=all_choices[1], bg = "light grey", command=lambda: check_answer(all_choices[1]))
    btn_choice3.config(text=all_choices[2], bg = "light grey", command=lambda: check_answer(all_choices[2]))
    btn_choice4.config(text=all_choices[3], bg = "light grey", command=lambda: check_answer(all_choices[3]))

def check_answer(selected_word):
    global attempts2, rep2, correct_ans
    if selected_word == correct_word:
        correct_ans += 1
        rep2 -= 1
        lbl_result.config(text="Correct!", fg="green")
        next_lvl()
    else:
        attempts2 -= 1
        rep2 -= 1
        lbl_hangman2.config(text=display_hangman2(attempts2))
        lbl_result.config(text=f"Nice try! The correct word was: {correct_word}", fg="red")
        next_lvl()

    if attempts2 == 0:  # Check if attempts have reached zero
        game_over2()
    
    if rep2 == 0:
        congrats()

def congrats():
    global correct_ans, total
    lbl_sentence.place_forget()
    lbl_hangman2.place_forget()
    btn_choice1.place_forget()
    btn_choice2.place_forget()
    btn_choice3.place_forget()
    btn_choice4.place_forget()
    lbl_result.place_forget()

    lbl_message1.config(text = f"Congratulations!! {player_name}", font=("Bookman Old Style", 80), fg = "red")
    lbl_message1.place(relx = 0.5, rely = 0.45, anchor = 'center')
    lbl_message2.config(text = f"You guessed {correct_ans} correct answers out of {total} questions", font=("Bookman Old Style", 35))
    lbl_message2.place(relx = 0.5, rely = 0.55, anchor = 'center')
    lbl_message3.config(text = "Would you like to play again?", font=("Bookman Old Style", 20))
    lbl_message3.place(relx = 0.5, rely = 0.6, anchor = 'center')

    btn_reset.place(relx = 0.5, rely = 0.7, anchor = 'center')
    btn_restart_lvl.place(relx = 0.3, rely = 0.7)

# Label to display the sentence with missing word
def game_over2():
    lbl_sentence.place_forget()
    lbl_hangman2.place_forget()
    btn_choice1.place_forget()
    btn_choice2.place_forget()
    btn_choice3.place_forget()
    btn_choice4.place_forget()

    lbl_message1.config(text = "Game Over!!", font=("Bookman Old Style", 80), fg = "red")
    lbl_message1.place(relx = 0.5, rely = 0.45, anchor = 'center')
    lbl_message3.config(text = "Would you like to play again?", font=("Bookman Old Style", 20))
    lbl_message3.place(relx = 0.5, rely = 0.6, anchor = 'center')

    btn_reset.place(relx = 0.7, rely = 0.7, anchor = 'center')
    btn_restart_lvl.place(relx = 0.3, rely = 0.7)

def restart():
    global attempts2, rep2, correct_ans, total
    btn_restart_lvl.place_forget()

    attempts2 = 6
    rep2 = 10
    correct_ans = 0
    total = 10

    next_lvl()

def display_hangman2(attempts2):  #this displays the drawing and draws the hangman one by one if your guess is wrong
    stages2 = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """,
        """
           
           |    
           |    
           |    
           |   
           |
        """,
    ]
    return stages2[attempts2]

#logo = PhotoImage(file="")
#window.iconphoto(False, logo)

lbl = Label(window, text="Welcome to Hangman", font=("Bookman Old Style", 40), fg = "black")  #this sets a message welcoming player to hangman if the window is displayed
lbl.place(relx=0.5, rely=0.25, anchor='center') #this sets the location of the message

lbl2 = Label(window, text="", font=("bookman old style", 35))   #this variable sets a message's font, foreground color, and font size
lbl2.place(relx=0.5, rely=0.05, anchor='center')    #this command sets the place of lbl2 variable
lbl2.place_forget()

lbl3 = Label(window, text="", font=("bookman old style", 35))
lbl3.place(relx=0.5, rely=0.05, anchor='center')
lbl3.place_forget()

lbl_name = Label(window, text="Enter your name:", font=("Bookman Old Style", 20))   #this displays a message to enter your name
lbl_name.place(relx=0.5, rely=0.35, anchor='center')    #this sets the location of the message
entry_name = Entry(window, font=("Bookman Old Style", 20), bg="white", fg="black")  #this displays an entry widget where you can enter your name
entry_name.place(relx=0.5, rely=0.4, anchor='center')   #this sete the location of the entry widget

lbl_section = Label(window, text="Enter your section:", font=("Bookman Old Style", 20)) #this displays a message to enter your section
lbl_section.place(relx=0.5, rely=0.46, anchor='center') #this sets the location of the message
entry_section = Entry(window, font=("Bookman Old Style", 20), bg="white", fg="black")   #this displays an entry widget where you can enter your section
entry_section.place(relx=0.5, rely=0.51, anchor='center')   #this sets the location of the entry widget

lbl_word = Label(window, text="", font=("Bookman Old Style", 30))   #this 
lbl_word.place(relx=0.5, rely=0.5, anchor='center')
lbl_word.place_forget()

lbl_hangman = Label(window, text="", font=("Courier", 40), justify='left', fg="red")    #this displays the drawing of hangman
lbl_hangman.place(relx=0.45, rely=0.35) #this sets the location of the drawing
lbl_hangman.place_forget()  #this erases the drawing while the start button is not clicked

lbl_hangman2 = Label(window, text = "", font=("Courier", 40), justify='left', fg="red")
lbl_hangman2.place(relx = 0.3, rely = 0.1)
lbl_hangman2.place_forget()

lbl_message = Label(window, text="", font=("Bookman Old Style", 20))    #this displays a message whether your guess is correct of wrong
lbl_message.place(relx=0.5, rely=0.12, anchor='center') #this sets the location of the message

lbl_message1 = Label(window, text="", font=("Bookman Old Style", 60), fg = "red")
lbl_message1.place(relx = 0.5, rely = 0.45, anchor = 'center')
lbl_message1.place_forget()

lbl_message2 = Label(window, text="", font=("Bookman Old Style", 35))
lbl_message2.place(relx = 0.5, rely = 0.55, anchor = 'center')
lbl_message2.place_forget()

lbl_message3 = Label(window, text="", font=("Bookman Old Style", 20))
lbl_message3.place(relx = 0.5, rely = 0.6, anchor = 'center')
lbl_message3.place_forget()

lbl_hint = Label(window, text="", font=("Bookman Old Style", 20))  # Hint label
lbl_hint.place(relx=0.5, rely=0.6, anchor='center') #this sets the location of the hint message
lbl_hint.place_forget() #this erases the hint message while the start button is not clicked

entry_guess = Entry(window, font=("Bookman Old Style", 20), width=5)   #this displays an entry widget where you can input your guessed letter
entry_guess.place(relx=0.5, rely=0.65, anchor='center') #this sets the location of the entry widget
entry_guess.place_forget()  #this erases the entry widget while the start button is not clicked

btn_start = Button(window, text="Start Game", bg="green", fg="white", command=start_game)   #this displays a button with a command to start a game
btn_start.place(relx=0.5, rely=0.56, anchor='center')   #this sets the location of the button

btn_mode_toggle = Button(window, text="Nigger on/off", bg="black", fg="white", command=toggle_mode)   #this displays a button with a command to turn on/off dark mode
btn_mode_toggle.place(relx=0.1, rely=0.2)   #this sets the location of the button

btn_guess = Button(window, text="Guess Letter", bg="black", fg="white", command=guess_letter)   #this displays a button with a command to register your guess
btn_guess.place(relx=0.5, rely=0.75, anchor='center')   #this sets the location of the button
btn_guess.place_forget()    #this erases the button while the start button is not clicked

btn_reset = Button(window, text="Play Again", bg="blue", fg="white", command=reset_game) #this displays a button with a command to reset the game
btn_reset.place(relx=0.5, rely=0.87, anchor='center')   #this sets the location of the button
btn_reset.place_forget()    #this erases the button while the start button is not clicked

btn_next = Button(window, text = "Next", bg = "green", fg = "white", command = next_lvl)
btn_next.place(relx = 0.8, rely = 0.87)
btn_next.place_forget()

btn_choice1 = Button(window, text="")
btn_choice1.place(relx=0.3, rely=0.7, anchor='center')
btn_choice1.place_forget()

btn_choice2 = Button(window, text="")
btn_choice2.place(relx=0.3, rely=0.75, anchor='center')
btn_choice2.place_forget()

btn_choice3 = Button(window, text="")
btn_choice3.place(relx=0.7, rely=0.7, anchor='center')
btn_choice3.place_forget()

btn_choice4 = Button(window, text="")
btn_choice4.place(relx=0.7, rely=0.75, anchor='center')
btn_choice4.place_forget()

entry_limit = (window.register(validate_guess_input), '%P')  #this sets the limit of the number of letters you can enter - '%P' passes the current value of the widget

entry_guess = Entry(window, font=("Bookman Old Style", 20), width=5, validate='key', validatecommand=entry_limit)   #this displays an entry widget where you can input your guessed letter
entry_guess.place(relx=0.5, rely=0.65, anchor='center') #this sets the location of the entry widget
entry_guess.place_forget()  #this erases the entry widget while the start button is not clicked

lbl_sentence = Label(window, text="", font=("Arial", 18))
lbl_sentence.place(relx=0.5, rely=0.4, anchor='center')  # Change to place() method
lbl_sentence.place_forget()  # Hide initially

btn_restart_lvl = Button(window, text = "Restart level", bg = "blue", fg = "white", command = restart)
btn_restart_lvl.place(relx = 0.5, rely = 0.8, anchor = 'center')
btn_restart_lvl.place_forget()

# Buttons for the 4 word choices
btn_choice1 = Button(window, text="", font=("Arial", 14), width=15)
btn_choice1.place(relx=0.3, rely=0.5, anchor='center')
btn_choice1.place_forget()  # Hide initially

btn_choice2 = Button(window, text="", font=("Arial", 14), width=15)
btn_choice2.place(relx=0.3, rely=0.55, anchor='center')
btn_choice2.place_forget()  # Hide initially

btn_choice3 = Button(window, text="", font=("Arial", 14), width=15)
btn_choice3.place(relx=0.7, rely=0.5, anchor='center')
btn_choice3.place_forget()  # Hide initially

btn_choice4 = Button(window, text="", font=("Arial", 14), width=15)
btn_choice4.place(relx=0.7, rely=0.55, anchor='center')
btn_choice4.place_forget()  # Hide initially

# Label to display result (Correct/Wrong)
lbl_result = Label(window, text="", font=("Arial", 18))
lbl_result.place(relx=0.5, rely=0.65, anchor='center')
lbl_result.place_forget()  # Hide initially

btn_skip = Button(window, text = "skip", bg = "purple", fg = "white", command = skip)
btn_skip.place(relx = 0.2, rely = 0.8)
btn_skip.place_forget()

window.mainloop()   #this lets the pop up window stay in display while not clicking the X button
