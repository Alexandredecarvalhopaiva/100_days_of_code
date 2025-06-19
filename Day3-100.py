print("Title: The Lost Stones – The Legend of the Church of the Three Marys")
print("You are Alexa, an archaeologist searching for a legendary artifact: the Keystone.")
print("After days of travel, you've arrived at a dense forest. Two paths open up in front of you...")
decision_1 = input("To start, I'd like to know which path you prefer to take?\n 1 - [right] \n 2 - [left]\n")

ascii_art = '''
        ..        ____                                               ____
       . |       / +  \\         ||                       ||         /+ . \\
      .  |       |o x.|        =**=          _          =**=        | o x|
     .   |       |____|         ||         _( )_         ||         |____|
    .    |                      ||        /_____\        ||
   .     |                 ______________//|   |/__________________
  .      |_______^________/                | + |                  /____^_____
 .      .       _U_      /                 |___|                 //   _U_
       .         |      /_______________________________________//     |
      .         /|\\     |______________________________________|/     /|\\
     .   (=========================)     .      . (==========================)
    .    |                         |/|  .       . |                          |
   .     |                         | | .        . |                          |
  .      |_________________________|/|.         . ||------------------------||
     (=========================)  || .          . (==========================|
     |                         |/|  .           . |                          |
     |                         | | .            . |                          |
     |_________________________|/|.             . ||------------------------||
 (=========================)  || .              . (==========================)
 |                         |/|  .               . |                          |
 |                         | | .                . |                          |
 |_________________________|/|.                 . | ________________________ |
 |                        || .                  . ||   -Steve Stewart-      ||
'''
ascii_art2 = r'''
   _____ ____ _____
  /    /      \    \
/____ /_________\____\
\    \          /    /
   \  \        /  /
      \ \    / /
        \ \/ /
          \/
'''


if decision_1 == "1":
    print("You took the path to the right, but fell into a hunters' trap. 🪤")
    print("💀 Game over.")
elif decision_1 == "2":
    print("Good choice! 🌿 You found a torn piece of an ancient map indicating the location of the Keystone.")
    print("After walking a bit further, you reach a river with a very strong current...")
    decision_2 = input("The map indicates that you must cross the river to reach a sacred ruin. Do you prefer:\n1 - [wait] for the current to calm down\n2 - [swim across the river]\nEnter your choice: \n")
    if decision_2 == "2":
        print("The current was too strong! You were swept away to a waterfall and fell... 💀 Game over.")
    elif decision_2 == "1":
        print("⏳ You waited patiently. A few hours later, a dam breaks upstream and the water disappears!")
        print("You easily cross the dry riverbed. 🌉")
        print("You find yourself in front of the old Church of the Three Marys, in ruins...")
        print(ascii_art)
        decision_3 = input("Inside the church, you see three paths:\n1 - Enter the priest’s room\n2 - Go upstairs to the choir loft\n3 - Explore an open trapdoor under the altar\nEnter 1, 2, or 3: \n")
        if decision_3 == "1" or decision_3 == "2":
            print("As soon as you enter, the fragile structure of the church collapses on you. Game over.")
        elif decision_3 == "3":
            print("🔎 You descend through the trapdoor and find a secret chamber.")
            print("💎 In the center of the room, surrounded by ancient runes, lies the **Keystone** – glowing with ancestral energy.")
            print("Congratulations! You've found the first of the Lost Stones! But be careful, the structure is about to collapse...")
            print(ascii_art2)
    else:
        print("Invalid choice. Restart the game.")
else:
    print("Invalid choice. Restart the game.")
