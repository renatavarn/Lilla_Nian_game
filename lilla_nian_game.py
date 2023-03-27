import random
import os
import time

word_library = {
    "word_list1": ["P", "CEPE", "CREEP", "CREEPS", "CREPE", "DEEP", "EPEE", "PEDS", "PEER", "PERE", "PERSE", "PERT",
                   "PEST",
                   "PESTER", "PETER",
                   "PRECEDE", "PRESET", "PREST", "RESPECT", "RESPECTED", "SCEPTER", "SCEPTRE", "SEEP", "SEPT", "SPEC",
                   "SPECTER", "SPECTRE",
                   "SPEED", "SPEEDER", "SPEER", "SPREE", "STEEP", "STEEPER", "STEP", "TEPEE"],
    "word_list2": ["T", "CLOT", "COLT", "CRIT", "IRITIC", "LICIT", "LICTOR", "LOTI", "LOTIC", "OTIC", "RIOT", "ROTI",
                   "ROTL",
                   "TIRO", "TOIL", "TORC", "TORI", "TORIC", "TRIO", "TRIOL", "VICTOR", "VITRIC", "VITRIOL", "VITRIOLIC",
                   "VOLT"],
    "word_list3": ["E", "EERY", "ENJOY", "ENJOYER", "ENURE", "ERNE", "EURO", "EYER", "JEER", "JEON", "JERRY", "JOEY",
                   "JOURNEY", "JOURNEYER", "ORNERY",
                   "REENJOY", "RERUN", "RUNE", "YORE"],
    "word_list4": ["T", "AIRT", "LILT", "TALL", "TIVY", "TRIAL", "TRIVIAL", "VITAL", "ARTY", "LYART", "TALLY", "TRAIL",
                   "TRILL", "TRIVIALLY", "VITALLY", "LAITY", "TAIL", "TILL", "TRAY", "TRIVIA", "VITA"],
    "word_list5": ["R", "ARETE", "EATER", "QUART", "QUARTE", "QUARTET", "QUARTETTE", "QUEER", "RATE", "RETE", "TARE",
                   "TART", "TATER", "TATTER", "TEAR", "TETRA", "TETTER", "TREAT", "TREE", "TRUE", "URATE",
                   "UREA", "UTTER"],
    "word_list6": ["D", "ADIT", "DIAL", "DIGITAL", "DISTAL", "GLAD", "SIALID", "TIDAL", "ALGID", "DIALIST", "DIGITALIS",
                   "DISTIL", "LAID", "SILD", "TSADI", "DAIS", "DIGIT", "DIGS", "GILD", "SAID", "STAID"],
}

title = """
  _      _ _ _         _   _ _             
 | |    (_) | |       | \ | (_)            
 | |     _| | | __ _  |  \| |_  __ _ _ __  
 | |    | | | |/ _` | | . ` | |/ _` | '_ \ 
 | |____| | | | (_| | | |\  | | (_| | | | |
 |______|_|_|_|\__,_| |_| \_|_|\__,_|_| |_|                                                                                   
"""

welcome_letter = "\nLilla Nian is a word guessing game where you guess as many words as possible in a grid of 9 letters.\nEvery letter can only be used once and the letter in the middle must be in all words.\n\n"

instructions = '\nIf you want to cheat, type: "help".\nWrite "exit" to quit or "?" to see this again.'


def sleep(num):
    time.sleep(num)


def clear_screen():
    """Clears the screen when run from terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def display_board(board, score, guessed_words):
    """Prints the board containing the master word"""
    print("\n")
    print('\t    |   |')
    print('\t  ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('\t    |   |')
    print('\t-------------')
    print('\t    |   |')
    print('\t  ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('\t    |   |')
    print('\t-------------')
    print('\t    |   |')
    print('\t  ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('\t    |   |')
    print(f"\nMy words: {score}    Total words: {len(word_list) - 1}")
    print(" | ".join(guessed_words))


def find_mandatory_letter(word_lst):
    """Finds the one-letter word and returns it"""
    for word in word_lst:
        return word if len(word) == 1 else None


def find_master_word(word_lst, center_letter):
    """Finds the 9-letter word. Shuffles the letters and keeps the master letter in the middle.
    Input/output: list"""
    word_as_lst = []
    for word in word_lst:
        if len(word) == 9:
            word_as_lst = list(word)
            random.shuffle(word_as_lst)
            # Swaps the mandatory letter with the center letter
            for index, element in enumerate(word_as_lst):
                if index == 4 and element != center_letter:
                    word_as_lst[word_as_lst.index(center_letter)] = element
                    word_as_lst[4] = center_letter
    return word_as_lst


def guess_word(word_lst, score, guessed_words):
    """Player makes a guess and if it's correct return it.
    Prompts the user if the guess is incorrect.
    Input: list, Output: string"""
    guess = ""
    while guess not in word_lst or guess == mandatory_letter:
        guess = input("Guess a word: ").upper()
        if guess == "HELP":
            clear_screen()
            print(" ".join(word_lst[1:]))
            sleep(2)
        elif guess == "EXIT":
            clear_screen()
            print("Good try, bye bye!")
            sleep(1000)
        elif guess == "?":
            print(instructions)
            sleep(3)
        elif len(guess) < 4:
            print("The word needs to be at least 4 letters.")
            sleep(2)
        elif len(guess) > 9:
            print("The word needs to be less than 10 letters.")
            sleep(2)
        elif guess not in word_lst:
            print("That is not correct!")
            sleep(1)
        clear_screen()
        display_board(master_word, score, guessed_words)
    else:
        print("That's right, good job!")
        sleep(1)
        return guess


def generate_rand_list(library):
    """Takes a dictionary consisting of str:list and returns 1 random list."""
    new_word_lst = [random.choice([value for key, value in library.items()])]
    return [y for x in new_word_lst for y in x]


def menu():
    """Starts the menu of the game"""
    my_score = 0
    my_words = []

    clear_screen()
    print(title)
    sleep(0.01)
    for x in welcome_letter:
        print(x, end="")
        sleep(0.001)
    sleep(1)
    game_on = input("\nDo you want to play? (Y/N) ").lower()
    while game_on != "n" and game_on != "y":
        clear_screen()
        game_on = input('\n¯\_(^^)_/¯\nWoooops! Press "Y" or "N": ').lower()
    if game_on == "n":
        clear_screen()
        print("Well fine, maybe you're not up for the challenge.")
    else:
        clear_screen()
        print(instructions)
        sleep(2)
        clear_screen()
        play_game(my_score, my_words)
        print("You have completed the game, you're awesome!")


def play_game(score, words):
    """Game is run until victory!"""
    while score != len(word_list) - 1:
        # Prints out the board, total words and the current score
        display_board(master_word, score, words)
        # Player makes a guess which is saved to my words
        words.append(guess_word(word_list, score, words))
        clear_screen()
        score += 1


word_list = generate_rand_list(word_library)  # Creates a word list from the library of word games.
mandatory_letter = find_mandatory_letter(word_list)  # Returns first letter in the word list which is the middle letter.
master_word = find_master_word(word_list, mandatory_letter)  # Finds the word containing 9 letters that will be displayed.


### STARTS THE MENU ###
menu()







# Run game from cmd:
# cd C:\Users\gusta\OneDrive\Documents\PycharmProjects\Nod\Nian
# python main.py



