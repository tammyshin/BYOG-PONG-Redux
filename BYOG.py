# Imports
import pygame, sys, os, time, random

# Force Static position of screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Global Variables
WIDTH = HEIGHT = 920

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 0, 138)
LIGHT_PINK = (225, 200, 230)

TIMER = 0

FPS = 60


# Game Class
class Game:
   def __init__(self):
       self.clock = pygame.time.Clock()
       self.new_round = False
       self.intro = True
       self.rules = False
       self.play = True
       self.outro = False
       self.is_power_up = False
       self.theme = self.choose_theme()

   # Chooses the theme for the game
   def choose_theme(self):
       theme = random.randrange(1, 5)

       return theme

   # Changes the images/appearances of objects depending on the theme
   def set_theme(self, ball, left_paddle, right_paddle, top_paddle, bottom_paddle, left_score, right_score):
       # Flower Themed
       if self.theme == 1:
           # Background
           background = pygame.image.load("flower/flower-field.png").convert()
           background = pygame.transform.scale(background, (WIDTH, HEIGHT))

           # Ball
           ball.image = pygame.image.load("flower/flower-ball.png").convert_alpha()
           ball.image = pygame.transform.scale(ball.image, (ball.width, ball.height))

           # Left Paddle
           left_paddle.image = pygame.image.load("flower/wood-left.png").convert_alpha()
           left_paddle.image = pygame.transform.scale(left_paddle.image, (left_paddle.width, left_paddle.height))

           # Right Paddle
           right_paddle.image = pygame.image.load("flower/wood-right.png").convert_alpha()
           right_paddle.image = pygame.transform.scale(right_paddle.image, (right_paddle.width, right_paddle.height))

           # Top Paddle
           top_paddle.image = pygame.image.load("flower/wood-top.png").convert_alpha()
           top_paddle.image = pygame.transform.scale(top_paddle.image, (top_paddle.width, top_paddle.height))

           # Bottom Paddle
           bottom_paddle.image = pygame.image.load("flower/wood-bottom.png").convert_alpha()
           bottom_paddle.image = pygame.transform.scale(bottom_paddle.image, (bottom_paddle.width, bottom_paddle.height))

           # Left Score
           left_score.image = left_score.font.render(str(left_paddle.score), 1, BLACK)

           # Right Score
           right_score.image = right_score.font.render(str(left_paddle.score), 1, BLACK)

           return background

       # Space Themed
       elif self.theme == 2:
           # Background
           background = pygame.image.load("space/space.png").convert()
           background = pygame.transform.scale(background, (WIDTH, HEIGHT))

           # Ball
           ball.image = pygame.image.load("space/star-ball.png").convert_alpha()
           ball.image = pygame.transform.scale(ball.image, (ball.width, ball.height))

           # Left Paddle
           left_paddle.image = pygame.image.load("space/space-left.png").convert_alpha()
           left_paddle.image = pygame.transform.scale(left_paddle.image, (left_paddle.width, left_paddle.height))

           # Right Paddle
           right_paddle.image = pygame.image.load("space/space-right.png").convert_alpha()
           right_paddle.image = pygame.transform.scale(right_paddle.image, (right_paddle.width, right_paddle.height))

           # Top Paddle
           top_paddle.image = pygame.image.load("space/Space-top.png").convert_alpha()
           top_paddle.image = pygame.transform.scale(top_paddle.image, (top_paddle.width, top_paddle.height))

           # Bottom Paddle
           bottom_paddle.image = pygame.image.load("space/Space-bottom.png").convert_alpha()
           bottom_paddle.image = pygame.transform.scale(bottom_paddle.image, (bottom_paddle.width, bottom_paddle.height))

           # Left Score
           left_score.image = left_score.font.render(str(left_paddle.score), 1, WHITE)

           # Right Score
           right_score.image = right_score.font.render(str(left_paddle.score), 1, WHITE)

           return background

       # Desert Themed
       elif self.theme == 3:
           # Background
           background = pygame.image.load("desert/desert.png").convert()
           background = pygame.transform.scale(background, (WIDTH, HEIGHT))

           # Ball
           ball.image = pygame.image.load("desert/cactus-ball.png").convert_alpha()
           ball.image = pygame.transform.scale(ball.image, (ball.width, ball.height))

           # Left Paddle
           left_paddle.image = pygame.image.load("desert/cactus-left.png").convert_alpha()
           left_paddle.image = pygame.transform.scale(left_paddle.image, (left_paddle.width, left_paddle.height))

           # Right Paddle
           right_paddle.image = pygame.image.load("desert/cactus-right.png").convert_alpha()
           right_paddle.image = pygame.transform.scale(right_paddle.image, (right_paddle.width, right_paddle.height))

           # Top Paddle
           top_paddle.image = pygame.image.load("desert/cactus-top.png").convert_alpha()
           top_paddle.image = pygame.transform.scale(top_paddle.image, (top_paddle.width, top_paddle.height))

           # Bottom Paddle
           bottom_paddle.image = pygame.image.load("desert/cactus-bottom.png").convert_alpha()
           bottom_paddle.image = pygame.transform.scale(bottom_paddle.image, (bottom_paddle.width, bottom_paddle.height))

           # Left Score
           left_score.image = left_score.font.render(str(left_paddle.score), 1, WHITE)

           # Right Score
           right_score.image = right_score.font.render(str(left_paddle.score), 1, WHITE)

           return background

       # Snow Themed
       elif self.theme == 4:
           # Background
           background = pygame.image.load("snow/snow-field.png").convert()
           background = pygame.transform.scale(background, (WIDTH, HEIGHT))

           # Ball
           ball.image = pygame.image.load("snow/snowball.png").convert_alpha()
           ball.image = pygame.transform.scale(ball.image, (ball.width, ball.height))

           # Left Paddle
           left_paddle.image = pygame.image.load("snow/snow-wood-left.png").convert_alpha()
           left_paddle.image = pygame.transform.scale(left_paddle.image, (left_paddle.width, left_paddle.height))

           # Right Paddle
           right_paddle.image = pygame.image.load("snow/snow-wood-right.png").convert_alpha()
           right_paddle.image = pygame.transform.scale(right_paddle.image, (right_paddle.width, right_paddle.height))

           # Top Paddle
           top_paddle.image = pygame.image.load("snow/snow-wood-top.png").convert_alpha()
           top_paddle.image = pygame.transform.scale(top_paddle.image, (top_paddle.width, top_paddle.height))

           # Bottom Paddle
           bottom_paddle.image = pygame.image.load("snow/snow-wood-bottom.png").convert_alpha()
           bottom_paddle.image = pygame.transform.scale(bottom_paddle.image, (bottom_paddle.width, bottom_paddle.height))

           # Left Score
           left_score.image = left_score.font.render(str(left_paddle.score), 1, BLACK)

           # Right Score
           right_score.image = right_score.font.render(str(left_paddle.score), 1, BLACK)

           return background

   # General updates for game
   def update(self, left_paddle, right_paddle, top_paddle, bottom_paddle, left_score, right_score, ball, screen):
       # Increments Left Team Score
       if ball.rect.left > WIDTH or ball.rect.bottom < 0:
           left_paddle.score = left_paddle.score + 1
           if self.theme == 2 or self.theme == 3:
               left_score.image = left_score.font.render(str(left_paddle.score), 1, WHITE)
           else:
               left_score.image = left_score.font.render(str(left_paddle.score), 1, BLACK)
           self.reset(left_paddle, right_paddle, top_paddle, bottom_paddle, ball)
           if left_paddle.score != 3:
               self.countdown(screen)

       # Increments Right Team Score
       elif ball.rect.right < 0 or ball.rect.top > HEIGHT:
           right_paddle.score = right_paddle.score + 1
           if self.theme == 2 or self.theme == 3:
               right_score.image = right_score.font.render(str(right_paddle.score), 1, WHITE)
           else:
               right_score.image = right_score.font.render(str(right_paddle.score), 1, BLACK)
           self.reset(left_paddle, right_paddle, top_paddle, bottom_paddle, ball)
           if right_paddle.score != 3:
               self.countdown(screen)

       # Game ends once a score is equal to 3
       if left_paddle.score == 3 or right_paddle.score == 3:
           time.sleep(2)
           self.play = False
           self.outro = True

   # Resets the ball and paddles at the start of new rounds
   def reset(self, left_paddle, right_paddle, top_paddle, bottom_paddle, ball):
       # Resets Ball Position
       ball.rect.centerx = WIDTH / 2
       ball.rect.centery = HEIGHT / 2

       # Resets Left Paddle Position
       left_paddle.rect.x = 40
       left_paddle.rect.centery = HEIGHT / 2

       # Resets Right Paddle Position
       right_paddle.rect.x = WIDTH - 80
       right_paddle.rect.centery = HEIGHT / 2

       # Resets Top Paddle Position
       top_paddle.rect.x = (WIDTH / 2) - 80
       top_paddle.rect.y = 40

       # Resets Bottom Paddle Position
       bottom_paddle.rect.x = (WIDTH / 2) - 80
       bottom_paddle.rect.y = HEIGHT - 80

       self.new_round = True

   # Countdown in between rounds
   def countdown(self, screen):
       is_countdown = True  # For while loop
       number = 4  # The number that will appear on screen
       cd = Text(150, str(number), 0, 409, WHITE)
       while is_countdown:  # Number on screen decreases by 1 and position of text changes
           number -= 1
           cd.image = cd.font.render(str(number), 1, WHITE)
           cd.rect.centerx += 210
           screen.blit(cd.image, cd.rect)
           time.sleep(1)

           # Limits Frames per iteration of while loop
           self.clock.tick(FPS)

           # Writes to main surface
           pygame.display.flip()

           if number == 0:
               is_countdown = False

   # Makes text blink
   def blink(self, object, screen):
       if pygame.time.get_ticks() % 1000 < 500:
           screen.blit(object.image, object.rect)


# Paddle Class
class Paddle:
   def __init__(self, width, height, xpos, ypos):
       self.width = width
       self.height = height
       self.speed = 8
       self.rect = pygame.Rect(xpos, ypos, self.width, self.height)
       self.up = False
       self.down = False
       self.left = False
       self.right = False
       self.score = 0
       self.power_up = False

   # Controls movement of paddle
   def update(self):
       # Paddle moves up
       if self.up:
           self.rect.y = self.rect.y - self.speed
       # Paddle moves down
       elif self.down:
           self.rect.y = self.rect.y + self.speed
       # Paddle moves left
       elif self.left:
           self.rect.x = self.rect.x - self.speed
       # Paddle moves right
       elif self.right:
           self.rect.x = self.rect.x + self.speed

       # Paddle cannot go off the top of the screen
       if self.rect.y < 40:
           self.rect.y = 40
       # Paddle cannot go off the bottom of the screen
       elif self.rect.bottom > HEIGHT - 80:
           self.rect.bottom = HEIGHT - 80
       # Paddle cannot go off the left side of the screen
       elif self.rect.left < 40:
           self.rect.left = 40
       # Paddle cannot go off the right side of the screen
       elif self.rect.right > WIDTH - 80:
           self.rect.right = WIDTH - 80


# Ball Class
class Ball:
   def __init__(self):
       self.width = 40
       self.height = 40
       self.speed = [3, 3]
       self.rect = pygame.Rect(WIDTH / 2, HEIGHT / 2 - (self.height / 2), self.width, self.height)
       self.num_bounce = 0  # The number of times the ball has bounced off a paddle

   # General updates for ball
   def update(self, left_paddle, right_paddle, top_paddle, bottom_paddle):

       # Bouncing off top paddle
       if self.rect.top > top_paddle.rect.bottom - 5 and self.rect.top < top_paddle.rect.bottom + 5 and self.rect.left < top_paddle.rect.right and self.rect.right > top_paddle.rect.left:
           self.speed[1] = -self.speed[1]
           self.num_bounce += 1

       # Bouncing off bottom paddle
       if self.rect.bottom < bottom_paddle.rect.top + 5 and self.rect.bottom > bottom_paddle.rect.top - 5 and self.rect.left < bottom_paddle.rect.right and self.rect.right > bottom_paddle.rect.left:
           self.speed[1] = -self.speed[1]
           self.num_bounce += 1

       # Bouncing off left paddle
       if self.rect.left > left_paddle.rect.right - 5 and self.rect.left < left_paddle.rect.right + 5 and self.rect.bottom > left_paddle.rect.top and self.rect.top < left_paddle.rect.bottom:
           self.speed[0] = -self.speed[0]
           self.num_bounce += 1

       # Bouncing off right paddle
       if self.rect.right < right_paddle.rect.left + 5 and self.rect.right > right_paddle.rect.left - 5 and self.rect.bottom > right_paddle.rect.top and self.rect.top < right_paddle.rect.bottom:
           self.speed[0] = -self.speed[0]
           self.num_bounce += 1

       # Keeps the ball moving
       self.rect = self.rect.move(self.speed)


# Power-Up Class
class PowerUp(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.width = 30
       self.height = 30
       self.speed = [3, -3]
       self.image = pygame.image.load("power-up/power-up.png").convert_alpha()
       self.image = pygame.transform.scale(self.image, (self.width, self.width))
       self.rect = self.image.get_rect()
       self.rect = pygame.Rect((WIDTH / 2) - self.width, HEIGHT - 165, self.width, self.height)
       self.type = self.type()  # The type of ability
       self.max_bounce = 10  # The number of times the ball will bounce before power-up disappears
       self.paddle_team = self.team()  # Team that the power-up buffs

   # Selects which team to buff
   def team(self):
       num = random.randrange(1, 11)
       # If num is an even number, then buff left + bottom team
       if num % 2 != 0:
           team = "left"
       # If num is an odd number, then buff right + top team
       else:
           team = "right"

       return team

   # Selects which ability it will have
   def type(self):
       # There are 4 different types, so random selection from numbers 1-4
       type = random.randrange(1, 5)
       return type

   # A brief description of the power-up depending on its type
   def detail(self, run, screen):
       detail = "N/A"
       timer = 1
       if self.type == 1:
           detail = "Team with power-up's paddle size increases, opponent's decrease"

       elif self.type == 2:
           detail = "Ball moves slower for team with power-up and faster for opponent"

       elif self.type == 3:
           detail = "Opponent paddle speed decreases"

       elif self.type == 4:
           detail = "Next power-up's maximum bounce is increased to 16"

       # The text of the description
       description = Text(40, detail, WIDTH / 2, HEIGHT / 2, WHITE)
       description.rect.centerx = description.rect.centery = WIDTH / 2

       # Display the text for a couple of seconds
       while timer % 150 != 0:
           screen.blit(description.image, description.rect)
           timer += 1
           run.clock.tick(FPS)
           pygame.display.flip()

   # Gives the ability to the power-up
   def ability(self, left_paddle, right_paddle, top_paddle, bottom_paddle, ball, run):
       # Causes the player's paddle to increase and the opponent's to decrease in size by 1/3.
       if self.type == 1:
           if self.paddle_team == "left":
               # Increase left and bottom paddle size by 1/3
               left_paddle.width = left_paddle.width * (4/3)
               left_paddle.height = left_paddle.height * (4/3)

               top_paddle.width = top_paddle.width * (4/3)
               top_paddle.height = top_paddle.height * (4/3)

               # Decrease right and top paddle size by 1/3
               right_paddle.width = right_paddle.width * (2/3)
               right_paddle.height = right_paddle.height * (2/3)

               bottom_paddle.width = bottom_paddle.width * (2/3)
               bottom_paddle.height = bottom_paddle.height * (2/3)

           else:
               # Increase right and top paddle size by 1/3
               right_paddle.width = right_paddle.width * (4/3)
               right_paddle.height = right_paddle.height * (4/3)

               bottom_paddle.width = bottom_paddle.width * (4/3)
               bottom_paddle.height = bottom_paddle.height * (4/3)

               # Decrease left and bottom paddle size by 1/3
               left_paddle.width = left_paddle.width * (2/3)
               left_paddle.height = left_paddle.height * (2/3)

               top_paddle.width = top_paddle.width * (2/3)
               top_paddle.height = top_paddle.height * (2/3)

       # Makes the ball slower for the player and faster for the opponent.
       elif self.type == 2:
           if self.paddle_team == "left":
               # When the ball is located on the left half of the screen, increase the speed of the ball
               if ball.rect.left >= WIDTH / 2:
                   ball.speed[0] += 2
                   ball.speed[1] += 2
               # When the ball is located on the right half of the screen, decrease the speed of the ball
               elif ball.rect.right < WIDTH / 2:
                   ball.speed[0] -= 2
                   ball.speed[1] -= 2

           else:
               # When the ball is located in the right half of the screen, increase the speed of ball
               if ball.rect.right <= WIDTH / 2:
                   ball.speed[0] += 2
                   ball.speed[1] += 2
               # When the ball is located in the left half other screen, decrease the speed of the ball
               elif ball.rect.left >= WIDTH / 2:
                   ball.speed[0] -= 2
                   ball.speed[1] -= 2

       # Causes the opponent's paddle to decrease in speed by 1/3.
       elif self.type == 3:
           # Decrease the right and top paddle speed
           if self.paddle_team == "left":
               right_paddle.speed -= 3
               bottom_paddle.speed -= 3

           # Decrease the left and bottom paddle speed
           else:
               left_paddle.speed -= 3
               top_paddle.speed -= 3

       # Causes the effects of the next Power Up that is eaten by the player to last 16 hits instead of 10.
       elif self.type == 4:
           # Increases maximum bounce to 16 and deletes power-up
           self.max_bounce = 16
           self.rect.x = 5000
           self.kill()
           run.is_power_up = False

       # Changes image of buffed team's paddle
       if self.type != 4:
           self.paddle_image(run, left_paddle, right_paddle, top_paddle, bottom_paddle)

   # Changes image of buffed team's paddle
   def paddle_image(self, run, left_paddle, right_paddle, top_paddle, bottom_paddle):
       if self.paddle_team == "left":
           # Flower Theme
           if run.theme == 1:
               left_paddle.image = pygame.image.load("flower/wood-power-left.png").convert_alpha()
               left_paddle.image = pygame.transform.scale(left_paddle.image, (left_paddle.width, left_paddle.height))

               top_paddle.image = pygame.image.load("flower/wood-power-top.png").convert_alpha()
               top_paddle.image = pygame.transform.scale(top_paddle.image, (top_paddle.width, top_paddle.height))

           # Space Theme
           elif run.theme == 2:
               left_paddle.image = pygame.image.load("space/space-power-left.png").convert_alpha()
               left_paddle.image = pygame.transform.scale(left_paddle.image, (left_paddle.width, left_paddle.height))

               top_paddle.image = pygame.image.load("space/space-power-top.png").convert_alpha()
               top_paddle.image = pygame.transform.scale(top_paddle.image, (top_paddle.width, top_paddle.height))

           # Desert Theme
           elif run.theme == 3:
               left_paddle.image = pygame.image.load("desert/cactus-power-left.png").convert_alpha()
               left_paddle.image = pygame.transform.scale(left_paddle.image, (left_paddle.width, left_paddle.height))

               top_paddle.image = pygame.image.load("desert/cactus-power-top.png").convert_alpha()
               top_paddle.image = pygame.transform.scale(top_paddle.image, (top_paddle.width, top_paddle.height))

           # Snow Theme
           elif run.theme == 4:
               left_paddle.image = pygame.image.load("snow/snow-wood-power-left.png").convert_alpha()
               left_paddle.image = pygame.transform.scale(left_paddle.image, (left_paddle.width, left_paddle.height))

               top_paddle.image = pygame.image.load("snow/snow-wood-power-top.png").convert_alpha()
               top_paddle.image = pygame.transform.scale(top_paddle.image, (top_paddle.width, top_paddle.height))



       if self.paddle_team == "right":
           # Flower Theme
           if run.theme == 1:
               right_paddle.image = pygame.image.load("flower/wood-power-right.png").convert_alpha()
               right_paddle.image = pygame.transform.scale(right_paddle.image, (right_paddle.width, right_paddle.height))

               bottom_paddle.image = pygame.image.load("flower/wood-power-bottom.png").convert_alpha()
               bottom_paddle.image = pygame.transform.scale(bottom_paddle.image, (bottom_paddle.width, bottom_paddle.height))

           # Space Theme
           elif run.theme == 2:
               right_paddle.image = pygame.image.load("space/space-power-right.png").convert_alpha()
               right_paddle.image = pygame.transform.scale(right_paddle.image, (right_paddle.width, right_paddle.height))

               bottom_paddle.image = pygame.image.load("space/space-power-bottom.png").convert_alpha()
               bottom_paddle.image = pygame.transform.scale(bottom_paddle.image, (bottom_paddle.width, bottom_paddle.height))

           # Desert Theme
           elif run.theme == 3:
               right_paddle.image = pygame.image.load("desert/cactus-power-right.png").convert_alpha()
               right_paddle.image = pygame.transform.scale(right_paddle.image, (right_paddle.width, right_paddle.height))

               bottom_paddle.image = pygame.image.load("desert/cactus-power-bottom.png").convert_alpha()
               bottom_paddle.image = pygame.transform.scale(bottom_paddle.image,
                                                            (bottom_paddle.width, bottom_paddle.height))

           # Snow Theme
           elif run.theme == 4:
               right_paddle.image = pygame.image.load("snow/snow-wood-power-right.png").convert_alpha()
               right_paddle.image = pygame.transform.scale(right_paddle.image, (right_paddle.width, right_paddle.height))

               bottom_paddle.image = pygame.image.load("snow/snow-wood-power-bottom.png").convert_alpha()
               bottom_paddle.image = pygame.transform.scale(bottom_paddle.image, (bottom_paddle.width, bottom_paddle.height))

   # General updates for power-up
   def update(self, left_paddle, right_paddle, top_paddle, bottom_paddle, ball, run):
       # Motion of the Power Up
       self.rect = self.rect.move(self.speed)

       if TIMER % 30 == 0:
           self.speed[0] = -self.speed[0]

       if self.rect.top < 150 or self.rect.bottom > HEIGHT - 100:
           self.speed[1] = -self.speed[1]

       # Remove Power Up
       if ball.num_bounce >= self.max_bounce and self.type != 4:
           self.reset(left_paddle, right_paddle, top_paddle, bottom_paddle, ball, run)
           self.rect.x = 5000
           self.kill()
           ball.num_bounce = 0
           run.is_power_up = False

   # Resetting after power-up expires
   def reset(self, left_paddle, right_paddle, top_paddle, bottom_paddle, ball, run):
       # Reset Paddle Width/Height
       if self.type == 1:
           left_paddle.width = 60
           left_paddle.height = 180

           right_paddle.width = 60
           right_paddle.height = 180

           top_paddle.width = 180
           top_paddle.height = 60

           bottom_paddle.width = 180
           bottom_paddle.height = 60

       # Reset Ball Speed
       elif self.type == 2:
           ball.speed = [3, 3]

       # Reset Paddle Speed
       elif self.type == 3:
           left_paddle.speed = 8
           right_paddle.speed = 8
           top_paddle.speed = 8
           bottom_paddle.speed = 8

       # Reset Max Number of Bounces
       self.max_bounce = 10

       # Reset Paddle Images
       # Flower Themed
       if run.theme == 1:
           # Left Paddle
           left_paddle.image = pygame.image.load("flower/wood-left.png").convert_alpha()
           left_paddle.image = pygame.transform.scale(left_paddle.image, (left_paddle.width, left_paddle.height))

           # Right Paddle
           right_paddle.image = pygame.image.load("flower/wood-right.png").convert_alpha()
           right_paddle.image = pygame.transform.scale(right_paddle.image, (right_paddle.width, right_paddle.height))

           # Top Paddle
           top_paddle.image = pygame.image.load("flower/wood-top.png").convert_alpha()
           top_paddle.image = pygame.transform.scale(top_paddle.image, (top_paddle.width, top_paddle.height))

           # Bottom Paddle
           bottom_paddle.image = pygame.image.load("flower/wood-bottom.png").convert_alpha()
           bottom_paddle.image = pygame.transform.scale(bottom_paddle.image, (bottom_paddle.width, bottom_paddle.height))

       # Space Themed
       elif run.theme == 2:
           # Left Paddle
           left_paddle.image = pygame.image.load("space/space-left.png").convert_alpha()
           left_paddle.image = pygame.transform.scale(left_paddle.image, (left_paddle.width, left_paddle.height))

           # Right Paddle
           right_paddle.image = pygame.image.load("space/space-right.png").convert_alpha()
           right_paddle.image = pygame.transform.scale(right_paddle.image, (right_paddle.width, right_paddle.height))

           # Top Paddle
           top_paddle.image = pygame.image.load("space/Space-top.png").convert_alpha()
           top_paddle.image = pygame.transform.scale(top_paddle.image, (top_paddle.width, top_paddle.height))

           # Bottom Paddle
           bottom_paddle.image = pygame.image.load("space/Space-bottom.png").convert_alpha()
           bottom_paddle.image = pygame.transform.scale(bottom_paddle.image, (bottom_paddle.width, bottom_paddle.height))

       # Desert Themed
       elif run.theme == 3:
           # Left Paddle
           left_paddle.image = pygame.image.load("desert/cactus-left.png").convert_alpha()
           left_paddle.image = pygame.transform.scale(left_paddle.image, (left_paddle.width, left_paddle.height))

           # Right Paddle
           right_paddle.image = pygame.image.load("desert/cactus-right.png").convert_alpha()
           right_paddle.image = pygame.transform.scale(right_paddle.image, (right_paddle.width, right_paddle.height))

           # Top Paddle
           top_paddle.image = pygame.image.load("desert/cactus-top.png").convert_alpha()
           top_paddle.image = pygame.transform.scale(top_paddle.image, (top_paddle.width, top_paddle.height))

           # Bottom Paddle
           bottom_paddle.image = pygame.image.load("desert/cactus-bottom.png").convert_alpha()
           bottom_paddle.image = pygame.transform.scale(bottom_paddle.image, (bottom_paddle.width, bottom_paddle.height))

       # Snow Themed
       elif run.theme == 4:
           # Left Paddle
           left_paddle.image = pygame.image.load("snow/snow-wood-left.png").convert_alpha()
           left_paddle.image = pygame.transform.scale(left_paddle.image, (left_paddle.width, left_paddle.height))

           # Right Paddle
           right_paddle.image = pygame.image.load("snow/snow-wood-right.png").convert_alpha()
           right_paddle.image = pygame.transform.scale(right_paddle.image, (right_paddle.width, right_paddle.height))

           # Top Paddle
           top_paddle.image = pygame.image.load("snow/snow-wood-top.png").convert_alpha()
           top_paddle.image = pygame.transform.scale(top_paddle.image, (top_paddle.width, top_paddle.height))

           # Bottom Paddle
           bottom_paddle.image = pygame.image.load("snow/snow-wood-bottom.png").convert_alpha()
           bottom_paddle.image = pygame.transform.scale(bottom_paddle.image, (bottom_paddle.width, bottom_paddle.height))


# Text Class
class Text:
   def __init__(self, size, text, xpos, ypos, color):
       self.font = pygame.font.SysFont("Britannic Bold", size)
       self.image = self.font.render(text, 1, color)
       self.rect = self.image.get_rect()
       self.rect = self.rect.move(xpos, ypos)


def main():
   # Global Variables
   global WIDTH, HEIGHT, WHITE, BLACK, TIMER, FPS

   # Screen
   screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)

   # Pygame
   pygame.init()
   pygame.display.set_caption("Pong")

   # Create Objects
   # Paddles
   left_paddle = Paddle(60, 180, 40, (HEIGHT / 2) - 80)  # left_paddle.width * 2
   right_paddle = Paddle(60, 180, WIDTH - 80, (HEIGHT / 2) - 80)  # WIDTH - (right_paddle.width * 3)
   top_paddle = Paddle(180, 60, (WIDTH / 2) - 80, 40)
   bottom_paddle = Paddle(180, 60, (WIDTH / 2) - 80, HEIGHT - 80)

   # Ball
   ball = Ball()

   # Texts
   title = Text(150, "Pong", WIDTH / 2.75, HEIGHT / 3, BLACK)
   subtitle = Text(100, "--Click Here--", WIDTH / 3.75, HEIGHT / 2, BLACK)

   left_score = Text(90, str(left_paddle.score), WIDTH / 4, HEIGHT / 10, WHITE)
   right_score = Text(90, str(right_paddle.score), WIDTH - (WIDTH / 4), HEIGHT / 10, WHITE)

   # Game Class - "run"
   run = Game()

   # Create Groups
   power_up_group = pygame.sprite.Group()

   # Images
   # Intro Background
   intro_back = pygame.image.load("backgrounds/intro-background.png").convert()
   intro_back = pygame.transform.scale(intro_back, (WIDTH, HEIGHT))

   # Rules Background / Ending Background
   rules_end_bg = pygame.image.load("backgrounds/rules and ending background.png").convert()
   rules_end_bg = pygame.transform.scale(rules_end_bg, (WIDTH, HEIGHT))

   # Background during the game (theme)
   background = run.set_theme(ball, left_paddle, right_paddle, top_paddle, bottom_paddle, left_score, right_score)

   # Game Loop
   while True:
       # Intro
       while run.intro:
           # Checks if window exit button pressed
           for event in pygame.event.get():
               # Exits game
               if event.type == pygame.QUIT:
                   sys.exit()
               # Starts game
               if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_SPACE] != 0:
                   run.intro = False
               # Goes to rule screen
               if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                   run.rules = True
                   # Rules
                   while run.rules:
                       # Checks if window exit button pressed
                       for event in pygame.event.get():
                           # Exits game
                           if event.type == pygame.QUIT:
                               sys.exit()
                           # Goes back to intro screen
                           if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                               run.rules = False

                       # Creating Objects
                       # Title
                       rules_header = Text(100, "RULES",  WIDTH / 2, 60, BLACK)

                       # Objective
                       objective1 = Text(45, "Objective: Hit the ball around with paddles.", WIDTH / 2, 140, BLACK)
                       objective2 = Text(45, "Get the ball to fall off the map on the",  WIDTH / 2, 180, BLACK)
                       objective3 = Text(45, "opponent's side. Prevent the ball from falling",  WIDTH / 2, 220, BLACK)
                       objective4 = Text(45, "off the map on your team's side.", WIDTH / 2, 260, BLACK)

                       # Controls
                       control_header = Text(80, "CONTROLS",  WIDTH / 2, 320, BLACK)
                       left_control = Text(45, "Left Paddle: W + S",  WIDTH / 2, 380, BLACK)
                       right_control = Text(45, "Right Paddle: Top Arrow + Bottom Arrow",  WIDTH / 2, 410, BLACK)
                       top_control = Text(45, "Top Paddle: F + G",  WIDTH / 2, 440, BLACK)
                       bottom_control = Text(45, "Bottom Paddle: J + K",  WIDTH / 2, 470, BLACK)

                       # Power-up info
                       power_up_header = Text(80, "POWER UPS",  WIDTH / 2, 530, BLACK)
                       power_up1 = Text(45, "Power-ups spawn periodically.",  WIDTH / 2, 600, BLACK)
                       power_up2 = Text(45, "It randomly chooses which team receives",  WIDTH / 2, 630, BLACK)
                       power_up3 = Text(45, "the power-up. The team that has glowing",  WIDTH / 2, 660, BLACK)
                       power_up4 = Text(45, "paddles has the power-up. Typically, power-ups",  WIDTH / 2, 690, BLACK)
                       power_up5 = Text(45, "last until the ball has bounced 10 times.", WIDTH / 2, 720, BLACK)

                       # "Go back"
                       go_back = Text(70, "Press [esc] to go back!", WIDTH / 2, 800, BLACK)

                       # Reposition
                       # Title
                       rules_header.rect.centerx = WIDTH / 2

                       # Objective
                       objective1.rect.centerx = WIDTH / 2
                       objective2.rect.centerx = WIDTH / 2
                       objective3.rect.centerx = WIDTH / 2
                       objective4.rect.centerx = WIDTH / 2

                       # Controls
                       control_header.rect.centerx = WIDTH / 2
                       left_control.rect.centerx = WIDTH / 2
                       right_control.rect.centerx = WIDTH / 2
                       top_control.rect.centerx = WIDTH / 2
                       bottom_control.rect.centerx = WIDTH / 2

                       # Power-up info
                       power_up_header.rect.centerx = WIDTH / 2
                       power_up1.rect.centerx = WIDTH / 2
                       power_up2.rect.centerx = WIDTH / 2
                       power_up3.rect.centerx = WIDTH / 2
                       power_up4.rect.centerx = WIDTH / 2
                       power_up5.rect.centerx = WIDTH / 2

                       # "Go-back"
                       go_back.rect.centerx = WIDTH / 2

                       # Blitting
                       # Background
                       screen.fill(WHITE)
                       screen.blit(rules_end_bg, rules_end_bg.get_rect())

                       # Title + Objective
                       screen.blit(rules_header.image, rules_header.rect)
                       screen.blit(objective1.image, objective1.rect)
                       screen.blit(objective2.image, objective2.rect)
                       screen.blit(objective3.image, objective3.rect)
                       screen.blit(objective4.image, objective4.rect)

                       # Controls
                       screen.blit(control_header.image, control_header.rect)
                       screen.blit(left_control.image, left_control.rect)
                       screen.blit(right_control.image, right_control.rect)
                       screen.blit(top_control.image, top_control.rect)
                       screen.blit(bottom_control.image, bottom_control.rect)

                       # Power-up info
                       screen.blit(power_up_header.image, power_up_header.rect)
                       screen.blit(power_up1.image, power_up1.rect)
                       screen.blit(power_up2.image, power_up2.rect)
                       screen.blit(power_up3.image, power_up3.rect)
                       screen.blit(power_up4.image, power_up4.rect)
                       screen.blit(power_up5.image, power_up5.rect)

                       # "Go-back"
                       run.blink(go_back, screen)

                       # Limits frames per iteration of while loop
                       run.clock.tick(FPS)

                       # Writes to main surface
                       pygame.display.flip()

           # Creating Objects
           rules_text = Text(70, "Press [R] to view the rules!", 146, HEIGHT * 4/5, BLACK)

           # Blitting
           # Background
           screen.blit(intro_back, intro_back.get_rect())

           # Text
           screen.blit(title.image, title.rect)
           run.blink(subtitle, screen)
           screen.blit(rules_text.image, rules_text.rect)

           # Limits frames per iteration of while loop
           run.clock.tick(FPS)

           # Writes to main surface
           pygame.display.flip()

       # Game
       while run.play:
           # Checks if window exit button pressed
           for event in pygame.event.get():
               # Exits game
               if event.type == pygame.QUIT:
                   sys.exit()

               # Keystrokes
               # When a key is pressed down
               if event.type == pygame.KEYDOWN:
                   # Exits game
                   if event.key == pygame.K_ESCAPE:
                       pygame.quit()
                       sys.exit()
                   # While W is pressed -> left paddle goes up
                   if event.key == pygame.K_w:
                       left_paddle.up = True
                       left_paddle.down = False
                   # While S is pressed -> left paddle goes down
                   elif event.key == pygame.K_s:
                       left_paddle.up = False
                       left_paddle.down = True
                   # While UP is pressed -> right paddle goes up
                   elif event.key == pygame.K_UP:
                       right_paddle.up = True
                       right_paddle.down = False
                   # While DOWN is pressed -> right paddle goes down
                   elif event.key == pygame.K_DOWN:
                       right_paddle.up = False
                       right_paddle.down = True
                   # While F is pressed -> top paddle goes left
                   elif event.key == pygame.K_f:
                       top_paddle.left = True
                       top_paddle.right = False
                   # While G is pressed -> top paddle goes right
                   elif event.key == pygame.K_g:
                       top_paddle.left = False
                       top_paddle.right = True
                   # While J is pressed -> bottom paddle goes left
                   elif event.key == pygame.K_j:
                       bottom_paddle.left = True
                       bottom_paddle.right = False
                   # While K is pressed -> bottom paddle goes right
                   elif event.key == pygame.K_k:
                       bottom_paddle.left = False
                       bottom_paddle.right = True

               # When a key is released, paddle stops moving
               elif event.type == pygame.KEYUP:
                   if event.key == pygame.K_w:
                       left_paddle.up = False
                       left_paddle.down = False
                   elif event.key == pygame.K_s:
                       left_paddle.up = False
                       left_paddle.down = False
                   elif event.key == pygame.K_UP:
                       right_paddle.up = False
                       right_paddle.down = False
                   elif event.key == pygame.K_DOWN:
                       right_paddle.up = False
                       right_paddle.down = False
                   elif event.key == pygame.K_f:
                       top_paddle.left = False
                       top_paddle.right = False
                   elif event.key == pygame.K_g:
                       top_paddle.left = False
                       top_paddle.right = False
                   elif event.key == pygame.K_j:
                       bottom_paddle.left = False
                       bottom_paddle.right = False
                   elif event.key == pygame.K_k:
                       bottom_paddle.left = False
                       bottom_paddle.right = False

           # Timer increases by 1 every iteration
           TIMER += 1

           # Spawns a power-up one at a time and at a certain time
           if TIMER % 200 == 0 and run.is_power_up == False:
               power_up = PowerUp()
               power_up.ability(left_paddle, right_paddle, top_paddle, bottom_paddle, ball, run)
               power_up.detail(run, screen)
               power_up_group.add(power_up)
               run.is_power_up = True

           # Update
           # Paddles
           left_paddle.update()
           right_paddle.update()
           top_paddle.update()
           bottom_paddle.update()

           # Ball
           ball.update(left_paddle, right_paddle, top_paddle, bottom_paddle)

           # Game
           run.update(left_paddle, right_paddle, top_paddle, bottom_paddle, left_score, right_score, ball, screen)

           # Power-up
           power_up_group.update(left_paddle, right_paddle, top_paddle, bottom_paddle, ball, run)

           # Blitting
           # Background
           screen.blit(background, background.get_rect())

           # Paddles
           screen.blit(left_paddle.image, left_paddle.rect)
           screen.blit(right_paddle.image, right_paddle.rect)
           screen.blit(top_paddle.image, top_paddle.rect)
           screen.blit(bottom_paddle.image, bottom_paddle.rect)

           # Ball
           screen.blit(ball.image, ball.rect)

           # Power-up
           power_up_group.draw(screen)

           # Scores
           screen.blit(left_score.image, left_score.rect)
           screen.blit(right_score.image, right_score.rect)

           # Limits frames per iteration of while loop
           run.clock.tick(FPS)

           # Writes to main surface
           pygame.display.flip()

       # Outro
       while run.outro:
           # Checks if window exit button pressed
           for event in pygame.event.get():
               # Exits game
               if event.type == pygame.QUIT:
                   sys.exit()
               # Restarts game
               if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_SPACE] != 0:
                   # Resets score
                   left_paddle.score = 0
                   right_paddle.score = 0

                   # Chooses new theme and sets background
                   run.theme = run.choose_theme()
                   background = run.set_theme(ball, left_paddle, right_paddle, top_paddle, bottom_paddle, left_score, right_score)

                   # Resets Power-ups
                   if run.is_power_up:
                       power_up.reset(left_paddle, right_paddle, top_paddle, bottom_paddle, ball, run)
                       power_up.kill()
                   run.is_power_up = False

                   # Goes back to game
                   run.outro = False
                   run.play = True

           # Blitting
           # Background
           screen.blit(rules_end_bg, rules_end_bg.get_rect())

           # Winner Text
           winner_text = Text(100, "WINNERS:", WIDTH / 2, HEIGHT / 3, BLACK)
           winner_text.rect.centerx = WIDTH / 2
           screen.blit(winner_text.image, winner_text.rect)
           if left_paddle.score == 3:  # If left and bottom paddle won
               winner = Text(90, "Left & Top Players!", WIDTH / 2, 380, BLACK)
               winner.rect.centerx = WIDTH / 2
               screen.blit(winner.image, winner.rect)

           elif right_paddle.score == 3:  # If right and top paddle won
               winner = Text(90, "Right & Bottom Players!", WIDTH / 2, 380, BLACK)
               winner.rect.centerx = WIDTH / 2
               screen.blit(winner.image, winner.rect)

           # Restart text
           restart_text = Text(100, "--Click to Restart--", WIDTH / 2, 570, BLACK)
           restart_text.rect.centerx = WIDTH / 2
           run.blink(restart_text, screen)

           # Limits frames per iteration of while loop
           run.clock.tick(FPS)

           # Writes to main surface
           pygame.display.flip()


if __name__ == "__main__":
   main()
