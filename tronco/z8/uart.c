/*************************************************
 *  Copyright (C) 1999-2004 by  ZiLOG, Inc.
 *  All Rights Reserved
 *************************************************/

#include <eZ8.h>
#include <stdio.h>
#include <sio.h> // non-standard I/O
#include "main.h"
#include "uart.h"


//////////////////////////////////////////////////////////
//Interrupt routine

//#pragma interrupt
//void isr_uart0_rx(void) 
//{
//    toggle_uart();
//}

//////////////////////////////////////////////////////////
//Intialize Timer-0 
void init_uart0(void)
{
    init_uart(_UART0,_DEFFREQ, _DEFBAUD); // Setup Uart0 
    select_port(_UART0);				 // Select port

	//PA4 as RxD0 and PA5 as TxD0
	PAADDR = 0x07 ; //PAFS1
	PACTL &= 0xCF ;	
	PAADDR = 0x08 ; //PASF2
	PACTL &= 0xCF ;	
	PAADDR = 0x00 ; // Clear to protect sub register

//	SET_VECTOR(UART0_RX, isr_uart0_rx);  // Define interrupt routine/
//	IRQ0ENH |= 0x10;					// Set Interrupt Priority High
//	IRQ0ENL |= 0x10;					// Set Interrupt Priority High
}

/**************************************************************************************/
//  Print character to console
/**************************************************************************************/
char putch(char c)
{
if (c == '\n') {
   do {
     } while (!(U0STAT0 & 0x04));  				// Transmit Data Bit enabled
    U0D = '\r';                   				// Send CR 
  }

do {
  } while (!(U0STAT0 & 0x04));  				// Transmit Data Bit enabled
U0D = c;        								// Send data
}
