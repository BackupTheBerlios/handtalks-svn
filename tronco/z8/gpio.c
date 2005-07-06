/*************************************************
 *  Copyright (C) 1999-2004 by  ZiLOG, Inc.
 *  All Rights Reserved
 *************************************************/

#include <eZ8.h>

#include "main.h"
#include "gatilho.h"

/* Initializes GPIO */
void inicia_gpio (void)
{
    // Port A initialization
//    PAOUT = 0xF8;        // Start with LEDs on, PA[2:0]

    PAADDR = P_AFS1;
    PACTL = 0xDA;        // Selects alternate functions:

    PAADDR = P_AFS2;
    PACTL = 0xDA;        // UART0 Rx/Tx

    PAADDR = P_AF;
    PACTL = 0x3A;        // Exposes alternate functions: UART0 Rx/Tx

    PAADDR = P_DD;
    PACTL = 0xFF;        // PA[7:0]-input

    PAADDR = P_NUL;

    inicia_gatilho();  // Initialize Test Button (Port C)
	
}


