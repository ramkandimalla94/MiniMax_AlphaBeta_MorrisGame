import sys
import utils


def ABGame(depth,board_position,alpha,beta,flag):
    param_inp = utils.Parameters()
    param_out = utils.Parameters()
    
    if(depth==0):

        count_white = board_position.count('W')
        count_black = board_position.count('B')   

        count_final = count_white - count_black
        
        L = utils.GenerateMovesMidgameEndgame(board_position)

        if(count_black<=2):
            param_out.estimate = 10000
        elif(count_white<=2):
            param_out.estimate = -10000
        elif(len(L)==0):
            param_out.estimate = 10000
        else:
            param_out.estimate = 1000*(count_final)-len(L)
        param_out.nodes_crossed = param_out.nodes_crossed+1
        param_out.board_position = board_position 
        return param_out
    
    if(flag==1):    
        L = utils.GenerateMovesMidgameEndgame(board_position)
        
    else:
        L = utils.GenerateMovesMidgameEndgameBlack(board_position)
            
    for position in L:
        if(flag==1):
            param_inp = ABGame(depth-1,position,alpha,beta,0)
            if(param_inp.estimate> alpha):
                alpha = param_inp.estimate
                param_out.board_position = position
            param_out.nodes_crossed = param_out.nodes_crossed + param_inp.nodes_crossed
        else:
            param_inp = ABGame(depth-1,position,alpha,beta,1)
            if(param_inp.estimate< beta):
                beta = param_inp.estimate
                param_out.board_position = position
            param_out.nodes_crossed = param_out.nodes_crossed + param_inp.nodes_crossed
        if(alpha>=beta):
            break
        
    if (flag==1):
        param_out.estimate = alpha
    else:
        param_out.estimate = beta
    return param_out


with open(sys.argv[1]) as f:
    input_string = list(f.readlines()[0])

estimate_max = sys.maxsize
estimate_min = - estimate_max

Board_Position = []

output = ABGame(int(sys.argv[3]),input_string,estimate_min,estimate_max,1)

print("Board Position:", ''.join(output.board_position))
print("Position evaluated by static estimation:",output.nodes_crossed)
print("MINIMAX esitmate:",output.estimate)

with open(sys.argv[2], 'w') as f:
    output_string = ''.join(output.board_position)
    f.write(output_string)