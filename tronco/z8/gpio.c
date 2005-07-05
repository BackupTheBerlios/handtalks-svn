/*************************************************
 *  Copyright (C) 1999-2004 by  ZiLOG, Inc.
 *  All Rights Reserved
 *************************************************/

#include <eZ8.h>

///////////////////////////////////////////////////////
// Initializes LED ports - Port A 
//

void init_led_gpio(void)
{
  PAADDR 	= 0x02;        //Changed to alternate mode to configure PA2
  PACTL 	&= 0xFB;		//as GPIO

  PAADDR 	= 0x01;     // PA Data Dir =
  PACTL 	&= 0xF8;   	// PA0-PA2 as Outputs

  PAOUT &= 0xF8;  	    // Turn on PA0-PA2  leds
}

///////////////////////////////////////////////////////
// Initializes Test button port - Port PA2 
//

void init_test_button_gpio(void)
{
  PAADDR 	= 0x01;     // PA Data Dir 
  PACTL 	|= 0x08;   	// PA3 as input
}

///////////////////////////////////////////////////////
//  Turns off ALL LEDs
//


