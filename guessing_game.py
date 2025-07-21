import random
import time

# Displays welcome message to user and gets their name
def welcome_user():
    print('''
_____________________________________________
---------------------------------------------
          
          Welcome to Pick-a-Number!
_____________________________________________
---------------------------------------------
    ''')
    
    first_time = input('>> Is this your first time playing? (Y/N)  ')
    name = input('\n>> Please enter your name:  ')

    if first_time.lower() == 'n':
        print(f'''

*** Welcome back, {name.title()}! ***''')
    else:
        print(f'''
              
*** Hi, {name.title()}. Please selection an option from the Menu ***''')
    return name

# Function to set the winning number and guess count when a new game is started
def game_setup(min_num, max_num):
    winning_number = random.randint(min_num, max_num)
    guess_count = 1
    print(f'''
          
*** The winning number is between {min_num}-{max_num} ***
    ''')
    return winning_number, guess_count

# Controls the game flow and whether a user wants to keep playing, when user is done playing, returns their scores
def play():
    min_num = 1
    max_num = 100
    scores = []
    winning_number, guess_count = game_setup(min_num, max_num)

    while True:
        if guess_count == 1 and scores:
            print(f'\nHigh Score: {sorted(scores)[0]}')
        try:
            guess = int(input('\n>> Enter your guess:  '))
            if guess < min_num or guess > max_num:
                raise Exception
        except ValueError:
            err = 'invalid guess'
            err_msg = 'Guess must be a whole number'
            show_error(err, err_msg)
        except Exception:
            err = 'outside range'
            err_msg = f'Guess must be inside the range ({min_num}-{max_num})'
            show_error(err, err_msg)
        else:
            if guess < winning_number:
                guess_count += 1
                print('\nIt\'s Higher')
            elif guess > winning_number:
                guess_count += 1
                print('\nIt\'s Lower')
            elif guess == winning_number:
                print(f'''
                      
*** Congratulations! {winning_number} is the winner! ***
---------------------------------------------
You found the winning number in {guess_count} tries.
                ''')
                scores.append(guess_count)
                selection = input('\n>> Do you want to play again? (Y/N)  ')

                if selection == 'n':
                    return sorted(scores)
                else:
                    winning_number, guess_count = game_setup(min_num, max_num)

# Print out the users stats if they have scores, else print message indicating no stats
def display_stats(scores,name):
    if scores:
        high_score = scores[0]
        lowest_score = scores[len(scores) - 1]
        games_played = len(scores)
        average_score = sum(scores)/len(scores)
        print(f'''
              
 Stats for {name.title()}
---------------------------------------------
    High Score: {high_score}
    Average Score: {average_score}
    Lowest Score: {lowest_score}
    Gamed Played: {games_played}
        ''')
    else:
        print(f'''
              
xxx No stats to show for user {name.title()}. xxx
        ''')
    time.sleep(2)

# Display the menu to the user and return the menu selection
def menu():
    print('''
---------------------------------------------    
 MAIN MENU 
---------------------------------------------
    1 - Play Game
    2 - My Stats
    3 - Quit
    ''')
    return input('>> Pick a menu option: (1-3) ')

# Print formatted errors
def show_error(err, err_msg):
    print(f'''  
          
xxx ERROR: {err.upper()} xxx
---------------------------------------------
{err_msg.capitalize()}     
    ''')

# Starts the program and controls flow
def start_game():
    name = welcome_user()
    scores = []

    selection = menu()
    while True:
        if selection == '1':
            scores.extend(play())
            print(f'''
                  
*** Thanks for playing, {name.title()}! ***
            ''')
            selection = menu()
        elif selection == '2':
            display_stats(scores,name)
            time.sleep(1)
            selection = menu()
        elif selection == '3':
            print(f'''
                  
*** Goodbye, {name.title()}! Hope to see you again! ***
            ''')
            break
        else:
            err = 'invalid selection'
            err_msg = 'Please select a menu option'
            show_error(err, err_msg)
            time.sleep(2)
            selection = menu()


    # Menu to play, view user stats, or quit game
    # When playing
    #   if it's not the first play through, show high score
    #   keep prompting until they guess the number (give feedback, catch exceptions)
    #   provide message when they win and show how many guesses it took
    #   prompt to play again
    #       if yes, repeat when playing loop
    #       if no, provide thanks for playing message and return to menu
    # Stats
    #   if no games have been played, tell user there are no stats for the current session and return to menu
    #   if scores has at least one value: show high score, average score, worst score, number of games played
    # Quit
    #   Show goodbye message

    # TODO: export scores to csv when user quits 
    #   when program starts, ask user if this is their first time every playing
    #   if yes, proceed to normal game loop
    #   if no, prompt for their name and import scores related to that name
    #   use all scores to show score statistics
    #   use all scores to show score history
    #   will need to ask user for their name so can retrieve the correct score history
    #       if user not found in history, report no play history for the current user
    
start_game()