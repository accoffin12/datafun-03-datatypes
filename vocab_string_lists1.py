"""Alexandra Coffin
2023/1/31
Data Analytic Fundementals
Mod. 3: Creating Strings and using them"""
# imports first

# reusable functions next

# call functions and execute code
# use if __name__ == "__main__":

import math
import statistics
import random

#Currently standing teams in F1 for 2023 season.
Grid_teams = ["Mercedes", "Ferrari", "Alpine", "Haas", "McLaren", "Red Bull", "Aston_Martin", "AlphaTauri", "Alpha Romea", "Williams"]

#Define Tracks calls
tracks = ["Bahrain", "Jeddah", "Melbourne", "Baku", "Miami", "Imola", "Monaco", "Catalunya", "Montreal", "Spielberg", "Silverstone", "Budapest", "Spa", "Zandvoort", "Monza", "Singapore", "Suzuka", "Qatar", "Austin", "Mexico_City", "Sao_Paulo", "Las_vegas", "Abu_Dhabi"]

#Define Track Parts 
track_local = ["Paddock", "Parc_Ferme", "Pit_Board", "Pit_Wall", "Pits", "Sectors", "Straight", "Shikaina", "S_turns", "DRS", "Speed_trap"]

#Define Drivers 
drivers_list = ["Verstappen", "Perez", "Leclarc", "Sainz", "Russell", "Hamilton", "Ocon", "Gasly", "Piastri", "Norris", "Bottas", "Zhou", "Stroll", "Alonso", "Magnussen", "Hulkenberg", "De_Vries", "Tsunoda", "Albon", "Sargeant"]

#Define Driver Numbers
Driver_numbers = [1, 11, 16, 55, 63, 44, 31, 10, 4, 77, 24, 18, 14, 20, 27, 45, 22, 23]

#Define Winning, Losing, Points, DNF, Podium
outcomes_list = ["winning", "losing", "points", "DNF", "Podium", "Polesitter"]

#Define Accident calls
accident = ["Safety_Car", "caution_flag", "safety_lap", "virtual_safety_car"]

#Define verbs
verbs = ["driving", "breaking", "passing", "folling_raceline", "undercut", "bottoming", "lift_and_coast", "oversteer", "understeer", "Porposing"]

#Define adverbs commonly used 
adverbs = ["quickly", "slowly", "loudly", "poorly", "furiously", "coolly"]

#Define adjectives commonly used
adjectives = ["windy", "wet", "dry", "dark", "bright", "high_altitude"]

#Define Colors
colors = ["red", "silver", "pink", "grey", "papya", "navy", "British_Racing_Green", "white", "royal_blue", "crimson"]

for name, team, color in zip(drivers_list, Grid_teams, colors):
    print(f'Driver ={drivers_list}; Team = {Grid_teams}; Color = {colors}')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
"""Using len() with tuples"""
HAM_tuple = 'Hamilton', 'silver', 'Mercedes', 44
len(HAM_tuple)
print(len(HAM_tuple))

RUS_tuple = 'Russell', 'silver', 'Mercedes', 63
len(RUS_tuple)
print(len(RUS_tuple))
print()
Mercedes_AMG = RUS_tuple + HAM_tuple
print(Mercedes_AMG)

#Fun Random Sentence: F1 and Drama are certainly something
sentence =(
       f"{random.choice(drivers_list)} is currently {random.choice(verbs)} "
    f"while {random.choice(Grid_teams)} is {random.choice(outcomes_list)}."
    f"We have yet to hear from driver number {random.choice(Driver_numbers)}, there was a {random.choice(accident)}."
    f"Never a dull moment at {random.choice(tracks)}."
)

print(sentence)
print()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
"""Using a Text File"""
with open("rivals_2023.txt", 'r') as rival:
    text = rival.read()
    list_words = text.split()
    unique_words = set(list_words)
    

word_count = len(list_words)
unique_word_ct = len(unique_words)
print(f"Word Counts from Rivals_2023 Article")
print(f"Word Count: {word_count}")
print()
print(f"Unique Word Count: {unique_word_ct}")
rival.close()