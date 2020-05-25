import random as r
import os
import time


class Enemy:

    def __init__(self, power, shield, health):
        self.power = power
        self.shield = shield
        self.health = health


class Me:

    def __init__(self, power, shield, health, util):
        self.power = power
        self.shield = shield
        self.health = health
        self.util = util


def showEnemies(es):
    print("\t\t\tPOWER\tSHIELD\tHEALTH")
    for idx, e in enumerate(es):
        print("Enemy {}".format(idx), e.power, e.shield, e.health, sep="\t\t")
    print(30 * "*")


def showMe(m: Me):
    print("POWER\tSHIELD\tHEALTH\tUTIL")
    print(m.power, m.shield, m.health, m.util, sep="\t\t")
    print(30 * "*")


def fight(es, m: Me):
    stat_en = {}
    idx_en = []
    for i in range(10):
        stat_en[i] = True
        idx_en.append(i)
        print("{} enemy ready to fight".format(i))

    time.sleep(3)
    os.system("clear")

    counter = 1
    e_order = 0
    defeat_enemies = 0
    util_flag = 0

    while defeat_enemies != 10 and m.health > 0:
        # enemy's round
        print("{} round!\n".format(counter))
        if counter % 3 == 0:
            print("Enemy turn")
            turn = r.choice(idx_en)
            toMe(es[turn],m)
        # my round
        else:
            print("My turn")
            fi = r.choice(idx_en)
            se = r.choice(idx_en)
            print("Selected : {} {}".format(fi,se))

            if counter % 5 == 0:
                util_flag = 1

            if stat_en.get(fi):
                toEnemy(m,es[fi],util_flag)
                if es[fi].health < 0:
                    stat_en[fi] = False
                    defeat_enemies += 1
                    idx_en.remove(fi)

            else:
                print("{}. enemy defeated".format(fi))

            if stat_en.get(se):
                toEnemy(m,es[se],util_flag)
                if es[se].health < 0:
                    stat_en[se] = False
                    defeat_enemies += 1
                    idx_en.remove(se)

            else:
                print("{}. enemy defeated".format(fi))

        # print(stat_en.values(), defeat_enemies)
        counter += 1
        util_flag = 0
        e_order += 1
        if e_order == 9:
            e_order = 0
        print("My health : ",m.health)
        print("Left enemies : ", len(idx_en))
        time.sleep(2)
        os.system("clear")

    if len(idx_en) == 0:
        print("Congratulations, You Win !")
    elif m.health <= 0:
        print("You can defeated {} enemies. Please try again".format(defeat_enemies))


def toMe(e:Enemy,m:Me):
    total = e.power - m.shield
    if total < 0:
        print("Given no damage to me")
    else:
        m.health -= total
        print("Stat (toMe): damage given ({})".format(total))


def toEnemy(m:Me, e:Enemy,util_flag):
    if util_flag == 1:
        print("Util used")
        total = m.power + m.util - e.shield
    else:
        total = m.power - e.shield

    if total < 0:
        print("Given no damage to enemy")
    else:
        e.health -= total
        print("Stat (toEnemy): damage given ({})".format(total))


enemies = []

for i in range(10):
    p = r.randint(10, 70)
    s = r.randint(10, 20)
    h = r.randint(50, 100)
    enemies.append(Enemy(p, s, h))

showEnemies(enemies)

me = Me(70, 30, 100, 40)

showMe(me)

fight(enemies,me)

