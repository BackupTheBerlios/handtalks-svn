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
char adc_data_available;
unsigned int ana[SENSORES];
unsigned char sensor = 0;



/**************************************************************************************/
// ADC Interrupt handler
/**************************************************************************************/
#pragma interrupt
void isr_ADC(void)  
{
	DI();
	valueH = ADHR;										// Get ADC Data High  		
	valueL = ADLR;										// Read the ADC low data 
	adc_data_available = YES;																
//	ADCCTL0  |= ADC_CEN;								// ADC Conversion Enable			
	EI();
} 


//Selected internal reference 2.0Volts default 
void inicia_adc(void)
{
	SET_VECTOR(ADC, isr_ADC);		

	ADCCTL0 &= ~ADC_REFSELL;	     		// 2V ref

	ADCCTL1 |= ADC_BUF_INPUT_X1;			// Single-ended, buffered with unity gain
	ADCCTL1 |= ADC_REFSELH;		     		// 2V ref

	IRQ0E1 |= ADC_INT_EN;					// Enable ADC interrupts
	IRQ0E0 |= ADC_INT_EN;					// 				
/*
	PAADDR = P_AF;   PACTL |= 0x0A;	//  - Habilita ANA1, ANA2 e ANA3
	PAADDR = P_AFS1; PACTL &= 0xFA;	//  
	PAADDR = P_AFS2; PACTL &= 0xFA;	// 
*/
	PAADDR = P_AF;   PACTL |= 0x02;	//  - Habilita ANA1 e ANA3
	PAADDR = P_AFS1; PACTL &= 0xF2;	//  
	PAADDR = P_AFS2; PACTL &= 0xF2;	// 

	PAADDR = P_NUL; 				//  Clear to protect sub register
}		

void captura_adc (unsigned char ana)
{
	switch (ana)
	{
		case 1:
			ADCCTL0 = ADC_ANAIN_ANA1; 	
			break;
		case 2:
//			ADCCTL0 = ADC_ANAIN_ANA2; 	
//			break;
		case 3:
			ADCCTL0 = ADC_ANAIN_ANA3; 	
			break;
		default:
			break;
	}
	ADCCTL0 |= ADC_CEN;
}



unsigned int actual_temp()				
{
	unsigned int valueH_new, valueL_new;
	if(adc_data_available == YES)			//check if new data available
	{
		//Read the temp
		adc_data_available = NO;
		valueH_new = (unsigned char)valueH;
		valueL_new = (unsigned char)valueL;
		valueL_new = valueL_new >> 5;									// Shift right 5 bits of ADC Data Low
		
		valueH_new = valueH_new <<3;									// Get Temp Data High byte (Hex) 
		
		valueH_new |= valueL_new;
	}

    return(valueH_new);
}//End of Actual temperature function


void le_sensores (void)
{
	if (adc_data_available == YES || sensor == 1)
	{
		adc_data_available = NO;
		ana[sensor] = actual_temp ();

		if (sensor <= SENSORES)
			captura_adc (sensor);

		sensor = (++sensor) % (SENSORES + 2);
	}
}


