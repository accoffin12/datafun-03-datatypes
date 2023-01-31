"""
Alexandra Coffin
Data Analytics Fundementals
1/29/2023
Mod. 3: Dictionaries for Teams and Tracks

"""

import statistics

"""Create some tuples"""

RB_VET_tuple = (256, 392, 281, 397, 167)
RB_RIC_tuple = (238, 92, 256, 200, 170)
RB_WEB_tuple = (10, 21, 69.5, 242, 258, 197, 199)
RB_ALB_tuple = (92, 105)
RB_PER_tuple = (190, 305)
RB_VER_tuple = (468, 368, 419, 417, 319, 585.5, 759)

RedBull_tPoints_tuple = RB_VER_tuple + RB_ALB_tuple + RB_PER_tuple + RB_RIC_tuple + RB_VET_tuple + RB_WEB_tuple
print(f'Total points from 2009 - 2020:', {RedBull_tPoints_tuple})

RedBull_con_tuple = RB_VET_tuple + RB_VER_tuple
print()

Avrg_RB_Points = statistics.mean(RedBull_con_tuple)
print(f'Average amount of points per driver in team Red Bull in a year', {Avrg_RB_Points})
print()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
"""Sets Practice using lap length. """
track_set_A = {5.412, 6.17, 5.27}
track_set_B = {4.309, 6.12, 5.281}

#Union between track lengths
track_set_union = {5.412, 6.17, 5.27}.union({4.309, 6.12, 5.281})
print(track_set_union)

track_intersection = {5.412, 6.17, 5.27}.intersection({4.309, 6.12, 5.281})
print(track_intersection)

print()
print()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

"""Track Dictionaries"""
bahrain_dict = {"track": "Bahrain", "circuit_length_km": 5.412, "#_laps": 57, "race_distancekm": 308.238}
saudi_arabia_dict = {"track": "Saudi_Arabia", "circuit_length_km": 6.174, "#_laps": 50, "race_distancekm": 308.45}
melbourne_dict = {"track": "Australia", "circuit_length_km": 5.278, "#_laps": 58, "race_distancekm": 306.124}
baku_dict = {"track": "Baku", "circuit_length_km": 6.003, "#_laps": 51, "race_distancekm": 306.049}
miami_dict = {"track": "Miami", "circuit_length_km": 5.412, "#_laps": 57, "race_distancekm": 308.326}
imola_dict = {"track": "Imola", "circuit_length_km": 4.909, "#_laps": 63, "race_distancekm": 309.049}
monaco_dict = {"track": "Monaco", "circuit_length_km": 3.337, "#_laps": 78, "race_distancekm": 260.286}
catalunya_dict = {"track": "Catalunya", "circuit_length_km": 4.675, "#_laps": 66, "race_distancekm": 308.424}
montreal_dict = {"track": "Montreal", "circuit_length_km": 4.361, "#_laps": 70, "race_distancekm": 305.27}
austria_dict = {"track": "Austria", "circuit_length_km": 4.318, "#_laps": 71, "race_distancekm": 306.452}
silverstone_dict = {"track": "Silverstone", "circut_length_km": 5.891, "#_laps": 52, "race_distancekm": 306.198}
budapest_dict = {"track": "Budapest", "circuit_length_km": 4.381, "#_laps": 70, "race_distancekm": 306.63}
spa_dict = {"track": "Belgium/Spa", "cicuit_length_km": 7.004, "#_laps": 44, "race_distancekm": 308.052}
netherlands_dict = {"track": "Netherlands", "circuit_length_km": 4.259, "#_laps": 72, "race_distancekm": 306.587}
monza_dict = {"track": "Monza", "circuit_length_km": 5.793, "#_laps": 53, "race_distancekm": 306.72}
singapore_dict = {"track": "Singapore", "circuit_length_km": 5.063, "#_laps": 61, "race_distancekm": 308.706}
qatar_dict = {"track": "Qatar", "circuit_length_km": 5.38, "#_laps": 57, "race_distancekm": 306.66}
austin_dict = {"track": "Austin", "circuit_length_km": 5.513, "#_laps": 56, "race_distancekm": 308.405}
mexico_dict = {"track": "Mexico_city", "circuit_length_km": 4.304, "#_laps": 71, "race_distancekm": 305.354}
sao_paulo_dict = {"track": "Sao_Paulo", "circuit_length_km": 4.309, "#_laps": 71, "race_distancekm": 305.879}
las_vegas_dict = {"track": "Las_Vegas", "circuit_length_km": 6.12, "#_laps": 50, "race_distancekm": 305.88}
abu_dhabi_dict = {"track": "Abu_Dhabi", "circuit_length_km": 5.281, "#_laps": 58, "race_distancekm": 306.183}


"""Team Dictionaries"""
alfa_romeo_dict = {"team": "Alfa_Romeo", "Base": "Switzerland", "Driver1": "Bottas", "Driver2": "Guanyu", "world_champ": "N/A"}
alpha_tauri_dict = {"team": "Scuderia_AlphaTauri", "Base": "Italy", "Driver1": "Tsunoda", "Driver2": "De_Vries", "world_champ": "N/A"}
alpine_dict = {"team": "BWT_Alpine", "Base": "United_Kingdom", "Driver1": "Gasly", "Driver2": "Ocon", "world_champ": 2}
aston_martin_dict = {"team": "Aston_Martin", "Base": "United_Kingdom", "Driver1": "Alonso", "Driver2": "Stroll", "world_Champ": "N/A"}
ferrari_dict = {"team": "Scuderia_Ferrari", "Base": "Italy", "Driver1": "Leclerc", "Driver2": "Sainz", "world_champ": 16}
haas_dict = {"team": "Haas", "Base": "United_States", "Driver1": "Magnussen", "Driver2": "Hulkenberg", "world_champ": "N/A"}
mclaren_dict = {"team": "McLaren", "Base": "United_Kingdom", "Driver1": "Norris", "Driver2": "Piastri", "world_champ": 8}
mercedes_dict = {"team": "Mercedes-AMG_PETRONAS", "Base": "United_Kingdom", "Driver1": "Hamilton", "Driver2": "Russell", "world_champ": 8, "nickname": "Silver_Arrows"}
red_bull_dict = {"team": "Red_Bull", "Base": "United_Kingdom", "Driver1": "Verstappen", "Driver2": "Perez", "world_champ": 5}
williams_dict = {"team": "Williams", "Base": "United_Kingdom", "Driver1": "Albon", "Driver2": "Sargeant", "world_champ": 9}

track_dict = {
    "track": ["Bahrain", "Saudi_Arabia", "Australia", "Baku", "Miami", "Imola", "Monaco", "Catalunya", "Montreal", "Austria", "Silverstone", "Budapest", "Belgium/Spa", "Netherlands", "Monza", "Singapore", "Qatar", "Austin", "Mexico_City", "Sao_Paulo", "Las_Vegas", "Abu_Dhabi"],
    "circuit_length_km": [5.412, 6.174, 5.278, 6.003, 5.412, 4.909, 3.337, 4.675, 4.361, 4.318, 5.891, 7.004, 4.259, 5.793, 5.063, 5.38, 5.513, 4.304, 4.309, 6.12, 5.281],
    "#_laps": [57, 50, 58, 51, 57, 63, 78, 66, 70, 71, 52, 70, 44, 72, 53, 61, 57, 56, 71, 71, 50, 58],
    "race_distancekm": [308.238, 308.45, 306.124, 306.049, 308.326, 309.049, 260.286, 308.424, 305.27, 306.452, 306.198, 306.052, 308.052, 306.587, 306.587, 306.72, 308.706, 306.66, 308.405, 305.879, 305.88, 306.183],
}

team_dict = {
    "team": ["Alfa_Romeo", "Scuderia_AlphaTauri", "BWT_Alpine", "Aston_Martin", "Scuderia_Ferrari", "Haas", "McLaren", "Mercedes-AMG_PETRONAS", "Red_Bull", "Williams"],
    "Base": ["Switzerland", "Italy", "United_Kingdom", "United_States"],
    "Driver1": ["Bottas", "Tsunoda", "Gasly", "Alonso", "Leclerc", "Magnussen", "Norris", "Hamilton", "Verstappen", "Albon"],
    "Driver2": ["Guanyu", "De_Vris", "Ocon", "Stroll", "Sainz", "Hulkenberg", "Piastri", "Russell", "Perez", "Sargent"],
    "world_champ": ["N/A", 2, 16, 8, 8, 5, 9],
    "nickname": ["Silver_Arrows"]
}

print()
with open("rivals_2023.txt", 'r') as rival:
    text = rival.read()
    list_words = text.split()
    unique_words = set(list_words)

word_counts_dict = {}
for word in list_words:
    if word in word_counts_dict:
        word_counts_dict[word] += 1
    else:
        word_counts_dict[word] = 1

print(word_counts_dict)
word_counts_dict = {word: list_words.count(word) for word in list_words}