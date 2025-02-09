#  Import required modules for generating random numbers and creating time stamps for session logs
import random
import datetime


#Create function to generate enemy numbers based on the attempt level
def generate_numbers(attempt):
    if 1 <= attempt <= 5:
        return [random.randint(15, 100) for i in range(5)]
    elif 6 <= attempt <= 10:
        return [random.randint(250, 2000) for i in range(5)]
    elif 11 <= attempt <= 15:
        return [random.randint(3000, 10000) for i in range(5)]
    elif 16 <= attempt <= 20:
        return [random.randint(20000, 100000) for i in range(5)]


#Create function to generate the player's initial life score
def generate_life_score():
    return random.randint(1, 50)


#Create function to start and run the game
def play():
    player_name = input("\nEnter player name: ")
    life_score = generate_life_score()
    total_attempts = 0
    final_score = life_score
    attempt_list = []   # List to store attempt details

    print("Player name: ",player_name)

    # Game loop for up to 20 attempts
    for attempt in range(1, 21):
        numbers_to_fight = generate_numbers(attempt)
        print("Attempt: ",attempt)
        print(f"{player_name}'s life score is: {life_score}")
        print("Your enemies : ")
        print(" ".join(map(str, numbers_to_fight)))
        total_attempts = total_attempts + 1

        try:
            selected_number = int(input("Select a number to fight: "))
            if selected_number not in numbers_to_fight:
                print("enemy not found")

                # Record unsuccessful attempt
                attempt_list.append({
                    'attempt_number': attempt,
                    'presented_enemies': numbers_to_fight,
                    'user_input': selected_number,
                    'won': False,
                    'life_score': life_score
                })

                break

            won = selected_number <= life_score

            #Creating a dictionary
            attempt_list.append({
                'attempt_number': attempt,
                'presented_enemies': numbers_to_fight,
                'user_input': selected_number,
                'won': won,
                'life_score': life_score
            })

            if won:
                print(f"{player_name} killed {selected_number}\n")
                life_score = life_score + selected_number
            else:
                print(f"{selected_number} killed {player_name}!\n")
                break

        except ValueError:
            print("Invalid input..Game over!! Try again next time\n")
            break

    print("\n*** Details of session DON(Destroy of numbers) ***\n")
    print("Player name: ",player_name)
    print("Total attempts: ",total_attempts)
    print("Final score: ",life_score)
    if final_score > 0 and total_attempts == 20:
        print(f"{player_name} saved letter-kind!!!")
    else:
        print(f"{player_name} was defeated!!!")

    # Passing life_score
    save_details(player_name, attempt_list, final_score, total_attempts, life_score)


def save_details(player_name, attempt_list, final_score, total_attempts, life_score):
    current_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    random_number = str(random.randint(0000, 9999)).zfill(4)  # to add 4 random numbers for the file name
    file_name = f"{current_time}_{random_number}.txt"

    #Create file to attempt data file
    with open(file_name, "w") as file:
        file.write(f"Player name: {player_name}\n")

        for attempt_list in attempt_list:
            file.write(f"\nAttempt number - {attempt_list['attempt_number']}:\n")
            file.write(f"Life score of {player_name}: {attempt_list['life_score']}n")
            file.write(f"Enemies given: {', '.join(map(str, attempt_list['presented_enemies']))}\n")
            file.write(f"Chosen enemy: {attempt_list['user_input']}\n")
            file.write(f"Status of the battle: {'WON' if attempt_list['won'] else 'LOST'}\n")

        file.write("\n*** Final Results of the game ***\n")
        file.write(f"Total attempts: {total_attempts}\n")
        file.write(f"Final score: {life_score}\n")
        if final_score > 0 and total_attempts == 20:
            file.write(f"{player_name} saved letter-kind!!!")
        else:
            file.write(f"{player_name} was defeated!!!")



#function calling
play()
