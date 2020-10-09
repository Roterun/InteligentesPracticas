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

public class Rook extends Piece {
	
	
	// constructor
	public Rook( int color){
		m_color = color;
		
		if (color==0) m_type = Utils.wRook;
		else m_type = Utils.bRook;
		
	}
	
	
	// this method must be completed with all the possible pieces
	
	public ArrayList<Action> getPossibleActions(State state){
		ArrayList<Action> list = null;
		
		list = this.getHorizontalLeftMoves(state);
		list.addAll(this.getHorizontalRightMoves(state));
		list.addAll(this.getVerticalDownMoves(state));
		list.addAll(this.getVerticalUpMoves(state));
		
		return list;
	}
	
	
	
	
}
