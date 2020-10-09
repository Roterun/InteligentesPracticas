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

public class King extends Piece {
    
    // constructor
	public King(int color){
		m_color = color;
		
		if(color==0) m_type = Utils.wKing;
		else m_type = Utils.bKing;
		
	}
	
	
	// this method must be completed with all the possible pieces
	
	public ArrayList<Action> getPossibleActions(State state){
            
		int c,r;
		c = state.m_agentPos.col;
		r = state.m_agentPos.row;
		Action action = null;
		
		if (m_color == 1){
		
		}
		
		ArrayList<Action> list = new ArrayList<Action>(15);
		
		if (m_color == 0){// white king
			if (state.m_board[r+1][c] == Utils.empty){
                            action = new Action(state.m_agentPos, new Position(r+1,c));
                            list.add(action);
			}
                        if ((state.m_board[r+1][c] != Utils.empty) && (Utils.getColorPiece(state.m_board[r+1][c]) != m_color)){
                            action = new Action(state.m_agentPos, new Position(r+1,c));
                            list.add(action);
			}
			if ((c<(state.m_boardSize-1)) && (state.m_board[r][c+1] == Utils.empty)){
                            action = new Action(state.m_agentPos, new Position(r,c+1));
                            list.add(action);
			}
                        if ((c<(state.m_boardSize-1)) && (state.m_board[r][c+1] != Utils.empty) 
                                                && (Utils.getColorPiece(state.m_board[r][c+1]) != m_color)){
                            action = new Action(state.m_agentPos, new Position(r,c+1));
                            list.add(action);
			}
			if ((c>0) && (state.m_board[r][c-1] == Utils.empty)){
                            action = new Action(state.m_agentPos, new Position(r,c-1));
                            list.add(action);
			}
                        if ((c>0) && (state.m_board[r][c-1] != Utils.empty) 
                                                && (Utils.getColorPiece(state.m_board[r][c-1]) != m_color)){
                            action = new Action(state.m_agentPos, new Position(r,c-1));
                            list.add(action);
			}
			if ((r>0) && (state.m_board[r-1][c] == Utils.empty)){
                            action = new Action(state.m_agentPos, new Position(r-1,c));
                            list.add(action);
			}
                        if ((r>0) && (state.m_board[r-1][c] != Utils.empty) 
                                                && (Utils.getColorPiece(state.m_board[r-1][c]) != m_color)){
                            action = new Action(state.m_agentPos, new Position(r-1,c));
                            list.add(action);
			}
                        if ((c>0) && (state.m_board[r+1][c-1] == Utils.empty)){
                            action = new Action(state.m_agentPos, new Position(r+1,c-1));
                            list.add(action);
			}
                        if ((c>0) && (state.m_board[r+1][c-1] != Utils.empty) 
                                                && (Utils.getColorPiece(state.m_board[r+1][c-1]) != m_color)){
                            action = new Action(state.m_agentPos, new Position(r+1,c-1));
                            list.add(action);
			}
			if ((c<(state.m_boardSize-1)) && (state.m_board[r+1][c+1] == Utils.empty)){
                            action = new Action(state.m_agentPos, new Position(r+1,c+1));
                            list.add(action);
			}
                        if ((c<(state.m_boardSize-1)) && (state.m_board[r+1][c+1] != Utils.empty) 
                                                && (Utils.getColorPiece(state.m_board[r+1][c+1]) != m_color)){
                            action = new Action(state.m_agentPos, new Position(r+1,c+1));
                            list.add(action);
			}
                        if ((r>0) && (c>0) && (state.m_board[r-1][c-1] == Utils.empty)){
                            action = new Action(state.m_agentPos, new Position(r-1,c-1));
                            list.add(action);
			}
                        if ((r>0) && (c>0) && (state.m_board[r-1][c-1] != Utils.empty) 
                                                && (Utils.getColorPiece(state.m_board[r-1][c-1]) != m_color)){
                            action = new Action(state.m_agentPos, new Position(r-1,c-1));
                            list.add(action);
			}
			if ((r>0) && (c<(state.m_boardSize-1)) && (state.m_board[r-1][c+1] == Utils.empty)){
                            action = new Action(state.m_agentPos, new Position(r-1,c+1));
                            list.add(action);
			}
                        if ((r>0) && (c<(state.m_boardSize-1)) && (state.m_board[r-1][c+1] != Utils.empty) 
                                                && (Utils.getColorPiece(state.m_board[r-1][c+1]) != m_color)){
                            action = new Action(state.m_agentPos, new Position(r-1,c+1));
                            list.add(action);
			}
		}	
				
		return list;
	}
}
