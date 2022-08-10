import sys
import utils


def MiniMaxGame(d,Board_Position,flag):
    
    param_out = utils.Parameters()
    param_inp = utils.Parameters()

    if(d==0):

        count_white = Board_Position.count('W')
        count_black = Board_Position.count('B')   

        count_final = count_white - count_black

        L = utils.GenerateMovesMidgameEndgameBlack(Board_Position)
        
        if(count_white<=2):
            param_out.estimate = -10000
        elif(count_black<=2):
            param_out.estimate = 10000
        elif(len(L)==0):
            param_out.estimate = 10000
        else:
            param_out.estimate = 1000*(count_final) - len(L)

        param_out.nodes_crossed +=1

        return param_out
    
    if(flag==1):

        L = utils.GenerateMovesMidgameEndgame(Board_Position)

        param_out.estimate = estimate_min
    else:
        L = utils.GenerateMovesMidgameEndgameBlack(Board_Position)
        param_out.estimate = estimate_max
        
    for position in L:

        if(flag==1):

            param_inp = MiniMaxGame(d-1,position,0)
            if(param_inp.estimate>param_out.estimate):
                param_out.estimate=param_inp.estimate
                param_out.Board_Position = position
            param_out.nodes_crossed = param_out.nodes_crossed + param_inp.nodes_crossed
            
        else:
            
            param_inp = MiniMaxGame(d-1,position,1)
            if(param_inp.estimate<param_out.estimate):
                param_out.estimate=param_inp.estimate
                param_out.Board_Position = position
            param_out.nodes_crossed = param_out.nodes_crossed + param_inp.nodes_crossed   

    return param_out


with open(sys.argv[1]) as f:
    input_string = list(f.readlines()[0])

estimate_max = sys.maxsize
estimate_min = - estimate_max

Board_Position = []

output = MiniMaxGame(int(sys.argv[3]),input_string,1)

print("Board Position:", ''.join(output.Board_Position))
print("Position evaluated by static estimation:",output.nodes_crossed)
print("MINIMAX esitmate:",output.estimate)

with open(sys.argv[2], 'w') as f:
    output_string = ''.join(output.Board_Position)
    f.write(output_string)