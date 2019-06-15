import motor
from time import sleep
left_have='R'
right_have='Y'
test="D2 R' D' F2 B D R2 D2 R' F2 D' F2 U' B2 L2 U2 D R2 U"
#left:0|grep:400,clkwise:0
R_Y={"B":[1,1,0],"G":[0,1,0],"W":[1,2,0],"O":[0,2,0]}
R_G={"B":[1,2,0],"Y":[1,1,0],"W":[0,1,0],"O":[0,2,0]}
R_B={"G":[1,2,0],"Y":[0,1,0],"W":[1,1,0],"O":[0,2,0]}
R_W={"G":[1,1,0],"Y":[1,2,0],"B":[0,1,0],"O":[0,2,0]}
Y_O={"G":[0,1,0],"R":[1,2,0],"W":[0,2,0],"B":[1,1,0]}
Y_B={"G":[1,2,0],"R":[1,1,0],"W":[0,2,0],"O":[0,1,0]}
Y_G={"R":[0,1,0],"B":[1,2,0],"W":[0,2,0],"O":[1,1,0]}
G_O={"R":[1,2,0],"Y":[1,1,0],"W":[0,1,0],"B":[0,2,0]}
G_W={"R":[0,1,0],"Y":[1,2,0],"B":[0,2,0],"O":[1,1,0]}
B_W={"G":[0,2,0],"Y":[1,2,0],"R":[1,1,0],"O":[0,1,0]}
B_O={"G":[0,2,0],"Y":[0,1,0],"W":[1,1,0],"R":[1,2,0]}
W_O={"G":[1,1,0],"Y":[0,2,0],"R":[1,2,0],"B":[0,1,0]}

Y_R={"B":[0,1,0],"G":[1,1,0],"W":[0,2,0],"O":[1,2,0]}
G_R={"B":[0,2,0],"Y":[0,1,0],"W":[1,1,0],"O":[1,2,0]}
B_R={"G":[0,2,0],"Y":[1,1,0],"W":[0,1,0],"O":[1,2,0]}
W_R={"G":[0,1,0],"Y":[0,2,0],"B":[1,1,0],"O":[1,2,0]}
O_Y={"G":[1,1,0],"R":[0,2,0],"W":[1,2,0],"B":[0,1,0]}
B_Y={"G":[0,2,0],"R":[0,1,0],"W":[1,2,0],"O":[1,1,0]}
G_Y={"R":[1,1,0],"B":[0,2,0],"W":[1,2,0],"O":[0,1,0]}
O_G={"R":[0,2,0],"Y":[0,1,0],"W":[1,1,0],"B":[1,2,0]}
W_G={"R":[1,1,0],"Y":[0,2,0],"B":[1,2,0],"O":[0,1,0]}
W_B={"G":[1,2,0],"Y":[0,2,0],"R":[0,1,0],"O":[1,1,0]}
O_B={"G":[1,2,0],"Y":[1,1,0],"W":[0,1,0],"R":[0,2,0]}
O_W={"G":[0,1,0],"Y":[1,2,0],"R":[0,2,0],"B":[1,1,0]}
def decide(mark):
    global left_have,right_have
    if left_have=="R" and right_have=="Y":
        return R_Y.get(mark)
    elif left_have=="R" and right_have=="G":
        return R_G.get(mark)
    elif left_have=="R" and right_have=="B":
        return R_B.get(mark)
    elif left_have=="R" and right_have=="W":
        return R_W.get(mark)
    elif left_have=="Y" and right_have=="O":
        return Y_O.get(mark)
    elif left_have=="Y" and right_have=="B":
        return Y_B.get(mark)
    elif left_have=="Y" and right_have=="G":
        return Y_G.get(mark)
    elif left_have=="G" and right_have=="O":
        return G_O.get(mark)
    elif left_have=="G" and right_have=="W":
        return G_W.get(mark)
    elif left_have=="B" and right_have=="W":
        return B_W.get(mark)
    elif left_have=="B" and right_have=="O":
        return B_O.get(mark)
    elif left_have=="W" and right_have=="O":
        return W_O.get(mark)
    elif left_have=="Y" and right_have=="R":
        return Y_R.get(mark)
    elif left_have=="G" and right_have=="R":
        return G_R.get(mark)
    elif left_have=="B" and right_have=="R":
        return B_R.get(mark)
    elif left_have=="W" and right_have=="R":
        return W_R.get(mark)
    elif left_have=="O" and right_have=="Y":
        return O_Y.get(mark)
    elif left_have=="B" and right_have=="Y":
        return B_Y.get(mark)
    elif left_have=="G" and right_have=="Y":
        return G_Y.get(mark)
    elif left_have=="O" and right_have=="G":
        return O_G.get(mark)
    elif left_have=="W" and right_have=="G":
        return W_G.get(mark)
    elif left_have=="W" and right_have=="B":
        return W_B.get(mark)
    elif left_have=="O" and right_have=="B":
        return O_B.get(mark)
    elif left_have=="O" and right_have=="W":
        return O_W.get(mark)

def clkwise_D():
    global left_have,right_have
    if left_have=="Y":
        motor.posi_unit("left",1)
    elif right_have=="Y":
        motor.posi_unit("right",1)
    else:
        own,deg,dir=decide("Y")
        if own==0:
            left_have="Y"
            motor.posi_group("right",deg)
            motor.posi_unit("left",1)
        else:
            right_have="Y"
            motor.posi_group("left", deg)
            motor.posi_unit("right",1) 
def clkwise_R():
    global left_have,right_have
    if left_have=="O":
        motor.posi_unit("left", 1)
    elif right_have=="O":
        motor.posi_unit("right", 1)
    else:
        own,deg,dir=decide("O")
        if own==0:
            left_have="O"
            motor.posi_group("right", deg)
            motor.posi_unit("left", 1)
        else:
            right_have="O"
            motor.posi_group("left",deg)
            motor.posi_unit("right",1)
def clkwise_U():
    global left_have,right_have
    if left_have=="W":
        motor.posi_unit("left", 1)
    elif right_have=="W":
        motor.posi_unit("right", 1)
    else:
        own,deg,dir=decide("W")
        if own==0:
            left_have="W"
            motor.posi_group("right", deg)
            motor.posi_unit("left", 1)
        else:
            right_have="W"
            motor.posi_group("left", deg)
            motor.posi_unit("right", 1)
def clkwise_F():
    global left_have,right_have
    if left_have=="B":
        motor.posi_unit("left", 1)
    elif right_have=="B":
        motor.posi_unit("right", 1)
    else:
        own,deg,dir=decide("B")
        if own==0:
            left_have="B"
            motor.posi_group("right", deg)
            motor.posi_unit("left", 1)
        else:
            right_have="B"
            motor.posi_group("left", deg)
            motor.posi_unit("right", 1)
def clkwise_L():
    global left_have,right_have
    if left_have=="R":
        motor.posi_unit("left", 1)
    elif right_have=="R":
        motor.posi_unit("right", 1)
    else:
        own,deg,dir=decide("R")
        if own==0:
            left_have="R"
            motor.posi_group("right", deg)
            motor.posi_unit("left", 1)
        else:
            right_have="R"
            motor.posi_group("left", deg)
            motor.posi_unit("right", 1)
def clkwise_B():
    global left_have,right_have
    if left_have=="G":
        motor.posi_unit("left", 1)
    elif right_have=="G":
        motor.posi_unit("right", 1)
    else:
        own,deg,dir=decide("G")
        if own==0:
            left_have="G"
            motor.posi_group("right", deg)
            motor.posi_unit("left", 1)
        else:
            right_have="G"
            motor.posi_group("left", deg)
            motor.posi_unit("right", 1)
def anticlk_B():
    global left_have,right_have
    if left_have=="G":
        motor.nega_unit("left", 1)
    elif right_have=="G":
        motor.nega_unit("right", 1)
    else:
        own,deg,dir=decide("G")
        if own==0:
            left_have="G"
            motor.posi_group("right", deg)
            motor.nega_unit("left", 1)
        else:
            right_have="G"
            motor.posi_group("left", deg)
            motor.nega_unit("right", 1)
def anticlk_L():
    global left_have,right_have
    if left_have=="R":
        motor.nega_unit("left", 1)
    elif right_have=="R":
        motor.nega_unit("right", 1)
    else:
        own,deg,dir=decide("R")
        if own==0:
            left_have="R"
            motor.posi_group("right", deg)
            motor.nega_unit("left", 1)
        else:
            right_have="R"
            motor.posi_group("left", deg)
            motor.nega_unit("right", 1)
def anticlk_R():
    global left_have,right_have
    if left_have=="O":
        motor.nega_unit("left", 1)
    elif right_have=="O":
        motor.nega_unit("right", 1)
    else:
        own,deg,dir=decide("O")
        if own==0:
            left_have="O"
            motor.posi_group("right", deg)
            motor.nega_unit("left", 1)
        else:
            right_have="O"
            motor.posi_group("left", deg)
            motor.nega_unit("right", 1)
def anticlk_D():
    global left_have,right_have
    if left_have=="Y":
        motor.nega_unit("left", 1)
    elif right_have=="Y":
        motor.nega_unit("right", 1)
    else:
        own,deg,dir=decide("Y")
        if own==0:
            left_have="Y"
            motor.posi_group("right", deg)
            motor.nega_unit("left", 1)
        else:
            right_have="Y"
            motor.posi_group("left", deg)
            motor.nega_unit("right", 1)
def anticlk_U():
    global left_have,right_have
    if left_have == "W":
        motor.nega_unit("left", 1)
    elif right_have == "W":
        motor.nega_unit("right", 1)
    else:
        own, deg, dir = decide("W")
        if own == 0:
            left_have = "W"
            motor.posi_group("right", deg)
            motor.nega_unit("left", 1)
        else:
            right_have = "W"
            motor.posi_group("left", deg)
            motor.nega_unit("right", 1)
def anticlk_F():
    global left_have,right_have
    if left_have=="B":
        motor.nega_unit("left", 1)
    elif right_have=="B":
        motor.nega_unit("right", 1)
    else:
        own,deg,dir=decide("B")
        if own==0:
            left_have="B"
            motor.posi_group("right", deg)
            motor.nega_unit("left", 1)
        else:
            right_have="B"
            motor.posi_group("left", deg)
            motor.nega_unit("right", 1)
def clk_B2():#####################180
    global left_have,right_have
    if left_have=="G":
        motor.posi_unit("left", 2)
    elif right_have=="G":
        motor.posi_unit("right", 2)
    else:
        own,deg,dir=decide("G")
        if own==0:
            left_have="G"
            motor.posi_group("right", deg)
            motor.posi_unit("left", 2)
        else:
            right_have="G"
            motor.posi_group("left", deg)
            motor.posi_unit("right", 2)
def clk_L2():
    global left_have,right_have
    if left_have == "R":
        motor.posi_unit("left", 2)
    elif right_have == "R":
        motor.posi_unit("right", 2)
    else:
        own, deg, dir = decide("R")
        if own == 0:
            left_have = "R"
            motor.posi_group("right", deg)
            motor.posi_unit("left", 2)
        else:
            right_have = "R"
            motor.posi_group("left", deg)
            motor.posi_unit("right", 2)
def clk_R2():
    global left_have,right_have
    if left_have=="O":
        motor.posi_unit("left", 2)
    elif right_have=="O":
        motor.posi_unit("right", 2)
    else:
        own,deg,dir=decide("O")
        if own==0:
            left_have="O"
            motor.posi_group("right", deg)
            motor.posi_unit("left", 2)
        else:
            right_have="O"
            motor.posi_group("left", deg)
            motor.posi_unit("right", 2)
def clk_D2():
    global left_have,right_have
    if left_have=="Y":
        motor.posi_unit("left", 2)
    elif right_have=="Y":
        motor.posi_unit("right", 2)
    else:
        own,deg,dir=decide("Y")
        if own==0:
            left_have="Y"
            motor.posi_group("right", deg)
            motor.posi_unit("left", 2)
        else:
            right_have="Y"
            motor.posi_group("left", deg)
            motor.posi_unit("right", 2)
def clk_U2():
    global left_have,right_have
    if left_have == "W":
        motor.posi_unit("left", 2)
    elif right_have == "W":
        motor.posi_unit("right", 2)
    else:
        own, deg, dir = decide("W")#decide which data!!
        if own == 0:
            left_have = "W"
            motor.posi_group("right", deg)
            motor.posi_unit("left", 2)
        else:
            right_have = "W"
            motor.posi_group("left", deg)
            motor.posi_unit("right", 2)
def clk_F2():
    global left_have,right_have
    if left_have=="B":
        motor.posi_unit("left", 2)
    elif right_have=="B":
        motor.posi_unit("right", 2)
    else:
        own,deg,dir=decide("B")
        if own==0:
            left_have="B"
            motor.posi_group("right", deg)
            motor.posi_unit("left", 2)
        else:
            right_have="B"
            motor.posi_group("left", deg)
            motor.posi_unit("right", 2)
dict_fun={"D":clkwise_D,"R":clkwise_R,"F":clkwise_F,"L":clkwise_L,"U":clkwise_U,"B":clkwise_B,
          "D'":anticlk_D,"R'":anticlk_R,"F'":anticlk_F,"L'":anticlk_L,"U'":anticlk_U,"B'":anticlk_B,
          "D2":clk_D2,"R2":clk_R2,"F2":clk_F2,"L2":clk_L2,"U2":clk_U2,"B2":clk_B2}
def str_split(pos):
    sto=pos.split(" ")
    fre=len(sto)
    #import pdb
    #pdb.set_trace()
    for i in range(fre):
        dict_fun.get(sto[i])()
