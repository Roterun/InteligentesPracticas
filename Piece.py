#import java.util.ArrayList;

# this class implements the getPossibleActions for each type of piece

import Utils
from Position import Position
from Action import Action
from State import State

class Piece:
	# this method must be completed with all the possible pieces

	def __init__(self):
		self.m_color = -1
		self.m_type = -1

	def getPossibleActions(self, state):

		return None # never arrive here


	# horizontal left moves
	def getHorizontalLeftMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

		busyCell = False
		for c in range(col0-1,-1,-1):
			if not busyCell:
				if state.m_board[row0][c] == Utils.empty: # add action
					action = Action(state.m_agentPos, Position(row0,c))
					l.append(action)
				else:
					busyCell = True
					if agentColor != Utils.getColorPiece(state.m_board[row0][c]): # capture piece
						action = Action(state.m_agentPos, Position(row0,c))
						l.append(action)

		return l

	# horizontal right moves
	def getHorizontalRightMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

		busyCell = False
		for c in range(col0+1,state.m_boardSize):
			if not busyCell:
				if state.m_board[row0][c] == Utils.empty: # add action
					action = Action(state.m_agentPos, Position(row0,c))
					l.append(action)
				else:
					busyCell = True
					if agentColor != Utils.getColorPiece(state.m_board[row0][c]): # capture piece
						action = Action(state.m_agentPos, Position(row0,c))
						l.append(action)

		return l

	# vertical up moves
	def getVerticalUpMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

		busyCell = False
		for r in range(row0-1,-1,-1):
			if not busyCell:
				if state.m_board[r][col0] == Utils.empty: # add action
					action = Action(state.m_agentPos, Position(r,col0))
					l.append(action)
				else:
					busyCell = True
					if agentColor != Utils.getColorPiece(state.m_board[r][col0]): # capture piece
						action = Action(state.m_agentPos, Position(r,col0))
						l.append(action)
		return l


	# vertical down moves
	def getVerticalDownMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

		busyCell = False
		for r in range(row0+1,state.m_boardSize):
			if not busyCell:
				if state.m_board[r][col0] == Utils.empty: # add action
					action = Action(state.m_agentPos, Position(r,col0))
					l.append(action)
				else:
					busyCell = True
					if agentColor != Utils.getColorPiece(state.m_board[r][col0]): # capture piece
						action = Action(state.m_agentPos, Position(r,col0))
						l.append(action)

		return l



	# diagonal up right moves
	def getDiagonalRightUpMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

		busyCell = False
		for r in range(row0-1,-1,-1):
			for c in range(col0+1,state.m_boardSize):
				if not busyCell:
					if ((col0+row0)==(c+r)):
						if state.m_board[r][c] == Utils.empty: # add action
							action = Action(state.m_agentPos, Position(r,c))
							l.append(action)
						else:
							busyCell = True
							if agentColor != Utils.getColorPiece(state.m_board[r][c]): # capture piece
								action = Action(state.m_agentPos, Position(r,c))
		return l

	# diagonal up left moves
	def getDiagonalLeftUpMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

		busyCell = False
		for r in range(row0-1,-1,-1):
			for c in range(col0-1,-1,-1):
				if not busyCell:
					if ((col0+row0)==(c+r)):
						if state.m_board[r][c] == Utils.empty: # add action
							action = Action(state.m_agentPos, Position(r,c))
							l.append(action)
						else:
							busyCell = True
							if agentColor != Utils.getColorPiece(state.m_board[r][c]): # capture piece
								action = Action(state.m_agentPos, Position(r,c))
								l.append(action)
		return l

	# diagonal down right moves
	def getDiagonalRightDownMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

		busyCell = False
		for r in range(row0+1,state.m_boardSize):
			for c in range(col0+1,state.m_boardSize):
				if not busyCell:
					if ((col0+row0)==(c+r)):
						if state.m_board[r][c] == Utils.empty: # add action
							action = Action(state.m_agentPos, Position(r,c))
							l.append(action)
						else:
							busyCell = True
							if agentColor != Utils.getColorPiece(state.m_board[r][c]): # capture piece
								action = Action(state.m_agentPos, Position(r,c))
								l.append(action)
		return l

	# diagonal down left moves
	def getDiagonalLeftDownMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

		busyCell = False
		for r in range(row0+1, state.m_boardSize):
			for c in range(col0-1,-1,-1):
				if not busyCell:
					if ((col0+row0)==(c+r)):
						if state.m_board[r][c] == Utils.empty: # add action
							action = Action(state.m_agentPos, Position(r,c))
							l.append(action)
						else:
							busyCell = True
							if agentColor != Utils.getColorPiece(state.m_board[r][c]): # capture piece
								action = Action(state.m_agentPos, Position(r,c))
								l.append(action)
		return l

	# Knight up right moves
	def getKnightRightUpMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

		busyCell = False
		for r in range(row0-1,-1,-1):
			for c in range(col0+1, state.m_boardSize):
				if not busyCell:
					if ((row0-r)*(row0-r)+(col0-c)*(col0-c)==5):
						if state.m_board[r][c] == Utils.empty: # add action
							action = Action(state.m_agentPos, Position(r,c))
							l.append(action)
						else:
							busyCell = True
							if agentColor != Utils.getColorPiece(state.m_board[r][c]): # capture piece
								action = Action(state.m_agentPos, Position(r,c))
								l.append(action)
		return l

	# Knight up left moves
	def getKnightLeftUpMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

		busyCell = False
		for r in range(row0-1,-1,-1):
			for c in range(col0-1,-1,-1):
				if not busyCell:
					if ((row0-r)*(row0-r)+(col0-c)*(col0-c)==5):
						if state.m_board[r][c] == Utils.empty: # add action
							action = Action(state.m_agentPos, Position(r,c))
							l.append(action)
						else:
							busyCell = True
							if agentColor != Utils.getColorPiece(state.m_board[r][c]): # capture piece
								action = Action(state.m_agentPos, Position(r,c))
								l.append(action)
		return l

	# Knight down right moves
	def getKnightRightDownMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

		busyCell = False
		for r in range(row0+1, state.m_boardSize):
			for c in range(col0+1, state.m_boardSize):
				if not busyCell:
					if ((row0-r)*(row0-r)+(col0-c)*(col0-c)==5):
						if state.m_board[r][c] == Utils.empty: # add action
							action = Action(state.m_agentPos, Position(r,c))
							l.append(action)
						else:
							busyCell = True
							if agentColor != Utils.getColorPiece(state.m_board[r][c]): # capture piece
								action = Action(state.m_agentPos, Position(r,c))
								l.append(action)
		return l

	# Knight down left moves
	def getKnightLeftDownMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

		busyCell = False
		for r in range(row0+1, state.m_boardSize):
			for c in range(col0-1,-1,-1):
				if not busyCell:
					if ((row0-r)*(row0-r)+(col0-c)*(col0-c)==5):
						if state.m_board[r][c] == Utils.empty: # add action
							action = Action(state.m_agentPos, Position(r,c))
							l.append(action)
						else:
							busyCell = True
							if agentColor != Utils.getColorPiece(state.m_board[r][c]): # capture piece
								action = Action(state.m_agentPos, Position(r,c))
								l.append(action)
		return l