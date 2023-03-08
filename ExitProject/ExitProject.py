#Celia Evans
#Period 2 CompSci110



#Exit Project: Bee Tycoon!



#XXXXXXXXXXXXXXXXXXXXXXXXXX INITIAL SETUP AND VARIABLES XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#comments

#----------------------------------imports----------------------------------------------
import pygame, sys                                                                      #imports the pygame package 
from pygame.locals import *                                                             #imports everything from local pygame folder
import random                                                                           #imports the random package
import time                                                                             #imports the time package
#-----------------------------initialize package----------------------------------------
pygame.init()                                                                           #initializes pygame system
pygame.mixer.init()                                                                     #initializes mixer system
#--------------------------------FPS settings-------------------------------------------
FPS = 65                                                                                #frames per second setting
fpsClock = pygame.time.Clock()                                                          #linking time.clock function to fpsClock variable
frameCounter=0                                                                          #resetting timer linked to events

#------------------------------window settings------------------------------------------
screen = pygame.display.set_mode((1200, 700), 0, 32)                                    #sets up the window
pygame.display.set_caption('Bee Tycoon!')                                               #Names the window
Icon = pygame.image.load('BeeGamePainting.png')                                         #loads the icon image
pygame.display.set_icon(Icon)                                                           #sets the icon image

#-------------------------general gameplay variables------------------------------------
location = 'menu'                                                                       #setting initial location to the menu
shop='closed'                                                                           #shop starts closed
store='none'                                                                            #no store is open to start
pollenCount=0                                                                           #resetting game currency
speed = 5                                                                               #player's movement speed
tooPoorTimer=3000                                                                       #set the notif length timer
multiplier=1                                                                            #set the multiplier to start
hatDirection='right'                                                                    #the hats start by facing right
facing='right'                                                                          #the character starts by facing right

names=['Bee Boy','Beast','Beats','Barry B. Benson','Buzzwell','Bumble','Bee Larry King','Brandy','Beethoven','Bernie Sanders','Benedict Cumberbatch','Brad Pitt','Bradley Cooper','Batman','Brie Larson','Bruno Mars','Britney Spears','Billie Eilish','Bug','Biscuit','Beef','Bacon','Bouncer','Bean','Banjo','Brownie','Bongo','Bagel','Bunny','Bart','Boomer','Blueberry','Boss','Boogie','Burger','Bingo','Bounty','Badger','Byte','Bones','Boon','Bamboo','Butler','Bunker','Baker','Bonsai','Buffy','Boba','Blizzard','Boba Fett','Beta','Boots','Button','Blondie','Berry','Bambi','BoBo','Bandit','Bucky','Brutus','Bennett','Baron','Benji','Buzz','Buzz Aldrin','Bear','Bullet','Birdie','Boo','Belvedeer','Benson','Brooke', 'Buzz Lightyear','Bobby', 'Bella', 'Ben', 'Bethany', 'Blake', 'Beatrice', 'Baby', 'Bailey', 'Bradley', 'Billy', 'Blair', 'Betsy', 'Brody', 'Biden','Barnaby', 'Beau', 'Belle', 'Bertie', 'Betty', 'Bonnie', 'Brandon', 'Brianna', 'Brooklyn', 'Bae', 'Balthazar', 'Benjamin', 'Barbara', 'Barney', 'Barry', 'Basil', 'Baxter', 'Bea', 'Becca', 'Beck', 'Becky', 'Belinda', 'Benedict', 'Benny', 'Bentley', 'Bernadette', 'Bernard', 'Bernice', 'Bessie', 'Beverley', 'Beyonce', 'Bianca', 'Bibi', 'Bill', 'Blade', 'Blaine', 'Blaze', 'Blane', 'Blanca', 'Blessing', 'Bliss', 'Blossom','Buttercup','Bubbles', 'Blue', 'Bluebell', 'Blythe', 'Bo', 'Bo Burnham', 'Bob', 'Boris', 'Boy', 'Bonita', 'Brad', 'Brayden', 'Bramwell', 'Braxton', 'Bree', 'Brenda', 'Brendan', 'Britta','Brennan', 'Brent', 'Brett', 'Bria', 'Brian', 'Bridget', 'Brittney', 'Brock', 'Barack Obama','Bee','Bronwyn', 'Bruce', 'Bruno', 'Bryce', 'Bryn', 'Buddy', 'Buster', 'Byron']
beeName=random.choice(names)                                                            #pick a random name from ^all possible bee names^ 

#---price hub---
#plants
SunPrice=50                                                                             #set sunflower price
BOPrice=100                                                                             #set blue orchid price
CTPrice=1000                                                                            #set cherry tree price
ATPrice=5000                                                                            #set apple tree price
#managers
m1Price=500                                                                             #set the first managers price
m2Price=750                                                                             #set the second managers price
m3Price=1500                                                                            #set the third managers price
#reboots
r1Price=1000                                                                            #set the first reboots price
r2Price=5000                                                                            #set the second reboots price
r3Price=10000                                                                           #set the third reboots price
#------------------------------music stuff---------------------------------------------
cuteBensound='bensound-cute.mp3'                                                        #import the game music as a variable
pygame.mixer.music.load(cuteBensound)                                                   #load the music in
pygame.mixer.pre_init(44100,16,2,4096)                                                  #set audio variables
volume=0.25                                                                             #make a variable for the musics volume
pygame.mixer.music.set_volume(volume)                                                   #set the musics volume
pygame.mixer.music.play(-1)                                                             #play the music
#----------------------------------bools------------------------------------------------
right = False                                                                           #no right movement to start
left = False                                                                            #no left movement to start
jumping = False                                                                         #not jumping at first

zeroPressed=False    #CHEAT
ctrlPressed=False    #"

tooPoor=False                                                                           #not too poor yet

#------------------------player positional variables------------------------------------
playerx=50                                                                              #player starting x
playery=379                                                                             #player starting y
startPos=playery                                                                        #base layer
jumpLimit=startPos - 380                                                                #set the jump limit
#---------------------------------images------------------------------------------------
#---other images---
Title=pygame.image.load('Title2.png')                                                   #load in the title logo
Title=pygame.transform.rotozoom(Title,0,0.75)                                           #shrink the title logo

hive=pygame.image.load('hive.png')                                                      #image of the bee hive
hive=pygame.transform.rotozoom(hive,0,0.5)                                              #shrinks it

hiveBackdrop=pygame.image.load('hiveBackdrop.png')                                      #image of the hive (store) background

controlsScreen=pygame.image.load('ControlsScreen.png')                                  #load in the control screen image
creditsScreen=pygame.image.load('credits.png')                                          #load in the credits screen image

storeButtons=pygame.image.load('storeButtons.png')                                      #load in the image of the store buttons 

shops=pygame.image.load('shops.png')                                                    #load in the general shops image

rightSign=pygame.image.load('sign.png')                                                 #load in the sign image
rightSign=pygame.transform.rotozoom(rightSign,0,0.5)                                    #shrink the sign image
leftSign=pygame.transform.flip(rightSign,True,False)                                    #make a flipped version of the sign image

reload=pygame.image.load('reload.png')                                                  #load in the reload symbol image

#---hats---
noHat=pygame.image.load('noHat.png')                                                    #load in a blank hat
bucketHatImg=pygame.image.load('bucketHat.png')                                         #load in the bucket hat
topHatImg=pygame.image.load('topHat.png')                                               #load in the top hat
spinnyHatImg=pygame.image.load('spinnyHat.png')                                         #load in the spinny hat
catEarsImg=pygame.image.load('catEars.png')                                             #load in the cat ears
ballCapImg=pygame.image.load('ballCap.png')                                             #load in the ball cap
crown=pygame.image.load('crown.png')                                                    #load in the crown

#---apple tree images---
appleTreeImg=pygame.image.load('appleTree.png')                                         #load in the apple tree
blossomATImg=pygame.image.load('blossomAT.png')                                         #load in the apple tree's blossom
flowerATImg=pygame.image.load('flowerAT.png')                                           #load in the apple tree's flower
appleATImg=pygame.image.load('appleAT.png')                                             #load in the apple tree's apple

#---cherry tree images---
cherryTreeImg=pygame.image.load('cherryTree.png')                                       #load in the cherry tree
blossomCTImg=pygame.image.load('blossomCT.png')                                         #load in the cherry tree's blossom
flowerCTImg=pygame.image.load('flowerCT.png')                                           #load in the cherry tree's flower
cherriesCTImg=pygame.image.load('cherriesCT.png')                                       #load in the cherry tree's cherries

#---pollen images---
pollenImg=pygame.image.load('pollen.png')                                               #image of og pollen particles
pollenImg=pygame.transform.rotozoom(pollenImg,0,0.5)                                    #shrinks it
sunPollenImg=pygame.image.load('sunflowerPollen.png')                                   #image of sunflower pollen particles
sunPollenImg=pygame.transform.rotozoom(sunPollenImg,0,0.7)                              #shrinks it
bluePollenImg=pygame.image.load('blueOrchidPollen.png')                                 #image of blue orchid pollen
bluePollenImg=pygame.transform.rotozoom(bluePollenImg,0,0.5)                            #shrinks it

#---flower images---
flowerImg=pygame.image.load('flower.png')                                               #image of og flower
sunflowerImg=pygame.image.load('sunflower.png')                                         #image of sunflower
blueOrchidImg=pygame.image.load('blueOrchid.png')                                       #image of blue orchid
managerFlowerImg=pygame.image.load('managerFlower.png')                                 #image of manager flower

#---manager images---
pinkImg1 = pygame.image.load('pinkp1.png')                                              #first pink manager image
pinkImg1 = pygame.transform.rotozoom(pinkImg1,0,0.5)                                    #shrink it
pinkImg2 = pygame.image.load('pinkp2.png')                                              #second pink manager image
pinkImg2 = pygame.transform.rotozoom(pinkImg2,0,0.5)                                    #shrink it
pinkImg3 = pygame.image.load('pinkp3.png')                                              #third pink manager image
pinkImg3 = pygame.transform.rotozoom(pinkImg3,0,0.5)                                    #shrink it

aquaImg1 = pygame.image.load('aquap1.png')                                              #first aqua manager image
aquaImg1 = pygame.transform.rotozoom(aquaImg1,0,0.5)                                    #shrink it
aquaImg2 = pygame.image.load('aquap2.png')                                              #second aqua manager image
aquaImg2 = pygame.transform.rotozoom(aquaImg2,0,0.5)                                    #shrink it
aquaImg3 = pygame.image.load('aquap3.png')                                              #third aqua manager image
aquaImg3 = pygame.transform.rotozoom(aquaImg3,0,0.5)                                    #shrink it

brownImg1 = pygame.image.load('brownp1.png')                                            #first brown manager image
brownImg1 = pygame.transform.rotozoom(brownImg1,0,0.5)                                  #shrink it
brownImg2 = pygame.image.load('brownp2.png')                                            #second brown manager image
brownImg2 = pygame.transform.rotozoom(brownImg2,0,0.5)                                  #shrink it
brownImg3 = pygame.image.load('brownp3.png')                                            #third brown manager image
brownImg3 = pygame.transform.rotozoom(brownImg3,0,0.5)                                  #shrink it

#---player images---
playerImg1 = pygame.image.load('bee1.png')                                              #image of 1st bee YELLOW
playerImg1 = pygame.transform.rotozoom(playerImg1,0,0.5)                                #shrinks it

playerImg2 = pygame.image.load('bee2.png')                                              #image of 2nd bee LIGHT BLUE
playerImg2 = pygame.transform.rotozoom(playerImg2,0,0.5)                                #shrinks it

playerImg3 = pygame.image.load('bee3.png')                                              #image of 3rd bee BLUE
playerImg3 = pygame.transform.rotozoom(playerImg3,0,0.5)                                #shrinks it

playerImg4 = pygame.image.load('bee4.png')                                              #image of 4th bee RED
playerImg4 = pygame.transform.rotozoom(playerImg4,0,0.5)                                #shrinks it
 
playerImg5 = pygame.image.load('bee5.png')                                              #image of 5th bee ORANGE
playerImg5 = pygame.transform.rotozoom(playerImg5,0,0.5)                                #shrinks it

playerImg6 = pygame.image.load('bee6.png')                                              #image of 6th bee LIME
playerImg6 = pygame.transform.rotozoom(playerImg6,0,0.5)                                #shrinks it

playerImg7 = pygame.image.load('bee7.png')                                              #image of 7th bee PURPLE
playerImg7 = pygame.transform.rotozoom(playerImg7,0,0.5)                                #shrinks it

#---image detail variables---
newImg=playerImg1                                                                       #starts new image off as original
hat=noHat                                                                               #starts off with no hat

#---animated images lists---
pinkList=[pinkImg1,pinkImg1,pinkImg1,pinkImg1,pinkImg1,pinkImg2,pinkImg2,pinkImg2,pinkImg2,pinkImg2,pinkImg3,pinkImg3,pinkImg3,pinkImg3,pinkImg3]
aquaList=[aquaImg1,aquaImg1,aquaImg1,aquaImg1,aquaImg1,aquaImg2,aquaImg2,aquaImg2,aquaImg2,aquaImg2,aquaImg3,aquaImg3,aquaImg3,aquaImg3,aquaImg3]
brownList=[brownImg1,brownImg1,brownImg1,brownImg1,brownImg1,brownImg2,brownImg2,brownImg2,brownImg2,brownImg2,brownImg3,brownImg3,brownImg3,brownImg3,brownImg3]
                                                                                        #^^^ lists with animated series for managers
#------------------------------COLOURS--------------------------------------------------
WHITE = (255,255,255)                                                                   #sets the colour white
RED = (255,0,0)                                                                         #sets the colour red
ORANGE = (255,160,0)                                                                    #sets the colour orange
YELLOW = (255,255,0)                                                                    #sets the colour yellow
LIME = (0,255,0)                                                                        #sets the colour lime
GREEN = (0,102,0)                                                                       #sets the colour green
darkGreen = (0,77,0)                                                                    #sets the colour darkGreen
BLUE = (0,0,255)                                                                        #sets the colour blue
lightBlue = (0,238,255)                                                                 #sets the colour light blue
SKY = (190,220,255)                                                                     #set the sky colour
PURPLE=(102,0,204)                                                                      #sets the colour purple
lightGray=(204,204,204)                                                                 #sets the colour light gray
MAGENTA=(255,0,255)                                                                     #sets the colour magenta
BROWN=(185,45,0)                                                                        #sets the colour brown
AQUA=(0,255,215)                                                                        #sets the colour aqua

#-------------------------------text----------------------------------------------------
font=pygame.font.SysFont('Comic Sans MS',32)                                            #sets font (comic sans of course) at size 32
font2=pygame.font.SysFont('Comic Sans MS',20)                                           #same font but size 20
Xfont=pygame.font.SysFont('Comic Sans MS',64)                                           #same font but size 64
efont=pygame.font.SysFont('Comic Sans MS',16)                                           #same font but size 16

playGame=font.render('Play Game', True, darkGreen, GREEN)                               #play button text
Credits=font.render('Credits', True, darkGreen,GREEN)                                   #credits button text
Credits2=font.render('Credits',True,lightGray,WHITE)                                    #credits title text
Controls2=font.render('Controls',True,lightGray,WHITE)                                  #controls title text
Controls=font.render('Controls',True,darkGreen,GREEN)                                   #controls button text

pollenCountWord=font.render('Pollen Count = '+str(pollenCount), True, WHITE)            #currency text
beeNameText=font.render('Bee\'s Name: '+beeName, True, WHITE)                           #bee name text

xButton=Xfont.render('X', True, RED)                                                    #store X button text
e=efont.render('e', True, WHITE)                                                        #sign e text

colourTitle=font.render('Colours', True, WHITE)                                         #colour title text
Red=font.render('Red', True, RED)                                                       #buy colour red text
Orange=font.render('Orange', True, ORANGE)                                              #buy colour orange text
Yellow=font.render('Yellow', True, YELLOW)                                              #buy colour yellow text
Lime=font.render('Lime', True, LIME)                                                    #buy colour lime text
LightBlue=font.render('Light Blue',True,lightBlue)                                      #buy colour light blue text
Blue=font.render('Blue', True, BLUE)                                                    #buy colour blue text
Purple=font.render('Purple',True,PURPLE)                                                #buy colour purple text

lolPoor=font.render('You can\'t buy this right now.',True,RED)                          #'you dont have the funds for this' notif text
default=font.render('Default',True,WHITE)                                               #default setting text

price25=font.render('25',True,WHITE)                                                    #text of price for all colours
price500=font.render('500',True,WHITE)                                                  #text of price for all hats
priceSun=font.render(str(SunPrice),True,WHITE)                                          #text of price for sunflowers
priceBO=font.render(str(BOPrice),True,WHITE)                                            #text of price for blue orchids
priceCT=font.render(str(CTPrice),True,WHITE)                                            #text of price for cherry tree
priceAT=font.render(str(ATPrice),True,WHITE)                                            #text of price for apple tree
priceM1=font.render(str(m1Price),True,WHITE)                                            #text of price for manager 1
priceM2=font.render(str(m2Price),True,WHITE)                                            #text of price for manager 2
priceM3=font.render(str(m3Price),True,WHITE)                                            #text of price for manager 3
priceR1=font.render(str(r1Price),True,WHITE)                                            #text of price for reboot 1
priceR2=font.render(str(r2Price),True,WHITE)                                            #text of price for reboot 2
priceR3=font.render(str(r3Price),True,WHITE)                                            #text of price for reboot 3

plantsTitle=font.render('Plants', True, WHITE)                                          #text for plants title
sunflowersT=font.render('Sunflowers', True, WHITE)                                      #buy sunflowers text
blueOrchidT=font.render('Blue Orchids', True, WHITE)                                    #buy blue orchids text
cherryTreeT=font.render('Cherry Tree', True, WHITE)                                     #buy cherry tree text
appleTreeT=font.render('Apple Tree', True, WHITE)                                       #buy apple tree text

managersTitle=font.render('Managers', True, WHITE)                                      #text for managers title
Manager1=font.render('Manager 1', True, MAGENTA)                                        #buy manager 1 text
Manager2=font.render('Manager 2', True, AQUA)                                           #buy manager 2 text
Manager3=font.render('Manager 3', True, BROWN)                                          #buy manager 3 text

rebootsTitle=font.render('Reboots', True, WHITE)                                        #text for reboots title
reboot1=font.render('2x Pollen', True, WHITE)                                           #buy reboot 1 text
reboot2=font.render('3x Pollen', True, WHITE)                                           #buy reboot 2 text
reboot3=font.render('4x Pollen', True, WHITE)                                           #buy reboot 3 text
rebootMessage=font.render('Reboots are reusable.', True, WHITE)                         #reboot reminder text

hatsTitle=font.render('Hats', True, WHITE)                                              #text for hats title
topHatT=font.render('Top Hat', True, WHITE)                                             #buy top hat text
catEarsT=font.render('Cat Ears', True, WHITE)                                           #buy cat ears text
spinnyHatT=font.render('Spinny Hat', True, WHITE)                                       #buy spinny hat text
bucketHatT=font.render('Bucket Hat', True, WHITE)                                       #buy bucket hat text
ballCapT=font.render('Ball Cap', True, WHITE)                                           #buy ball cap text
crownT=font.render('Crown', True, WHITE)                                                #buy crown text
noHatT=font.render('No Hat', True, WHITE)                                               #no hat button text

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX CLASSES XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class flower:                                                                           #create flower class
    def __init__(self,x,y):                                                             #initialize class and associated variables
        self.flower=flowerImg                                                           #create flower image variable
        self.lilFlower=pygame.transform.rotozoom(flowerImg,0,0.5)                       #create shrunk flower image variable
        self.sunflower=pygame.transform.rotozoom(sunflowerImg,0,0.7)                    #create sunflower image variable
        self.blueOrchid=pygame.transform.rotozoom(blueOrchidImg,0,0.5)                  #create blue orchid image variable
        self.managerFlower=pygame.transform.rotozoom(managerFlowerImg,0,0.5)            #create manager flower image variable
        self.x = x                                                                      #flower's x variable
        self.y = y                                                                      #flower's y variable
    def drawFlower(self):                                                               #defining this classes draw flower function
        screen.blit(self.flower,(self.x,self.y))                                        #blit the image of the flower
    def drawLilFlower(self):                                                            #defining this classes draw little flower function
        screen.blit(self.lilFlower,(self.x,self.y))                                     #blit the image of the little flower
    def drawSunflower(self):                                                            #defining this classes draw sunflower function
        screen.blit(self.sunflower,(self.x,self.y))                                     #blit the image of the sunflower
    def drawBlueOrchid(self):                                                           #defining this classes draw blue orchid function
        screen.blit(self.blueOrchid,(self.x,self.y))                                    #blit the image of the blue orchid
    def drawManagerFlower(self):                                                        #defining this classes draw manager flower function
        screen.blit(self.managerFlower,(self.x,self.y))                                 #blit the image of the manager flower

class pollen:                                                                           #create pollen class
    def __init__(self,pollenInUse,x,y,pollinated,rand):                                 #initialize class and associated variables in order
        self.pollen=pollenImg                                                           #create pollen image variable within class
        self.sunPollen=sunPollenImg                                                     #create sunflower pollen image variable within class
        self.bluePollen=bluePollenImg                                                   #create blue orchid pollen image variable within class
        self.pollenInUse=pollenInUse                                                    #create pollen in use variable
        self.x = x                                                                      #pollen x coord variable
        self.y = y                                                                      #pollen y coord variable
        self.pollinated = pollinated                                                    #create pollinated bool variable
        self.rand = rand                                                                #create random number variable
    def pollinate(self):                                                                #define pollinate function
        screen.blit(self.pollen,(self.x,self.y))                                        #blit the pollen
    def sunPollinate(self):                                                             #define sunflower pollinate function
        screen.blit(self.sunPollen,(self.x,self.y))                                     #blit the sunflower pollen
    def bluePollinate(self):                                                            #define blue orchid pollinate function
        screen.blit(self.bluePollen,(self.x,self.y))                                    #blit the sunflower pollen

class managers:                                                                         #create manager class
    def __init__(self,bought,timerStart,manx,many,manSpeed,manCollect,images,
                 currentImg,miniTimer,manFacing,drawMan):                               #initialize class and variables within class
        self.bought=bought                                                              #set class bought variable
        self.timerStart=timerStart                                                      #set class timer start variable
        self.manx = manx                                                                #set manager x variable
        self.many = many                                                                #set manager y variable
        self.manSpeed = manSpeed                                                        #set manager speed variable
        self.manCollect = manCollect                                                    #set manager collect rate variable
        self.images=images                                                              #set manager image list variable
        self.currentImg=currentImg                                                      #set manager current image variable
        self.miniTimer=miniTimer                                                        #set mini timer variable
        self.manFacing=manFacing                                                        #set manager facing variable
        self.drawMan=drawMan                                                            #set manager image to draw variable

class stores:                                                                           #create stores class
    def __init__(self,maxx,minx,maxy,miny,boughtVar,imgSwap,ty,price,priceNum):         #initialize class and class variables
        self.maxx = maxx                                                                #set button max x variable
        self.minx = minx                                                                #set button min x variable
        self.maxy = maxy                                                                #set button max y variable
        self.miny = miny                                                                #set button min y variable
        self.boughtVar = boughtVar                                                      #set bought item bool variable
        self.imgSwap = imgSwap                                                          #set image swap variable
        self.ty=ty                                                                      #set text y variable
        self.price=price                                                                #set price text variable
        self.priceNum=priceNum                                                          #set price integer variable

#--------------------------------class variables---------------------------------
#---managers class related variables---
pinkMan=managers(False,False,75,385,3,1,pinkList,1,0,'right',pinkImg2)                  #pink manager class variables
aquaMan=managers(False,False,75,380,5,3,aquaList,1,0,'right',aquaImg2)                  #aqua manager class variables
brownMan=managers(False,False,75,375,7,5,brownList,1,0,'right',brownImg2)               #brown manager class variables
managers=[pinkMan,aquaMan,brownMan]                                                     #list of all managers and their variables

#---stores class related variables---
#colours
reD=stores(770,505,290,266,False,playerImg4,255,price25,25)                             #red bee colour store class variables
orangE=stores(770,505,335,308,False,playerImg5,295,price25,25)                          #orange bee colour store class variables
limE=stores(770,505,413,388,False,playerImg6,375,price25,25)                            #lime bee colour store class variables
bluE=stores(770,505,492,467,False,playerImg3,455,price25,25)                            #blue bee colour store class variables
lightbluE=stores(770,505,455,427,False,playerImg2,415,price25,25)                       #light blue bee colour store class variables
purplE=stores(770,505,535,507,False,playerImg7,495,price25,25)                          #purple bee colour store class variables
myColours=[reD,orangE,limE,bluE,lightbluE,purplE]                                       #list of all colours and their variables
#plants
sunfloweR=stores(770,490,290,270,False,sunflowerImg,255,priceSun,SunPrice)              #sunflower plant class variables
blueOrchiD=stores(770,490,330,305,False,blueOrchidImg,295,priceBO,BOPrice)              #blue orchid plant class variables
cherryTreE=stores(770,490,370,350,False,cherryTreeImg,335,priceCT,CTPrice)              #cherry tree plant class variables
appleTreE=stores(770,490,412,390,False,appleTreeImg,375,priceAT,ATPrice)                #apple tree plant class variables
myPlants=[sunfloweR,blueOrchiD,cherryTreE,appleTreE]                                    #list of all plants and their variables
#hats
TopHat=stores(770,490,290,265,False,topHatImg,255,price500,500)                         #top hat store class variables
CatEars=stores(770,490,330,305,False,catEarsImg,295,price500,500)                       #cat ears store class variables 
SpinnyHat=stores(770,490,370,350,False,spinnyHatImg,335,price500,500)                   #spinny hat store class variables 
BucketHat=stores(770,490,412,390,False,bucketHatImg,375,price500,500)                   #bucket hat store class variables 
BallCap=stores(770,490,450,430,False,ballCapImg,415,price500,500)                       #ball cap store class variables 
Crown=stores(770,490,490,465,False,crown,455,price500,500)                              #crown store class variables 
myHats=[TopHat,CatEars,SpinnyHat,BucketHat,BallCap,Crown]                               #list of all hats and their variables
#managers
pinK=stores(625,470,295,270,False,pinkImg1,260,priceM1,m1Price)                         #pink manager store class variables
aquA=stores(625,470,340,315,False,aquaImg1,305,priceM2,m2Price)                         #aqua manager store class variables
browN=stores(625,470,385,360,False,brownImg1,350,priceM3,m3Price)                       #brown manager store class variables
myManagers=[pinK,aquA,browN]                                                            #list of all managers and their store class variables
#reboots
double=stores(625,470,295,270,False,2,260,priceR1,r1Price)                              #2x multiplier reboot store class variables
triple=stores(625,470,340,315,False,3,305,priceR2,r2Price)                              #3x multiplier reboot store class variables
quadruple=stores(625,470,385,360,False,4,350,priceR3,r3Price)                           #4x multiplier reboot store class variables
myReboots=[double,triple,quadruple]                                                     #list of all reboots
#all store lists except reboots
storeLists=[myColours,myPlants,myManagers,myHats]                                       #list of all store lists (expect reboots)
#all store lists
allLists=[myColours,myPlants,myHats,myManagers,myReboots]                               #list of all store lists

#---flower class related variables---
#og flowers
fx=400                                                                                  #flowers starting x
fy=390                                                                                  #flowers starting y
f1=flower(fx,fy)                                                                        #flower 1
f2=flower(fx,fy)                                                                        #flower 2
f3=flower(fx,fy)                                                                        #flower 3
f4=flower(fx,fy)                                                                        #flower 4
f5=flower(fx,fy)                                                                        #flower 5
f6=flower(fx,fy)                                                                        #flower 6
f7=flower(fx,fy)                                                                        #flower 7
f8=flower(fx,fy)                                                                        #flower 8
f9=flower(fx,fy)                                                                        #flower 9
f10=flower(fx,fy)                                                                       #flower 10
myFlowers=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]                                              #list of OG flowers
#sunflowers
s1=flower(fx,fy)                                                                        #sunflower 1
s2=flower(fx,fy)                                                                        #sunflower 2
s3=flower(fx,fy)                                                                        #sunflower 3
s4=flower(fx,fy)                                                                        #sunflower 4
s5=flower(fx,fy)                                                                        #sunflower 5
s6=flower(fx,fy)                                                                        #sunflower 6
s7=flower(fx,fy)                                                                        #sunflower 7
s8=flower(fx,fy)                                                                        #sunflower 8
s9=flower(fx,fy)                                                                        #sunflower 9
sunflowers=[s1,s2,s3,s4,s5,s6,s7,s8,s9]                                                 #list of sunflowers
#blue orchids
b1=flower(fx,fy)                                                                        #blue orchid 1
b2=flower(fx,fy)                                                                        #blue orchid 2
b3=flower(fx,fy)                                                                        #blue orchid 3
b4=flower(fx,fy)                                                                        #blue orchid 4
b5=flower(fx,fy)                                                                        #blue orchid 5
b6=flower(fx,fy)                                                                        #blue orchid 6
b7=flower(fx,fy)                                                                        #blue orchid 7
b8=flower(fx,fy)                                                                        #blue orchid 8
b9=flower(fx,fy)                                                                        #blue orchid 9
blueOrchids=[b1,b2,b3,b4,b5,b6,b7,b8,b9]                                                #list of blue orchids
#manager flowers
fx=375                                                                                  #manager flower starting x
fy=400                                                                                  #manager flower starting y
m1=flower(fx,fy)                                                                        #manager flower 1
m2=flower(fx,fy)                                                                        #manager flower 2
m3=flower(fx,fy)                                                                        #manager flower 3
m4=flower(fx,fy)                                                                        #manager flower 4
m5=flower(fx,fy)                                                                        #manager flower 5
m6=flower(fx,fy)                                                                        #manager flower 6
m7=flower(fx,fy)                                                                        #manager flower 7
m8=flower(fx,fy)                                                                        #manager flower 8
m9=flower(fx,fy)                                                                        #manager flower 9
myMFs=[m1,m2,m3,m4,m5,m6,m7,m8,m9]                                                      #list of manager flowers

#---pollen class related variables---
#og pollen
py=363                                                                                  #og pollens y
p1=pollen(pollenImg,173,py,False,random.randint(0,2000))                                #og pollen 1
p2=pollen(pollenImg,273,py,False,random.randint(0,2000))                                #og pollen 2
p3=pollen(pollenImg,373,py,False,random.randint(0,2000))                                #og pollen 3
p4=pollen(pollenImg,473,py,False,random.randint(0,2000))                                #og pollen 4
p5=pollen(pollenImg,573,py,False,random.randint(0,2000))                                #og pollen 5
p6=pollen(pollenImg,673,py,False,random.randint(0,2000))                                #og pollen 6
p7=pollen(pollenImg,773,py,False,random.randint(0,2000))                                #og pollen 7
p8=pollen(pollenImg,873,py,False,random.randint(0,2000))                                #og pollen 8
p9=pollen(pollenImg,973,py,False,random.randint(0,2000))                                #og pollen 9
p10=pollen(pollenImg,1073,py,False,random.randint(0,2000))                              #og pollen 10
pollens=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]                                                #list of og pollens
#sunflower pollen
suny=281                                                                                #sunflower pollens y
sp1=pollen(sunPollenImg,160,suny,False,random.randint(0,2000))                          #sunflower pollen 1
sp2=pollen(sunPollenImg,260,suny,False,random.randint(0,2000))                          #sunflower pollen 2
sp3=pollen(sunPollenImg,360,suny,False,random.randint(0,2000))                          #sunflower pollen 3
sp4=pollen(sunPollenImg,460,suny,False,random.randint(0,2000))                          #sunflower pollen 4
sp5=pollen(sunPollenImg,560,suny,False,random.randint(0,2000))                          #sunflower pollen 5
sp6=pollen(sunPollenImg,660,suny,False,random.randint(0,2000))                          #sunflower pollen 6
sp7=pollen(sunPollenImg,760,suny,False,random.randint(0,2000))                          #sunflower pollen 7
sp8=pollen(sunPollenImg,860,suny,False,random.randint(0,2000))                          #sunflower pollen 8
sp9=pollen(sunPollenImg,960,suny,False,random.randint(0,2000))                          #sunflower pollen 9
sunPollens=[sp1,sp2,sp3,sp4,sp5,sp6,sp7,sp8,sp9]                                        #list of sunflower pollens
#blue orchid pollen
bluey=371                                                                               #blue orchid pollens y
bp1=pollen(bluePollenImg,240,bluey,False,random.randint(0,2000))                        #blue orchid pollen 1
bp2=pollen(bluePollenImg,340,bluey,False,random.randint(0,2000))                        #blue orchid pollen 2
bp3=pollen(bluePollenImg,440,bluey,False,random.randint(0,2000))                        #blue orchid pollen 3
bp4=pollen(bluePollenImg,540,bluey,False,random.randint(0,2000))                        #blue orchid pollen 4
bp5=pollen(bluePollenImg,640,bluey,False,random.randint(0,2000))                        #blue orchid pollen 5
bp6=pollen(bluePollenImg,740,bluey,False,random.randint(0,2000))                        #blue orchid pollen 6
bp7=pollen(bluePollenImg,840,bluey,False,random.randint(0,2000))                        #blue orchid pollen 7
bp8=pollen(bluePollenImg,940,bluey,False,random.randint(0,2000))                        #blue orchid pollen 8
bp9=pollen(bluePollenImg,1040,bluey,False,random.randint(0,2000))                       #blue orchid pollen 9
bluePollens=[bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bp9]                                       #list of blue orchid pollens
#Apple Tree
at1=pollen(blossomATImg,698,50,1,random.randint(0,2000))                                #apple tree pollen 1
at2=pollen(blossomATImg,818,1,1,random.randint(0,2000))                                 #apple tree pollen 2
at3=pollen(blossomATImg,770,122,1,random.randint(0,2000))                               #apple tree pollen 3
at4=pollen(blossomATImg,674,170,1,random.randint(0,2000))                               #apple tree pollen 4
at5=pollen(blossomATImg,746,218,1,random.randint(0,2000))                               #apple tree pollen 5
at6=pollen(blossomATImg,914,194,1,random.randint(0,2000))                               #apple tree pollen 6
at7=pollen(blossomATImg,866,98,1,random.randint(0,2000))                                #apple tree pollen 7
at8=pollen(blossomATImg,938,26,1,random.randint(0,2000))                                #apple tree pollen 8
at9=pollen(blossomATImg,986,122,1,random.randint(0,2000))                               #apple tree pollen 9
at10=pollen(blossomATImg,1034,50,1,random.randint(0,2000))                              #apple tree pollen 10
at11=pollen(blossomATImg,1058,194,1,random.randint(0,2000))                             #apple tree pollen 11
at12=pollen(blossomATImg,1106,122,1,random.randint(0,2000))                             #apple tree pollen 12
atPollens=[at1,at2,at3,at4,at5,at6,at7,at8,at9,at10,at11,at12]                          #list of all apple tree pollens
#Cherry Tree
ct1=pollen(blossomCTImg,202,186,1,random.randint(0,2000))                               #cherry tree pollen 1
ct2=pollen(blossomCTImg,178,234,1,random.randint(0,2000))                               #cherry tree pollen 2
ct3=pollen(blossomCTImg,226,266,1,random.randint(0,2000))                               #cherry tree pollen 3
ct4=pollen(blossomCTImg,234,218,1,random.randint(0,2000))                               #cherry tree pollen 4
ct5=pollen(blossomCTImg,262,166,1,random.randint(0,2000))                               #cherry tree pollen 5
ct6=pollen(blossomCTImg,314,153,1,random.randint(0,2000))                               #cherry tree pollen 6
ct7=pollen(blossomCTImg,314,210,1,random.randint(0,2000))                               #cherry tree pollen 7
ct8=pollen(blossomCTImg,362,170,1,random.randint(0,2000))                               #cherry tree pollen 8
ct9=pollen(blossomCTImg,418,154,1,random.randint(0,2000))                               #cherry tree pollen 9
ct10=pollen(blossomCTImg,402,202,1,random.randint(0,2000))                              #cherry tree pollen 10
ct11=pollen(blossomCTImg,394,258,1,random.randint(0,2000))                              #cherry tree pollen 11
ct12=pollen(blossomCTImg,450,234,1,random.randint(0,2000))                              #cherry tree pollen 12
ctPollens=[ct1,ct2,ct3,ct4,ct5,ct6,ct7,ct8,ct9,ct10,ct11,ct12]                          #list of all cherry tree pollens
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX FUNCTIONS/DEFS XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#==============================misc. loops============================
def drawHat():                                                                          #define draw hat function
    global hatDirection                                                                 #globalize hatDirection variable
    global hat                                                                          #globalize hat variable
    if facing == 'right' and hatDirection=='right':                                     #what direction is everything facing? both right?
        screen.blit(hat,(playerx+30,playery))                                           #if both right, blit original drawn hat 30 pixels to the right of the bees x coord
    elif facing == 'left' and hatDirection=='right':                                    #is the bee facing left, but the hat is facing right?
        hatDirection='left'                                                             #if so, set the hat to face left now
        hat=pygame.transform.flip(hat,True,False)                                       #and flip the hat drawing
        screen.blit(hat,(playerx+4,playery))                                            #and then blit the hat 4 pixels to the right of the bees x coord
    elif facing == 'left' and hatDirection=='left':                                     #are they both facing left?
        screen.blit(hat,(playerx+4,playery))                                            #If so, blit the current hat variable 4 pixels to the right of the bees x coord
    elif facing == 'right' and hatDirection=='left':                                    #is the bee facing right, but the hat is facing left?
        hatDirection='right'                                                            #if so, set the hat to face right now
        hat=pygame.transform.flip(hat,True,False)                                       #and flip the current hat drawing
        screen.blit(hat,(playerx+30,playery))                                           #and blit original drawn hat 30 pixels to the right of the bees x coord
#==============================bee movements=============================
def fall():                                                                             #define the fall function (bascially the gravity)
    global playery                                                                      #globalize the playery variable
    if playery < startPos:                                                              #is the player y smaller than the starting y?
        playery = playery + speed                                                       #if so, add to the player y (go down)
    
def jump():                                                                             #define the jump function
    global playery                                                                      #globalize the playery variable
    global jumping                                                                      #globalize the jumping variable
    playery = playery - speed                                                           #take away from the player y (go up)
    if playery < jumpLimit:                                                             #is the playery smaller than the jump limit?
        jumping = False                                                                 #if so, stop jumping/going up

def moveRight():                                                                        #define the moving right function
    global playerx                                                                      #globalize the playerx variable
    playerx = playerx + speed                                                           #add to the player x (go right)
    if playerx > 1180:                                                                  #is the player x larger than 1180 (aka the right limit)?
        while playerx > 1180:                                                           #if so, while the player x is larger,
            playerx -= 1                                                                #continue to subtract 1 (move to the left).

def moveLeft():
    global playerx                                                                      #globalize the playerx variable
    playerx = playerx - speed                                                           #take away from the player x (go left)
    if playerx < 0:                                                                     #is the player x smaller than 0 (aka the left limit)?
        while playerx < 0:                                                              #if so, while the player x is smaller,
            playerx += 1                                                                #continue to add 1 (move to the right).

#=============================class loops=============================
#---------------------------drawing flowers---------------------------
def flowersOnMenu():                                                                    #define the flowers on menu function
    global flowerImg                                                                    #globalize the flower image variable
    fx=0                                                                                #set the starting flower x 
    fy=505                                                                              #set the starting flower y
    for i in myFlowers:                                                                 #repeat loop for every og flower
        fx=fx+100                                                                       #   add 100 to the flower x
        i = flower(fx,fy)                                                               #   set the flower to have the set x and y
        i.drawFlower()                                                                  #   run flower class's draw flower function

def flowersOnMain():                                                                    #define the flowers on main function
    global flowerImg                                                                    #globalize the flower image variable
    #draw regular flowers
    fx=75                                                                               #set the starting flower x 
    fy=371                                                                              #set the starting flower y
    for i in myFlowers:                                                                 #repeat the following for every og flower
        fx=fx+100                                                                       #   add 100 to the flower x
        i = flower(fx,fy)                                                               #   set the flower to have the set x and y
        i.drawLilFlower()                                                               #   run flower class's draw little flower function
    #draw sunflowers
    if sunfloweR.boughtVar == True:                                                     #have you bought the sunflowers yet? If so:
        fx=60                                                                           #set the starting flower x 
        fy=281                                                                          #set the starting flower y
        for i in sunflowers:                                                            #repeat the following for every sunflower
            fx = fx+100                                                                 #   add 100 to the flower x
            i=flower(fx,fy)                                                             #   set the flower to have the set x and y
            i.drawSunflower()                                                           #   run flower class's draw sunflower function
    #draw blue orchids
    if blueOrchiD.boughtVar == True:                                                    #have you bought the blue orchids yet? If so:
        fx=140                                                                          #set the starting flower x 
        fy=371                                                                          #set the starting flower y
        for i in blueOrchids:                                                           #repeat the following for every blue orchid
            fx = fx+100                                                                 #   add 100 to the flower x
            i=flower(fx,fy)                                                             #   set the flower to have the set x and y
            i.drawBlueOrchid()                                                          #   run flower class's draw blue orchid function

def drawingManagerFlowers():
    if pinK.boughtVar == True or aquA.boughtVar == True or browN.boughtVar == True:     #Have you bought any managers yet? If so:
        fx=125                                                                          #set the starting flower x 
        fy=380                                                                          #set the starting flower y
        for i in myMFs:                                                                 #repeat the following for every Manager Flower
            fx=fx+100                                                                   #   add 100 to the flower x
            i = flower(fx,fy)                                                           #   set the flower to have the set x and y
            i.drawManagerFlower()                                                       #   run flower class's draw manager flower function

#---------------------------drawing the pollen---------------------------
def pollenRegen():                                                                      #define the pollen regeneration function
    global pollenCount                                                                  #globalize the pollen count variable
    #OG pollen
    for i in pollens:                                                                   #repeat for every og pollen
        if i.pollinated == False and frameCounter == i.rand:                            #is the pollinated variable false and the frame count the same as the random number variable? If so:
            i.pollinated=True                                                           #   Set the pollinated variable to true
            if location == 'main':                                                      #   if the location is the main screen:
                i.pollinate()                                                           #       run the pollen class's pollinate function (aka draw it)
        elif i.pollinated == True and location == 'main':                               #otherwise is the pollinated variable true and the location the main screen? If so:
            i.pollinate()                                                               #       run the pollen class's pollinate function (aka draw it)
            if playerx >= i.x-30 and playerx <= i.x+35 and playery <= i.y+15 and playery >= i.y-35:#If the bee is touching the pollen,
                i.rand=random.randint(0,2000)                                           #           reset the random number,
                pollenCount=pollenCount+1*multiplier                                    #           add the collected pollen to the pollen count
                i.pollinated = False                                                    #           set the pollinated variable to false
    #sunflower pollen
    if sunfloweR.boughtVar == True:                                                     #Have you bought the sunflowers? If so run the following
        for i in sunPollens:                                                            #for every sunflower pollen:
            if i.pollinated == False and frameCounter == i.rand:                        #is the pollinated variable false and the frame count the same as the random number variable? If so:
                i.pollinated=True                                                       #   set the pollinated variable to true
                if location == 'main':                                                  #   if the location is the main sceen,
                    i.sunPollinate()                                                    #       run the pollen class's sunflower pollinate function (aka draw it)
            elif i.pollinated == True and location == 'main':                           #otherwise is the pollinated variable true and the location the main screen? If so:
                i.sunPollinate()                                                        #       run the pollen class's sunflower pollinate function (aka draw it)
                if playerx >= i.x+15 and playerx <= i.x+75 and playery <= i.y+35 and playery >= i.y-35:#If the bee is touching the pollen,
                    i.rand=random.randint(0,2000)                                       #           reset the random number,
                    pollenCount=pollenCount+5*multiplier                                #           add the collected pollen to the pollen count
                    i.pollinated = False                                                #           set the pollinated variable to false
    #blue orchid pollen
    if blueOrchiD.boughtVar == True:                                                    #Have you bought the blue orchids? If so run the following
        for i in bluePollens:                                                           #for every blue orchid pollen:
            if i.pollinated == False and frameCounter == i.rand:                        #is the pollinated variable false and the frame count the same as the random number variable? If so:
                i.pollinated=True                                                       #   set the pollinated variable to true
                if location == 'main':                                                  #   if the location is the main sceen,
                    i.bluePollinate()                                                   #       run the pollen class's blue orchid pollinate function (aka draw it)
            elif i.pollinated == True and location == 'main':                           #otherwise is the pollinated variable true and the location the main screen? If so:
                i.bluePollinate()                                                       #       run the pollen class's blue orchid pollinate function (aka draw it)
                if playerx >= i.x-45 and playerx <= i.x+40 and playery >= i.y-35:       #       If the bee is touching the pollen,
                    i.rand=random.randint(0,2000)                                       #           reset the random number,
                    pollenCount=pollenCount+5*multiplier                                #           add the collected pollen to the pollen count
                    i.pollinated = False                                                #           set the pollinated variable to false

def appleTreePollenRegen():                                                             #define the apple trees pollen regeneration
    global pollenCount                                                                  #globalize the pollen count variable
    #apple tree pollen
    if appleTreE.boughtVar == True:                                                     #Have you bought the apple tree yet? If so:
        for i in atPollens:                                                             #for every apple tree pollen:
            #first blossom
            if i.pollinated == 1:                                                       #Is the pollen at the first stage of pollination? If so:
                i.pollenInUse=blossomATImg                                              #   set the pollen in use to the blossom
                if location == 'secondField':                                           #   If you're in the second field,
                    screen.blit(i.pollenInUse,(i.x,i.y))                                #   draw the pollen in use. (blossom)
                if frameCounter == i.rand:                                              #   If the random timer matches the frame count,
                    i.pollenInUse=flowerATImg                                           #   change the pollen in use to the open flower 
                    i.pollinated=2                                                      #   and move on to the net stage of pollination.
            #flower
            elif i.pollinated == 2 and location == 'secondField':                       #Is the pollen at the second stage of pollination and the bee in the second field? If so:
                screen.blit(i.pollenInUse,(i.x,i.y))                                    #   Draw the pollen in use (aka the flower)
                if playerx >= i.x-50 and playerx <= i.x+45 and playery >= i.y-35 and playery <= i.y+45:#If the bee touches the flower,
                    i.rand=random.randint(0,2000)                                       #   pick a new random number for the timer,
                    pollenCount=pollenCount+25*multiplier                               #   add the pollen to the pollen count,
                    i.pollenInUse=blossomATImg                                          #   set the pollen in use back to the blossom,
                    i.pollinated=3                                                      #   and move on to the next stage of polination.
            #second blossom
            elif i.pollinated == 3:                                                     #Is the pollen at the third stage of pollination? If so:
                if location == 'secondField':                                           #   If you're in the second field,
                    screen.blit(i.pollenInUse,(i.x,i.y))                                #   draw the pollen in use. (blossom)
                if frameCounter == i.rand:                                              #   If the random timer matches the frame count,
                    i.pollenInUse=appleATImg                                            #   change the pollen in use to the apple
                    i.pollinated=4                                                      #   and move on to the net stage of pollination.
            #apple
            elif i.pollinated == 4 and location == 'secondField':                       #Is the pollen at the forth stage of pollination and the bee in the second field? If so:
                screen.blit(i.pollenInUse,(i.x,i.y))                                    #   Draw the pollen in use. (aka the apple)
                if playerx >= i.x-50 and playerx <= i.x+45 and playery >= i.y-35 and playery <= i.y+45:#If the bee touches the apple,
                    i.rand=random.randint(0,2000)                                       #   pick a new random number for the timer,
                    pollenCount=pollenCount+50*multiplier                               #   add the pollen to the pollen count,
                    i.pollenInUse=blossomATImg                                          #   set the pollen in use back to the blossom,
                    i.pollinated=1                                                      #   and reset the stage of pollination back to the beginning.

def cherryTreePollenRegen():                                                            #define the cherry tree's pollen regeneration
    global pollenCount                                                                  #globalize the pollen count variable
    #cherry tree pollen
    if cherryTreE.boughtVar == True:                                                    #Have you bought the cherry tree yet? If so:
        for i in ctPollens:                                                             #for every cherry tree pollen:
            #first blossom
            if i.pollinated == 1:                                                       #Is the pollen at the first stage of pollination? If so:
                i.pollenInUse=blossomCTImg                                              #   set the pollen in use to the blossom
                if location == 'secondField':                                           #   If you're in the second field,
                    screen.blit(i.pollenInUse,(i.x,i.y))                                #   draw the pollen in use. (blossom)
                if frameCounter == i.rand:                                              #   If the random timer matches the frame count,
                    i.pollenInUse=flowerCTImg                                           #   change the pollen in use to the open flower 
                    i.pollinated=2                                                      #   and move on to the net stage of pollination.
            #flower
            elif i.pollinated == 2 and location == 'secondField':                       #Is the pollen at the second stage of pollination and the bee in the second field? If so:
                screen.blit(i.pollenInUse,(i.x,i.y))                                    #   Draw the pollen in use (aka the flower)
                if playerx >= i.x-50 and playerx <= i.x+20 and playery >= i.y-30 and playery <= i.y+17:#If the bee touches the flower,
                    i.rand=random.randint(0,2000)                                       #   pick a new random number for the timer,
                    pollenCount=pollenCount+10*multiplier                               #   add the pollen to the pollen count,
                    i.pollenInUse=blossomCTImg                                          #   set the pollen in use back to the blossom,
                    i.pollinated=3                                                      #   and move on to the next stage of polination.
            #second blossom
            elif i.pollinated == 3:                                                     #Is the pollen at the third stage of pollination? If so:
                if location == 'secondField':                                           #   If you're in the second field,
                    screen.blit(i.pollenInUse,(i.x,i.y))                                #   draw the pollen in use. (blossom)
                if frameCounter == i.rand:                                              #   If the random timer matches the frame count,
                    i.pollenInUse=cherriesCTImg                                         #   change the pollen in use to the cherries
                    i.pollinated=4                                                      #   and move on to the net stage of pollination.
            #apple
            elif i.pollinated == 4 and location == 'secondField':                       #Is the pollen at the forth stage of pollination and the bee in the second field? If so:
                screen.blit(i.pollenInUse,(i.x,i.y))                                    #   Draw the pollen in use. (aka the cherries)
                if playerx >= i.x-50 and playerx <= i.x+20 and playery >= i.y-30 and playery <= i.y+17:#If the bee touches the cherries,
                    i.rand=random.randint(0,2000)                                       #   pick a new random number for the timer,
                    pollenCount=pollenCount+25*multiplier                               #   add the pollen to the pollen count,
                    i.pollenInUse=blossomCTImg                                          #   set the pollen in use back to the blossom,
                    i.pollinated=1                                                      #   and reset the stage of pollination back to the beginning.

#---------------------------buying colours---------------------------
def colourStoreIfs():                                                                   #Define the colour store ifs function
    global pollenCount                                                                  #Globalize the pollen count variable
    global tooPoorTimer                                                                 #Globalize the poor notif timer variable
    global tooPoor                                                                      #Globalize the too poor variable
    global newImg                                                                       #Globalize the new image variable
    #all colours except yellow
    for i in myColours:                                                                 #Repeat for every colour
        if store == 'colour' and mx>=i.minx and mx<=i.maxx and my>=i.miny and my<=i.maxy:#If the player clicks on this colour
            if pollenCount>=25 and i.boughtVar==False:                                  #  If they haven't bought it already and have enough money
                i.boughtVar=True                                                        #    Set it to bought
                pollenCount = pollenCount-25                                            #    Take away the cost of the item from the player
                newImg = i.imgSwap                                                      #    Switch the players skin to the new bought one
                if facing == 'left':                                                    #    If the player is facing left
                    newImg=pygame.transform.flip(newImg,True,False)                     #      Flip the image to face left
            elif i.boughtVar==True:                                                     #  If they've already bought it
                newImg = i.imgSwap                                                      #    Switch the players skin to this one
                if facing == 'left':                                                    #    And if they're facing left
                    newImg=pygame.transform.flip(newImg,True,False)                     #    Flip them to face the right way
            elif i.boughtVar==False:                                                    #  If they haven't already bought it and don't have enough money
                tooPoor = True                                                          #    Set it up so a temporary reminder will pop up on their screen
                tooPoorTimer=frameCounter                                               #    By setting up a timer
                if tooPoorTimer>=1941:                                                  #    And if the timer surpasses the frame counter
                    tooPoorTimer=2000-tooPoorTimer                                      #      Flip it back around to the start of the frame count.
    #yellow
    if store == 'colour' and mx>=505 and mx<=770 and my>=348 and my<=372:               #If the player clicks on yellow
        newImg = playerImg1                                                             #  switch the players skin to yellow
        if facing == 'left':                                                            #  if the player is facing left
            newImg=pygame.transform.flip(newImg,True,False)                             #    flip the image to face left
#---------------------------hat store ifs---------------------------
def hatsStoreIfs():                                                                     #Define the hats store ifs function
    global hat                                                                          #Globalize the pollen count variable
    global pollenCount                                                                  #Globalize the pollen count variable
    global tooPoorTimer                                                                 #Globalize the pollen count variable
    global tooPoor                                                                      #Globalize the pollen count variable
    global hatDirection                                                                 #Globalize the pollen count variable
    for i in myHats:                                                                    #Repeat for every colour
        if store == 'hats' and mx>=i.minx and mx<=i.maxx and my>=i.miny and my<=i.maxy: #If the player clicks on this hat
            if pollenCount>=i.priceNum and i.boughtVar==False:                          #  If they haven't bought it already and have enough money
                i.boughtVar=True                                                        #    Set it to bought
                pollenCount = pollenCount-i.priceNum                                    #    Take away the cost of the item from the player
                hat = i.imgSwap                                                         #    Switch the current hat to the new bought one
                hatDirection='right'                                                    #    Recognize that the hat starts off facing right
                if facing=='left' and hatDirection=='right':                            #    but if the player is facing left,
                    hatDirection='left'                                                 #      set the hat to face left
                    hat=pygame.transform.flip(hat,True,False)                           #      and flip the image to face left.
            elif i.boughtVar==True:                                                     #  If they've already bought it
                hat = i.imgSwap                                                         #    Switch the current hat to the new bought one
                hatDirection='right'                                                    #    Recognize that the hat starts off facing right
                if facing=='left' and hatDirection=='right':                            #    but if the player is facing left,
                    hatDirection='left'                                                 #      set the hat to face left
                    hat=pygame.transform.flip(hat,True,False)                           #      and flip the image to face left.
            elif i.boughtVar==False:                                                    #  If they haven't already bought it and don't have enough money
                tooPoor = True                                                          #    Set it up so a temporary reminder will pop up on their screen
                tooPoorTimer=frameCounter                                               #    By setting up a timer
                if tooPoorTimer>=1941:                                                  #    And if the timer surpasses the frame counter
                    tooPoorTimer=2000-tooPoorTimer                                      #      Flip it back around to the start of the frame count.
    if store == 'hats' and mx>=490 and mx<=770 and my>=505 and my<=535:                 #If the player selects no hat.
        hat = noHat                                                                     #  Set the players hat to no hat.
#---------------------------buying plants---------------------------
def plantStoreIfs():                                                                    #Define the hats store ifs function
    global pollenCount                                                                  #Globalize the pollen count variable
    global tooPoorTimer                                                                 #Globalize the too poor timer variable
    global tooPoor                                                                      #Globalize the too poor variable
    for i in myPlants:                                                                  #Repeat for every plant
        if store == 'plants' and mx>=i.minx and mx<=i.maxx and my>=i.miny and my<=i.maxy:#If the player clicks on this plant
            if pollenCount>=i.priceNum and i.boughtVar==False:                          #  If they haven't bought it already and have enough money
                i.boughtVar = True                                                      #    Set it to bought
                pollenCount = pollenCount-i.priceNum                                    #    Take away the cost of the item from the player
            elif i.boughtVar==False:                                                    #  If they haven't already bought it and don't have enough money
                tooPoor = True                                                          #    Set it up so a temporary reminder will pop up on their screen
                tooPoorTimer=frameCounter                                               #    By setting up a timer
                if tooPoorTimer>=1941:                                                  #    And if the timer surpasses the frame counter
                    tooPoorTimer=2000-tooPoorTimer                                      #      Flip it back around to the start of the frame count.
#-------------------------hiring managers----------------------------
def managerStoreIfs():                                                                  #Define the manager store ifs function
    global pollenCount                                                                  #Globalize the pollen count variable
    global tooPoorTimer                                                                 #Globalize the too poor timer variable
    global tooPoor                                                                      #Globalize the too poor variable
    for i in myManagers:                                                                #Repeat for every plant
        if store == 'managers' and mx>=i.minx and mx<=i.maxx and my>=i.miny and my<=i.maxy:#if the player clicks on this manager button
            if pollenCount>=i.priceNum and i.boughtVar==False:                          #  If they haven't bought it already and have enough money
                i.boughtVar = True                                                      #    Set it to bought
                pollenCount = pollenCount-i.priceNum                                    #    Take away the cost of the item from the player
            elif i.boughtVar==False:                                                    #  If they haven't already bought it and don't have enough money
                tooPoor = True                                                          #    Set it up so a temporary reminder will pop up on their screen
                tooPoorTimer=frameCounter                                               #    By setting up a timer
                if tooPoorTimer>=1941:                                                  #    And if the timer surpasses the frame counter
                    tooPoorTimer=2000-tooPoorTimer                                      #      Flip it back around to the start of the frame count.
    indexNum=0                                                                          #Reset the indexNum variable to 0
    for i in managers:                                                                  #Repeat for all of my managers
        if myManagers[indexNum].boughtVar == True:                                      #  If the associated manager store bought variable is true
            i.bought=True                                                               #    relay that to the manager function related variables
        indexNum+=1                                                                     #  move on to the next manager
#--------------------------reboots in store------------------------------------
def rebootStoreIfs():                                                                   #Define the reboot store ifs function
    global pollenCount                                                                  #Globalize the pollen count variable
    global tooPoorTimer                                                                 #Globalize the too poor timer variable
    global tooPoor                                                                      #Globalize the too poor variable
    global multiplier                                                                   #Globalize the multiplier variable
    global newImg                                                                       #Globalize the new image variable
    global hat                                                                          #Globalize the hat variable
    for i in myReboots:                                                                 #Repeat for every plant
        if store == 'reboots' and mx>=i.minx and mx<=i.maxx and my>=i.miny and my<=i.maxy:#if the player clicks on this manager button
            if pollenCount>=i.priceNum and i.boughtVar==False:                          #  If they haven't bought it already and have enough money
                i.boughtVar = True                                                      #    Set it to bought
                pollenCount=0                                                           #    Reset the pollen count
                newImg = playerImg1                                                     #    Reset the player image
                hat=noHat                                                               #    Reset the player's hat
                if facing == 'left':                                                    #    If the player is facing left
                    newImg=pygame.transform.flip(newImg,True,False)                     #      Flip the image
                multiplier=i.imgSwap                                                    #    Set the multiplier to the bought multiplier.
                #resetting store variables
                for i in storeLists:                                                    #Repeat for every store
                    for n in i:                                                         #  Repeat for every item within each store
                        n.boughtVar=False                                               #    Unbuy it
                for i in managers:                                                      #Repeat for every manager
                    i.bought=False                                                      #  Notify them that they have been let go
            elif i.boughtVar==False:                                                    #  If they haven't already bought it and don't have enough money
                tooPoor = True                                                          #    Set it up so a temporary reminder will pop up on their screen
                tooPoorTimer=frameCounter                                               #    By setting up a timer
                if tooPoorTimer>=1941:                                                  #    And if the timer surpasses the frame counter
                    tooPoorTimer=2000-tooPoorTimer                                      #      Flip it back around to the start of the frame count.
            elif i.boughtVar==True:                                                     #  If they've already bought it
                pollenCount=0                                                           #    Reset the pollen count
                newImg = playerImg1                                                     #    Reset the player image
                hat=noHat                                                               #    Reset the player's hat
                if facing == 'left':                                                    #    If the player is facing left
                    newImg=pygame.transform.flip(newImg,True,False)                     #      Flip the image
                multiplier=i.imgSwap                                                    #    Set the multiplier to the bought multiplier.
                #resetting store variables
                for i in storeLists:                                                    #Repeat for every store
                    for n in i:                                                         #  Repeat for every item within each store
                        n.boughtVar=False                                               #    Unbuy it
                for i in managers:                                                      #Repeat for every manager
                    i.bought=False                                                      #  Notify them that they have been let go
#--------------------------------manager functions-----------------------------
def managerFunctions():                                                                 #define the manager functions
    global pollenCount                                                                  #globalize the pollen count variable
    for i in managers:                                                                  #For each manager,
        if i.bought==True:                                                              #if you've bought them;
            #pollen adding stuff
            if i.timerStart == False:                                                   # if the timer hasnt started,
                i.miniTimer = frameCounter + 60                                         #  set the new timer.
                if i.miniTimer > 2000:                                                  #  if the timer number is too high,
                    i.miniTimer-=2000                                                   #   start it on the next frame loop.
                i.timerStart = True                                                     #  Then start the timer.
            elif i.timerStart == True and frameCounter == i.miniTimer:                  # if the timer has started and it has counted down,
                manAdd=i.manCollect * multiplier                                        #  calculate how much pollen you're adding,
                pollenCount += manAdd                                                   #  then add it,
                i.timerStart = False                                                    #  and stop the timer.
            #drawing stuff
            if location == 'main':                                                      # if the player is on the main playing screen,
                screen.blit(i.drawMan,(i.manx,i.many))                                  #  draw the manager
                i.currentImg+=1                                                         #  continue the animation along
                if i.currentImg>8:                                                      #  If the current image number surpasses the number of images,
                    i.currentImg=0                                                      #   reset the images back to the start
                if i.manFacing == 'right':                                              #  If the manager is facing right,
                    i.manx=i.manx+i.manSpeed                                            #   move it to the right
                    i.drawMan=i.images[i.currentImg]                                    #   set the image to draw as the current image
                    if i.manx >= 1125:                                                  #   if the manager is too far over,
                        i.manFacing='left'                                              #    turn him around
                elif i.manFacing == 'left':                                             #  If the manager is facing left,
                    i.manx=i.manx-i.manSpeed                                            #   move it to the left
                    i.drawMan=pygame.transform.flip(i.images[i.currentImg],True,False)  #   set the image to draw as a left facing version of the current image
                    if i.manx <= 75:                                                    #   if the manager is too far over,
                        i.manFacing='right'                                             #    turn him around
#---------------------------blitting price vs check mark---------------------------
def OwnedStatusC():                                                                     #Define the owned status function for colours
    for i in myColours:                                                                 #Check for every colour;
        if i.boughtVar == True:                                                         #If you bought it,
            pygame.draw.line(screen, LIME,[685,i.miny+15],[700,i.maxy],3)               #draw a check mark
            pygame.draw.line(screen, LIME,[700,i.maxy],[750,i.miny],3)                  #using two lines next to it's name.
        elif i.boughtVar == False:                                                      #But if you havent bought it,
            screen.blit(i.price,(710,i.ty))                                             #blit the price next to it's name.

def OwnedStatusH():                                                                     #Define the owned status function for hats
    for i in myHats:                                                                    #Check for every colour;
        if i.boughtVar == True:                                                         #If you bought it,
            pygame.draw.line(screen, LIME,[685,i.miny+15],[700,i.maxy],3)               #draw a check mark
            pygame.draw.line(screen, LIME,[700,i.maxy],[750,i.miny],3)                  #using two lines next to it's name.
        elif i.boughtVar == False:                                                      #But if you havent bought it,
            screen.blit(i.price,(710,i.ty))                                             #blit the price next to it's name.

def OwnedStatusP():                                                                     #Define the owned status function for plants
    for i in myPlants:                                                                  #Check for every colour;
        if i.boughtVar == True:                                                         #If you bought it,
            pygame.draw.line(screen, LIME,[685,i.miny+15],[700,i.maxy],3)               #draw a check mark
            pygame.draw.line(screen, LIME,[700,i.maxy],[750,i.miny],3)                  #using two lines next to it's name.
        elif i.boughtVar == False:                                                      #But if you havent bought it,
            screen.blit(i.price,(710,i.ty))                                             #blit the price next to it's name.

def OwnedStatusM():                                                                     #Define the owned status function for managers
    for i in myManagers:                                                                #Check for every colour;
        if i.boughtVar == True:                                                         #If you bought it,
            pygame.draw.line(screen, LIME,[685,i.miny+15],[700,i.maxy],3)               #draw a check mark
            pygame.draw.line(screen, LIME,[700,i.maxy],[750,i.miny],3)                  #using two lines next to it's name.
        elif i.boughtVar == False:                                                      #But if you havent bought it,
            screen.blit(i.price,(710,i.ty))                                             #blit the price next to it's name.

def OwnedStatusR():                                                                     #Define the owned status function for reboots
    for i in myReboots:                                                                 #Check for every colour;
        if i.boughtVar == True:                                                         #If you bought it,
            pygame.draw.line(screen, LIME,[685,i.miny+15],[700,i.maxy],3)               #draw a check mark
            pygame.draw.line(screen, LIME,[700,i.maxy],[750,i.miny],3)                  #using two lines next to it's name.
        elif i.boughtVar == False:                                                      #But if you havent bought it,
            screen.blit(i.price,(690,i.ty))                                             #blit the price next to it's name.
                
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX MAIN WHILE LOOP XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

while True:                                                                             #main loop runs entire game while true
    
    #===========================Location Appearances==================================
    screen.fill(SKY)                                                                    #main backdrop

    #----------------------------Controls screen graphics----------------------------
    if location == 'Controls':                                                          #If you're in the controls manual,
        screen.blit(controlsScreen,(0,0))                                               #draw in the image of all the controls
        screen.blit(Controls2,(540,150))                                                #and write 'Controls' as the title.

    #----------------------------Credits screen graphics----------------------------
    if location == 'Credits':                                                           #If you're on the credits page,
        screen.blit(creditsScreen,(0,0))                                                #draw in the image of all the credits
        screen.blit(Credits2,(540,150))                                                 #and write 'Credits' as the title.
        
    #----------------------------Main Game Screen Graphics----------------------------
    if location == 'main':                                                              #If on main playing screen
        pygame.draw.rect(screen, GREEN,[0,420,1200,300])                                #draw ground
        #class drawing
        flowersOnMain()                                                                 #draw flowers
    pollenRegen()                                                                       #run random pollen generation whether on main screen or not
    if location == 'main':                                                              #Back on main playing screen
        #images
        screen.blit(hive,(20,345))                                                      #draw the hive
        screen.blit(rightSign,(1150,371))                                               #draw the directional sign on the right
        screen.blit(e,(1169,375))                                                       #write 'e' on the sign
        #PLAYER
        drawHat()                                                                       #draw the hat on the player
        screen.blit(newImg,(playerx,playery))                                           #draw player
        #man. flowers over player
        drawingManagerFlowers()                                                         #draw the manager projects
        #variables/stats
        pollenCountWord=font.render('Pollen Count = '+str(pollenCount), True, WHITE)    #set text to most recent pollen count
        screen.blit(pollenCountWord,(10,50))                                            #write the pollen count
        screen.blit(beeNameText,(10,10))                                                #write the bee name 
        
    #-------------------------------Menu Graphics--------------------------------------
    elif location == 'menu':                                                            #If on game menu/pause screen
        pygame.draw.rect(screen, GREEN,[0,600,1200,100])                                #draw decorative ground
        #class loop
        flowersOnMenu()                                                                 #draw decorative flowers
        #draw buttons
        pygame.draw.rect(screen, GREEN, [400,200,400,100])                              #draw play game button rectangle
        pygame.draw.rect(screen, GREEN, [410,310,380,75])                               #draw controls button rectangle
        pygame.draw.rect(screen, GREEN, [410,395,380,75])                               #draw credits button rectangle
        #blit text and images
        screen.blit(Title,(108,-150))                                                   #Draw the title logo on the menu
        screen.blit(playGame,(525,225))                                                 #Write play game on the first button
        screen.blit(Controls,(540,320))                                                 #write controls on the second button
        screen.blit(Credits,(545,405))                                                  #Write credits on the last button

    #------------------------------Hive Graphics---------------------------------------
    elif location == 'hive':                                                            #inside the hive/the store
        screen.blit(hiveBackdrop,(0,0))                                                 #draw premade hive backdrop
        screen.blit(storeButtons,(282,92))                                              #draw on colour shop button
        screen.blit(rightSign,(1150,371))                                               #draw the right sign 
        screen.blit(e,(1169,375))                                                       #write e on the sign
        #PLAYER
        drawHat()                                                                       #draw the hat on the player
        screen.blit(newImg,(playerx,playery))                                           #draw player
        #variables/stats
        pollenCountWord=font.render('Pollen Count = '+str(pollenCount), True, WHITE)    #set text to most recent pollen count
        screen.blit(pollenCountWord,(10,50))                                            #draw pollen count text
        screen.blit(reload,(5,20))                                                      #draw the reload button
        screen.blit(beeNameText,(45,10))                                                #write the bee name
        #shops
        if shop == 'open':                                                              #if a shop is open
            #basic store visuals
            screen.blit(shops,(0,0))                                                    #draw the shop hexagon
            screen.blit(xButton,(1130,0))                                               #draw the x button
            if tooPoor == True:                                                         #If the player is attempting to buy something that they cannot afford,
                screen.blit(lolPoor,(25,650))                                           #remind them that they are poor.
            #colour store
            if store == 'colour':                                                       #if the player opened the colour store:
                screen.blit(colourTitle,(550,130))                                      # write 'colours' as the title
                screen.blit(Red,(505,255))                                              # write in the red button,
                screen.blit(Orange,(505,295))                                           # orange button,
                screen.blit(Yellow,(505,335))                                           # yellow button,
                screen.blit(Lime,(505,375))                                             # lime button,
                screen.blit(LightBlue,(505,415))                                        # light blue button,
                screen.blit(Blue,(505,455))                                             # blue button,
                screen.blit(Purple,(505,495))                                           # and the purple button.
                screen.blit(default,(635,335))                                          # Also, write default next to yellow.
                #prices
                OwnedStatusC()                                                          # Run the owned status function for colours to draw the prices or the checks.
            #hat store
            if store == 'hats':                                                         #if the player opened the colour store:
                screen.blit(hatsTitle,(575,130))                                        # write 'hats' as the title
                screen.blit(topHatT,(490,255))                                          # write in the top hat button,
                screen.blit(catEarsT,(490,295))                                         # cat ears button,
                screen.blit(spinnyHatT,(490,335))                                       # spinny hat button,
                screen.blit(bucketHatT,(490,375))                                       # bucket hat button,
                screen.blit(ballCapT,(490,415))                                         # ball cap button,
                screen.blit(crownT,(490,455))                                           # crown button,
                screen.blit(noHatT,(490,495))                                           # and the no hat button.
                screen.blit(default,(650,495))                                          # Also, write default next to 'no hat'.
                #prices
                OwnedStatusH()                                                          # Run the owned status function for hats to draw the prices or the checks.
            #plant store
            if store == 'plants':                                                       #if the player opened the plant store:
                screen.blit(plantsTitle,(570,130))                                      # write 'plants' as the title
                screen.blit(sunflowersT,(480,255))                                      # write in the sunflower button,
                screen.blit(blueOrchidT,(480,295))                                      # blue orchid button,
                screen.blit(cherryTreeT,(480,335))                                      # cherry tree button,
                screen.blit(appleTreeT,(480,375))                                       # and the apple tree button.
                #prices
                OwnedStatusP()                                                          # Run the owned status function for plants to draw the prices or the checks.
            #manager store
            if store == 'managers':                                                     #if the player opened the manager store:
                screen.blit(managersTitle,(550,130))                                    # write 'Managers' as the title
                screen.blit(Manager1,(470,pinK.ty))                                     # write in the 1st manager button,
                screen.blit(Manager2,(470,aquA.ty))                                     # 2nd manager button,
                screen.blit(Manager3,(470,browN.ty))                                    # and the third manager button.
                #prices
                OwnedStatusM()                                                          # Run the owned status function for managers to draw the prices or the checks.
            #reboot store
            if store == 'reboots':                                                      #if the player opened the reboot store:
                screen.blit(rebootsTitle,(550,130))                                     # write 'Reboots' as the title
                screen.blit(reboot1,(470,pinK.ty))                                      # write in the 2x reboot button,
                screen.blit(reboot2,(470,aquA.ty))                                      # 3x reboot button,
                screen.blit(reboot3,(470,browN.ty))                                     # and the 4x reboot button.
                if quadruple.boughtVar == True:                                         # if the last one has been bought,
                    screen.blit(rebootMessage,(470,400))                                #  tell the player that they can reuse it.
                #prices
                OwnedStatusR()                                                          # Run the owned status function for reboots to draw the prices or the checks.

    #--------------------------Second Field graphics-------------------------
    elif location == 'secondField':                                                     #if the player is in the second field
        pygame.draw.rect(screen, GREEN,[0,420,1200,300])                                #draw the ground
        screen.blit(leftSign,(0,371))                                                   #draw the left sign
        screen.blit(e,(23,375))                                                         #write e on it
        #blit plants
        if appleTreE.boughtVar==True:                                                   #If the apple tree has been bought,
            screen.blit(appleTreeImg,(0,0))                                             # draw the apple tree.
        if cherryTreE.boughtVar==True:                                                  #If the cherry tree has been bought,
            screen.blit(cherryTreeImg,(160,128))                                        # draw the cherry tree.
    appleTreePollenRegen()                                                              #Whether in the second field or not, run the apple tree pollen regen,
    cherryTreePollenRegen()                                                             #and the cherry tree pollen regen.
    if location == 'secondField':                                                       #Back in the second field,
        #pollen count
        pollenCountWord=font.render('Pollen Count = '+str(pollenCount), True, WHITE)    #set text to most recent pollen count
        screen.blit(pollenCountWord,(10,50))                                            #draw pollen count
        screen.blit(beeNameText,(10,10))                                                #write the bee's name on screen
        #PLAYER
        drawHat()                                                                       #draw the player's hat on the bee
        screen.blit(newImg,(playerx,playery))                                           #draw the player/bee
    #----------------------------manager functions-----------------------------
    managerFunctions()                                                                  #Have the managers always adding pollen to the pollen count and draw them if necessary
    
    #==============================EVENTS===================================
    for event in pygame.event.get():                                                    #runs every time an event occurs

        #------------------------Quit Event---------------------------------
        if event.type == QUIT:                                                          #was it the quit event?
            pygame.quit()                                                               #if so quit pygame
            sys.exit()                                                                  #and exit the system

        #-----------------------menu buttons--------------------------------
        if location == 'menu':                                                          #On the main menu
            #mouse motion
            if event.type==MOUSEMOTION:                                                 #WHEN THE MOUSE MOVES,
                mx,my=event.pos                                                         #set the mouse x and y as the event position.
                #play game button visual changes
                if mx>400 and mx<800 and my>200 and my<300:                             #if the mouse moves over the play game button
                    playGame=font.render('Play Game',True,WHITE,GREEN)                  # make the text white,
                else:                                                                   #otherwise
                    playGame=font.render('Play Game',True,darkGreen,GREEN)              # make it dark green.
                #controls button visual changes
                if mx>410 and mx<790 and my>310 and my<385:                             #if the mouse moves over the controls button
                    Controls=font.render('Controls',True,WHITE,GREEN)                   # make the text white,
                else:                                                                   #otherwise
                    Controls=font.render('Controls',True,darkGreen,GREEN)               # make it dark green.
                #credits button visual changes
                if mx>410 and mx<790 and my>395 and my<470:                             #if the mouse moves over the credits button
                    Credits=font.render('Credits',True,WHITE,GREEN)                     # make the text white,
                else:                                                                   #otherwise
                    Credits=font.render('Credits',True,darkGreen,GREEN)                 # make it dark green.
            #clicks
            if event.type==MOUSEBUTTONDOWN:                                             #WHEN THE MOUSE IS CLICKED,
                mx,my=event.pos                                                         #set the mouse x and y as the event position.
                if mx>400 and mx<800 and my>200 and my<300:                             #if you click on the play game button
                    location='main'                                                     # send the player to the main playing screen
                if mx>410 and mx<790 and my>310 and my<385:                             #if you click on the controls button
                    location='Controls'                                                 # send the player to the controls screen
                if mx>410 and mx<790 and my>395 and my<470:                              #if you click on the credits button
                    location='Credits'                                                    # send the player to the credits screen
                                                                                           #    
        #--------------------hive store buttons------------------------------               #
        if location == 'hive' and event.type==MOUSEBUTTONDOWN:                              #If you're in the hive and the mouse button is clicked, the following can happen:
            mx,my=event.pos                                                                 #define the mouse x and y as the event position
            if shop == 'closed':                                                            #When the shops are closed, 
                if mx>5 and mx<40 and my>20 and my<50:                                      #  You can click on the name reload button
                    beeName=random.choice(names)                                            #  which would pick a new name for your bee
                    beeNameText=font.render('Bee\'s Name: '+beeName, True, WHITE)           #  and rewrite it in the name label.
                if mx>282 and mx<367 and my>232 and my<329:                                 #  You can click on the colour shop button,
                    shop = 'open'                                                           #  which would open
                    store = 'colour'                                                        #  the colour store.
                if mx>485 and mx<570 and my>162 and my<259:                                 #  You can click on the plant shop button,
                    shop = 'open'                                                           #  which would open
                    store = 'plants'                                                        #  the plants store.
                if mx>689 and mx<774 and my>232 and my<329:                                 #  You can click on the manager shop button,
                    shop = 'open'                                                           #  which would open
                    store = 'managers'                                                      #  the manager store.
                if mx>891 and mx<976 and my>162 and my<259:                                 #  You can click on the reboot shop button,
                    shop = 'open'                                                           #  which would open
                    store = 'reboots'                                                       #  the reboot store.
                if mx>685 and mx<775 and my>95 and my<195:                                  #  You can click on the hat shop button,
                    shop = 'open'                                                           #  which would open
                    store = 'hats'                                                          #  the hat store.
            colourStoreIfs()                                                                #  You can click on and buy the colours in the colour shop.
            plantStoreIfs()                                                                 #  You can click on and buy the plants in the plant shop.
            hatsStoreIfs()                                                                  #  You can click on and buy the hats in the hat shop.
            managerStoreIfs()                                                               #  You can click on and buy the managers in the manager shop.
            rebootStoreIfs()                                                                #  You can click on and buy the reboots in the reboot shop.
            if mx>1130 and my<75:                                                           #  Finally, you can click on the X button,
                shop = 'closed'                                                             #  which would close the shops
                store = 'none'                                                              #  so that you would have none open.
                    
        #-------------------------basic gameplay---------------------------       
        if location == 'main' or 'hive' or 'secondField':                                   #If the location has the player visible in it, the following can happen.
            #---keydowns---
            if event.type==KEYDOWN:                                                         #is it a key down event?
                #motion
                if event.key==K_LEFT or event.key==K_a:                                     #If left arrow key,
                    left = True                                                             #move player left.
                if event.key==K_RIGHT or event.key==K_d:                                    #If right arrow key,
                    right = True                                                            #move player right.
                if event.key==K_UP or event.key==K_w:                                       #If up arrow key,
                    jumping=True                                                            #move player up.
                #extra buttons                
                if event.key==K_0:              #CHEAT
                    zeroPressed=True            #"
                if event.key==K_LCTRL:          #"
                    ctrlPressed=True            #"
                if event.key==K_COMMA:                                                      #Press COMMA KEY: Volume down
                    volume=volume-0.05                                                      #  take away from the volume number
                    pygame.mixer.music.set_volume(volume)                                   #  set the volume to the smaller number
                if event.key==K_PERIOD:                                                     #Press PERIOD KEY: Volume up
                    volume=volume+0.05                                                      #  add to the volume number
                    pygame.mixer.music.set_volume(volume)                                   #  set the volume to the higher number
                #area change buttons
                if event.key==K_ESCAPE:                                                     #Press ESCAPE KEY:
                    location='menu'                                                         #  take you to the main menu
                if event.key==K_e or event.key==K_RSHIFT:                                   #Press E or SHIFT KEY: Location changer
                    shop = 'closed'                                                         #  make sure the stores are closed
                    store = 'none'                                                          #  and that you havent opened one yet
                    if location == 'secondField':                                           #  If youre in the SECOND FIELD,
                        if playerx<=50:                                                     #  near the left wall,
                            location = 'main'                                               #  it will take you to the main playing screen
                            playerx=1150                                                    #  and the player will appear on the right side of the screen.
                    elif location == 'hive':                                                #  If you're in the HIVE,
                        if playerx>=1110:                                                   #  near the right wall,
                            location = 'main'                                               #  it'll take you to the main playing screen
                            playerx=0                                                       #  and the player will appear on the left side of the screen.
                    elif location == 'main':                                                #  When you're on the MAIN playing screen,                                               
                        if playery>=330 and playery<=379 and playerx<=95:                   #  if you're touching the hive,
                            location = 'hive'                                               #  it'll take you to the hive
                            playerx=1150                                                    #  and the player will appear on the right side of the screen.
                        elif playerx>=1110:                                                 #  But if you're near the right wall,
                            location = 'secondField'                                        #  it'll take you to the second field
                            playerx=0                                                       #  and the player will appear on the left side of the screen.
            #---key ups---
            if event.type==KEYUP:                                                           #is it a key up event?
                if event.key==K_LEFT or event.key==K_a:                                     #if left arrow key up
                    left = False                                                            #don't move player left
                if event.key==K_RIGHT or event.key==K_d:                                    #if right arrow key up
                    right = False                                                           #don't move player right
                if event.key==K_UP or event.key==K_w:                                       #if up arrow key up
                    jumping = False                                                         #fall
                if event.key==K_0:              #CHEAT
                    zeroPressed=False           #"
                if event.key==K_LCTRL:          #"
                    ctrlPressed=False           #"

    #------------------------------------ifs-----------------------------------------------                    
    if zeroPressed == True and ctrlPressed==True:   #CHEAT
        pollenCount=pollenCount+420                 #"

    if frameCounter==tooPoorTimer+60:                                                       #if the frame count is the same as the timer that keep the "too poor" on the screen
        tooPoor=False                                                                       #   remove it from the screen
        tooPoorTimer=3000                                                                   #   and set the timer to an impossible number until it is needed again.

    #---movement functions---        
    if right == True:                                                                       #right key held
        if facing == 'left':                                                                #If the bee image is currently facing left,
            newImg=pygame.transform.flip(newImg,True,False)                                 #   flip the image so he is facing right,
            facing = 'right'                                                                #   and record that he is now facing right.
        moveRight()                                                                         #continue to move right until key up
    if left == True:                                                                        #left key held
        if facing == 'right':                                                               #If the bee image is currently facing right,
            newImg=pygame.transform.flip(newImg,True,False)                                 #   flip the image so he is facing left,
            facing = 'left'                                                                 #   and record that he is now facing left.
        moveLeft()                                                                          #continue to move left until key up
    if jumping == True:                                                                     #up key held
        jump()                                                                              #continue to jump until key up
    if jumping == False:                                                                    #up key not held
        fall()                                                                              #fall back down after jump

    #------------------------------visuals and frames--------------------------------------
    pygame.display.update()                                                                 #updates the visuals to latest version
    fpsClock.tick(FPS)                                                                      #waits the FPS speed to update again
    frameCounter+=1                                                                         #adds 1 to counter every frame
    if frameCounter > 2000:                                                                 #max count is 2000 frames
        frameCounter = 0                                                                    #resets the counter

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
