import Utils
from Position import Position
from Piece import Piece
from Action import Action

# this class implements the getPossibleActions for each type of piece

class King(Piece): 
	
	# constructor
	def __init__(self, color):
		self.m_color = color
		
		if color==0: 
			self.m_type = Utils.wKing
		else:
			self.m_type = Utils.bKing

	
	# this method must be completed with all the possible pieces	
	def getPossibleActions(self, state):
		
		r = state.m_agentPos.row
		c = state.m_agentPos.col
		action = None
		
		l = []
		
		oponent_color = -1
		if self.m_color == 0: 
			oponent_color = 1
		elif self.m_color == 1: 
			oponent_color = 1

		if (r<(state.m_boardSize-1)) and (state.m_board[r+1][c] == Utils.empty):
			l.append(Action(state.m_agentPos, Position(r+1,c)))
        if (r>0) and (state.m_board[r-1][c] == Utils.empty):
			l.append(Action(state.m_agentPos, Position(r-1,c)))
        if (c<(state.m_boardSize-1)) and (state.m_board[r][c+1] == Utils.empty):
			l.append(Action(state.m_agentPos, Position(r,c+1)))
        if (c>0) and (state.m_board[r][c-1] == Utils.empty):
			l.append(Action(state.m_agentPos, Position(r,c-1)))
        if (r<(state.m_boardSize-1)) and (c<(state.m_boardSize-1)) and (state.m_board[r+1][c+1] == Utils.empty):
			l.append(Action(state.m_agentPos, Position(r+1,c+1)))
        if (r<(state.m_boardSize-1)) and (c>0) and (state.m_board[r+1][c-1] == Utils.empty):
			l.append(Action(state.m_agentPos, Position(r+1,c-1)))
        if (r>0) and (c<(state.m_boardSize-1)) and (state.m_board[r-1][c+1] == Utils.empty):
			l.append(Action(state.m_agentPos, Position(r-1,c+1)))
        if (r>0) and (c>0) and (state.m_board[r-1][c-1] == Utils.empty):
			l.append(Action(state.m_agentPos, Position(r-1,c-1)))
            
        if (r<(state.m_boardSize-1)) and (state.m_board[r+1][c] != Utils.empty) and (Utils.getColorPiece(state.m_board[r+1][c]) == oponent_color):
			l.append(Action(state.m_agentPos, Position(r+1,c)))
        if (r>0) and (state.m_board[r-1][c] != Utils.empty) and (Utils.getColorPiece(state.m_board[r-1][c]) == oponent_color):
			l.append(Action(state.m_agentPos, Position(r-1,c)))
        if (c<(state.m_boardSize-1)) and (state.m_board[r][c+1] != Utils.empty) and (Utils.getColorPiece(state.m_board[r][c+1]) == oponent_color):
			l.append(Action(state.m_agentPos, Position(r,c+1)))
        if (c>0) and (state.m_board[r][c-1] != Utils.empty) and (Utils.getColorPiece(state.m_board[r][c-1]) == oponent_color):
			l.append(Action(state.m_agentPos, Position(r,c-1)))
        if (r<(state.m_boardSize-1)) and (c<(state.m_boardSize-1)) and (state.m_board[r+1][c+1] != Utils.empty) and (Utils.getColorPiece(state.m_board[r+1][c+1]) == oponent_color):
			l.append(Action(state.m_agentPos, Position(r+1,c+1)))
        if (r<(state.m_boardSize-1)) and (c>0) and (state.m_board[r+1][c-1] != Utils.empty) and (Utils.getColorPiece(state.m_board[r+1][c-1]) == oponent_color):
			l.append(Action(state.m_agentPos, Position(r+1,c-1)))
        if (r>0) and (c<(state.m_boardSize-1)) and (state.m_board[r-1][c+1] != Utils.empty) and (Utils.getColorPiece(state.m_board[r-1][c+1]) == oponent_color):
			l.append(Action(state.m_agentPos, Position(r-1,c+1)))
        if (r>0) and (c>0) and (state.m_board[r-1][c-1] != Utils.empty) and (Utils.getColorPiece(state.m_board[r-1][c-1]) == oponent_color):
			l.append(Action(state.m_agentPos, Position(r-1,c-1)))

		return l
