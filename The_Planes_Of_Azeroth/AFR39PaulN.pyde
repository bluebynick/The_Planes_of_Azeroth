#UNITSUMMATIVE_R39PaulN.pyde
   # The Planes of Azeroth
   # Nicholas Paul
   # This program is a pull back matrix which will launch a Symbol 
   # at a target from the MMORPG World of Warcraft. Players have
   # the option to play as either the Alliance faction or the 
   # Horde faction, two warring groups in WoW. The symbol lsuncehd
   # is affected by gravity and will trigger an explosion if it
   # hits the target after only one wall bounce, otherwise it'll 
   # pass right over unharmed. There is 4 different sound tracks
   # playing throughout the game and there is also many sound 
   # effects such as explosions. The symbol chosen as missle 
   # will bounces off all the walls and after 4 bounces it will 
   # no longer be contained within the screen and will fall out.
   # After you hit the target 5 times there is a special surprise
   # from one of the game's most loved characters, Lord Jaraxxus. 
"""Key Features:
-two different games to choose from (horde v alliance or alliance v horde)
-text is different for each game
-hit detect after only 1 wall bounce 
-fall out after 4 wall bounces
-hit and bounce counters
-after 5 hits it changes to a timer in seconds (not frames)
-randomly changing background with jarraxxus flying around 
and bouncing off the walls
-Sound in the beggining 
-Sound as he's flying
-Sound in the intro
-Different soundtracks for each game
-Explosion sound effect if target is hit
-Game resets after 8 seconds of jaraxxus madness
-I drew the Horde symbol
-Handed in early"""
   # March 11th 2016, R39
#Setup
add_library('sound')
def setup():
    
    size(1280, 700) #size 
    textSize (width/64) #text size
    textAlign(CENTER) #draw images from the center
    frameRate(40)  #this means the program is set to run the draw() function 40 times in one second.
    initialize() #initialize all the variables

#Methods   

def initialize():
    global posSymbol, posExplode, posHorde, posTurret, posJax #positions 
    global velSymbol, velExplode, velHorde, velJax #velocities
    global sclSymbol, launchSymbol #Symbol symbol properties 
    global hordeFill, sclHorde #horde symbol properties
    global sclJax #jax properties
    global explosion, allianceSymbol, bimage, jax #images
    global backgr, backgr2, backgr3, sclBackgr,backgr, back1 #background properties
    global counter, timer, hitCounter, timerJax #miscelaneous int 
    global introscreen, sequence, hit, appear,mouse #miscelaneous booleans
    global grav #miscelaneous vectors
    global file, fileStart, theme, themeStart, allTheme #sound stuff
    global allThemeStart, horTheme, horThemeStart #sound stuff
    global allMouse, horMouse, exSound, exSoundStart #character select
    
    #Vectors
    posSymbol = PVector(width/4,height/2) #Symbol symbol position
    posExplode = PVector(width/2,height/2) #position of the explosion image
    posTurret = PVector(width/3,height/2) #this is position from where the pull back launching occurs literally just 0,0
    posHorde =  PVector(width/1.2,height/2) #this is the position of the moving target
    posJax = PVector(width/2,height/2) #Jaraxxus' position
    
    velSymbol = PVector () #Symbol symbol velocity
    velExplode = PVector () #velocity of the explosion image
    velHorde = PVector(10,10) #horde symbol velocity
    velJax = PVector (100,100) #jarraus' velocity

    grav = PVector(0,.4) #gravity
    
    #Variables
    allianceSymbol = loadImage("AllianceSymbol.png") #assigning images to variables to be called later
    explosion = loadImage("explosion.png")
    bimage= loadImage("lichKing.jpg")
    jax = loadImage("jaxGif.gif")
    sclSymbol=.2 #scale the alliance symbol
    sclHorde = 1 #scale the horde symbol
    sclBackgr=width*0.00056 #scale the background
    sclJax = width/width #scale jaraxxus
    launchSymbol=False #boolean for symbol launch
    introscreen=False #boolean for the welcome screen change
    hit = False #boolean to register a hit
    appear = False #boolean to make the explosion appear
    mouse = False #boolean to ensure the mouse is clicked at a certain time
    allMouse = False #boolean to start the alliance version of the game
    horMouse = False #boolean to start the horde version of the game
    back1 = False #boolean to initialize the first background image only
    counter=0
    timer= 75 #idk why but my code is too big so framerate slows to approx. 25 fps
              #every time hit is registered so i changed timer to accomodate
    hitCounter= 0 #hit counter
    backgr = 0 #background variables that are able to randomize later
    backgr2 = 0
    backgr3 = 0
    hordeFill = backgr #to ensure the "see-through" parts of the horde symbol are still "see-through"
    file = SoundFile(this,"jaraxxus.mp3") #sounds
    theme = SoundFile(this, "wowTheme.mp3")
    allTheme = SoundFile(this, "allTheme.mp3")
    horTheme = SoundFile(this, "horTheme.mp3") 
    exSound = SoundFile(this, "exSound.mp3")
    fileStart = False #booleans to ensure each sound plays once
    themeStart = False
    allThemeStart = False
    horThemeStart = False
    exSoundStart = False
    timerJax = 900 #timer before jaraxxus and reset
    
def alliance(): #draw the alliance symbol
    imageMode(CENTER) #this is to draw the images in this method from the center
    pushMatrix(); 
    image(allianceSymbol,0,0)
    popMatrix()
    
def horde(): #draw the horde symbol
     pushMatrix()
     noStroke();
     fill(255, 0, 0);
     triangle(18,16,80,-15,17,98);
     triangle(-83,-16,-15,18,-17,120);
     triangle(0,-100,-70,-30,70,-30);
     rect(-67,-30,132,43);
     rect(43,-30,25,30);
    
     #black around middle triangle 
     stroke(hordeFill);
     fill(hordeFill);
     arc(0,-10, 60, 120, 0, 180); 
    
     #middle triangle
     fill(255, 0, 0);
     noStroke();
     triangle(-18,-25,18,-25,0,-50);
     triangle(-18,-25,18,-25,0,0);
    
     #top lines and triangles
     line(0,-100,40,-60);
     line(0,-100,-40,-60);
     triangle(40,-60,50,-50,52,-64);
     triangle(-40,-60,-50,-50,-52,-64);
     line(-40,-60,-70,-30);
     line(40,-60,70,-30);
    
     #left and right arcs
     fill(hordeFill);
     arc(-68,-20,8,20,-119,110);
     arc(68,-20,8,20,-290,-56);
     line(-81,-15,-68,-9);
     line(68,-9,81,-15);
     line(81,-15,62,15);
     line(-88,-15,-67,15);
    
     #bottom left arc and down
     arc(-57,42,36,61,-129,14);
     arc(-57,42,36,66,0,51);
     line(-53,47,-17,120);
     line(-17,120,-16,27);
    
    #bottom right arc and down
     arc(55,28,25,28,53,144);
     line(53,33,17,98);
     line(17,98,17,27);
     popMatrix()     
    
def drawSymbol(): #draw the projectile
    global posSymbol,sclSymbol,allianceSymbol,posExplode,introscreen, horMouse,allMouse, sclHorde
    imageMode(CENTER) #this is to draw the images in this method from the center
    
    pushMatrix(); 
    translate(posSymbol.x,posSymbol.y);  
    #this reorients the origin to be at the posSymbol.x and posSymbol.y variables

    if(allMouse == True) or (introscreen == False): #if it's the alliance game the projectile is the alliance symbol
        scale(sclSymbol) #scale it to the alliance scale
        alliance() 
    if(horMouse == True): #if it's the horde game the projectile is the horde symbol
        scale(sclHorde) #scale it to the horde scale
        horde()
    
    popMatrix(); #this essentially resets the origin 
                                           
def drawExplode(): #draw the explosion
    global posExplode, explosion, hit, exSound, exSoundStart
    imageMode(CENTER) #this is to draw the images in this method from the center
    pushMatrix(); 
    
    translate(posExplode.x,posExplode.y); 
    #this reorients the origin to be at the posExplode.x and posExplode.y variables
    
    image(explosion,0,0)
    if(exSoundStart == False): #activate the explosion sound effect only once
        exSound.play()
        exSoundStart = True
    
    
    
    popMatrix()
    
def drawTarget(): #this is the target symbol
    
    global posHorde, hordeFill, sclHorde, sclSymbol, allMouse, horMouse,allianceSymbol
    
    pushMatrix()
    translate(posHorde.x,posHorde.y)
    #this reorients the origin to be at the posHorde.x and posHorde.y variables
    if(allMouse == True) or (introscreen == False): #if it's the alliance game the target is the horde
        scale(sclHorde) #assign the horde scale to the horde target  
        horde()
    
    if(horMouse == True): #if it's the horde game the target is the alliance
        scale(sclSymbol) #assign the alliance scale to the alliance symbol
        alliance()
 
    popMatrix(); #this essentially resets the origin
    
def moveSymbol(): #below is the moving of the projectile 
    global vel,pos,grav,gravity,sclSymbol,velSymbol
    global posSymbol,counter, allMouse, horMouse
     
    pushMatrix();
    translate(posSymbol.x, posSymbol.y); 
    posSymbol.add(velSymbol) #move the Symbol by the Symbol velocity
    velSymbol.add(grav) #add gravity to the symbol's velocity
    
    if(counter <4):
        if(posSymbol.x+sclSymbol*235>width) or (posSymbol.x<sclSymbol*235) : 
            velSymbol.x*=-1  #if the object reaches the end of the
                               #screen reverse it's direction
                               #if the object reaches the beggining
                               #of the screen reverse it's direction
            counter +=1
        if(allMouse == True):
            if(posSymbol.y+sclSymbol*280>height) or (posSymbol.y-sclSymbol*200 <0):
                velSymbol.y*=-1 #if the object reaches the bottom of 
                              #the screen reverse it's direction
                              #if the object reaches the top of 
                              #the screen reverse it's direction
                counter +=1
                velSymbol.add(grav) #this is to assure after every bounce it's only
                                    #increasing velSymbol by grav
        if(horMouse == True):
            if(posSymbol.y+sclSymbol*590>height) or (posSymbol.y<sclSymbol*460):           
                velSymbol.y*=-1 #if the object reaches the bottom of 
                              #the screen reverse it's direction
                              #if the object reaches the top of 
                              #the screen reverse it's direction
                counter +=1
                velSymbol.add(grav) #this is to assure after every bounce it's only
                                    #increasing velSymbol by grav 
    popMatrix()
    
def mouseClicked(): 
    global posSymbol, posTurret, velSymbol, launchSymbol,introscreen,counter,mouse, allMouse, horMouse, theme
    if(mouse == True):
        counter =0
        posSymbol.x = mouseX   
        posSymbol.y = mouseY
        launchSymbol = True #Variable Initialized as false so missle won't draw until mouse clicked
        velSymbol.set(posTurret.x,posTurret.y)  #sets the values of posTurret and assigns it to velSymbol
        velSymbol.sub(posSymbol) #the value of posSymbol minus velSymbol.  The result is placed in the velSymbol 
        velSymbol.mult(.1) #becuase the value is so large, it is being scaled down by being multiplied by a decimal
    
    else:
        if(mouseX<width/2): #if it's clicked on the left side of the screen run the allinace game
            allMouse = True 
            introscreen = True #stop the intro screen
            theme.stop() #stop the intro music
        else:
            horMouse = True #if it's clicked on the right side of the screen run the horde game
            introscreen = True #stop the intro screen
            theme.stop() #stop the intro music

def pullBack(): #drawing the line
    global posTurret
    
    stroke(255)
    line(posTurret.x,posTurret.y,mouseX, mouseY)

def colDetect():  

    global colDist, posExplode, posHorde, posSymbol, hit, counter 

    colDist = posHorde.dist(posSymbol) # colDist is the distance between the target and 
                                         # Symbol
     
    if(counter == 1) and (colDist <150): #if it's only bounced off one wall and the distance
                                         #is less than 150 pixels, run the code

        posExplode.x = posHorde.x #put the exlosion where the target was
        posExplode.y = posHorde.y
        
        posSymbol.x = width*2 #move the symbol off the screen
        posSymbol.y = height*2
        
        if(counter == 1): 
            hit = True # turn hit true
        
def default(): #this is what happens after an explosion or immediately after the intro screen
               #leaves
               
    global hit,timer, counter,backgr,bimage,hitCounter,mouse
    background(backgr) #this is just to help with the horde symbol colouring; assigns
                       #background to the backgr coulour
    posSymbol = width*2 #the symbol starts resets off the screen
    posSymbol = height*2
    pullBack() #pullBack method
    if(allMouse == True): #specific text for the alliance game
        drawTarget() #draw the target
        fill(255)
        textSize(20)
        text("Target Hits:", width/2.3,height/11)
        text(hitCounter, width/2,height/11)
        text("Bounces:", width/2.3,height/7)
        text("Click the mouse to launch an Alliance Symbol. The longer the line, the faster the inital velocity", width /2, height/5.25)
        text("Try to hit that nasty horde symbol, it'll trigger a explosion if you hit it after 1 wall bounce. FOR THE ALLIANCE!",width/2,height/4)
        text("After 4 bounces or if you hit the horde symbol,", width/2, height/3.3)
        text("the alliance symbol will disapear and you'll have to wait 3 seconds to click again.",width/2,height/2.8)
        text("Warning: after you destroy the horde 5 times, they'll get mad...", width/2, height/2.4)
        text("Legal Disclaimer: Do not stay on the final screen for too long, epilepsy warning", width/2, height/1.1)
    #Instructional text
    if(horMouse == True): #specific text for the horde game
        drawTarget()
        fill(255)
        textSize(20)
        text("Target Hits:", width/2.3,height/11)
        text(hitCounter, width/2,height/11)
        text("Bounces:", width/2.3,height/7)
        text("Click the mouse to launch a Horde Symbol. The longer the line, the faster the inital velocity", width /2, height/5.25)
        text("Try to hit that weak Alliance symbol, it'll trigger a explosion if you hit it after 1 wall bounce. FOR THE HORDE!",width/2,height/4)
        text("After 4 bounces or if you hit the alliance symbol,", width/2, height/3.3)
        text("the horde symbol will disapear and you'll have to wait 3 seconds to click again.",width/2,height/2.8)
        text("Warning: after you destroy the alliance 5 times, they'll get mad...", width/2, height/2.4)
        text("Legal Disclaimer: Do not stay on the final screen for too long, epilepsy warning", width/2, height/1.1)
        
        
    colDetect() #detect a collision
    mouse = True #the mouse is clicked
    
def reset(): #this resets the code after the explosion to keep it running 
    
    global colDist, posExplode, posHorde, posSymbol, hit,timer, exSoundStart,hitCounter
    posExplode.x = width*2 #move the explosion off the screen
    posExplode.y = height*2
    counter = 0 #reset the counter
    hit = False #it hasn't hit yet
    launchSymbol = False #it hasn't launched yet
    exSoundStart = False #the explosion sound hasn't started
    posSymbol.x = width*2 #the Symbol sybol's off the screen
    posSymbol.y = height*2
    posHorde.x=random(0,width) #randomizes posistion of horde symbol
    posHorde.y=random(0,height)
    timer = 75 #reset the timer
    hitCounter = hitCounter+1
    
def jaxSound():
    global fileStart, file,timerJax 
    if(fileStart == False): #this is to play the jaraxxus song only once
        file.play()
        fileStart = True
        if(timerJax <=-150): #reset the whole code after 8 seconds of jaraxxus
            file.stop()
            initialize()
        
def jaxBack(): #randomize the background for jaraxxus
    global backgr,backgr2,backgr3
    backgr=random(0,255)
    backgr2=random(0,255)
    backgr3=random(0,255)
    background(backgr,backgr2,backgr3)
    drawJax()
    
def drawJax(): #draw the jaraxxus image
    global posJax,sclJax,jax
    imageMode(CENTER) #this is to draw the images in this method from the center
    pushMatrix(); 
    translate(posJax.x,posJax.y);  
    #this reorients the origin to be at the posJax.x and posJax.y variables 
    scale(sclJax) #this assigns the scale to be the sclJax variable
    image(jax,0,0)
    popMatrix(); #this essentially resets the origin 

def moveJax(): #move jaraxxus
    global velJax,posJax,sclJax,velJax,posJax,counter
     
    pushMatrix();
    translate(posJax.x, posJax.y); 
    
    
    scale(sclJax) #this assigns the scale to be the sclJax variable
    posJax.add(velJax) #move the Jax by Jax velocity
    
    if(posJax.x+sclJax*130>width) or (posJax.x<sclJax*117) : 
        velJax.x*=-1           #if the object reaches the end of the
                               #screen reverse it's direction
                               #if the object reaches the beggining
                               #of the screen reverse it's direction
        
    if(posJax.y+sclJax*163>height) or (posJax.y<sclJax*175):
        velJax.y*=-1          #if the object reaches the bottom of 
                              #the screen reverse it's direction
                              #if the object reaches the top of 
                              #the screen reverse it's direction 
    popMatrix()
    
def welcome(): #intro screen
    global introscreen,bimage,sclBackgr,back1,theme,themeStart
    if(back1 == True): #this is here because the background continually
                       #draws itself overtop and displaces. Workaround.
        pushMatrix(); 
        scale(sclBackgr) #this assigns the scale to be the sclBackgr variable 
        image(bimage,width/1.5, height/1.5)
        popMatrix(); #this resets the origin  
    drawTarget() #draw the "target" on the intro screen
    drawSymbol() #draw the non-moving "projectile" on the intro screen
    fill(255)
    textSize(25) #intro text
    text("Welcome to Azeroth, upon whose planes we do battle...", width/2,height/1.15)
    fill(255)
    text("Click the alliance or the horde symbol with the mouse", width/2,height/1.05)
    textSize(100)
    text("CHOOSE YOUR SIDE", width /2, height/4)    
    #introduction text    
    back1 = True #boolean for workaround

def SymbolGame():
    global launchSymbol, instruct1,counter,introscreen,hit,timer, timerJax,hitCounter,file,fileStart
    if(introscreen==True) and (hitCounter < 5): #if we're past the welcome screen and there is less than 5 hits
        default() #run the base program
        if (launchSymbol == True): #once the symbol is launched
            moveSymbol()  #run the move symbol method
            if(hit==True):  #if it hits the target
                drawExplode() #draw the explosion
                timer = timer -1  #decrease the timer by 1
                counter = 0 #reset the counter
                if (timer ==0): #if the timer is 0
                    reset() #run the reset
            else: #if there is no hit
                drawSymbol() #keep drawing the symbol
                fill(255) #instructions
                text(counter, width/2,height/7)
                moveSymbol() #keep moving the symbol
                colDetect() #check for collisions
                                    
def draw ():
    global launchSymbol, instruct1,counter,introscreen,hit,timer
    global timerJax,hitCounter,file, allianceSymbol,fileStart 
    global allMouse,horMouse, allTheme, allThemeStart, horTheme, horThemeStart,theme, themeStart
    print (hit,timer,frameRate,introscreen, timerJax)
    if(themeStart == False): #this is to assure that the track only plays once
        theme.play() #play the intro music
        themeStart = True 
    if(introscreen== True) and (allMouse == True): #play the alliance game
        SymbolGame() 
        if(allThemeStart == False):
            allTheme.play() #play the alliance background music
            allThemeStart = True
    if(introscreen== True) and (horMouse == True): #play the horde game
        SymbolGame() 
        if(horThemeStart == False): 
            horTheme.play() #play the horde background music
            horThemeStart = True
    
    if(introscreen==True) and (hitCounter >= 5): #if 5 hits happen, oh man get ready
        allTheme.stop() #stop all the music
        horTheme.stop()
        background(0)
        jaxSound() #play jax's soundtrack
        timerJax = timerJax -1
        textSize(25) #jax instructions
        text("Wait for the timer to expire", width/2, height/1.5)
        textSize(100)
        text(timerJax/40, width/3, height/2)
        text("SECONDS",width/1.7, height/2) 
        #I know this timer is tedious but I kept it in cause I 
        #feel like it creates a buildup  
        #I am completely capable of taking it out
        if(-600 <timerJax <=0): #start the madness
            jaxBack()
            drawJax()
            moveJax()
        if(timerJax <=-600): #after 8 seconds of madness reset the game
            file.stop() #stop jax's music
            initialize()
               
    if(introscreen==False):
        welcome() #at the beggining run welcome()
        

        