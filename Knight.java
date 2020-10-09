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

public class Knight extends Piece {
	
	
	// constructor
	public Knight( int color){
		m_color = color;
		
		if (color==0) m_type = Utils.wKnight;
		else m_type = Utils.bKnight;
		
	}
	
	
	// this method must be completed with all the possible pieces
	
	public ArrayList<Action> getPossibleActions(State state){
		ArrayList<Action> list = null;
		
		list = this.getKnightLeftDownMoves(state);
		list.addAll(this.getKnightRightDownMoves(state));
		list.addAll(this.getKnightLeftUpMoves(state));
		list.addAll(this.getKnightRightUpMoves(state));
		
		return list;
	}
	
	
	
	
}