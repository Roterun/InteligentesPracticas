# import java.util.ArrayList;
# import java.util.Hashtable;
# import java.util.Random;

# this class implements a simple search method which explores a single sequence of actions.
# The process is quite simple. At each state we look for the agent possible actions and choose one at random.
# The action is then applied and if the new state is final, the method stops returning the list of applied actions.
# On the other hand, we iterate.

import sys
import random
import Utils
from Node import Node
from Position import Position
from Action import Action
from State import State
from Piece import Piece
from Rook import Rook
from Pawn import Pawn
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from King import King


class DepthAlgorithm:
    # member variables
    m_initialState = None
    m_seedRS = -1
    #	Random m_generator = null;
    m_solution = None
    m_cost = 0.0
    m_piece = Piece()
    m_finalState = None

    # constructor
    def __init__(self, s0, seed):
        self.m_initialState = s0
        self.m_seedRS = seed
        #		m_generator = new Random(m_seedRS);
        self.m_cost = 0.0
        random.seed(seed)

        self.m_piece = s0.m_piece

    # search method
    def doSearch(self):

        abiertos = []
        cerrados = []
        sucesores = []

        aux = self.m_initialState.copy()

        self.m_solution = []
        solutionFound = False
        #current = None
        noSolution = False

        abiertos.append(aux)

        # main loop
        #current = self.m_initialState.copy()
        while (len(abiertos)!=0) and (solutionFound!=True):

            aux = abiertos.pop(0)

            if aux not in cerrados:

                if aux.isFinal():

                    solutionFound = True
                    self.m_finalState = aux

                    while aux.getParent():
                        self.m_solution.append(aux.getAction())
                        aux = aux.getParent()

                    self.m_solution.reverse()

                sucesores = aux.getSucessors()

                for sucesor in sucesores:
                    abiertos.append(sucesor)

#                if len(abiertos) > openMaxSize:
#                    openMaxSize = len(abiertos)

                cerrados.append(aux)

#                if len(cerrados) > exploredMaxSize:
#                    exploredMaxSize = len(cerrados)
        return self.m_finalState
# main method


if __name__ == '__main__':
    print(len(sys.argv))

    if (len(sys.argv) != 6):
        print("\n**Sorry, correct usage require 5 params:");
        print("Board size: int.");
        print("Density: (0.1,1]. Probability for each piece to be included.");
        print("Seed1: int. To initialize the problem instance random number generator (for reproducibility)");
        print("Agent: {0,1,2,3,4,5} standing for white pawn, rook, bishop, knight, queen or king.");
        print("Seed2: int. To initialize the Random Search instance random number generator (for reproducibility)");
        sys.exit()
    else:
        size = int(sys.argv[1])
        density = float(sys.argv[2])
        seed1 = int(sys.argv[3])
        agent = int(sys.argv[4])
        seed2 = int(sys.argv[5])

        if size < 4:
            print("\nSorry: board to small, modified to 4")
            size = 4

        if density < 0.1 or density > 1.0:
            print("\nSorry: bad density value, modified to 0.25")
            density = 0.25

        if density * 32 > size * size:
            print("\nSorry: too much pieces for the board size, modifying density to 0.25")
            density = 0.25

        if agent < 0 or agent > 5:
            print("\nSorry: bad selected agent, modified to 1 (white rook)")
            agent = Utils.wRook

        # getting the initial state
        state = Utils.getProblemInstance(size, density, seed1, agent)
        Utils.printBoard(state)

        dp = DepthAlgorithm(state, seed2)
        dp.m_finalState = dp.doSearch()

        if dp.m_finalState == None:
            print("\nSorry, no solution found ....")
        else:
            print("Solution length: %d" % len(dp.m_solution))
            print("Solution cost:   %f" % dp.m_cost)

            print("Solution:\n")
            for i in range(len(dp.m_solution)):
                print("%d : " % (i + 1), end="")
                print(dp.m_solution[i])
            Utils.printBoard(dp.m_finalState)

        print()
