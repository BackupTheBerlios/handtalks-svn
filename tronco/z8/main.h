/*************************************************
 *  Copyright (C) 1999-2004 by  ZiLOG, Inc.
 *  All Rights Reserved
 *************************************************/

#ifndef MAIN_H
#define MAIN_H


#define YES		(unsigned char)1
#define NO		(unsigned char)0


//////////////////////////////////////////////////////////////////////////////
// GPIO sub-register mnemonics
#define P_NUL    0x00  // No function
#define P_DD     0x01  // Data Direction
#define P_AF     0x02  // Alternate Function
#define P_0C     0x03  // Output Control (Open-Drain)
#define P_HDE    0x04  // High Drive Enable
#define P_SMRE   0x05  // STOP Mode Recovery Source Enable
#define P_PUE    0x06  // Pull-up Enable
#define P_AFS1   0x07  // Alternate Function Set 1
#define P_AFS2   0x08  // Alternate Function Set 2
                       // 09H–FFH No function


///////////////////////////////////////////////////////////
// Function Prototypes

void setStatus( int status );
void toggle_port(void);
void init_led_gpio(void);
void toggle_uart(void);
void init_test_button_gpio(void);
void turn_off_led(void);
void turn_on_led(void);

#endif // MAIN_H
