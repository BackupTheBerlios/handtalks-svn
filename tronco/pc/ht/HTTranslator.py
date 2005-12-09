#!/usr/bin/env python
# -*- coding: latin-1 -*-

class HTTranslator (object):
    """ Classe responsável pela tradução de um dado sinal da luva.
    
    O sinal corresponde a duas tuplas, uma com os valores dos sensores
    AD de cada dedo, e outra com os valores booleanos dos contatos.

    finger = (polegar, indicador, médio, anelar, mínimo)
    contacts = (pol_ind_frente, pol_ind_costas,
                pol_med_ponta, pol_med_base,
                ind-med)
    """

    def __init__ (self):
        """ Método de inicialização dos atributos
        """

        # Ajuste da lógica fuzzy
        self.strained = ()  # esticado
        self.relaxed = ()   # relaxado
        self.contracted = ()    # dobrado

        # Valor atual dos sensores
        self.fingers = self.relaxed
        self.contacts = (False, False, False, False, False)
        
    # __init__

    def adjust (strained=None, relaxed=None, contracted=None):
        """ Ajusta os patamares da lógica fuzzy.
        Cada parâmetro é uma tupla com cinco valores, um para cada dedo
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

