# First Project Snake, Gun, Water Game.

import random
def gameWin(comp,you):
    if comp == you:
        return None
    
      # If Computer Chose "s" :-
    elif comp == "s":
        if you == 'w':
            return False
        elif you == "g":
            return True
       # If Computer Chose "w" :- 
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
        
         # If Computer Chose "g" :- 
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True
        
print("comp Turn: Snake(s) Water(w) Gun(g)?:") 
randNo = random.randint(1,3)
if randNo == 1:
    comp="s"
elif randNo ==2:
    comp="w"
elif randNo == 3:
    comp = "g"
    
you = input("Your Turn: Snake(s) Water(w) Gun(g)?:")
a = gameWin (comp,you)

print(f"Computer chose:{comp}")
print(f"You Chose:{you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")              
        
        
                
            
            
        