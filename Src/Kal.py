import time
import random
import tkinter 
import os
import numpy 
import simpleaudio as sa


ch=0

print("Hello I am Kal , " )
print("Your personal assistant.....")
wave_obj = sa.WaveObject.from_wave_file("Assets//Phrase 1 Intro.wav")
play_obj = wave_obj.play()
play_obj.wait_done()
time.sleep(3)
print(" ")

for i in range(0,15):
    print("*****" , end = " ")
    time.sleep(0.1)

print(' ')

def Choice( ):
    global ch
    print (''' Here are a list of things i can do for you
1.  Set a Timer [ enter timer ]
2.  Play a game [ enter game ]
3.  Solve Quadratic Equations [ enter solve ]
4.  Convert Text to Binary [ enter binary ]
5.  Convert Text to Morse code [ enter morse ]
6.  Convert text to PigLatin [ enter piglatin ]
7.  Print the Fibbonaci Series upto n terms [ enter fib ]
8.  Shop Online [ enter shop ]
9.  Understand Kal [ enter UK]
10. Play a sound of any specific frequency [ enter sound]
11. Dice Roll Simulator [ enter dice]
12. Play some of your favourite songs [ enter song ]
13. Solve a Sudoku for you[ enter sudoku ]
14. To draw multiple types of Shapes [ enter shapes ] ''')
    wave_obj = sa.WaveObject.from_wave_file("Assets//Choice 2.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    ch = input("\nJust enter the number of what you want to do : ")
    ch = ch.upper( )
    if(ch=="TIMER" or ch=="1"):
        timer( )
    elif(ch=="GAME"or ch=="2"):
        Game( ) 
    elif(ch=="SOLVE"or ch=="3"):
        Solve( )
    elif(ch=="BINARY"or ch=="4"):
        Binary( )
    elif(ch=="MORSE"or ch=="5"):
        Morse( )
    elif(ch=="PIGLATIN"or ch=="6"):
        PigLatin( )
    elif(ch=="FIB"or ch=="7"):
        Fib( )
    elif(ch=="SHOP"or ch=="8"):
        Shop( )
    elif(ch=="UK" or ch=="9"):
        import Information
        print("")
        Choice( )
    elif(ch=="SOUND" or ch =="10"):
        import SimpleSound 
        print("")
        Choice( )
    elif(ch=="DICE" or ch=="11"):
        import dice
        print("")
        Choice( ) 
    elif(ch == "SONG" or ch=="12"):
        import Songs
        print("")
        Choice( )
    elif(ch =="SUDOKU" or ch=="13"):
        import SudokuSolver
        print("")
        Choice( )
    elif(ch=="SHAPES" or ch=="14"):
        import Shapes
        print(" ")
        Choice( )     
    
    else:
        print("Invaild Choice\n")
        Choice( )

         
def timer( ) :
    t = float(input("Enter how long you want the timer to be in minutes : "))
    for x in range(1 ,int( t*60+1)):
        if( x % 15 ==0):
            print("T - " , x , end = " seconds ")              

        time.sleep(0.9)
    print("Time up ") 

def Game( ):
    print('''I have five games you can play
1. I try and guess the number you thinking of in under 12 tries
2. Tik Tak Toe [2 player game]
3. Hand Cricket
4. HangMan [ Animals and Words ]
5. Adventure Game
6. Snake Game ''')
    
    wave_obj = sa.WaveObject.from_wave_file("Games Voice.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    ch=int(input("Enter your choice : "))
    for i in range(0,15):
        print("*****" , end = " ")
        time.sleep(0.1)
    print("")    
    if(ch==1):
        NG( )
    elif(ch==2):
        TicTacToe( )
    elif(ch==3):
        HC( )
    elif(ch==4):
        HM( )
    elif(ch==5):
        AG( )
    elif(ch==6):
        SnakeGame( ) 
        
def NG( ):
    print("Hello !!!")
    print("My name is Jarvis , I am a master of mathematics and strategy ")
    time.sleep(1)
    for x in range ( 0 , 20):
        print("*****" , end="")
        time.sleep(0.1)
   
    time.sleep(1)
    print("\nThink of a number between 0 to 1000")
    time.sleep(5)
    print("Done ?")
    time.sleep(1)
    print("Well done ")
    ch = 'n'
    s=0
    l=1000
    m=500
    count = 1
    while( ch == 'n') :
        print(" Is your number above " , m)
        k = input("y/n or enter e if equal ")
        if(k=='n'):
            l=m
        elif(k=='y'):
            s=m
        elif(k=='e'):
            print(" Your number is found " , m , " and it only took me " , count , " guesses")
            break 
        m=int((l+s)//2)
        count = count + 1    


def TicTacToe( ):
    os.system("TicTacToeCode.py")
    Choice( ) 

def HC( ):
    import main
    print("")
    Choice( ) 

def HM( ):
    import Hangman
    print("")
    Choice( ) 

def AG( ):
    import AdventureGame
    print("")
    Choice( )

def Solve( ):
    print(" a * x^2  +  b * x  + c = 0")
    a=float(input("Enter value of a"))
    b=float(input("Enter value of b"))
    c=float(input("Enter value of c"))
    x1 =( -b + 4*a*c + (((b**2 ) - 4*a*c)**0.5))/2
    x2 =( -b + 4*a*c - (((b**2 ) - 4*a*c)**0.5))/2
    print(" x = " , x1 ," , " , x2)
    Choice( ) 
    
def Binary( ):
    test_str = input("Enter a phrase or word to convert to Binary")
    print("The original string is : " + str(test_str)) 
    res = ''.join(format(ord(i), 'b') for i in test_str) 
    print("The string after binary conversion : " + str(res))
    Choice( )


def Morse( ):
    import Morse
    Morse.main( )
    Choice( )
    
def PigLatin( ):
    import PigLatin
    PigLatin.main( )
    Choice( )

def Fib( ):
    nterms = int(input("How many terms? "))

    # first two terms
    n1, n2 = 0, 1
    count = 0

# check if the number of terms is valid
    if nterms <= 0:
       print("Please enter a positive integer")
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    else:
       print("Fibonacci sequence:")
       while count < nterms:
           print(n1)
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1
    Choice( )

    
def Shop( ) :
    import ShoppingApp
    ShoppingApp.main( )
    Choice( ) 
    
def SnakeGame( ):
    
    try:
        import SnakeGame
    except :
        print(" ") 
    finally:
        Choice( )
    




    
Choice( )
m=input("Do you want me to do any other task [y/n]")
m = m.strip( ) 
if(m=='y'):
    print("\n\n")
    Choice( )
elif(m=='n'):
    print("Thank you for letting me assist you")







        
