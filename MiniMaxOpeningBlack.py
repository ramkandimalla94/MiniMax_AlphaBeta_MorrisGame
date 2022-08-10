import sys
import utils



def StaticEstimation_Opening (Board_Position):

  numWhitePieces = Board_Position.count('W')
  numBlackPieces = Board_Position.count('B')

  return  numBlackPieces - numWhitePieces


def MiniMaxBlack(depth,gameBoard,flag):

    param_out = utils.Parameters()
    param_inp = utils.Parameters()

    if(depth==0):
        finalCount = StaticEstimation_Opening(gameBoard)
        param_out = utils.Parameters(finalCount,param_out.nodes_crossed+1,gameBoard)
        return param_out
    
    if(flag==1):
        L = utils.GenerateMoveOpeningBlack(gameBoard)
        param_out.estimate = estimate_min
    
    else:
        L = utils.GenerateMovesOpening(gameBoard)
        param_out.estimate = estimate_max
        
    for position in L:
        if(flag==1):
            param_inp = MiniMaxBlack(depth-1,position,0)
            if(param_inp.estimate>param_out.estimate):
                param_out.estimate=param_inp.estimate
                param_out.Board_Position = position
            param_out.nodes_crossed = param_out.nodes_crossed + param_inp.nodes_crossed
            
        else:
            param_inp = MiniMaxBlack(depth-1,position,1)
            if(param_inp.estimate<param_out.estimate):
                param_out.estimate=param_inp.estimate
                param_out.Board_Position = position
            param_out.nodes_crossed = param_out.nodes_crossed + param_inp.nodes_crossed
            
    return param_out


with open(sys.argv[1]) as f:
    input = list(f.readlines()[0])


Board_Position = []

estimate_max = sys.maxsize
estimate_min = - estimate_max

output = MiniMaxBlack(int(sys.argv[3]),input,1)

print("Board Position:", ''.join(output.Board_Position))
print("Position evaluated by static estimation:",output.nodes_crossed)
print("MINIMAX esitmate:",output.estimate)

with open(sys.argv[2], 'w') as f:
    output_string = ''.join(output.Board_Position)
    f.write(output_string)
