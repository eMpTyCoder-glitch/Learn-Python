from turtle import Turtle, Screen
import random 
def generate_random(t):
    r=random.randint(0,90)
    a=random.randint(0,10)
    directions=["Left","Right"]
    rDirections=random.choice(directions)
    t.forward(r)
    if rDirections=="Left":
        t.left(a)
    else:
        t.right(a)

def turtle_position():
    return(Leonardo.pos(),Raphael.pos(),Donatello.pos(),Michelangelo.pos())
    
def find_winner(L,R,D,M):
    max_pos=max(L,R,D,M)
    if L==max_pos:
        return "Leonardo is the winner"
    if R==max_pos:
        return "Raphael is the winner"
    elif D==max_pos:
        return "Donatello is the winner"
    elif M==max_pos:
        return "Michelangelo is the winner"
screen = Screen()
screen.title("Welcome to Turtle Race")
Leonardo=Turtle()
Leonardo.shape("turtle")
Leonardo.color("blue")
Leonardo.teleport(-800,-300)
Leonardo.write("Leonardo")

Raphael=Turtle()
Raphael.shape("turtle")
Raphael.color("Red")
Raphael.teleport(-800,0)
Raphael.write("Raphael")

Donatello=Turtle()
Donatello.shape("turtle")
Donatello.color("Purple")
Donatello.teleport(-800,300)
Donatello.write("Donatello")

Michelangelo=Turtle()
Michelangelo.shape("turtle")
Michelangelo.color("Orange")
Michelangelo.teleport(-800,600)
Michelangelo.write("Michelangelo")


L,R,D,M=turtle_position()
finpoint=1000
while(L[0]<finpoint and R[0]<finpoint and D[0]<finpoint and M[0]<finpoint):
    generate_random(Leonardo)
    generate_random(Raphael)
    generate_random(Donatello)
    generate_random(Michelangelo)
    L,R,D,M=turtle_position()  

screen.title(find_winner(L[0],R[0],D[0],M[0]))
t=Turtle()
t.hideturtle()
t.write(find_winner(L[0],R[0],D[0],M[0]))
screen.mainloop()