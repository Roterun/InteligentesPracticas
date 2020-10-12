import Utils
from Piece import Piece

# this class implements the getPossibleActions for each type of piece

class Bishop(Piece): 
	
	# constructor
	def __init__(self, color):
		self.m_color = color
		
		if color==0: 
			self.m_type = Utils.wBishop
		else:
			self.m_type = Utils.bBishop

	
	# this method must be completed with all the possible pieces	
	def getPossibleActions(self, state):
		l = []
		
		l = self.getDiagonalLefUptMoves(state)
		l += self.getDiagonalRightDownMoves(state)
		l += self.getDiagonalLeftDownMoves(state)
		l += self.getDiagonalRightUpMoves(state)
		
		return l