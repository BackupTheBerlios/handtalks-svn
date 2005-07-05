/*************************************************
 * Hand-Talks!
 *
 * Módulo do gatilho
 *************************************************/

#include <eZ8.h>
#include "main.h"
#include "gatilho.h"

extern unsigned char sensor;

//////////////////////////////////////////////////////////
// Rotina de interrupção
#pragma interrupt
void isr_gatilho(void) 
{
	sensor = 1;
}


//////////////////////////////////////////////////////////
// Inicia a interrupção do gatilho
void inicia_gatilho(void)
{
	SET_VECTOR(P3AD, isr_gatilho); 
//	SET_VECTOR(P2AD, isr_gatilho); 

	PAADDR = 0x01;		// PA Data Dir = input:updated
	PACTL |= 0x08;      // PA3 input Ctrl
//	PACTL |= 0x04;      // PA2 input Ctrl

	IRQ1ENH |= 0x08;	// Set Interrupt Priority High
	IRQ1ENL |= 0x08;	// Set Interrupt Priority High
}


