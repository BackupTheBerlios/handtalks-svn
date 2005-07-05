/*************************************************
 *  Copyright (C) 1999-2004 by  ZiLOG, Inc.
 *  All Rights Reserved
 *************************************************/

#include <eZ8.h>
#include "main.h"
#include "test_button.h"


//////////////////////////////////////////////////////////
//Interrupt routine

#pragma interrupt
void isr_A3(void) 
{
//   	toggle_port();
}


//////////////////////////////////////////////////////////
//Intialize Test Button 
void init_test_button(void)
{
	SET_VECTOR(P3AD , isr_A3); 
	PAADDR = 0x01;		//PA Data Dir = input :updated
	PACTL |= 0x08;       //PA3 input Ctrl
	IRQ1ENH |= 0x08;	// Set Interrupt Priority High
	IRQ1ENL |= 0x08;	// Set Interrupt Priority High
}


