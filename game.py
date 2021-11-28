import time, random, os, pygame


class Game(object):
    class Ship:
        def __init__(self, x, y, health=100):
            self.x = x
            self.y = y
            self.health = health
            self.ship_img = None
            self.laser_img = None
            self.lasers = []
            self.cool_down_counter = 0

        def draw(self, window):
            window.blit(self.ship_img, (self.x, self.y))

        def get_width(self):
            return self.ship_img.get_width()

        def get_height(self):
            return self.ship_img.get_height()

    class Player(Ship):
        def __init__(self, x, y, health=100):
            super().__init__(x, y, health)
            self.ship_img = YellowSpaceShip
            self.laser_img = YellowLaser
            self.mask = pygame.mask.from_surface(self.ship_img)
            self.max_health = health

    class Enemy(Ship):
        def __init__(self, x, y, color, health=100):
            super().__init__(x, y, health)


    def __init__(self):
        global RedSpaceShip, BlueSpaceShip, YellowSpaceShip, GreenSpaceShip, RedLaser, GreenLaser, BlueLaser, YellowLaser
        pygame.font.init()
        self.width, self.height = 800, 750
        self.window = pygame.display.set_mode((self.width, self.height))
        self.FPS = 60
        self.cLock = pygame.time.Clock()
        self.status = True
        pygame.display.set_caption("Space Invaders")
        RedSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
        GreenSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
        BlueSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
        YellowSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
        RedLaser = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
        GreenLaser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
        BlueLaser = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
        YellowLaser = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
        self.BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")),
                                         (self.width, self.height))

        self.level = 1
        self.lives = 10
        self.font = pygame.font.SysFont("comicsans", 50)
        self.ColorBlack = (255, 255, 255)
        self.level_label = self.font.render(f"Level : {self.level}", 1, self.ColorBlack)
        self.lives_label = self.font.render(f"Lives : {self.lives}", 1, self.ColorBlack)
        self.player = self.Player(300, 650)
        self.player_vel = 5
        self.game_loop()

    def game_loop(self):
        while self.status:
            self.cLock.tick(self.FPS)
            self.redraw_window()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.status = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and self.player.x - self.player_vel > 0:
                self.player.x -= self.player_vel

            if keys[pygame.K_d] and self.player.x + self.player_vel + self.player.get_width() < self.width:
                self.player.x += self.player_vel

            if keys[pygame.K_w] and self.player.y - self.player_vel > 0:
                self.player.y -= self.player_vel

            if keys[pygame.K_s] and self.player.y + self.player_vel + self.player.get_height() < self.height:
                self.player.y += self.player_vel

    def redraw_window(self):
        self.window.blit(self.BG, (0, 0))
        self.window.blit(self.lives_label, (10, 10))
        self.window.blit(self.level_label, (self.width - self.level_label.get_width() - 10, 10))
        self.player.draw(self.window)
        pygame.display.update()


if __name__ == '__main__':
    Game()
