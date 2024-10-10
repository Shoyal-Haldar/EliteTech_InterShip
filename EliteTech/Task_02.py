    # random story gen.
import random as R

def strygen():    
    name = ["Amina", "Zaid", "Fatima", "Omar", "Hiroshi", "Sakura", "Yuki", "Akira", "Aarav", "Priya", "Raj", "Meera", "Oliver", "Charlotte", "Henry", "Emily"]
    surnames = ["Al-Farsi", "Hassan", "Khan", "Saeed", "Takahashi", "Tanaka", "Yamamoto", "Saito", "Patel", "Sharma", "Singh", "Mehta", "Smith", "Johnson", "Brown", "Taylor"]
    gender_ch = ["male","female"]
    roles = ["killer", "doctor", "scientist", "storyteller", "knight", "wizard", "dragon", "thief", "archer", "detective", "robot", "pirate", "vampire", "werewolf", "alien", "assassin", "king", "queen", "priest", "sorcerer", "necromancer", "spy", "warrior", "hunter", "merchant", "engineer", "guard", "healer", "jester", "general", "explorer"]
    place = ["Starlight Academy", "Evergreen College", "Saint Mercy Hospital", "Helix Research Center", "Ironclad Defense Base", "Arcane Hollow Academy", "Shadowfall Bunker", "Cursed Willow Mansion", "Nebula-7 Space Station", "Whispering Pines Camp", "Sunken Echo Temple", "Obsidian Labs", "Crimsonspire Castle", "Abyssal Reef City", "Echoes of Industry Factory", "Ravenwood Village", "Black Sails Pirate Ship", "Isle of Lost Souls", "Chrono Gate Museum", "Silver Trail Station", "Eagle’s Nest Hideout", "Celestial Gateway Airport", "Quantum Labs", "Dragonclaw Dungeon", "Titan Academy"]
    place2 = ['in a dark forest', 'on a distant planet', 'in a haunted house', 'in a magical kingdom', 'at the bottom of the sea']
    # actions = ['found a mysterious artifact', 'fought a monster', 'discovered a hidden treasure', 'created a time machine', 'saved the world', 'learned a powerful spell', 'broke an ancient curse', 'traveled to an alternate dimension', 'befriended a magical creature', 'unlocked the secrets of the universe', 'invented a groundbreaking technology', 'solved an unsolvable mystery', 'escaped from a hidden labyrinth', 'won a battle against an evil sorcerer', 'found a portal to another world', 'discovered a new superpower', 'rescued a kingdom from peril', 'defeated an army of robots', 'uncovered a government conspiracy', 'prevented a catastrophic event', 'made peace with a rival kingdom']

    Name = f"{R.choice(name)} {R.choice(surnames)}"
    gender = R.choice(gender_ch)
    age = R.randint(13,70)
    role_ = R.choice(roles)
    pls = R.choice(place)
    pls2 = R.choice(place2)
    
    actions = [
    f"One day, while exploring an ancient ruin, {Name} discovered a mysterious artifact that granted them the ability to speak to animals, leading them on a quest to save a trapped creature in the forest.",
    f"During a stormy night, {Name} found themselves face-to-face with a dragon that had been terrorizing their village. With courage and wit, they devised a plan to outsmart the beast and bring peace to their home.",
    f"As a skilled {role_}, {Name} created a time machine in their lab. As they stepped through the portal, they found themselves in the midst of a historical battle, where they had to choose between changing history or preserving it.",
    f"{Name}, a wandering {role_}, stumbled upon a magical kingdom hidden in the clouds. There, they met a princess who needed help to defeat an evil sorcerer threatening to plunge her realm into darkness.",
    f"In the heart of a bustling city, {Name}, a brilliant {role_}, uncovered a government conspiracy while investigating a series of unexplained disappearances. They raced against time to expose the truth and save innocent lives.",
    f"{Name}, a talented {role_}, broke an ancient curse that had plagued their family for generations. With newfound powers, they embarked on a journey to reclaim their family's honor and restore their legacy.",
    f"{Name}, a clever {role_}, stumbled upon a hidden treasure map that led them deep into an enchanted forest. Along the way, they encountered magical creatures and learned that not all treasure is gold.",
    f"{Name}, a young {role_}, discovered a portal to another world while hunting in the woods. Drawn into a fantastical realm, they had to use their skills to navigate through challenges and find their way back home.",
    f"{Name}, a courageous {role_}, fought against a fearsome army of robots that threatened to enslave humanity. With the help of their friends, they devised a daring plan to defeat the machines and save their world.",
    f"{Name}, a curious {role_}, unlocked the secrets of an ancient temple and awakened a sleeping guardian. Together, they embarked on an adventure to protect the land from a rising darkness."
]
    
    act = R.choice(actions)
    
    if  (gender == "male"):
        inpositon = "He" 
    else:
        inpositon = "She"
    
    The_Story = f"{Name} {age} old {gender} {role_} in {pls}.\nOne day, {Name} was {pls2}, {inpositon} {act}"

    print("Here the Ramdomly Genrated Story.....\n")
    print(The_Story)
strygen()