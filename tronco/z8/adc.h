/*************************************************************************
 * File       : adc.h
 * Description: 
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

#ifndef ADC_H
#define ADC_H
 
#define SENSORES		2

#define ADC_INT_EN			0x01				// Enable ADC interrupts

//ADC Control Register 1 control bits
#define ADC_CEN			0x80				// ADC Conversion Enable
#define ADC_REFSELL		0x40
#define ADC_REFEXT		0x20
#define ADC_CONT		0x10
#define ADC_ANAIN_ANA1 	0x01
#define ADC_ANAIN_ANA2 	0x02				
#define ADC_ANAIN_ANA3 	0x03				
#define ADC_ANAIN_TEMP 	0x0e				// Select ADC Temperature Sensor Input 

//ADC Control Register 2 control bits
#define ADC_REFSELH			0x80
#define ADC_UNBUF_INPUT 	0x00				// Single-ended, unbuffered input
#define ADC_BUF_INPUT_X1 	0x01				// Single-ended, buffered with unity gain

// void isr_ADC(void);
void inicia_adc(void);
void le_sensores (void);

#endif // ADC_H

