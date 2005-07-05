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
#include "timer.h"
#include "test_button.h"
#include "uart.h"
#include "adc.h"

#define CLOCK_INTERNAL 0
#define CLOCK_EXTERNAL 1
#define CLOCKSOURCE	CLOCK_INTERNAL
#define YES		(unsigned char)1
#define NO		(unsigned char)0
//#define CLOCKSOURCE	CLOCK_EXTERNAL 	// Notes: XIN could not be used during debugging because
										//        its pin is used for DBG. Instead, CLKIN is used
										//        in this example

extern void init_adc(void);
unsigned int actual_temp();
void display_data(unsigned int);
void display_int_data(unsigned int);
//void puts (char * src);
void bin_to_decimal(unsigned char L_byte, char *buffer);
void bin_to_int(unsigned int L_byte, char *buffer);


///////////////////////////////////////////////////////
// Global - Variable
int ProgStat = BUSY;     		// Program status
int ProgDir  = UP;
int button_push = 0;			// 0-1 Wait State 2 > Change State
unsigned int  valueH_new, valueL_new;
char adc_data_available  =  NO;					// Initially ADC New data  Available
extern unsigned char  valueH, valueL;


////////////////////////////////////////////////////////
// A Simple status routine that gets called by the ISR to
// Change status 
void setStatus( int status )
{
	 ProgStat = status; 		//Program status
}

////////////////////////////////////////////////////////
// A Simple routine that toggles the direction of
// leds 
/*
void toggle_uart( void )
{
	 puts("toggle_uart!\n");
	 //getch();
	 button_push = 1; 		//Program status
}
*/
////////////////////////////////////////////////////////
// A Simple routine that toggles the direction of
// leds 
/*
void toggle_port( void )
{
	 puts("toggle_uart!\n");
	 button_push = button_push+1;
}*/
/*
void osc_delay()
{
	asm("DELAY_COUNT	.set (15000/36)");		//15000 cycles delay for oscillator to stabilize.
	asm("\tpush R12");						    // rev BA requires longer delay.
	asm("\tpush R13");
	asm("\tpush R14");
	asm("\tpush R15");

	asm("\tLD   R12, #HIGH(DELAY_COUNT>>16)");
    asm("\tLD   R13, #LOW(DELAY_COUNT>>16)");
    asm("\tLD   R14, #HIGH(DELAY_COUNT)");
	asm("\tLD   R15, #LOW(DELAY_COUNT)");
	
	asm("$delayCountDown:");					//this loop takes about 36 cycles"
	asm("\tCP   R15,#%0");
	asm("\tCPC  R14,#%0");
	asm("\tCPC  R13,#%0");
	asm("\tCPC  R12,#%0");
    asm("\tJR   ule,$delay_done");
	asm("\tSUB  R15,#%1");
    asm("\tSBC  R14,#%0");
    asm("\tSBC  R13,#%0");
    asm("\tSBC  R12,#%0");
	asm("\tjr $delayCountDown");
	asm("$delay_done:");
	asm("\tpop R15");
	asm("\tpop R14");
	asm("\tpop R13");
	asm("\tpop R12");
}
*/
////////////////////////////////////////////////////////
// Initialize system clock source to use external crystal
//
void init_systemclock()
{
#if (CLOCKSOURCE == CLOCK_EXTERNAL)
	if((OSCCTL & 0x2) != 0x2)		//not currently external ?
	{
		OSCCTL = 0xE7;					// Unlock sequence for OSCTL write
		OSCCTL = 0x18;					//
   		OSCCTL	=0x04;					//start external oscillator
		osc_delay();					//wait for oscillator to stabilize				
	 }
#else
	if((OSCCTL & 0x87) != 0x80)		//not currently internal ?
	{
		OSCCTL = 0xE7;					// Unlock sequence for OSCTL write
		OSCCTL = 0x18;					//
   		OSCCTL	=0x80;					// switch to internal
	}
#endif								
}

////////////////////////////////////////////////////////
// Main program beings here 
// This  program blinks LED-3 on the evaluation board 

main ()
{
	int  measured_temp;	
    int ledstate = 2;
	int i;
	init_systemclock();				// Initialize System clock source
//	init_led_gpio();				// Initializes LED ports (Port A and C)
 //   init_test_button_gpio();        // Initialize Test Button (Port C)
/*    PAAF |= 0x02;
    PAAFS1 = 0x02;
    PAAFS2 = 0x02;*/
	PAADDR = 0x02 ; //PAAF
	PACTL |= 0x02 ;	
	PAADDR = 0x07 ; //PAFS1
	PACTL |= 0x02 ;	
	PAADDR = 0x08 ; //PAFS2
	PACTL |= 0x02 ;	


   	DI();							// Disable Interrupts
// 	init_timer0();					// Intialize Timer-0
	init_uart0();                   // Intialize Uart
    init_adc();
//	init_test_button();       		// Initialize Test Button
    ADCCTL0  |= ADC_EN;
   	EI();							// Enable Interrupts

	while(1)
	{
	
		if (adc_data_available == YES)
		{
			measured_temp=actual_temp();
			printf("mt: %d\n", measured_temp);
			if((measured_temp > 5000 ) && (measured_temp < 50000))
			{
				 turn_on_led();
				 putch('A');
	 		}
			else
			{
				turn_off_led();
				putch('B');
			}
			putch(' ');
			display_int_data(measured_temp);
		}
		

	}
}	// End of main program


void turn_off_led(void)
{
  PAOUT |= 0x05;                            // Turn off all three leds
}

void turn_on_led(void)
{
  PAOUT &= 0xFA;                      //Turn on red LED
}



/**************************************************************************************/
//Explain this function
//10-bit analog output is used for temp measurement (sign bit is ignored)
/**************************************************************************************/


unsigned int actual_temp()				
{
	if(adc_data_available == YES)			//check if new data available
	{
		 //Read the temp
		 adc_data_available = NO;
		 valueH_new = (unsigned char)valueH;
		 valueL_new = (unsigned char)valueL;
		valueL_new = valueL_new >> 5;									// Shift right 5 bits of ADC Data Low

		valueH_new = valueH_new <<3;									// Get Temp Data High byte (Hex) 

		valueH_new |= valueL_new;

 		return(valueH_new);
	}
	    return(valueH_new);
}//End of Actual temperature function

void display_data(unsigned int measured_temp)
{
	unsigned char H_byte,L_byte;
	char buffer[3];
	buffer[0] = 0x00;
	L_byte = (unsigned char)(measured_temp);
	bin_to_decimal(L_byte, buffer);
	puts(buffer);
	putch('\n');
}//End of display data routine

void display_int_data(unsigned int measured_temp)
{
	char buffer[6];
	buffer[0] = 0x00;
	bin_to_int(measured_temp, buffer);
	puts(buffer);
	putch('\n');
}//End of display data routine
/**************************************************************************************/
//  Print string to console
/**************************************************************************************
void puts (char src[20])//(char far * src)
{
	while (*src)									// Print character to console
   		putch (*src++);								// until null termination of the string
}//End of puts routine

*/
/**************************************************************************************/

/**************************************************************************************/
void bin_to_decimal(unsigned char c, char *buffer) 
{

	while(*buffer)
 	{
  		buffer++;
  	}
  	buffer[1] = (c%10) + '0';
	c/=10;
	buffer[0]= (c%10) + '0';
	buffer[2] ='\0';
  
}//End of bin_to_decimal routine

void bin_to_int(unsigned int c, char *buffer) 
{

	while(*buffer)
 	{
  		buffer++;
  	}
  	buffer[4] = (c%10) + '0';
	c/=10;
	buffer[3]= (c%10) + '0';
	c/=10;
	buffer[2]= (c%10) + '0';
	c/=10;
	buffer[1]= (c%10) + '0';
	c/=10;
	buffer[0]= (c%10) + '0';
	buffer[5] ='\0';
  
}// fim


