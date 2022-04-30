import pygame


class Player():
    def __init__(self, id, x, y, width, height, color, name):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 2
        self.speed = [0, 0]
        self.name = name

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def drawname(self, win):
        font = pygame.font.Font(None, 20)
        text = font.render(str(self.name), True, "White")
        rect = text.get_rect(topleft=(self.x, self.y))
        win.blit(text, rect)

    def move(self):
        keys = pygame.key.get_pressed()
        keydirection = pygame.Vector2(0, 0)

        if keys[pygame.K_LEFT]:
            keydirection.x -= 1
        if keys[pygame.K_RIGHT]:
            keydirection.x += 1
        if keys[pygame.K_UP]:
            keydirection.y -= 1
        if keys[pygame.K_DOWN]:
            keydirection.y += 1

        if keydirection.length() == 0:
            self.speed = [0, 0]
            return
        keydirection.normalize_ip()
        self.speed = keydirection * self.vel
        self.update()

    def update(self, dt=1/60):
        self.x += self.speed[0] * 60 * dt
        self.y += self.speed[1] * 60 * dt
        self.rect = (self.x, self.y, self.width, self.height)
