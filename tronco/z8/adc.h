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
void isr_ADC(void);
 
#define ADC_INT_EN			0x01				// Enable ADC interrupts

//ADC Control Register 1 control bits
#define ADC_EN				0x80				// ADC Conversion Enable
#define ADC_TEMP_CHANNEL 	0x13				// Select ADC Temperature Sensor Input 

//ADC Control Register 2 control bits
#define ADC_BUF_INPUT_X1 	0x00				// Single-ended, buffered with unity gain
