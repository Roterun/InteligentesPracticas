/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.util.ArrayList;

/**
 *
 * @author Pablo
 */

//this class implements the getPossibleActions for each type of piece

public class Pawn extends Piece {
	
	
	// constructor
	public Pawn( int color){
		m_color = color;
		
		if (color==0) m_type = Utils.wPawn;
		else m_type = Utils.bPawn;
		
	}
	
	
	// this method must be completed with all the possible pieces
	
	public ArrayList<Action> getPossibleActions(State state){
		
		int c,r;
		c = state.m_agentPos.col;
		r = state.m_agentPos.row;
		Action action = null;
		
		if (m_color == 1){//black pawn ... I will let this for now ...
		
		}
		
		ArrayList<Action> list = new ArrayList<Action>(3);
		
		if (m_color == 0){// white pawn
			if (state.m_board[r+1][c] == Utils.empty){//standard pawn move
                            action = new Action(state.m_agentPos, new Position(r+1,c));
                            list.add(action);
			}
                        if ((r==1) && (state.m_board[r+2][c] == Utils.empty)){//starting pawn move
                            action = new Action(state.m_agentPos, new Position(r+2,c));
                            list.add(action);
			}
                        if ((c>0) && (state.m_board[r+1][c-1] != Utils.empty) 
						&& (Utils.getColorPiece(state.m_board[r+1][c-1]) == 1)){//capture
                            action = new Action(state.m_agentPos, new Position(r+1,c-1));
                            list.add(action);
			}
			if ((c<(state.m_boardSize-1)) && (state.m_board[r+1][c+1] != Utils.empty) 
						&& (Utils.getColorPiece(state.m_board[r+1][c+1]) == 1)){//capture
                            action = new Action(state.m_agentPos, new Position(r+1,c+1));
                            list.add(action);
			}
		}	
				
		return list;
	}
	
	
	
	
}
