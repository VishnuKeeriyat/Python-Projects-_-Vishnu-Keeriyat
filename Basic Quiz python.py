print("welcome to the quiz game?")

playing = input("Do you wanna play the epic quiz? ")

if playing != 'yes':
    quit()

print("Let's play :D")
score = 0
answer = input("what does CPU stand for? ")


if answer.upper() == "CENTRAL PROCESSING UNIT":
    print('correct!')
    score = score + 1
else:
    print('incorrect')

answer = input("what does RAM stand for? ")
if answer.upper() == "RANDOM ACCESS MEMORY":
    print('correct!')
    score = score + 1
else:
    print('incorrect')


answer = input("what does GPU stand for? ")
if answer.upper() == "GRAPHIC PROCESSING UNIT":
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input("what does the display device called? ")
if answer.upper() == "MONITOR":
    print('correct!')
    score += 1
else:
    print('incorrect')

print("You got " + str(score)+ "questions correct!, Conragtx :X ")
print ("You got " + str((score/4)*100)+ "%")
