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

public class Bishop extends Piece {
	
	
	// constructor
	public Bishop( int color){
		m_color = color;
		
		if (color==0) m_type = Utils.wBishop;
		else m_type = Utils.bBishop;
		
	}
	
	
	// this method must be completed with all the possible pieces
	
	public ArrayList<Action> getPossibleActions(State state){
		ArrayList<Action> list = null;
		
		list = this.getDiagonalLeftDownMoves(state);
		list.addAll(this.getDiagonalRightDownMoves(state));
		list.addAll(this.getDiagonalLeftUpMoves(state));
		list.addAll(this.getDiagonalRightUpMoves(state));
		
		return list;
	}
	
	
	
	
}