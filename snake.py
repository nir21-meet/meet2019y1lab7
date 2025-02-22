
import turtle
import random #We'll need this later in the lab
turtle.write("snake game",font=("Arial", 55, "normal"))


turtle.direction=None
turtle.tracer(1,0) #This helps the turtle move more smoothly
score=[]
UP_EDGE = 500
DOWN_EDGE = -500
RIGHT_EDGE = 500
LEFT_EDGE = -500
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
turtle.pensize(22)                            #size.    
turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 7

#Initialize lists
div_pos=[]
div_list=[]
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
divsnake=turtle.clone()
snake = turtle.clone()
snake.TIME_STEP = 100

food=turtle.clone()
snake.shape("turtle")
snake.color("blue")
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    id1 = snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(id1)
    
#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for num  in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]
    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE
 

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()
def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position

snake.direction="Up" 
def up():
    snake.direction="Up" #Change direction to up
    print("You pressed the up key!")
    



turtle.onkeypress(up, "Up") # Create listener for up key
turtle.listen()
def down():
    snake.direction="Down" #Change direction to up
    print("You pressed the down key!")



turtle.onkeypress(down, "Down") # Create listener for up key
turtle.listen()
def right():
    snake.direction="Right" #Change direction to up
    print("You pressed the right key!")



turtle.onkeypress(right, "Right") # Create listener for up key
turtle.listen()
def left():
    snake.direction="Left" #Change direction to up
    print("You pressed the left key!")


turtle.onkeypress(left, "Left") # Create listener for up key
turtle.listen()
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    foodcor=(food_x,food_y)
    food.goto(food_x,food_y)
    food_pos.append(foodcor)
    stamp1=food.stamp()
    food_stamps.append(stamp1)
    stamp=snake.stamp()
    stamp_list.append(stamp)
    
    
    print(len(score)-7)
def div():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    #Pick a position that is a random multiple of SQUARE_SIZE
    div_x = random.randint(min_x,max_x)*SQUARE_SIZE
    div_y = random.randint(min_y,max_y)*SQUARE_SIZE
    divcor=(div_x,div_y)
    divsnake.goto(div_x,div_y)
    div_pos.append(divcor)
    
    stamp2=divsnake.stamp()
    div_list.append(stamp2)

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    for pos in pos_list:
        if pos== my_pos and pos_list.index(pos)==0:
            quit()
        #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
    elif snake.direction=="Right":
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
    elif snake.direction=="Left":
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
    new_stamp()
    
    remove_tail()
     #Add new lines to the end of the function
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif new_x_pos<=LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    elif new_y_pos>=UP_EDGE:
        print("You hit the UP edge! Game over!")
        quit()
    elif new_y_pos<=DOWN_EDGE:
        print("You hit the DOWN edge! Game over!")
        quit()
    ######## SPECIAL PLACE - Remember it for Part 5

    #If snake is on top of food item
    if snake.pos() in food_pos:
        
        score.append("g")
        turtle.write(len(score),font=("Arial", 66, "normal"))
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        snake.TIME_STEP-=10
        print("You have eaten the food!")
        
    if snake.pos() in div_pos:
        div_index=div_pos.index(snake.pos()) #What does this do?
        divsnake.clearstamp(div_list[div_index]) #Remove eaten food stamp
        div_pos.pop(div_index) #Remove eaten food position
        div_list.pop(div_index) #Remove eaten food stamp
        print("You have eaten the food!")
        for clr in range(len(stamp_list)//2):
            stamp_list.pop()
        

    turtle.ontimer(move_snake,snake.TIME_STEP)
    turtle.ontimer(div,100000000000)
    if len(food_stamps)<=6:
        make_food()
    if len(div_list)<=1:
        div()
     # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE
    
turtle.listen()
turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food.shape("trash.gif") 

#Locations of food
food.penup()
# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don't forget to hide the food turtle!
for this_food_pos in food_pos :
    
    food.goto(this_food_pos)
    stamp1=food.stamp()
    food_stamps.append(stamp1)
for this_div_pos in div_list :
    
    divsnake.goto(this_food_pos)
    stamp1=divsnake.stamp()
    div_list.append(stamp1)
    ####WRITE YOUR CODE HERE!!
move_snake()


                
        
        
    


turtle.mainloop()
