from src.setting import *


def createstage0(map):
    """
    reset all obstacle then add new obstacle to stage 0
    then draw this stage
    """
    stage = 0
    map.reset()

    for i in range(10):
        map.addflyfloor(500+45*i, floor-50-100, stage)
    for i in range(10):
        map.addflyfloor(950+45*i, floor-50-200, stage)
    for i in range(3):
        map.addhedgehog(400+75*i, floor-50, stage, 200)
    map.setobstacle()


def createstage1(map):
    """
    reset all obstacle then add new obstacle to stage 1
    then draw this stage
    """
    stage = 1
    map.reset()

    for i in range(2):
        map.addflyfloor(45*i, floor-50-200, stage)
    for i in range(14):
        map.addspike(125+75*i, floor-50, stage)
    for i in range(2):
        map.addflyfloor(300+45*i, floor-50-300, stage)
    for i in range(2):
        map.addflyfloor(600+45*i, floor-50-400, stage)
    for i in range(2):
        map.addflyfloor(900+45*i, floor-50-500, stage)
    for i in range(2):
        map.addflyfloor(1200+45*i, floor-50-400, stage)
    map.setobstacle()


def createstage2(map):
    """
    reset all obstacle then add new obstacle to stage 1
    then draw this stage
    """
    stage = 2
    map.reset()

    for i in range(14):
        map.addspike(125+75*i, floor-50, stage)
    map.addflyfloor(200, floor-50-100, stage)
    map.addflyfloor(400, floor-50-250, stage)
    map.addflyfloor(600, floor-50-400, stage)
    map.addflyfloor(800, floor-50-550, stage)
    map.setobstacle()


def createstage3(map):
    """
    reset all obstacle then add new obstacle to stage 1
    then draw this stage
    """
    stage = 3
    map.reset()

    for i in range(14):
        map.addspike(125+75*i, floor-50, stage)
    for i in range(4):
        map.addflyfloor(200+45*i, floor-50-150, stage)
    map.addhedgehog(200, floor-50-200, stage, 180)
    for i in range(4):
        map.addflyfloor(500+45*i, floor-50-150, stage)
    map.addhedgehog(500, floor-50-200, stage, 180)
    for i in range(4):
        map.addflyfloor(800+45*i, floor-50-150, stage)
    map.addhedgehog(800, floor-50-200, stage, 180)
    map.setobstacle()


def createstage4(map):
    """
    reset all obstacle then add new obstacle to stage 1
    then draw this stage
    """
    stage = 4
    map.reset()

    map.addhedgehog(150, floor-50, stage, 200)
    map.addhedgehog(350, floor-50, stage, 200)
    map.addhedgehog(550, floor-50, stage, 200)
    map.addhedgehog(750, floor-50, stage, 200)
    map.addhedgehog(950, floor-50, stage, 200)
    map.setobstacle()


def createstage5(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 5
    map.reset()

    for i in range(14):
        map.addspike(125+75*i, floor-50, stage)
    for i in range(16):
        map.addflyfloor(335+45*i, floor-50-300, stage)
    for i in range(5):
        map.addflyfloor(50+50*(i+1), floor-50-100-50*i, stage)
    for i in range(4):
        map.addflyfloor(1005+50*(i+1), floor-50-250+50*i, stage)
    map.addjellyfish(200, floor-50-400, stage, 300)
    map.addjellyfish(400, floor-50-600, stage, 500)
    map.addjellyfish(600, floor-50-500, stage, 400)
    map.addjellyfish(800, floor-50-300, stage, 200)
    map.addjellyfish(1000, floor-50-500, stage, 200)
    map.setobstacle()


def createstage6(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 6
    map.reset()

    map.addjumpboost(600, floor-50-200, stage)
    map.addtext("Reset Jump?", 570, floor-50-230, 24)
    map.setobstacle()


def createstage7(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 7
    map.reset()

    map.addjumpboost(250, floor-50-200, stage)
    map.addjumpboost(550, floor-50-200, stage)
    map.addjumpboost(850, floor-50-200, stage)
    for i in range(13):
        map.addspike(175+75*i, floor-50, stage)
    map.setobstacle()


def createstage8(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 8
    map.reset()

    map.addjellyfish(200, floor-50-400, stage, 400)
    map.addjellyfish(350, floor-50-500, stage, 500)
    map.addjellyfish(500, floor-50-100, stage, 100)
    map.addjellyfish(650, floor-50-200, stage, 200)
    map.addjellyfish(800, floor-50-400, stage, 400)
    map.addjellyfish(950, floor-50-200, stage, 200)
    map.addjellyfish(1100, floor-50-600, stage, 600)
    map.setobstacle()


def createstage9(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 9
    map.reset()

    for i in range(13):
        map.addspike(200+71.25*i, floor-50, stage)
    for i in range(20):
        map.addflyfloor(200+45*i, floor-200, stage)
    map.addhedgehog(400, floor-50-200, stage, 200)
    map.addhedgehog(700, floor-50-200, stage, 200)

    for i in range(20):
        map.addflyfloor(200+45*i, floor-400, stage)
    map.addhedgehog(250, floor-50-400, stage, 200)
    map.addhedgehog(550, floor-50-400, stage, 200)
    map.addhedgehog(850, floor-50-400, stage, 200)

    for i in range(20):
        map.addflyfloor(200+45*i, floor-600, stage)
    for i in range(13):
        map.addspike(200+71.25*i, floor-600+15, stage, 180)
    map.setobstacle()


def createstage10(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 10
    map.reset()

    map.addjumpboost(200, floor-50-200, stage)
    for i in range(13):
        map.addspike(200+71.25*i, floor-50, stage)
    for i in range(4):
        map.addflyfloor(500+45*i, floor-50-150, stage)
    map.addhedgehog(500, floor-50-200, stage, 180)
    for i in range(4):
        map.addflyfloor(800+45*i, floor-50-150, stage)
    map.addhedgehog(800, floor-50-200, stage, 180)
    map.addtext("Checkpoint", 10, floor-50-40, 25)
    map.setobstacle()


def createstage11(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 11
    map.reset()

    for i in range(13):
        map.addspike(200+71.25*i, floor-50, stage)
    map.addjumpboost(200, floor-50-200, stage)
    map.addjellyfish(350, floor-50-350, stage, 200)
    map.addjumpboost(500, floor-50-200, stage)
    map.addjellyfish(650, floor-50-350, stage, 200)
    map.addjumpboost(800, floor-50-200, stage)
    map.addjellyfish(950, floor-50-350, stage, 200)
    map.setobstacle()


def createstage12(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 12
    map.reset()

    for i in range(3):
        map.addspike(200+60*i, floor-50, stage)

    for i in range(3):
        map.addspike(450+60*i, floor-50, stage)

    for i in range(3):
        map.addspike(700+60*i, floor-50, stage)

    for i in range(3):
        map.addspike(950+60*i, floor-50, stage)
    map.setobstacle()


def createstage13(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 13
    map.reset()
    map.addhedgehog(200, floor-50, stage, 300)
    map.addhedgehog(500, floor-50, stage, 300)
    map.addhedgehog(800, floor-50, stage, 300)
    map.addjellyfish(350, floor-50-300, stage, 300)
    map.addjellyfish(650, floor-50-300, stage, 200)
    map.addjellyfish(950, floor-50-200, stage, 150)
    map.setobstacle()


def createstage14(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 14
    map.reset()
    for i in range(4):
        map.addwall(200, floor-90-85*i, stage)
    map.addwall(200, floor-390, stage, rotate=True)
    for i in range(9):
        map.addwall(400+85*i, floor-390, stage, rotate=True)
    map.addflyfloor(155, floor-195, stage)
    map.addflyfloor(155, floor-390, stage)
    for i in range(3):
        map.addhedgehog(500+200*i, floor-50-390, stage, 200)
    for i in range(12):
        map.addspike(300+75*i, floor-50, stage)
    for i in range(10):
        map.addspike(410+75*i, floor-340, stage, 180)
    map.addjumpboost(600, floor-200, stage)
    map.addjellyfish(750, floor-300, stage, 200)
    map.addjumpboost(900, floor-200, stage)
    map.setobstacle()


def createstage15(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 15
    map.reset()

    for i in range(6):
        map.addwall(100, floor-200-85*i, stage)
    for i in range(7):
        map.addwall(100+85*i, floor-600-75, stage, rotate=True)
    for i in range(6):
        map.addspike(100+85*i, floor-600-25, stage, 180)
    for i in range(6):
        map.addwall(300, floor-90-85*i, stage)
    map.addwall(350, floor-515, stage, rotate=True)
    for i in range(6):
        map.addwall(435, floor-90-85*i, stage)
    map.addflyfloor(150, floor-125, stage)
    map.addflyfloor(255, floor-280, stage)
    map.addflyfloor(150, floor-435, stage)
    for i in range(6):
        map.addwall(645, floor-200-85*i, stage)
    map.addspike(645-48, floor-475-25, stage, 270)
    map.addspike(645-48, floor-400-25, stage, 270)
    map.addspike(645-48, floor-325-25, stage, 270)
    map.addspike(490, floor-225-25, stage, 90)
    map.addspike(490, floor-150-25, stage, 90)
    map.addspike(490, floor-75-25, stage, 90)
    for i in range(7):
        map.addwall(697+85*i, 527, stage, True)
    map.addjellyfish(750, floor-120, stage, 100)
    map.addspike(900, floor-50, stage, 0)
    map.addspike(975, floor-110, stage, 180)
    map.addspike(1050, floor-50, stage, 0)
    map.addspike(1125, floor-110, stage, 180)
    map.setobstacle()


def createstage16(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 16
    map.reset()
    for i in range(5):
        map.addwall(200, floor-90-85*i, stage)
    map.addwall(200, floor-480, stage, rotate=True)
    for i in range(3):
        map.addflyfloor(155, floor-160*(i+1), stage)
    for i in range(8):
        map.addhedgehog(250+100*i, floor-50, stage, 100)
    map.addjumpboost(370, floor-400, stage)
    map.addjumpboost(670, floor-400, stage)
    map.addjumpboost(950, floor-400, stage)
    map.addjumpboost(370, floor-250, stage)
    map.addjumpboost(670, floor-250, stage)
    map.addjumpboost(950, floor-250, stage)
    for i in range(5):
        map.addwall(1090, floor-90-85*i, stage)
    map.addwall(1055, floor-480, stage, rotate=True)
    for i in range(3):
        map.addflyfloor(1145, floor-160*(i+1), stage)
    map.addjellyfish(520, floor-500, stage, 200)
    map.addjellyfish(520, floor-500, stage, 350)
    map.addjellyfish(820, floor-500, stage, 250)
    map.addjellyfish(820, floor-500, stage, 300)
    # map.addjellyfish(20, floor-600, stage, 500)
    map.setobstacle()


def createstage17(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 17
    map.reset()
    map.addhedgehog(300, floor-50, stage, 1000)
    map.addhedgehog(400, floor-50, stage, 900)

    map.addhedgehog(300, floor-50, stage, 450)
    map.addhedgehog(350, floor-50, stage, 400)

    map.addhedgehog(700, floor-50, stage, 450)
    map.addhedgehog(750, floor-50, stage, 400)
    map.setobstacle()


def createstage18(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 18
    map.reset()
    map.addwall(200, floor-90, stage)
    for i in range(3):
        map.addwall(535, floor-90-85*i, stage)
    for i in range(5):
        map.addwall(870, floor-90-85*i, stage)
    map.addspike(365, floor-50, stage)
    map.addspike(695, floor-50, stage)
    map.setobstacle()


def createstage19(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 19
    map.reset()
    map.addjumpboost(300, floor-230, stage)
    map.addwall(250, floor-90, stage)
    map.addwall(250, floor-175, stage)
    map.addflyfloor(635, floor-400, stage)
    map.addflyfloor(1100, floor-100, stage)
    for i in range(11):
        map.addspike(350+75*i, floor-50, stage)
    map.setobstacle()


def createstage20(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 20
    map.reset()
    map.addinvisible(625, floor-225, stage)
    for i in range(12):
        map.addhedgehog(400+50*i, floor-50, stage, 100)
    map.addtext("Invisible?", 610, floor-250, 24)
    map.setobstacle()


def createstage21(map):
    """
    reset all obstacle then add new obstacle to stage 0 
    then draw this stage
    """
    stage = 21
    map.reset()
    map.addtext("Congratulation, You win!", 300, floor-525, 80)
    map.addtext("SlimeAdventure 2.0", 375, floor-425, 80)
    map.addtext("Thank you for playing!", 350, floor-275, 80)
    map.addtext("See you next time!", 400, floor-200, 80)
    map.setobstacle()
