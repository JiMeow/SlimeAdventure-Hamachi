import pygame


def getAllSkin():
    # set player wing img
    playerimg = ["temp"]
    # set player1 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player1.png"), (50, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    # set player2 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player2.png"), (60, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    # set player3 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player3.png"), (50, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    # set player4 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player4.png"), (50, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    # set player5 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player5.png"), (62, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))
    # set player6 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player6.png"), (50, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    # set player7 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player7.png"), (45, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    # set player8 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player8.png"), (50, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    # set player9 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player9.png"), (52, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    # set player10 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player10.png"), (50, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    # set player11 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player11.png"), (55, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    # set player12 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player12.png"), (45, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    # set player13 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player13.png"), (45, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    # set player14 img
    imgleft = pygame.transform.scale(
        pygame.image.load("JiMeow/photo/player14.png"), (45, 34))
    imgright = pygame.transform.flip(imgleft, True, False)
    playerimg.append((imgright, imgleft))

    return playerimg
