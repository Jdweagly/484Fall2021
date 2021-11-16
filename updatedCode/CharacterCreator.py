import random
import json

# Global Values In Lists
Race_Choices = ['Human', 'Half-Elf', 'Elf', 'Dwarf', 'Half-Orc', 'Halfling', 'Tiefling', 'Dragonborn', 'Gnome']
Dwarf_Sub_Race_Choices = ['Hill Dwarf', 'Mountain Dwarf']
Elf_Sub_Race_Choices = ['High Elf', 'Wood Elf', 'Dark Elf']
Gnome_Sub_Race_Choices = ['Forrest Gnome', 'Rock Gnome']
Class_Choices = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer',
                 'Warlock', 'Wizard']
Barbarian_Sub_Class_Choices = ['Path of the Berserker', 'Path of the Totem Warrior']
Bard_Sub_Class_Choices = ['College of Lore', 'College of Valor']
Cleric_Sub_Class_Choices = ['Knowledge Domain', 'Life Domain', 'Light Domain', 'Nature Domain', 'Tempest Domain',
                            'Trickery Domain', 'War Domain']
Druid_Sub_Class_Choices = ['Cirlce of the Land', 'Circle of the Moon']
Fighter_Sub_Class_Choices = ['Champion', 'Battle Master', 'Eldritch Knight']
Monk_Sub_Class_Choices = ['Way of the Open Hand', 'Way of the Shadow', 'Way of the Four Elements']
Paladin_Sub_Class_Choices = ['Oath of Devotion', 'Oath of the Ancients', 'oath of Vengeance']
Ranger_Sub_Class_Choices = ['Hunter', 'Beast Master']
Rogue_Sub_Class_Choices = ['Thief', 'Assassin', 'Arcane Trickster']
Sorcerer_Sub_Class_Choices = ['Draconic Bloodline', 'Wild Magic']
Warlock_Sub_Class_Choices = ['The Archfey', 'The Fiend', 'The Great Old One']
Wizard_Sub_Class_Choices = ['School of Abjuration', 'School of Conjuration', 'School of Divination',
                            'School of Enhancement', 'School of Evocation', 'School of Illusion',
                            'School of Necromancy']
Alignments = ['Lawful Good', 'Neutral Good', 'Chaotic Good', 'Lawful Neutral', 'True Neutral', 'Chaotic Neutral',
              'Lawful Evil', 'Neutral Evil', 'Chaotic Evil']
Backgrounds = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit',
               'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin']
Ability_Score_Modifiers = {'1': '-5', '2': '-4', '3': '-4', '4': '-3', '5': '-3', '6': '-2', '7': '-2', '8': '-1',
                           '9': '-1', '10': '0', '11': '0', '12': '+1', '13': '+1', '14': '+2', '15': '+2', '16': '+3',
                           '17': '+3', '18': '+4', '19': '+4', '20': '+5', '21': '+5', '22': '+6'}


class Pc:
    def __init__(self, pc_race, pc_class, pc_subrace, pc_subclass, pc_background, pc_alignment, pc_str_stat,
                 pc_str_mod, pc_dex_stat, pc_dex_mod, pc_wis_stat, pc_wis_mod, pc_int_stat, pc_int_mod, pc_con_stat,
                 pc_con_mod, pc_cha_stat, pc_cha_mod):
        self.pc_race = pc_race
        self.pc_class = pc_class
        self.pc_subrace = pc_subrace
        self.pc_subclass = pc_subclass
        self.pc_background = pc_background
        self.pc_alignment = pc_alignment
        self.pc_str_stat = pc_str_stat
        self.pc_str_mod = pc_str_mod
        self.pc_dex_stat = pc_dex_stat
        self.pc_dex_mod = pc_dex_mod
        self.pc_wis_stat = pc_wis_stat
        self.pc_wis_mod = pc_wis_mod
        self.pc_int_stat = pc_int_stat
        self.pc_int_mod = pc_int_mod
        self.pc_con_stat = pc_con_stat
        self.pc_con_mod = pc_con_mod
        self.pc_cha_stat = pc_cha_stat
        self.pc_cha_mod = pc_cha_mod

    def print_race(self):
        return 'Race:{}'.format(self.pc_race)
        #return self.pc_race

    def print_class(self):
        return 'Class:{}'.format(self.pc_class)
        #return self.pc_class

    def print_subrace(self):
        return 'Sub Race:{}'.format(self.pc_subrace)
        #return self.pc_subrace

    def print_subclass(self):
        return 'Sub Class:{}'.format(self.pc_subclass)
        #return self.pc_subclass

    # Prints the initiative bonus for the character
    def print_init(self):
        #return 'Initiative Bonus:{}'.format(self.pc_dex_mod)
        return self.pc_dex_mod

    # Prints the maximum health + the constitution mod
    def print_health(self):
        if self.pc_class == 'Barbarian':
            maximum_health = "12 + Constitution Modifier!"
            #return 'Maximum Health:{}'.format(maximum_health)
            return maximum_health
        elif self.pc_class == 'Bard':
            maximum_health = "8 + Constitution Modifier!"
            #return 'Maximum Health:{}'.format(maximum_health)
            return maximum_health
        elif self.pc_class == 'Cleric':
            maximum_health = "8 + Constitution Modifier!"
            #return 'Maximum Health:{}'.format(maximum_health)
            return maximum_health
        elif self.pc_class == 'Druid':
            maximum_health = "8 + Constitution Modifier!"
            #return 'Maximum Health:{}'.format(maximum_health)
            return maximum_health
        elif self.pc_class == 'Fighter':
            maximum_health = "10 + Constitution Modifier!"
            #return 'Maximum Health:{}'.format(maximum_health)
            return maximum_health
        elif self.pc_class == 'Monk':
            maximum_health = "8 + Constitution Modifier!"
            #return 'Maximum Health:{}'.format(maximum_health)
            return maximum_health
        elif self.pc_class == 'Paladin':
            maximum_health = "10 + Constitution Modifier!"
            #return 'Maximum Health:{}'.format(maximum_health)
            return maximum_health
        elif self.pc_class == 'Ranger':
            maximum_health = "10 + Constitution Modifier!"
            #return 'Maximum Health:{}'.format(maximum_health)
            return maximum_health
        elif self.pc_class == 'Rogue':
            maximum_health = "8 + Constitution Modifier!"
            #return 'Maximum Health:{}'.format(maximum_health)
            return maximum_health
        elif self.pc_class == 'Sorcerer':
            maximum_health = "6 + Constitution Modifier!"
            #return 'Maximum Health:{}'.format(maximum_health)
            return maximum_health
        elif self.pc_class == 'Warlock':
            maximum_health = "8 + Constitution Modifier!"
            #return 'Maximum Health:{}'.format(maximum_health)
            return maximum_health
        elif self.pc_class == 'Wizard':
            maximum_health = "6 + Constitution Modifier!"
            #return 'Maximum Health:{}'.format(maximum_health)
            return maximum_health

    # Prints the base movement speed
    def print_movement(self):
        if self.pc_race == 'Dwarf':
            #return 'Base Movement Speed:{}'.format(25)
            return 25
        elif self.pc_race == 'Halfling':
            #return 'Base Movement Speed:{}'.format(25)
            return 25
        elif self.pc_race == 'Gnome':
            #return 'Base Movement Speed:{}'.format(25)
            return 25
        else:
            #return 'Base Movement Speed:{}'.format(30)
            return 30

    def print_background(self):
        #return 'Background:{}'.format(self.pc_background)
        return self.pc_background

    def print_alignment(self):
        #return 'Alignment:{}'.format(self.pc_alignment)
        return self.pc_alignment

    # Prints age of character
    def print_age(self):
        if self.pc_race == 'Dwarf':
            #return 'Age:{}'.format(random.randint(50, 350))
            return random.randint(50, 350)
        elif self.pc_race == 'Elf':
            #return 'Age:{}'.format(random.randint(100, 750))
            return random.randint(100, 750)
        elif self.pc_race == 'Halfling':
            #return 'Age:{}'.format(random.randint(20, 250))
            return random.randint(20, 250)
        elif self.pc_race == 'Human':
            #return 'Age:{}'.format(random.randint(18, 80))
            return random.randint(18, 80)
        elif self.pc_race == 'Dragonborn':
            #return 'Age:{}'.format(random.randint(15, 80))
            return random.randint(15, 80)
        elif self.pc_race == 'Gnome':
            #return 'Age:{}'.format(random.randint(40, 500))
            return random.randint(40, 500)
        elif self.pc_race == 'Half-Elf':
            #return 'Age:{}'.format(random.randint(20, 180))
            return random.randint(20, 180)
        elif self.pc_race == 'Half-Orc':
            #return 'Age:{}'.format(random.randint(14, 75))
            return random.randint(14, 75)
        elif self.pc_race == 'Tiefling':
            #return 'Age:{}'.format(random.randint(18, 90))
            return random.randint(18, 90)

    def print_str_stat(self):
        return '{} (Modifier of:{})'.format(self.pc_str_stat, self.pc_str_mod)

    def print_dex_stat(self):
        return '{} (Modifier of:{})'.format(self.pc_dex_stat, self.pc_dex_mod)

    def print_wis_stat(self):
        return '{} (Modifier of:{})'.format(self.pc_wis_stat, self.pc_wis_mod)

    def print_int_stat(self):
        return '{} (Modifier of:{})'.format(self.pc_int_stat, self.pc_int_mod)

    def print_con_stat(self):
        return '{} (Modifier of:{})'.format(self.pc_con_stat, self.pc_con_mod)

    def print_cha_stat(self):
        return '{} (Modifier of:{})'.format(self.pc_cha_stat, self.pc_cha_mod)

    def display(self):
        output = {'Race:': self.pc_race,'Subrace:': self.pc_subrace, 'Class:': self.pc_class,
                  'Subclass:': self.pc_subclass, 'Age:': self.print_age(), 'Health': self.print_health(),
                  'Background': self.print_background(), 'Alignment:': self.print_alignment(),
                  'Movement:': self.print_movement(), 'Initiative Bonus:': self.print_init(),
                  'Strength:': self.print_str_stat(), 'Dexterity': self.print_dex_stat(),
                  'Wisdom:': self.print_wis_stat(), 'Intelligence:': self.print_int_stat(),
                  'Constitution:': self.print_con_stat(), 'Charisma:': self.print_cha_stat()}
        return output


def roll_for_stats():  # Rolls four 6 sided dice and drops the lowest number rolled
    rolls = []
    for roll in range(4):
        x = random.randint(1, 6)
        rolls.append(x)

    del rolls[rolls.index(min(rolls))]  # deletes the lowest number
    stat = sum(rolls)  # totals the remaining 3 numbers
    return stat


# Return a sub race from the appropriate list
def sub_race_generator(s_r):
    if s_r == 'Dwarf':
        return random.choice(Dwarf_Sub_Race_Choices)
    elif s_r == 'Elf':
        return random.choice(Elf_Sub_Race_Choices)
    elif s_r == 'Gnome':
        return random.choice(Gnome_Sub_Race_Choices)
    else:
        return 'N/A'


# Return a sub class from the appropriate list
def sub_class_generator(s_c):
    if s_c == 'Barbarian':
        return random.choice(Barbarian_Sub_Class_Choices)
    elif s_c == 'Bard':
        return random.choice(Bard_Sub_Class_Choices)
    elif s_c == 'Cleric':
        return random.choice(Cleric_Sub_Class_Choices)
    elif s_c == 'Druid':
        return random.choice(Druid_Sub_Class_Choices)
    elif s_c == 'Fighter':
        return random.choice(Fighter_Sub_Class_Choices)
    elif s_c == 'Monk':
        return random.choice(Monk_Sub_Class_Choices)
    elif s_c == 'Paladin':
        return random.choice(Paladin_Sub_Class_Choices)
    elif s_c == 'Ranger':
        return random.choice(Ranger_Sub_Class_Choices)
    elif s_c == 'Rogue':
        return random.choice(Rogue_Sub_Class_Choices)
    elif s_c == 'Sorcerer':
        return random.choice(Sorcerer_Sub_Class_Choices)
    elif s_c == 'Warlock':
        return random.choice(Warlock_Sub_Class_Choices)
    elif s_c == 'Wizard':
        return random.choice(Wizard_Sub_Class_Choices)


# Return a background from the list
def background():
    return random.choice(Backgrounds)


# Return an alignment from the list
def alignment():
    return random.choice(Alignments)


# Return the modifier for the characters strength stat
def strength_mod(s_r, str_r):
    # Race Bonuses

    if s_r == 'Human':
        str_bonus = 1
        strength = str(int(str_r) + int(str_bonus))
    elif s_r == 'Dwarf':
        str_bonus = 2
        strength = str(int(str_r) + int(str_bonus))
    elif s_r == 'Dragonborn':
        str_bonus = 2
        strength = str(int(str_r) + int(str_bonus))
    elif s_r == 'Half-Orc':
        str_bonus = 2
        strength = str(int(str_r) + int(str_bonus))
    else:
        strength = str_r

    # Modifier Code
    for key in Ability_Score_Modifiers:
        if key == strength:
            return Ability_Score_Modifiers[strength]
        else:
            pass


def new_strength(s_r, str_r):
    if s_r == 'Human':
        str_bonus = 1
        strength = str(int(str_r) + int(str_bonus))
    elif s_r == 'Dwarf':
        str_bonus = 2
        strength = str(int(str_r) + int(str_bonus))
    elif s_r == 'Dragonborn':
        str_bonus = 2
        strength = str(int(str_r) + int(str_bonus))
    elif s_r == 'Half-Orc':
        str_bonus = 2
        strength = str(int(str_r) + int(str_bonus))
    else:
        strength = str_r

    return strength


# Return the modifier for the characters dexterity stat
def dexterity_mod(s_r, dex_r):
    # RaceBonuses

    if s_r == 'Elf':
        dex_bonus = 2
        dexterity = str(int(dex_r) + int(dex_bonus))
    elif s_r == 'Halfling':
        dex_bonus = 2
        dexterity = str(int(dex_r) + int(dex_bonus))
    elif s_r == 'Human':
        dex_bonus = 1
        dexterity = str(int(dex_r) + int(dex_bonus))
    else:
        dexterity = dex_r

    # Modifier Code

    for key in Ability_Score_Modifiers:
        if key == dexterity:
            return Ability_Score_Modifiers[dexterity]
        else:
            pass


def new_dexterity(s_r, dex_r):
    if s_r == 'Elf':
        dex_bonus = 2
        dexterity = str(int(dex_r) + int(dex_bonus))
    elif s_r == 'Halfling':
        dex_bonus = 2
        dexterity = str(int(dex_r) + int(dex_bonus))
    elif s_r == 'Human':
        dex_bonus = 1
        dexterity = str(int(dex_r) + int(dex_bonus))
    else:
        dexterity = dex_r

    return dexterity


# Return the modifier for the characters wisdom stat
def wisdom_mod(s_r, wis_r):
    # RaceBonuses

    if s_r == 'Human':
        wis_bonus = 1
        wisdom = str(int(wis_r) + int(wis_bonus))
    else:
        wisdom = wis_r

    # Modifier Code

    for key in Ability_Score_Modifiers:
        if key == wisdom:
            return Ability_Score_Modifiers[wisdom]
        else:
            pass


def new_wisdom(s_r, wis_r):
    if s_r == 'Human':
        wis_bonus = 1
        wisdom = str(int(wis_r) + int(wis_bonus))
    else:
        wisdom = wis_r

    return wisdom


# Return the modifier for the characters intelligence stat
def intelligence_mod(s_r, int_r):
    # RaceBonuses

    if s_r == 'Gnome':
        int_bonus = 2
        intelligence = str(int(int_r) + int(int_bonus))
    elif s_r == 'Tiefling':
        int_bonus = 1
        intelligence = str(int(int_r) + int(int_bonus))
    elif s_r == 'Human':
        int_bonus = 1
        intelligence = str(int(int_r) + int(int_bonus))
    else:
        intelligence = int_r

    # Modifier Code

    for key in Ability_Score_Modifiers:
        if key == intelligence:
            return Ability_Score_Modifiers[intelligence]
        else:
            pass


def new_intelligence(s_r, int_r):
    if s_r == 'Gnome':
        int_bonus = 2
        intelligence = str(int(int_r) + int(int_bonus))
    elif s_r == 'Tiefling':
        int_bonus = 1
        intelligence = str(int(int_r) + int(int_bonus))
    elif s_r == 'Human':
        int_bonus = 1
        intelligence = str(int(int_r) + int(int_bonus))
    else:
        intelligence = int_r

    return intelligence


# Return the modifier for the characters constitution stat
def constitution_mod(s_r, con_r):
    # RaceBonuses

    if s_r == 'Half-Orc':
        con_bonus = 1
        constitution = str(int(con_r) + int(con_bonus))
    elif s_r == 'Human':
        con_bonus = 1
        constitution = str(int(con_r) + int(con_bonus))
    else:
        constitution = con_r

    # Modifier Code

    for key in Ability_Score_Modifiers:
        if key == constitution:
            return Ability_Score_Modifiers[constitution]
        else:
            pass


def new_constitution(s_r, con_r):
    if s_r == 'Half-Orc':
        con_bonus = 1
        constitution = str(int(con_r) + int(con_bonus))
    elif s_r == 'Human':
        con_bonus = 1
        constitution = str(int(con_r) + int(con_bonus))
    else:
        constitution = con_r

    return constitution


# Return the modifier for the characters charisma stat
def charisma_mod(s_r, cha_r):
    # RaceBonuses

    if s_r == 'Dragonborn':
        cha_bonus = 1
        charisma = str(int(cha_r) + int(cha_bonus))
    elif s_r == 'Half-Elf':
        cha_bonus = 2
        charisma = str(int(cha_r) + int(cha_bonus))
    elif s_r == 'Tiefling':
        cha_bonus = 2
        charisma = str(int(cha_r) + int(cha_bonus))
    elif s_r == 'Human':
        cha_bonus = 1
        charisma = str(int(cha_r) + int(cha_bonus))
    else:
        charisma = cha_r
    
    # Modifier Code
    for key in Ability_Score_Modifiers:
        if key == charisma:
            return Ability_Score_Modifiers[charisma]
        else:
            pass


def new_charisma(s_r, cha_r):
    if s_r == 'Dragonborn':
        cha_bonus = 1
        charisma = str(int(cha_r) + int(cha_bonus))
    elif s_r == 'Half-Elf':
        cha_bonus = 2
        charisma = str(int(cha_r) + int(cha_bonus))
    elif s_r == 'Tiefling':
        cha_bonus = 2
        charisma = str(int(cha_r) + int(cha_bonus))
    elif s_r == 'Human':
        cha_bonus = 1
        charisma = str(int(cha_r) + int(cha_bonus))
    else:
        charisma = cha_r

    return charisma


def create_pc(s_r, s_c):
    str_roll = str(roll_for_stats())
    dex_roll = str(roll_for_stats())
    wis_roll = str(roll_for_stats())
    int_roll = str(roll_for_stats())
    con_roll = str(roll_for_stats())
    cha_roll = str(roll_for_stats())

    my_player = Pc(s_r, s_c, sub_race_generator(s_r),
                   sub_class_generator(s_c), background(), alignment(),
                   new_strength(s_r, str_roll), strength_mod(s_r, str_roll),
                   new_dexterity(s_c, dex_roll), dexterity_mod(s_c, dex_roll),
                   new_wisdom(s_r, wis_roll), wisdom_mod(s_r, wis_roll),
                   new_intelligence(s_r, int_roll), intelligence_mod(s_r, int_roll),
                   new_constitution(s_r, con_roll), constitution_mod(s_r, con_roll),
                   new_charisma(s_r, cha_roll), charisma_mod(s_r, cha_roll))

    return my_player.display() 

def main():
    user = True
    while user:
        user_choice = input('Would you like to create a character?')
        if user_choice == 'y':
            user = True
            selected_race = random.choice(Race_Choices)
            selected_class = random.choice(Class_Choices)
            print (json.dumps(create_pc(selected_race, selected_class), indent = 2))
        else:
            user = False


if __name__ == '__main__':
    main()
