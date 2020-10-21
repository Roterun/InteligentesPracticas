# This class contains the information needed to represent a state
# and some useful methods

import sys
import copy
import Utils
from Piece import Piece
from Rook import Rook
from Pawn import Pawn
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from King import King

class State:
	m_board = None
	m_agentPos = None
	m_agent = -1 # the type of piece
	m_color = 0  # 0 for white, 1 for black
	m_boardSize = -1
	m_piece = Piece()
	m_parent = None
	m_action = None

	# constructor
	def __init__(self, board, position, agent):
		self.m_board = board
		self.m_agentPos = position
		self.m_agent = agent
		if (self.m_agent >11):
			print("\n*** Invalid piece ***\n")
			sys.exit(0)
		else:
			if (self.m_agent >5):
				self.m_color = 1 # black

		self.m_boardSize = len(board[0])

		if self.m_agent == Utils.wPawn:
			self.m_piece = Pawn(0)
		elif self.m_agent == Utils.bPawn:
			self.m_piece = Pawn(1)
		elif self.m_agent == Utils.wRook:
			self.m_piece = Rook(0)
		elif self.m_agent == Utils.bRook:
			self.m_piece = Rook(1)
		elif self.m_agent == Utils.wBishop:
			self.m_piece = Bishop(0)
		elif self.m_agent == Utils.bBishop:
			self.m_piece = Bishop(1)
		elif self.m_agent == Utils.wKnight:
			self.m_piece = Knight(0)
		elif self.m_agent == Utils.bKnight:
			self.m_piece = Knight(1)
		elif self.m_agent == Utils.wQueen:
			self.m_piece = Queen(0)
		elif self.m_agent == Utils.bQueen:
			self.m_piece = Queen(1)
		elif self.m_agent == Utils.wKing:
			self.m_piece = King(0)
		elif self.m_agent == Utils.bKing:
			self.m_piece = King(1)
		else:
			# define the rest of pieces
			print("Chess piece not implemented")
			sys.exit()

	# compares if the current state is final, i.e. the agent is in the last row
	def isFinal(self):
		if (self.m_agentPos.row == self.m_boardSize-1):
			return True
		else:
			return False

	# hard copy of an State
	def copy(self, memodict={}):
		#print '__deepcopy__(%s)' % str(memo)
		newState = State(self.m_board, self.m_agentPos, self.m_agent)
		newState.__dict__.update(self.__dict__)
		newState.m_board = copy.deepcopy(self.m_board, memodict)
		newState.m_agentPos = copy.deepcopy(self.m_agentPos, memodict)
		newState.m_agent = copy.deepcopy(self.m_agent, memodict)
		newState.m_color = copy.deepcopy(self.m_color, memodict)
		newState.m_boardSize = copy.deepcopy(self.m_boardSize, memodict)

		return newState

	# apply a given action over the current state -which remains unmodified. Return a new state

	def applyAction(self,action):
		newState = self.copy()
		newState.m_board[action.m_initPos.row][action.m_initPos.col] = Utils.empty
		newState.m_board[action.m_finalPos.row][action.m_finalPos.col] = newState.m_agent
		self.m_action = action
		newState.m_parent = self.copy()
		newState.m_agentPos = action.m_finalPos

		return newState

	def getSucessors(self):

		successors = []
		thisState = self.copy()

		actions = self.m_piece.getPossibleActions(thisState)

		for action in actions:
			newState = self.applyAction(action)
			successors.append(newState)

		return successors

	def getParent(self):
		if self.m_agentPos.row == 0:
			return print("No tiene padre")
		else:
			return self.m_parent

	def getAction(self):
		return self.m_action
