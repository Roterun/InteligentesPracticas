
import Utils
import Piece
from Position import Position
from Action import Action
from State import State

class Node:

	m_state = None
	m_parent = None
	m_action = None
	m_cost = 0
	m_depth = 0
	m_Nnode = 0
	m_piece = 0

	def __init__(self, state, parent = None, action = None, cost = 0, n_node = 0, piece = -1):
		self.m_state = state
		self.m_parent = parent
		self.m_action = action
		self.m_cost = cost
		self.m_depth = 0
		self.m_n_node = n_node
		if parent:
			self.m_depth = parent.m_depth + 1
		self.m_piece = piece

	def getState(self):
		#definimos hash
		return hash(self.m_state)

	def getDepth(self):
		return self.m_depth

	def getCost(self):
		return self.m_cost

	def getN_Node(self):
		#diferenciar nodos
		return self.m_n_node

	def getParent(self):
		return self.m_parent

	def getAction(self):
		return self.m_action

	def __eq__(self, other):
		#Comprueba si dos nodos son iguales
		return isinstance(other, Node) and self.m_state == other.getState()

	def __str__(self):
		return "Node ("+str(self.m_state)+")"

	def printInfo(self):
		print("Node ("+str(self.m_state)+"):"+"\n\t depth:"+self.m_depth+"\n\t cost:"+self.m_cost+".")

	def solution(self):
		#Devuelve la secuencia de acciones para ir desde la raiz hasta este nodo.
		return [node.getAction() for node in self.camino()[1:]]

	def camino(self):
		#Devuelve una lista de nodos formando el camino desde la raiz hasta este nodo.
		node, path_back = self, []
		while node:
			path_back.append(node)
			node = node.getParent()
		return list(reversed(path_back))

	def getSuccessors(self, node):
		successors = []
		actions = node.m_piece.getPossibleActions(node.m_state)

		for action in actions:
			newState = node.m_state.applyAction(action)
			newNode = Node(newState,node,action,action.getCost(),node.getNNode() + 1,node.m_piece)
			successors.append(newNode)

		return successors


