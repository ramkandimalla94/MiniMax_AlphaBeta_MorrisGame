import sys
import utils


def StaticEstimation_Opening (Board_Position):

  numWhitePieces = Board_Position.count('W')
  numBlackPieces = Board_Position.count('B')

  return numWhitePieces - numBlackPieces


def ABOpening(depth,board,alpha,beta,flag):

    param_inp = utils.Parameters()
    param_out = utils.Parameters()

    if(depth==0):
        count_final = StaticEstimation_Opening(board)
        param_out.estimate = count_final
        param_out.nodes_crossed = param_out.nodes_crossed +1
        return param_out
    
    if(flag==1):
        L = utils.GenerateMovesOpening(board)

    else:
        L = utils.GenerateMoveOpeningBlack(board)
       
    for position in L:
        if(flag==1):
            param_inp = ABOpening(depth-1,position,alpha,beta, 0)
            if (param_inp.estimate > alpha):
                alpha = param_inp.estimate
                param_out.Board_Position = position
            param_out.nodes_crossed = param_out.nodes_crossed + param_inp.nodes_crossed
        else:
             param_inp = ABOpening(depth-1,position,alpha,beta, 1)
             if (param_inp.estimate < beta):
                beta = param_inp.estimate
                param_out.Board_Position = position
             param_out.nodes_crossed = param_out.nodes_crossed + param_inp.nodes_crossed
        if(alpha>=beta):
            break
        
    if (flag==1):
        param_out.estimate = alpha
    else:
        param_out.estimate = beta
    return param_out


with open(sys.argv[1]) as f:
    input = list(f.readlines()[0])


Board_Position = []
 
estimate_max = sys.maxsize
estimate_min = - estimate_max

output = ABOpening(int(sys.argv[3]),input,estimate_min,estimate_max,1)

print("Board Position:", ''.join(output.Board_Position))
print("Position evaluated by static estimation:",output.nodes_crossed)
print("MINIMAX esitmate:",output.estimate)

with open(sys.argv[2], 'w') as f:
    output_string = ''.join(output.Board_Position)
    f.write(output_string)
