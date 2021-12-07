import random
import json

Villian_Choices = ['Dragon', 'Vampire', 'Orc Warchief', 'Giant', 'Lich', 'Hydra']
Dragon_desc = "The odor of sulfur and pumice surrounds a red dragon, whose swept-back horns and spinal frill define its silhouette. Its beaked snout vents smoke at all times, and its eyes dance with flame when it is angry."
Vampire_desc = "An undead creature. Looks as it did in life, with pale skin, haunting red eyes, and a feral cast to its features. "
OrcWarchief_desc = "The war chief of an orc tribe is its strongest and most cunning member. The reign of a war chief lasts only as long as it commands the fear and respect of other tribe members, whose bloodlust must be regularly satisfied lest the chief appear weak."
Giant_desc = "Giants are humanoid creatures of great strength and size. All giants have low-light vision."
Lich_desc = "A lich is an evil humanoid spellcaster who has become undead through the use of dark magic. Their iconic ability is to cheat death by hiding their soul in an object known as a phylactery."
Hydra_desc = "The hydra is a reptilian horror with a crocodilian body and multiple heads on long, serpentine necks. Although its heads can be severed, the hydra magically regrows them in short order."
Dragon_abilites = ['Multiattack: The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.', 'Claw: Melee Weapon Attack: +17 to hit, reach 10 ft., one target. Hit: 17 (2d6 + 10) slashing damage.' , 'Tail: Melee Weapon Attack: +17 to hit, reach 20 ft., one target. Hit: 19 (2d8 + 10) bludgeoning damage.', 'Fire Breath: The dragon exhales fire in a 90-foot cone. Each creature in that area must make a DC 24 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save']
Vampire_abilities = ['Multiattack: The vampire makes three attacks, only one of which can be a bite attack.', 'Bite:  Melee Weapon Attack: +14 to hit, reach 5 ft., one willing creature, or a creature that is grappled by the vampire, incapacitated, or restrained. Hit: 16 (3d6 + 6) piercing damage plus 21 (6d6) necrotic damage.', 'Claw: Melee Weapon Attack: +14 to hit, reach 5 ft, one creature. Hit: 11 (1d10 + 6) bludgeoning damage. ', 'Vamparic Touch: Melee Spell Attack: +15 to hit, reach 10 ft., one creature. Hit: 28 (6d6 + 7) necrotic damage. The vampire regains hit points equal to half the necrotic damage dealt.', 'Charm: The vampire targets one humanoid it can see within 30 feet of it. If the target can see the vampire lord, the target must succeed on a DC 23 Wisdom saving throw against this magic or be charmed by the vampire.']
Orc_abilities = ['Multiattack: The orc makes two attacks with its greataxe or its spear.', 'Great-axe: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 15 (1d12 + 4 plus 1d8) slashing damage.', 'Spear: Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 12 (1d6 + 4 plus 1d8) piercing damage.', 'Battle Cry: Each creature of the war chief’s choice that is within 30 feet of it, can hear it, and not already affected by Battle Cry gain advantage on attack rolls until the start of the war chief’s next turn. ']
Giant_abilities = ['Multiattack: The giant makes two greatclub attacks', 'Greatclub: Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: (3d8 + 5) bludgeoning damage.', 'Rock:  Ranged Weapon Attack: +8 to hit, reach 60/240 ft., one target. Hit: (3d10 + 5) bludgeoning damage.']
Lich_abilities = ['Paralyzing Touch: Melee Spell Attack: +12 to hit, reach 5 ft., one creature. Hit: 10 (3d6) cold damage. The target must succeed on a DC 18 Constitution saving throw or be paralyzed for 1 minute. ']
Hydra_abilities = ['Multiattack: The hydra makes as many bite attacks as it has heads.', 'Bite: Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: (1d10 + 5) piercing damage.']

class villan:
    def __init__(self, the_bbeg, the_villan_desc, the_villan_str_stat, the_villan_str_mod, the_villan_dex_stat, the_villan_dex_mod, the_villan_wis_stat, the_villan_wis_mod, 
                    the_villan_int_stat, the_villan_int_mod, the_villan_con_stat, the_villan_con_mod, the_villan_cha_stat, the_villan_cha_mod, the_villan_health, the_villan_ac,
                    the_villan_speed, the_villan_abilites):
        self.the_bbeg = the_bbeg
        self.the_villan_desc = the_villan_desc
        self.the_villan_str_stat = the_villan_str_stat
        self.the_villan_str_mod = the_villan_str_mod
        self.the_villan_dex_stat = the_villan_dex_stat
        self.the_villan_dex_mod = the_villan_dex_mod
        self.the_villan_wis_stat = the_villan_wis_stat
        self.the_villan_wis_mod = the_villan_wis_mod
        self.the_villan_int_stat = the_villan_int_stat
        self.the_villan_int_mod = the_villan_int_mod
        self.the_villan_con_stat = the_villan_con_stat
        self.the_villan_con_mod = the_villan_con_mod
        self.the_villan_cha_stat = the_villan_cha_stat
        self.the_villan_cha_mod = the_villan_cha_mod
        self.the_villan_health = the_villan_health
        self.the_villan_ac = the_villan_ac
        self.the_villan_speed = the_villan_speed
        self.the_villan_abilites = the_villan_abilites
    

    def the_villan_desc(self):
        return self.the_villan_desc
    
    def the_villan_str_stat(self):
        return self.the_villan_str_stat
    
    def the_villan_str_mod(self):
        return self.the_villan_str_mod

    def the_villan_dex_stat(self):
        return self.the_villan_dex_stat
    
    def the_villan_dex_mod(self):
        return self.the_villan_dex_mod

    def the_villan_wis_stat(self):
        return self.the_villan_wis_stat
        
    def the_villan_wis_mod(self):
        return self.the_villan_wis_mod
    
    def the_villan_int_stat(self):
        return self.the_villan_int_stat
    
    def the_villan_int_mod(self):
        return self.the_villan_int_mod
    
    def the_villan_con_stat(self):
        return self.the_villan_con_stat
    
    def the_villan_con_mod(self):
        return self.the_villan_con_mod
    
    def the_villan_cha_stat(self):
        return self.the_villan_cha_stat
    
    def the_villan_cha_mod(self):
        return self.the_villan_cha_mod

    def the_villan_health(self):
        return self.the_villan_health

    def the_villan_ac(self):
        return self.the_villan_ac
    
    def the_villan_speed(self):
        return self.the_villan_speed
    
    def the_villan_abilites(self):
        return self.the_villan_abilites
    
    def print_str_stat(self):
        return '{} (Modifier of:{})'.format(self.the_villan_str_stat, self.the_villan_str_mod)

    def print_dex_stat(self):
        return '{} (Modifier of:{})'.format(self.the_villan_dex_stat, self.the_villan_dex_mod)
    
    def print_wis_stat(self):
        return '{} (Modifier of:{})'.format(self.the_villan_wis_stat, self.the_villan_wis_mod)

    def print_int_stat(self):
        return '{} (Modifier of:{})'.format(self.the_villan_int_stat, self.the_villan_int_mod)
    
    def print_con_stat(self):
        return '{} (Modifier of:{})'.format(self.the_villan_con_stat, self.the_villan_con_mod)
    
    def print_cha_stat(self):
        return '{} (Modifier of:{})'.format(self.the_villan_cha_stat, self.the_villan_cha_mod)
    
    def print_health(self):
        return self.the_villan_health
    
    def print_ac(self):
        return self.the_villan_ac
    
    def print_movement(self):
        return self.the_villan_speed

    def print_abilities(self):
        return self.the_villan_abilites
    
    def display(self):
         output = {'Name': self.the_bbeg,
             'Description': self.the_villan_desc,
             'Armor Class': self.print_ac(),
             'Health': self.print_health(),
             'Movement:': self.print_movement(),
             'Abilities': self.print_abilities(),
             'Strength:': self.print_str_stat(), 
             'Dexterity': self.print_dex_stat(),
             'Wisdom:': self.print_wis_stat(), 
             'Intelligence:': self.print_int_stat(),
             'Constitution:': self.print_con_stat(), 
             'Charisma:': self.print_cha_stat()} 
         return output
    
def villan_desc(evilGuy):
        if evilGuy == "Dragon":
            return Dragon_desc
        elif evilGuy ==  "Vampire":
            return Vampire_desc
        elif evilGuy == "Orc Warchief":
            return OrcWarchief_desc
        elif evilGuy == "Giant":
            return Giant_desc
        elif evilGuy == "Lich":
            return Lich_desc
        elif evilGuy == "Hydra":
            return Hydra_desc
        else: 
            return 0

def villan_abilities(evilGuy):
        if evilGuy == "Dragon":
            return Dragon_abilites
        elif evilGuy ==  "Vampire":
            return Vampire_abilities
        elif evilGuy == "Orc Warchief":
            return Orc_abilities
        elif evilGuy == "Giant":
            return Giant_abilities
        elif evilGuy == "Lich":
            return Lich_abilities
        elif evilGuy == "Hydra":
            return Hydra_abilities
        else: 
            return 0
    
def villan_str_stat(evilGuy):
        if evilGuy == "Dragon":
            return 30
        elif evilGuy ==  "Vampire":
            return 18
        elif evilGuy == "Orc Warchief":
            return 16
        elif evilGuy == "Giant":
            return 21
        elif evilGuy == "Lich":
            return 11
        elif evilGuy == "Hydra":
            return 20
        else: 
            return 0

def villan_str_mod(evilGuy):
        if evilGuy == "Dragon":
            return 10
        elif evilGuy ==  "Vampire":
            return 4
        elif evilGuy == "Orc Warchief":
            return 3
        elif evilGuy == "Giant":
            return 5
        elif evilGuy == "Lich":
            return 0
        elif evilGuy == "Hydra":
            return 5
        else: 
            return 0

def villan_dex_stat(evilGuy):
        if evilGuy == "Dragon":
            return 10
        elif evilGuy ==  "Vampire":
            return 18
        elif evilGuy == "Orc Warchief":
            return 12
        elif evilGuy == "Giant":
            return 10
        elif evilGuy == "Lich":
            return 16
        elif evilGuy == "Hydra":
            return 12
        else: 
            return 0

def villan_dex_mod(evilGuy):
        if evilGuy == "Dragon":
            return 0
        elif evilGuy ==  "Vampire":
            return 4
        elif evilGuy == "Orc Warchief":
            return 1
        elif evilGuy == "Giant":
            return 0
        elif evilGuy == "Lich":
            return 3
        elif evilGuy == "Hydra":
            return 1
        else: 
            return 0

def villan_wis_stat(evilGuy):
        if evilGuy == "Dragon":
            return 15
        elif evilGuy ==  "Vampire":
            return 15
        elif evilGuy == "Orc Warchief":
            return 11
        elif evilGuy == "Giant":
            return 10
        elif evilGuy == "Lich":
            return 14
        elif evilGuy == "Hydra":
            return 10
        else: 
            return 0

def villan_wis_mod(evilGuy):
        if evilGuy == "Dragon":
            return 2
        elif evilGuy ==  "Vampire":
            return 2
        elif evilGuy == "Orc Warchief":
            return 0
        elif evilGuy == "Giant":
            return 0
        elif evilGuy == "Lich":
            return 2
        elif evilGuy == "Hydra":
            return 0
        else: 
            return 0

def villan_int_stat(evilGuy):
        if evilGuy == "Dragon":
            return 18
        elif evilGuy ==  "Vampire":
            return 17
        elif evilGuy == "Orc Warchief":
            return 10
        elif evilGuy == "Giant":
            return 10
        elif evilGuy == "Lich":
            return 20
        elif evilGuy == "Hydra":
            return 10
        else: 
            return 0

def villan_int_mod(evilGuy):
        if evilGuy == "Dragon":
            return 4
        elif evilGuy ==  "Vampire":
            return 3
        elif evilGuy == "Orc Warchief":
            return 0
        elif evilGuy == "Giant":
            return 10
        elif evilGuy == "Lich":
            return 5
        elif evilGuy == "Hydra":
            return 0
        else: 
            return 0

def villan_con_stat(evilGuy):
        if evilGuy == "Dragon":
            return 29
        elif evilGuy ==  "Vampire":
            return 18
        elif evilGuy == "Orc Warchief":
            return 16
        elif evilGuy == "Giant":
            return 19
        elif evilGuy == "Lich":
            return 16
        elif evilGuy == "Hydra":
            return 20
        else: 
            return 0

def villan_con_mod(evilGuy):
        if evilGuy == "Dragon":
            return 9
        elif evilGuy ==  "Vampire":
            return 4
        elif evilGuy == "Orc Warchief":
            return 3
        elif evilGuy == "Giant":
            return 4
        elif evilGuy == "Lich":
            return 3
        elif evilGuy == "Hydra":
            return 5
        else: 
            return 0

def villan_cha_stat(evilGuy):
        if evilGuy == "Dragon":
            return 23
        elif evilGuy ==  "Vampire":
            return 18
        elif evilGuy == "Orc Warchief":
            return 10
        elif evilGuy == "Giant":
            return 10
        elif evilGuy == "Lich":
            return 16
        elif evilGuy == "Hydra":
            return 10
        else: 
            return 0

def villan_cha_mod(evilGuy):
        if evilGuy == "Dragon":
            return 6
        elif evilGuy ==  "Vampire":
            return 4
        elif evilGuy == "Orc Warchief":
            return 0
        elif evilGuy == "Giant":
            return 0
        elif evilGuy == "Lich":
            return 3
        elif evilGuy == "Hydra":
            return 0
        else: 
            return 0

def villan_health(evilGuy):
        if evilGuy == "Dragon":
            return 546
        elif evilGuy ==  "Vampire":
            return 144
        elif evilGuy == "Orc Warchief":
            return 100
        elif evilGuy == "Giant":
            return 105
        elif evilGuy == "Lich":
            return 135
        elif evilGuy == "Hydra":
            return 172
        else: 
            return 0

def villan_ac(evilGuy):
        if evilGuy == "Dragon":
            return 22
        elif evilGuy ==  "Vampire":
            return 16
        elif evilGuy == "Orc Warchief":
            return 13
        elif evilGuy == "Giant":
            return 13
        elif evilGuy == "Lich":
            return 17
        elif evilGuy == "Hydra":
            return 15
        else: 
            return 0

def villan_speed(evilGuy):
        if evilGuy == "Dragon":
            return 40
        elif evilGuy ==  "Vampire":
            return 30
        elif evilGuy == "Orc Warchief":
            return 30
        elif evilGuy == "Giant":
            return 40
        elif evilGuy == "Lich":
            return 30
        elif evilGuy == "Hydra":
            return 30
        else: 
            return 0


def create_Villan():
    bbeg = random.choice(Villian_Choices)
    myVillan = villan(bbeg, 
                villan_desc(bbeg), 
                villan_str_stat(bbeg), 
                villan_str_mod(bbeg), 
                villan_dex_stat(bbeg), 
                villan_dex_mod(bbeg), 
                villan_wis_stat(bbeg), 
                villan_wis_mod(bbeg), 
                villan_int_stat(bbeg), 
                villan_int_mod(bbeg), 
                villan_con_stat(bbeg), 
                villan_con_mod(bbeg), 
                villan_cha_stat(bbeg), 
                villan_cha_mod(bbeg), 
                villan_health(bbeg), 
                villan_ac(bbeg), 
                villan_speed(bbeg),
                villan_abilities(bbeg))
    return myVillan.display()


def main():
    print(create_Villan())
    #print (json.dumps(create_Villan(), indent = 2))
    #user = True
    #while user:
        #user_choice = input('Would you like to create a villan?')
        #if user_choice == 'y':
            #user = True
            #print (json.dumps(create_Villan(), indent = 2))
        #else:
            #user = False

if __name__ == '__main__':
    main()