/*************************************************
 *  Copyright (C) 1999-2004 by  ZiLOG, Inc.
 *  All Rights Reserved
 *************************************************/

#ifndef MAIN
#define MAIN

///////////////////////////////////////////////////////////
// Definition Program status
#define RUN			0
#define BUSY		1
#define UP			0
#define DOWN		1
#define HIGH_SET_TEMP	40			//Higher temperature limit 
#define LOW_SET_TEMP    10          //Lower  temperature limit
#define YES		(unsigned char)1
#define NO		(unsigned char)0

///////////////////////////////////////////////////////////
// Function Prototypes

void setStatus( int status );
void toggle_port(void);
void init_led_gpio(void);
void toggle_uart(void);
void init_test_button_gpio(void);
void turn_off_led(void);
void turn_on_led(void);

#endif
