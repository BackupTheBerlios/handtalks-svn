/******************************************************************************
 * File       : adc.c 
 * Description: Initializes  Xp's on chip ADC  peripheral to single shot
 *				conversion mode.The ISR  reads the the values fro the ADC 
 *				data register and stores in to a  variable.

 * Copyright 2004 ZiLOG Inc.  ALL RIGHTS RESERVED.

 * The source code in this file was written by an
 * authorized ZiLOG employee or a licensed consultant.
 * The source code has been verified to the fullest
 * extent possible.
 * Permission to use this code is granted on a royalty-free
 * basis. However users are cautioned to authenticate the
 * code contained herein.
 * ZiLOG DOES NOT GUARANTEE THE VERACITY OF THE SOFTWARE.
 ************************************************************************/
#include <ez8.h>
#include <stdio.h>
#include "adc.h"
#include "main.h"

unsigned char  valueH, valueL;
extern char adc_data_available;

//Selected internal reference 2.0Volts default 
void init_adc(void)
{
	SET_VECTOR(ADC, isr_ADC);				// Pass the vector number and the ISR address
									// to be placed into the interrupt table 
	ADCCTL0 = ADC_TEMP_CHANNEL; 			// ADC conversion disable,
											//Select ADC Temperature Sensor Input 
											//Internal reference voltage 2.0V,disable
											//external reference,single shot conversion

//	ADCCTL1 |= ADC_BUF_INPUT_X1;			// Single-ended, buffered with unity gain
	ADCCTL1 = 0X80;		     			// Single-ended, buffered with unity gain

	IRQ0E1 |= ADC_INT_EN;					// Enable ADC interrupts
	IRQ0E0 |= ADC_INT_EN;					// 				

}		


/**************************************************************************************/
// ADC Interrupt handler
/**************************************************************************************/
#pragma interrupt
void isr_ADC(void)  
{
	

	DI();
//	printf("int_adc\n");
	valueH = ADHR;										// Get ADC Data High  		
	valueL = ADLR;										// Read the ADC low data 
	adc_data_available = YES;																
	ADCCTL0  |= ADC_EN;									// ADC Conversion Enable			
	EI();
} 

