import random
import json
import CharacterCreator


Setting = ["Desert", "Haunted Town", "Tavern", "Magical University", "Forrest", "Mountains"]
Desert_NPC = ["Sorcerer"]
Haunted_Town_NPC = ["Cleric", "Paladin"]
Tavern_NPC = ["Rogue", "Fighter"]
Magical_University_NPC = ["Wizard"]
Forrest_NPC = ["Druid", "Ranger"]
Mountains_NPC = ["Barbarian", "Ranger"]
Race_Choices = ['Human', 'Half-Elf', 'Elf', 'Dwarf', 'Half-Orc', 'Halfling', 'Tiefling', 'Dragonborn', 'Gnome']

def getNPC(s_s):
    if s_s == "Desert":
        s_c = random.choice(Desert_NPC)
    elif s_s == "Haunted Town":
        s_c = random.choice(Haunted_Town_NPC)
    elif s_s == "Tavern":
        s_c = random.choice(Tavern_NPC)
    elif s_s == "Magical University":
        s_c = random.choice(Magical_University_NPC)
    elif s_s == "Forrest":
        s_c = random.choice(Forrest_NPC)
    elif s_s == "Mountains":
        s_c = random.choice(Mountains_NPC)
    return s_c

def main():
    selected_race = random.choice(Race_Choices)
    selected_setting = random.choice(Setting)
    print("Your Setting: ", selected_setting)
    print("Your NPC: ")
    print (json.dumps(CharacterCreator.create_pc(selected_race, getNPC(selected_setting)), indent = 2))
    #user = True
    #while user:
        #user_choice = input('Would you like to create a setting?')
        #if user_choice == 'y':
            #user = True
            #selected_race = random.choice(Race_Choices)
            #selected_setting = random.choice(Setting)
            #print("Your Setting: ", selected_setting)
            #print("Your NPC: ")
            #print (json.dumps(CharacterCreator.create_pc(selected_race, getNPC(selected_setting)), indent = 2))
        #else:
            #user = False

if __name__ == '__main__':
    main()
