import random
import time
 
player = 0
computer = 0 
while True:
    
    x = input("Give me a sign - o/r: ")
    if x == "0": break
    elif x == "o": x = "eagle"
    elif x == "r": x = "tails"
    else:
        print("Please make the correct choice")
        print("o - eagle")
        print("r - tails")
        print("0 - game ending")
        
        
        continue
    
    y = random.choice(["eagle", "tails"])
    
    
    for i in range(0,3):
        print(3-i)
        time.sleep(1)
        
    print("Rool result: ",y)
    
    if x == y:
        player+=1
    else:
        computer+=1
        
        
    print("Total results.")
    print("User", player)
    print("computer", computer)