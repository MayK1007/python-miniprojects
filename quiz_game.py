print("Welcome to my Quiz !")

playing=input("Do you want to play ? ")

if playing.lower() != "yes" :
 quit()
 
print("Okay let's play :) ") 
score = 0

answer = input("1. What does CPU stands for ? ").lower()
if answer == "central processing unit":
    print("Correct !")
    score += 1
else :
    print("Incorrect")    
 
answer = input("2. What does GPU stands for ? ").lower()
if answer == "graphics processing unit":
    print("Correct !")
    score += 1
else :
    print("Incorrect")    
 
answer = input("3. What does RAM stands for ? ").lower()
if answer == "random acess memory":
    print("Correct !")
    score += 1
else :
    print("Incorrect")    
 
answer = input("4. What does PSU stands for ? ").lower()
if answer == "power supply":
    print("Correct !")
    score += 1
else :
    print("Incorrect")    
    
print("You got "+ str(score) +" Questions Correct !")    
print("You got "+ str((score/4) * 100) +"%")   
 
 