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

    # Constantes da Lógica Fuzzy
    STRAINED, RELAXED, CONTRACTED = range(3)

    # Mapeamento das letras
    TABELA = {
            'A': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'B': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'C': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'D': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'E': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'F': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'G': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'H': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'I': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'J': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'K': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'L': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'M': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'N': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'O': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'P': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'Q': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'R': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'S': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'T': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'U': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'V': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'W': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'X': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'Y': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            'Z': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            ' ': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            ',': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            '.': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            '!': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            '?': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)},
            '\n': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, False)}
            }

    def __init__ (self):
        """ Método de inicialização dos atributos
        """

        # Ajuste da lógica fuzzy
        self.strained = None  	# esticado
        self.relaxed = None   	# relaxado
        self.contracted = None  # contraído

        # Valor atual dos sensores
        self.fingers = None
        self.contacts = None

        # Saída
        self._result = None
        
    # __init__()


    def getResult (self):
        return self._result

    result = property (getResult, None, None, "Resultado (letra) da tradução")


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

    # adjust()

    def translate (fingers=None, contacts=None):
        if strained is not None:
            self.strained = strained
        if relaxed is not None:
            self.relaxed = relaxed
        

    # translate()

    

