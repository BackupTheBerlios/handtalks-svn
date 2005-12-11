#!/usr/bin/env python
# -*- coding: latin-1 -*-

class HTTranslator (object):
    """ Classe responsável pela tradução de um dado sinal da luva.
    
    O sinal corresponde a duas tuplas, uma com os valores dos sensores
    AD de cada dedo, e outra com os valores booleanos dos contatos.

    fingers = (polegar, indicador, médio, anelar, mínimo)
    contacts = (pol_ind_frente, pol_ind_costas,
                pol_med_ponta, pol_med_base,
                ind-med)
    """

    # Constantes da Lógica Fuzzy
    INPUT_VARIABLES = 3
    CONTRACTED, RELAXED, STRAINED = range(INPUT_VARIABLES)

    # Mapeamento das letras
    MAPPING = {
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
    } # MAPPING 


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
        self.__result = None
        
    # __init__()


    def getResult (self):
        """ Retorna o resultado (letra) da última tradução efetuada.
        """
        return self.__result

    result = property (getResult, None, None, "Resultado (letra) da última tradução")


    def adjust (self, strained=None, relaxed=None, contracted=None):
        """ Ajusta os patamares da lógica fuzzy.
        Cada parâmetro é uma tupla com cinco valores, um para cada dedo
        """

        # TODO: Verificar consistência dos valores
        if strained is not None:
            self.strained = tuple ([ float(x) for x in strained ])
        if relaxed is not None:
            self.relaxed = tuple ([ float(x) for x in relaxed ])
        if contracted is not None:
            self.contracted = tuple ([ float(x) for x in contracted ])

    # adjust()
    

    def translate (self, fingers=None, contacts=None):
        """ Método que efetivamente faz a tradução do sinal de entrada numa
        letra, utilizando lógica fuzzy.
        """
        
        if fingers is not None:
            self.fingers = fingers 
        if contacts is not None:
            self.contacts = contacts 

        # Calcula o peso de cada variável de entrada (contraído etc.)
        input_weight = [ [0.0 for finger in range(5)]
                         for input in range (self.INPUT_VARIABLES) ]
        for finger in range(5):
            if self.fingers[finger] <= self.contracted[finger]:
                input_weight[self.CONTRACTED] [finger] = 1.0
                input_weight[self.RELAXED] [finger] = 0.0
                input_weight[self.STRAINED] [finger] = 0.0
            
            elif self.contracted[finger] < self.fingers[finger] <= self.relaxed[finger]:
                input_weight[self.CONTRACTED] [finger] = ((self.fingers[finger]    - self.relaxed[finger]) /
                                                          (self.contracted[finger] - self.relaxed[finger]))
                input_weight[self.RELAXED] [finger] = 1.0 - input_weight[self.CONTRACTED] [finger]
                input_weight[self.STRAINED] [finger] = 0.0

            elif self.relaxed[finger] < self.fingers[finger] <= self.strained[finger]:
                input_weight[self.CONTRACTED] [finger] = 0.0
                input_weight[self.RELAXED] [finger] = ((self.fingers[finger] - self.strained[finger]) /
                                                       (self.relaxed[finger] - self.strained[finger]))
                input_weight[self.STRAINED] [finger] = 1.0 - input_weight[self.RELAXED] [finger]

            elif self.fingers[finger] > self.strained[finger]:
                input_weight[self.CONTRACTED] [finger] = 0.0
                input_weight[self.RELAXED] [finger] = 0.0
                input_weight[self.STRAINED] [finger] = 1.0

        print u"** Pesos de entrada **"
        for inputs in range (self.INPUT_VARIABLES):
            print "%d: " % inputs,
            for valor in input_weight[inputs]:
                print "%d%%" % (valor*100),
            print
        print

        print u"** Pesos de saída **"

        # Calcula o peso de cada variável de saída (letras)
        output_weight = {}
        max_output_weight = 0.0
        output_letter = None
        for letter in self.MAPPING:
            # Ignora letras que não coincidiram pelos contatos
            if self.MAPPING[letter]['contacts'] == self.contacts:
                print "letra %s:" % letter,
                output_weight [letter] = 0.0
                
                for finger in range(5):
                    finger_input = self.MAPPING[letter]['fingers'][finger]
                    finger_weight = input_weight [finger_input][finger]
                    print "%d%%" % (finger_weight*100),
                    output_weight [letter] += finger_weight

                output_weight [letter] /= 5.0
                print ": %d%%" % (output_weight[letter]*100)

                if output_weight [letter] > max_output_weight:
                    max_output_weight = output_weight [letter]
                    output_letter = letter

        print u"Máximo: %s, %d%%" % (output_letter, max_output_weight*100)

        self.__result = output_letter
        return self.__result

    # translate()

    
# Código de teste da classe HTTranslator
if __name__ == "__main__":
    contraido = (1, 2, 1, 1, 2)
    relaxado = (65, 70, 72, 68, 71)
    esticado = (165, 170, 172, 168, 171)

    tradutor = HTTranslator ()
    tradutor.adjust (esticado, relaxado, contraido)

    # Letra A
    dedos = (150, 4, 6, 3, 1)
    contatos = (True, False, False, False, True)
    tradutor.translate (dedos, contatos)
    
    print "Resultado: ", tradutor.result
    
