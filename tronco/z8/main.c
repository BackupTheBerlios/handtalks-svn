/********************************************************************
 *  Copyright (C) 1999-2004 by  ZiLOG, Inc.
 *  All Rights Reserved
 ********************************************************************/

/*********************************************************************
 *   Zilog LedBlink sample was design to demonstrates the following 
 *   functionality on the standard development boards:
 *   - Setting up status routine to monitor events
 *   - Setting up a timer to toggle the leds
 *   - Setting up a Uart to transmit led colors and receive input 
 *     a keyboard event to toggle the direction of the leds
 *   - Setting up an event on a port to toggle the direction of the 
 *     leds
 * 
 *  Required terminal setup to communicate with the Sample:
 *      57600 bps, 8 bits per character, No parity, 1 stop bit, No flow ctrl
 *
 * NOTE:  Including UART specific statements while the UART is disabled will
 *        prevent the program from operating as intended.
 *        
 *        We recommend that you remove the printf()statements from this 
 *        program if you disable the evaluation board's UART.
 *
 *****************************************************************************/

#include <eZ8.h>
#include <stdio.h>
#include <sio.h> // non-standard I/O
#include <string.h>
#include "main.h"
#include "gatilho.h"
#include "uart.h"
#include "adc.h"


void inicia_gpio(void);

///////////////////////////////////////////////////////
// Global - Variable
char leitura_efetuada = NO;					// Initially ADC New data  Available

// Globais Externas
extern unsigned int ana[2];
extern unsigned char sensor;
extern char adc_data_available;
extern unsigned char valueH, valueL;


////////////////////////////////////////////////////////
// Initialize system clock source to use internal crystal
//
void inicia_clock_sistema()
{
	if((OSCCTL & 0x87) != 0x80)		//not currently internal ?
	{
		OSCCTL = 0xE7;					// Unlock sequence for OSCTL write
		OSCCTL = 0x18;					//
   		OSCCTL	=0x80;					// switch to internal
	}
}


main ()
{
	unsigned int sensor_anterior=0, i=0;


   	DI();							// Disable Interrupts
    inicia_gpio();
	inicia_clock_sistema();	
	inicia_uart0();
    inicia_adc();
   	EI();							// Enable Interrupts

	while(1)
	{
//		printf(".");
		i++;
		if (i == 10000)
		{
			sensor = 1;
			i = 0;
		}

		if (sensor)
		{
			if (sensor != sensor_anterior)
			{
				printf("sensor %d\n", sensor);
				sensor_anterior = sensor;
			}
			le_sensores();

			if (! sensor)
				leitura_efetuada = YES;
		}

		if (leitura_efetuada == YES)
		{
			leitura_efetuada = NO;
			printf(" %d,%d,%d\n", ana[0], ana[1], ana[2]);
		}
	}
} // main





