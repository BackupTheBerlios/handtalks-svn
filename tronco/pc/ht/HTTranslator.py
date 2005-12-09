#!/usr/bin/env python
# -*- coding: latin-1 -*-

class HTTranslator (object):
    """ Classe respons�vel pela tradu��o de um dado sinal da luva.
    
    O sinal corresponde a duas tuplas, uma com os valores dos sensores
    AD de cada dedo, e outra com os valores booleanos dos contatos.

    finger = (polegar, indicador, m�dio, anelar, m�nimo)
    contacts = (pol_ind_frente, pol_ind_costas,
                pol_med_ponta, pol_med_base,
                ind-med)
    """

    def __init__ (self):
        """ M�todo de inicializa��o dos atributos
        """

        # Ajuste da l�gica fuzzy
        self.strained = ()  # esticado
        self.relaxed = ()   # relaxado
        self.contracted = ()    # dobrado

        # Valor atual dos sensores
        self.fingers = self.relaxed
        self.contacts = (False, False, False, False, False)
        
    # __init__

    def adjust (strained=None, relaxed=None, contracted=None):
        """ Ajusta os patamares da l�gica fuzzy.
        Cada par�metro � uma tupla com cinco valores, um para cada dedo
        """
        if strained is not None:
            self.strained = strained
        if relaxed is not None:
            self.relaxed = relaxed
        if contracted is not None:
            self.contracted = folded

    # adjust

    def translate (fingers=None, contacts=None):
        if strained is not None:
            self.strained = strained
        if relaxed is not None:
            self.relaxed = relaxed

    # translate

