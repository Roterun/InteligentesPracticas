import Utils
from Piece import Piece

# this class implements the getPossibleActions for each type of piece

class Knight(Piece): 
	
	# constructor
	def __init__(self, color):
		self.m_color = color
		
		if color==0: 
			self.m_type = Utils.wKnight
		else:
			self.m_type = Utils.bKnight

	
	# this method must be completed with all the possible pieces	
	def getPossibleActions(self, state):
		l = []
		
		l = self.getKnightLeftUpMoves(state)
		l += self.getKnightRightDownMoves(state)
		l += self.getKnightLeftDownMoves(state)
		l += self.getKnightRightUpMoves(state)
		
		return l

