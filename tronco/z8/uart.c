/*************************************************
 * Hand-Talks!
 *
 * Módulo da UART (serial)
 *************************************************/

#include <eZ8.h>
#include <stdio.h>
#include <sio.h> 	// non-standard I/O
#include "main.h"
#include "uart.h"


//////////////////////////////////////////////////////////
// Inicia UART0
void inicia_uart0(void)
{
    init_uart(_UART0,_DEFFREQ, _DEFBAUD); // Setup Uart0 
    select_port(_UART0);				  // Select port
	
	PAADDR = P_AF;   PACTL |= 0x30;	//  - Habilita TXD0
	PAADDR = P_AFS1; PACTL &= 0xCF;	//  - Desabilita RXD0
	PAADDR = P_AFS2; PACTL &= 0xCF;	// 
	PAADDR = P_NUL; 				//  Clear to protect sub register

	U0CTL0 = 0x80 ;		// Transmissor ligado, Receptor inibido, sem Paridade, 1 Stop bit.
}

/**************************************************************************************/
//  Print character to console
/**************************************************************************************/
/*
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
}*/
