# Basic tutorial from Kids Can Code -https://www.youtube.com/watch?v=VO8rTszcW4s&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw
#Assets from -Kenny  (Credit "Kenney.nl" or "www.kenney.nl")
#Added feature - Options Menu
# added feature - Life Powerup
# made by Jatin Jain
import pygame
import time
import random
import os
game_width = 480
game_height = 600
fps = 60
powerup_time = 5000
Total_Score = 0
hs_file = "highScore.txt"

pygame.init()
pygame.mixer.init()
screen =pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption("Shoot!")
clock =pygame.time.Clock()

white=(255,255,255)
red =(255,0,0)
green=(0,255,0)
blue =(0,0,255)
black =(0,0,0)
yellow=(255,255,0)

game_path=os.path.dirname(__file__)
img_path =os.path.join(game_path,"images")
snd_path =os.path.join(game_path,"sound")

font_name =pygame.font.match_font('arial')
bullettype = 0
player_lifetype =0
background_type =0

def draw_text(surf,text,size,x,y):
    font =pygame.font.Font(font_name,size)
    text_surface =font.render(text,True,white)
    text_rect =text_surface.get_rect()
    text_rect.midtop =(x,y)
    surf.blit(text_surface,text_rect)

def newmob():
    m =Mob()
    all_sprites.add(m)
    mobs.add(m)

def draw_shield_bar(surf,x,y,pct):
    if pct<0:
        pct =0
    bar_length =100
    bar_height =10
    fill =(pct/100)*bar_length
    outline_rect =pygame.Rect(x,y,bar_length,bar_height)
    fill_rect =pygame.Rect(x,y,fill,bar_height)
    pygame.draw.rect(surf,green,fill_rect)
    pygame.draw.rect(surf,white,outline_rect,1)

def draw_lives(surf,x,y,lives,img):
    for i in range(lives):
        img_rect =img.get_rect()
        img_rect.x =x+ 30*i
        img_rect.y =y
        surf.blit(img,img_rect)

def button(x,y,width,height,icon,action = None):
    global bullettype
    global player_lifetype
    global background_type
    Mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > Mouse[0] > x and y+height > Mouse[1] > y:
        if action == "background_2" or action =="background_3":
            screen.blit(background_options_overlay, (x, y))
        else:
            screen.blit(background_options,(x,y))
        if click[0] ==1 and action!=None:
            if action == "player_options_img_2":
                player.image = pygame.transform.scale(player_img_2, (50, 38))
                player.image.set_colorkey(black)
                player_lifetype =1
            if action == "player_options_img_3":
                player.image = pygame.transform.scale(player_img_3, (50, 38))
                player.image.set_colorkey(black)
                player_lifetype = 2
            if action == "player_options_img_4":
                player.image = pygame.transform.scale(player_img_4, (50, 38))
                player.image.set_colorkey(black)
                player_lifetype = 3
            if action == "bullet_img_2":
                bullettype =1
            if action == "bullet_img_3":
                bullettype = 2
            if action == "bullet_img_4":
                bullettype = 3
            if action == "background_2":
                background_type = 1
            if action == "background_3":              
                background_type = 2
    else:
       screen.blit(icon, (x, y))
    pygame.display.flip()

def OptionsMenu():
    

    screen.blit(background, background_rect)
    draw_text(screen, "Options Menu", 30, game_width/2, 22)
    draw_text(screen, "Choose player", 25, game_width/2, 90)
    screen.blit(player_options_img_2,(game_width/2-130,150))
    screen.blit(player_options_img_3,(game_width/2-20,150))
    screen.blit(player_options_img_4, (game_width/2+90, 150))
    draw_text(screen,"Choose bullet",25,game_width/2,220)
    draw_text(screen, "Press Space to go back",18, game_width/2 , game_height*3.4/4)
    screen.blit(bullet_img_2, (game_width/2-110, 260))
    screen.blit(bullet_img_3, (game_width/2, 260))
    screen.blit(bullet_img_4, (game_width/2+110, 260))
    draw_text(screen,"Choose background",25,game_width/2,350)
    screen.blit(background_options_2, (game_width/2+40, 400))
    screen.blit(background_options_3, (game_width/2-110, 400))
    pygame.display.flip()

    Options =True
    while Options:
        button(game_width/2-130, 150, 40, 31,player_options_img_2, 'player_options_img_2')
        button(game_width/2-20, 150, 40, 31,player_options_img_3, 'player_options_img_3')
        button(game_width/2+90, 150, 40, 31,player_options_img_4, 'player_options_img_4')

        button(game_width/2-110, 260, 13, 57, bullet_img_2, 'bullet_img_2')
        button(game_width/2, 260, 13, 57,bullet_img_3, 'bullet_img_3')
        button(game_width/2+110, 260, 13, 57,bullet_img_4, 'bullet_img_4')

        button(game_width/2+40, 400, 80, 80,background_options_2, 'background_2')
        button(game_width/2-110, 400, 80, 80, background_options_3, 'background_3')
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Options = False
                    show_go_screen()

def show_go_screen():
    screen.blit(background,background_rect)
    draw_text(screen,"Space Shooter!",64,game_width/2,game_height/4)
    draw_text(screen,"Arrow Keys to move,Space to Fire",22,game_width/2,game_height/2)
    draw_text(screen,"Press Space to begin",18,game_width/2,game_height*3/4)
    draw_text(screen,"Press d for Options",18,game_width/2,game_height*3.2/4)
    if Total_Score > player.high_Score:
        player.high_Score =Total_Score
        with open(os.path.join(game_path,hs_file),'w') as fp:
            fp.write(str(Total_Score))
        draw_text(screen,"NEW High Score",22,game_width/2,40) 
    draw_text(screen,"High Score"+str(player.high_Score),22,game_width/2,15)
    
 
    pygame.display.flip()
    waiting =True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting =False
                elif event.key == pygame.K_d:
                    OptionsMenu()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.transform.scale(player_img,(50,38))
        self.image.set_colorkey(black)
        self.rect =self.image.get_rect()
        self.radius =21
        # pygame.draw.circle(self.image,red,self.rect.center,self.radius)
        self.rect.centerx =game_width/2
        self.rect.bottom =game_height-10
        self.speedx =0
        self.shield =100
        self.shoot_delay =250
        self.last_shot =pygame.time.get_ticks()
        self.lives =3
        self.hidden =False
        self.hide_timer =pygame.time.get_ticks()
        self.power =1
        self.power_time =pygame.time.get_ticks()
        with open(os.path.join(game_path,hs_file),'r') as f:
            try:
                self.high_Score =int(f.read())
            except:
                self.high_Score =0
    def update(self):
        #timeout for powerups
        if self.power>=2 and pygame.time.get_ticks() - self.power_time >powerup_time:
            self.power =1
            self.power_time =pygame.time.get_ticks()
        #High Score
        #unhide the player
        if self.hidden and pygame.time.get_ticks()-self.hide_timer >1000:
            self.hidden =False
            self.rect.centerx =game_width/2
            self.rect.bottom =game_height-10
        self.speedx =0
        keystate =pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx =-5
        if keystate[pygame.K_RIGHT]:
            self.speedx =5
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x +=self.speedx
        if self.rect.right>game_width:
            self.rect.right =game_width
        if self.rect.left <0:
            self.rect.left =0

    def powerup(self):
            self.power +=1
            self.power_time =pygame.time.get_ticks()

    def shoot(self):
        now =pygame.time.get_ticks()
        if now-self.last_shot > self.shoot_delay:
            self.last_shot =now
            if self.power ==1:
                bullet =Bullet(self.rect.centerx,self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            if self.power ==2:
                bullet1 =Bullet(self.rect.left,self.rect.centery)
                bullet2 =Bullet(self.rect.right,self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()
            if self.power >=3:
                bullet1 =Bullet(self.rect.left,self.rect.centery)
                bullet2 =Bullet(self.rect.right,self.rect.centery)
                bullet3 =Bullet(self.rect.centerx,self.rect.top)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                all_sprites.add(bullet3)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(bullet3)
                shoot_sound.play()
    
    def hide(self):
        #Hide the Player
        self.hidden =True
        self.hide_timer =pygame.time.get_ticks()
        self.rect.center =(game_width/2,game_height+200)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig =random.choice(meteor_shower)
        self.image_orig.set_colorkey(black)
        self.image =self.image_orig.copy()
        self.rect =self.image.get_rect()
        self.radius =int((self.rect.width*.85)/2)
        # pygame.draw.circle(self.image,red,self.rect.center,self.radius)
        self.rect.x =random.randrange(game_width-self.rect.width)
        self.rect.y =random.randrange(-100,-40)
        self.speedy =random.randrange(5,8)
        self.speedx=random.randrange(-2,2)
        self.rotate =0
        self.rotate_speed =random.randrange(-3,3)
        self.last_update =pygame.time.get_ticks()

    def rotation(self):
        now =pygame.time.get_ticks()
        if now-self.last_update >50:
            self.last_update =now
            self.rotate =(self.rotate + self.rotate_speed)%360
            new_image =pygame.transform.rotate(self.image_orig,self.rotate)
            old_center =self.rect.center
            self.image =new_image
            self.rect =self.image.get_rect()
            self.rect.center =old_center

    def update(self):
        self.rotation()
        self.rect.y +=self.speedy
        self.rect.x +=self.speedx
        if self.rect.top>game_height+10 or self.rect.left< -25 or self.rect.right>game_width+25:
            self.rect.x =random.randrange(game_width-self.rect.width)
            self.rect.y =random.randrange(-100,-40)
            self.speedy =random.randrange(1,8)

class Bullet(pygame.sprite.Sprite):
    global bullettype
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image= bullet_img
        if bullettype ==1:
            self.image = bullet_img_2
        if bullettype == 2:
            self.image = bullet_img_3
        if bullettype == 3:
            self.image = bullet_img_4
        self.rect =self.image.get_rect()
        self.rect.bottom =y
        self.rect.centerx=x
        self.speedy =-12

    def update(self):
        self.rect.y +=self.speedy
        #kill if goes out of screen
        if self.rect.bottom<0:
            self.kill()

class Powerups(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.type =random.choice(['shield','gun','life'])
        self.image=powerup_img[self.type]
        self.image.set_colorkey(black)
        self.rect =self.image.get_rect()
        self.rect.center=center
        self.speedy = 4

    def update(self):
        self.rect.y +=self.speedy
        #kill if goes out of screen
        if self.rect.top>game_height:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size =size
        self.image =explosion_animation[self.size][0]
      
        self.rect =self.image.get_rect()
        self.rect.center =center
        self.frame =0
        self.last_update =pygame.time.get_ticks()
        self.frame_rate =75

    def update(self):
        now =pygame.time.get_ticks()
        if now-self.last_update >self.frame_rate:
            self.frame +=1
            if self.frame ==len(explosion_animation[self.size]):
                self.kill()
            else:
                center =self.rect.center
                self.image =explosion_animation[self.size][self.frame]
                self.rect =self.image.get_rect()
                self.rect.center =center

#load all game graphics:-
background =pygame.image.load(os.path.join(img_path,"Space Shooter Background.png")).convert()
background_rect =background.get_rect()
background_2 = pygame.image.load(os.path.join(img_path, "black.png")).convert()
background_2 = pygame.transform.scale(background_2, (game_width, game_height))
background_2_rect = background_2.get_rect()
background_3 = pygame.image.load(os.path.join(img_path, "background_3.png")).convert()
background_3 = pygame.transform.scale(background_3, (game_width, game_height))
background_3_rect = background_3.get_rect()

player_img =pygame.image.load(os.path.join(img_path,"playerShip2_orange.png")).convert()
player_life_img = pygame.transform.scale(player_img, (25, 19))
player_life_img.set_colorkey(black)
player_img_2 = pygame.image.load(os.path.join(img_path, "playerShip2_blue.png")).convert()
player_life_img_2 = pygame.transform.scale(player_img_2, (25, 19))
player_life_img_2.set_colorkey(black)
player_img_3 = pygame.image.load(os.path.join(img_path, "playerShip2_red.png")).convert()
player_life_img_3 = pygame.transform.scale(player_img_3, (25, 19))
player_life_img_3.set_colorkey(black)
player_img_4 = pygame.image.load(os.path.join(img_path, "playerShip2_green.png")).convert()
player_life_img_4 = pygame.transform.scale(player_img_4, (25, 19))
player_life_img_4.set_colorkey(black)



bullet_img = pygame.image.load(os.path.join(img_path,"laserRed16.png")).convert()
bullet_img.set_colorkey(black)
bullet_img_2 = pygame.image.load(os.path.join(img_path, "laserBlue12.png")).convert()
bullet_img_2.set_colorkey(black)
bullet_img_3 = pygame.image.load(os.path.join(img_path, "laserRed13.png")).convert()
bullet_img_3.set_colorkey(black)
bullet_img_4 = pygame.image.load(os.path.join(img_path, "laserGreen03.png")).convert()
bullet_img_4.set_colorkey(black)

#Options Menu Images
player_options_img_2 = pygame.transform.scale(player_img_2, (40, 31))
player_options_img_2.set_colorkey(black)
player_options_img_3 = pygame.transform.scale(player_img_3, (40, 31))
player_options_img_3.set_colorkey(black)
player_options_img_4 = pygame.transform.scale(player_img_4, (40, 31))
player_options_img_4.set_colorkey(black)
background_options = pygame.image.load(os.path.join( img_path, "Background_Options.png")).convert()
background_options = pygame.transform.scale(background_options, (40, 60))
background_options_2 = pygame.transform.scale(background_2, (80, 80))
background_options_2rect = background_options_2.get_rect()
background_options_3 = pygame.transform.scale(background_3, (80, 80))
background_options_3rect = background_options_3.get_rect()

background_options_overlay = pygame.image.load(os.path.join(img_path, "Background_Options.png")).convert()
background_options_overlay = pygame.transform.scale(background_options, (80, 80))



meteor_shower =[]
meteor_list =['meteorBrown_big3.png','meteorBrown_med1.png',
               'meteorBrown_med3.png','meteorBrown_small1.png','meteorBrown_small2.png',
               'meteorBrown_tiny1.png','meteorBrown_tiny2.png']
for meteor_img in meteor_list:
    meteor_shower.append(pygame.image.load(os.path.join(img_path,meteor_img)).convert())
explosion_animation ={}
explosion_animation["large"]=[]
explosion_animation["small"]=[]
explosion_animation["player"]=[]
powerup_img ={}
powerup_img['shield'] =pygame.image.load(os.path.join(img_path,'shield_gold.png')).convert()
powerup_img['gun'] =pygame.image.load(os.path.join(img_path,'bolt_gold.png')).convert()
powerup_img['life'] = player_life_img

for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img =pygame.image.load(os.path.join(img_path,filename)).convert()
    img_large =pygame.transform.scale(img,(75,75))
    img_large.set_colorkey(black)
    explosion_animation["large"].append(img_large)
    img_small =pygame.transform.scale(img,(32,32))
    img_small.set_colorkey(black)
    explosion_animation["small"].append(img_small)
    filename ='sonicExplosion0{}.png'.format(i)
    img =pygame.image.load(os.path.join(img_path,filename)).convert()
    img.set_colorkey(black)
    explosion_animation["player"].append(img)

#Loading sounds
shoot_sound =pygame.mixer.Sound(os.path.join(snd_path,"sfx_laser2.ogg"))
player_die_sound =pygame.mixer.Sound(os.path.join(snd_path,"rumble1.ogg"))
explosion_sounds =[]
for explosion_sound in ["explosion_sound2.wav","explosion_sound1.wav"]:
    explosion_sounds.append(pygame.mixer.Sound(os.path.join(snd_path,explosion_sound)))
pygame.mixer.music.load(os.path.join(snd_path,"tgfcoder-FrozenJam-SeamlessLoop.ogg"))
pygame.mixer.music.set_volume(0.4)



pygame.mixer.music.play(-1)

game_over =True
running =True
while running:

    if game_over:
        
         
        all_sprites =pygame.sprite.Group()
        mobs =pygame.sprite.Group()
        bullets =pygame.sprite.Group()
        powerups =pygame.sprite.Group()
        player =Player()
        all_sprites.add(player)
        for i in range(12):
            newmob()
        Score =0 
        show_go_screen() 
        game_over =False

    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running =False
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                player.shoot()

    #update
    all_sprites.update()
    #checking bullets mobs
    hits_bullets=pygame.sprite.groupcollide(mobs,bullets,True,True)
    for hit_bullet in hits_bullets:
        random.choice(explosion_sounds).play()
        if hit_bullet.radius <10:
            Score +=2
        else:
            Score+=1
        if random.random() >0.9:
            power =Powerups(hit_bullet.rect.center)
            all_sprites.add(power)
            powerups.add(power)
        newmob()
    #checking the player mobs
    hits =pygame.sprite.spritecollide(player,mobs,True,pygame.sprite.collide_circle)

    for hit in hits:
        random.choice(explosion_sounds).play()
        player.shield -=hit.radius*2
        expl =Explosion(hit.rect.center,"small")
        all_sprites.add(expl)
        newmob()

        if player.shield<= 0:
            player_die_sound.play()
            death_explosion =Explosion(player.rect.center,'player')
            all_sprites.add(death_explosion)
            player.hide()
            player.lives +=-1
            player.shield =100

    if player.lives ==0 and not death_explosion.alive():
            game_over =True

    #Checking Poweups hitting the player
    if player_lifetype == 0:
        powerup_img['life'] = player_life_img
    if player_lifetype == 1:
        powerup_img['life'] = player_life_img_2
    if player_lifetype == 2:
        powerup_img['life'] = player_life_img_3
    if player_lifetype == 3:
        powerup_img['life'] = player_life_img_4
    hit_powerup =pygame.sprite.spritecollide(player,powerups,True)
    for hit in hit_powerup:
        if hit.type =='shield':
            player.shield  +=random.randrange(10,30)
            if player.shield >=100:
                player.shield =100
        if hit.type =='gun':
            player.powerup()
        if hit.type =='life':
            player.lives +=1
            if player.lives >=4:
                player.lives = 4
            
        #Draw
    if player_lifetype == 0:
        player_life_img = player_life_img
    if player_lifetype == 1:
        player_life_img = player_life_img_2
    if player_lifetype == 2:
        player_life_img = player_life_img_3
    if player_lifetype == 3:
        player_life_img = player_life_img_4
    screen.fill(black)
    if background_type ==0:
        screen.blit(background,background_rect)
    elif background_type == 1:
        screen.blit(background_2, background_2_rect)
    elif background_type == 2:
        screen.blit(background_3, background_3_rect)
    all_sprites.draw(screen)
    draw_text(screen,str(Score),18,game_width/2,10)
    draw_shield_bar(screen,5,5,player.shield)
    draw_lives(screen,game_width-129,5,player.lives,player_life_img)
    Total_Score =Score
    pygame.display.flip()
pygame.quit()
quit()
