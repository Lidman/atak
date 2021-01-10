from personages.race import Human, Archer, Knight, Wizard
import random
gfprint("Welcome")
name = input("Enter heroes name: ")
ans = 0
money = 0
while ans not in [1,2,3]:
    ans = int(input("Choose role: 1 - Archer, 2 - Knight, 3 - Wizard: "))
    if ans == 1:
        hero = Archer(1)
    elif ans == 2:
        hero = Knight(1)
    elif ans == 3:
        hero = Wizard(1)
    else:
        print("Error! Try Again")
print("My hero is", hero)
rand1 = random.randint(1, 3)
if rand1 == 1:
    en1 = Archer(1)
elif rand1 == 2:
    en1 = Knight(1)
else:
    en1 = Wizard(1)
while en1.hp > 0 and hero.hp > 0:

    en1.hp = en1.hp - hero.attack_func()
    if en1.hp > 0:
        hero.hp -= en1.attack_func()
if en1.hp <= 0:
    print(f"You win!")
else:
    print(f"You lose!")
