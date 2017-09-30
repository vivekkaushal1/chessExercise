'''A Function to print all the possible moves
of chess piece from a specific position'''

import argparse, sys

class chessExercise():
    def __init__(self):
        parser = argparse.ArgumentParser(description='Return the list of possible moves.')
        parser.add_argument('-piece', dest='pType', help='The type of the piece')
        parser.add_argument('-position',dest='pos', help='The position of the piece')
        self.args = parser.parse_args()

    def getAllValidMoves(self):

        pType = self.args.pType
        currPos = list(self.args.pos)
        
        x = (ord(currPos[0]) - 97) #Subtract the from the position of 'a'
        y = int(currPos[1])
        
        potential_moves = []
        valid_moves = []
        
        #if the piece is a rook
        if pType.lower() == 'rook':
            moves = [((x, y+i),(x, y-i),(x-i, y),(x+i, y)) for i in range(1, 8)]
            for row in moves:
                potential_moves += row
                
        #if the piece is a knight
        elif pType.lower() == 'knight':
            potential_moves += [(x+2, y+1), (x+2, y-1)
                       ,(x+1, y+2), (x+1, y-2)
                       ,(x-2, y-1), (x-2, y+1)
                       ,(x-1, y+2), (x-1, y-2)]
            
        #if the piece is a queen. Queen moves can be a union of Rook and bishop. 
        elif pType.lower() == "queen":
            
            uRight = [(x+i, y+i) for i in range(1,8)]
            dRight = [(x+i, y-i) for i in range(1,8)]
            uLeft = [(x-i, y+i) for i in range(1,8)]
            dLeft = [(x-i, y-i) for i in range(1,8)]
            sMoves = [((x, y+i),(x, y-i),(x-i, y),(x+i, y)) for i in range(1, 8)]
            
            for row in sMoves:
                potential_moves += row
            potential_moves += uRight + dRight + uLeft + dLeft
            print (potential_moves)
        else:
            return ('Only Rook, Queen and Knight supported by current version')
        
        #Filter the moves invalid moves, i.e. the moves that are outside the 8*8 board
        for move in potential_moves:
            if 0 <= move[0] < 8 and 1 <= move[1] <= 8:
                valid_moves.append(chr(97+move[0])+str(move[1]))
        
        return (valid_moves)

def main():
    chessMoves = chessExercise()
    print(chessMoves.getAllValidMoves())

if __name__ == '__main__':
    sys.exit(main())
