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
    MAPEAMENTO = {
            'A': {'fingers': (STRAINED, CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED),
                  'contacts': (True, False, False, False, True)},
            'B': {'fingers': (CONTRACTED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'C': {'fingers': (RELAXED, RELAXED, RELAXED, RELAXED, RELAXED),
                  'contacts': (False, False, False, False, True)},
            'D': {'fingers': (RELAXED, STRAINED, RELAXED, RELAXED, RELAXED),
                  'contacts': (False, False, True, False, True)},
            'E': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'F': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'G': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'H': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'I': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'J': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'K': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'L': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'M': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'N': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'O': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'P': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'Q': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'R': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'S': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'T': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'U': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'V': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'W': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'X': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'Y': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            'Z': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            ' ': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            ',': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            '.': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            '!': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            '?': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)},
            '\n': {'fingers': (STRAINED, STRAINED, STRAINED, STRAINED, STRAINED),
                  'contacts': (False, False, False, False, True)}
            } # MAPEAMENTO 

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
        if fingers is not None:
            self.fingers = fingers 
        if contacts is not None:
            self.contacts = contacts 

        # Calcula o peso de cada opção
        #relaxed_weight
        

        for letra in MAPEAMENTO:
            if letra['contacts'] == self.contacts:
                pass
        

    # translate()

    

if __name__ == "__main__":
    esticado = (1, 2, 1, 1, 2)
    relaxado = (65, 70, 72, 68, 71)
    contraido = (165, 170, 172, 168, 171)

    # Letra A
    dedos = (3, 4, 6, 3, 1)
    contatos = (True, False, False, False, True)
    
    tradutor = HTTranslator ()
    tradutor.adjust (esticado, relaxado, contraido)
    tradutor.translate (dedos, contatos)
    
    print "Resultado: ", tradutor.result
    
