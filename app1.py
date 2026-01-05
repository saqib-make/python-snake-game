import random
score = 0
while True:
    roll = random.randint(1, 6)
    print("You rolled:", roll)

    if roll == 6:
      score += 1
      print("Score:", score)
    else:
       print("Game Over")
    break 