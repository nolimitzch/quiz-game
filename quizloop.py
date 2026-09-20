questions = [
    ("How many championships has lebron james won?", "4"),
    ("Who has the most 3 pointers in the NBA as of 2026?", "steph curry"),
    ("What team went 73-9 in the 2015-2016 season?", "golden state warriors"),
    ("Who scored 100 points in a single NBA game, the most in league history?", "wilt chamberlain"),
    ("Which player won the most NBA championships as a player, with 11 titles?", "bill russell"),
    ("Who was the first player to be a unanimous MVP?", "steph curry"),
    ("Who is the coach of the Golden State Warriors as of 2026?", "steve kerr"),
    ("Who currently has the most points of all time as of 2026?", "lebron james"),
    ("Who held the NBA record for most career assists in 2026?", "john stockton"),
    ("Which team went on a 28-game losing streak in the 2023-2024 NBA Season?", "detroit pistons"),
    
    ]

score = 0


for question, correct_answer in questions:
    answer = input(question + " ")
    if answer.lower().strip() == correct_answer:
        print ("Correct!")
        score += 1
    else:
        print ("Wrong, the answer was", correct_answer)
            
        
print ("You got", score, "Out of" , len(questions))

try :
    
    with open ("highscore.txt") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0
    
    
if score > high_score:
    print("New high score!")
    with open("highscore.txt", "w") as file:
        file.write(str(score))
                  
else:
    print("The highscore is", high_score)