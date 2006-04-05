#!/usr/bin/env python
# -*- coding: latin-1 -*-

class HTTranslator (object):
    """ Classe responsável pela tradução de um dado sinal da luva.
    
    O sinal corresponde a duas tuplas, uma com os valores dos sensores
    AD de cada dedo, e outra com os valores booleanos dos contatos.

    fingers = [polegar, indicador, médio, anelar, mínimo]
    contacts = (polegar_indicador, 
                polegar_medio_ponta, polegar_medio_base,
                indicador_medio)
    """

    # Constantes da Lógica Fuzzy
    INPUT_VARIABLES = 3
    CONTRACTED, RELAXED, STRAINED = range(INPUT_VARIABLES)

    # Mapeamento das letras
    MAPPING = {
            'A': {'fingers': [STRAINED, CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, True]},
            'B': {'fingers': [CONTRACTED, STRAINED, STRAINED, STRAINED, STRAINED],
                  'contacts': [False, False, True, False]},
            'C': {'fingers': [STRAINED, CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, False]},
            'D': {'fingers': [RELAXED, STRAINED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [True, False, False, False]},
            'E': {'fingers': [CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, False]},
            'F': {'fingers': [STRAINED, RELAXED, STRAINED, STRAINED, STRAINED],
                  'contacts': [False, False, False, True]},
            'G': {'fingers': [RELAXED, STRAINED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, True]},
            'H': {'fingers': [STRAINED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, True, True, False]},
            'I': {'fingers': [CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED, STRAINED],
                  'contacts': [False, False, True, False]},
            'J': {'fingers': [CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED, RELAXED],
                  'contacts': [False, False, True, False]},
            'K': {'fingers': [STRAINED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, True, False, False]},
            'L': {'fingers': [STRAINED, STRAINED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, False]},
            'M': {'fingers': [CONTRACTED, STRAINED, STRAINED, STRAINED, CONTRACTED],
                  'contacts': [False, False, True, True]},
            'N': {'fingers': [CONTRACTED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, True]},
            'O': {'fingers': [RELAXED, CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [True, False, True, False]},
            'P': {'fingers': [STRAINED, STRAINED, RELAXED, CONTRACTED, CONTRACTED],
                  'contacts': [False, True, False, False]},
            'Q': {'fingers': [RELAXED, RELAXED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, True]},
            'R': {'fingers': [RELAXED, STRAINED, RELAXED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, False]},
            'S': {'fingers': [RELAXED, CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, False]},
            'T': {'fingers': [RELAXED, RELAXED, STRAINED, STRAINED, STRAINED],
                  'contacts': [False, False, False, False]},
            'U': {'fingers': [CONTRACTED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, False]},
            'V': {'fingers': [CONTRACTED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, False]},
            'W': {'fingers': [RELAXED, STRAINED, STRAINED, STRAINED, CONTRACTED],
                  'contacts': [False, False, False, False]},
            'X': {'fingers': [RELAXED, RELAXED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, False]},
            'Y': {'fingers': [STRAINED, CONTRACTED, CONTRACTED, CONTRACTED, STRAINED],
                  'contacts': [False, False, True, False]},
            'Z': {'fingers': [RELAXED, STRAINED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, False]},
            'VI': {'fingers': [RELAXED, CONTRACTED, CONTRACTED, STRAINED, STRAINED],
                  'contacts': [False, False, True, False]},
            'PT': {'fingers': [STRAINED, STRAINED, STRAINED, STRAINED, STRAINED],
                  'contacts': [True, False, True, False]},
            'EX': {'fingers': [STRAINED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, False]},
            'IN': {'fingers': [STRAINED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, False]},
            'SP': {'fingers': [RELAXED, STRAINED, STRAINED, STRAINED, STRAINED],
                  'contacts': [False, False, True, True]},
            'BS': {'fingers': [STRAINED, STRAINED, STRAINED, STRAINED, STRAINED],
                  'contacts': [False, False, True, False]},
            'CR': {'fingers': [STRAINED, STRAINED, CONTRACTED, CONTRACTED, STRAINED],
                  'contacts': [False, False, False, False]}
    } # MAPPING 

    """
    # Mapeamento alternativo das letras
    MAPPING = {
            'A': {'fingers': [STRAINED, CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, True]},
            'B': {'fingers': [CONTRACTED, STRAINED, STRAINED, STRAINED, STRAINED],
                  'contacts': [False, False, True, False]},
#            'C': {'fingers': [RELAXED, RELAXED, RELAXED, RELAXED, RELAXED],
#                  'contacts': [False, False, True, False]},
#            'D': {'fingers': [RELAXED, STRAINED, RELAXED, RELAXED, RELAXED],
#                  'contacts': [True, False, False, False]},
            'E': {'fingers': [CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, False]},
            'F': {'fingers': [RELAXED, RELAXED, STRAINED, STRAINED, STRAINED],
                  'contacts': [False, False, False, True]},
            'G': {'fingers': [RELAXED, STRAINED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, True]},
            'H': {'fingers': [RELAXED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, True, True, False]},
            'I': {'fingers': [RELAXED, CONTRACTED, CONTRACTED, CONTRACTED, STRAINED],
                  'contacts': [False, False, True, False]},
            'J': {'fingers': [RELAXED, CONTRACTED, CONTRACTED, CONTRACTED, RELAXED],
                  'contacts': [False, False, True, False]},
            'K': {'fingers': [RELAXED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, True, False, False]},
            'L': {'fingers': [STRAINED, STRAINED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, False]},
            'M': {'fingers': [RELAXED, STRAINED, STRAINED, STRAINED, CONTRACTED],
                  'contacts': [False, False, True, False]},
            'N': {'fingers': [RELAXED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, True]},
            'O': {'fingers': [RELAXED, RELAXED, RELAXED, RELAXED, RELAXED],
                  'contacts': [True, False, True, False]},
            'P': {'fingers': [RELAXED, STRAINED, RELAXED, CONTRACTED, CONTRACTED],
                  'contacts': [False, True, False, False]},
            'Q': {'fingers': [RELAXED, RELAXED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, True]},
            'R': {'fingers': [RELAXED, STRAINED, RELAXED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, False]},
            'S': {'fingers': [RELAXED, CONTRACTED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, False]},
            'T': {'fingers': [RELAXED, RELAXED, STRAINED, STRAINED, STRAINED],
                  'contacts': [False, False, False, False]},
            'U': {'fingers': [RELAXED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, False]},
            'V': {'fingers': [RELAXED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, False]},
            'W': {'fingers': [RELAXED, STRAINED, STRAINED, STRAINED, CONTRACTED],
                  'contacts': [False, False, False, False]},
            'X': {'fingers': [RELAXED, RELAXED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, False]},
            'Y': {'fingers': [STRAINED, CONTRACTED, CONTRACTED, CONTRACTED, STRAINED],
                  'contacts': [False, False, True, False]},
            'Z': {'fingers': [RELAXED, STRAINED, CONTRACTED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, False]},
            ',': {'fingers': [RELAXED, CONTRACTED, CONTRACTED, STRAINED, STRAINED],
                  'contacts': [False, False, True, False]},
            '.': {'fingers': [STRAINED, STRAINED, STRAINED, STRAINED, STRAINED],
                  'contacts': [True, False, True, False]},
            '!': {'fingers': [STRAINED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, True, False]},
            '?': {'fingers': [STRAINED, STRAINED, STRAINED, CONTRACTED, CONTRACTED],
                  'contacts': [False, False, False, False]},
            '<SP>': {'fingers': [RELAXED, STRAINED, STRAINED, STRAINED, STRAINED],
                  'contacts': [False, False, True, True]},
            '<BS>': {'fingers': [STRAINED, STRAINED, STRAINED, STRAINED, STRAINED],
                  'contacts': [False, False, True, False]},
            '<CR>': {'fingers': [STRAINED, STRAINED, CONTRACTED, CONTRACTED, STRAINED],
                  'contacts': [False, False, False, False]}
    } # MAPPING 
    """

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

        # Pesos de entrada
        self.__u_in = [ [0.0 for finger in range(5)]
                        for input in range (self.INPUT_VARIABLES) ]

        # Saída
        self.__result = None
        
    # __init__()


    def getResult (self):
        """ Retorna o resultado (letra) da última tradução efetuada.
        """
        return self.__result

    def getUIn (self):
        """ Retorna pesos de entrada da última tradução efetuada.
        """
        return self.__u_in

    result = property (getResult, None, None, "Resultado (letra) da última tradução")
    u_in = property (getUIn, None, None, "Pesos de entrada da última tradução")


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

#        print "Dedos:", self.fingers
#        print "Contatos:", self.contacts

        """
        # Calcula o peso de cada variável de entrada (contraído etc.)
        self.__u_in = [ [0.0 for finger in range(5)]
                 for input in range (self.INPUT_VARIABLES) ]
        for finger in range(5):
            if self.fingers[finger] <= self.contracted[finger]:
                self.__u_in[self.CONTRACTED] [finger] = 1.0
                self.__u_in[self.RELAXED] [finger] = 0.0
                self.__u_in[self.STRAINED] [finger] = 0.0
            
            elif self.contracted[finger] < self.fingers[finger] <= self.relaxed[finger]:
                self.__u_in[self.CONTRACTED] [finger] = ((self.fingers[finger]    - self.relaxed[finger]) /
                                                  (self.contracted[finger] - self.relaxed[finger]))
                self.__u_in[self.RELAXED] [finger] = 1.0 - self.__u_in[self.CONTRACTED] [finger]
                self.__u_in[self.STRAINED] [finger] = 0.0

            elif self.relaxed[finger] < self.fingers[finger] <= self.strained[finger]:
                self.__u_in[self.CONTRACTED] [finger] = 0.0
                self.__u_in[self.RELAXED] [finger] = ((self.fingers[finger] - self.strained[finger]) /
                                               (self.relaxed[finger] - self.strained[finger]))
                self.__u_in[self.STRAINED] [finger] = 1.0 - self.__u_in[self.RELAXED] [finger]

            elif self.fingers[finger] > self.strained[finger]:
                self.__u_in[self.CONTRACTED] [finger] = 0.0
                self.__u_in[self.RELAXED] [finger] = 0.0
                self.__u_in[self.STRAINED] [finger] = 1.0
        """

        # ALTERNATIVA: Calcula o peso de cada variável de entrada (contraído etc.)
        for finger in range(5):
            x1 = self.contracted[finger]
            x2 = x1 + 20
            x3 = x2 + 40
            x4 = self.strained[finger]

            if self.fingers[finger] <= x1:
                self.__u_in[self.CONTRACTED][finger] = 1.0
                self.__u_in[self.RELAXED]   [finger] = 0.0
                self.__u_in[self.STRAINED]  [finger] = 0.0
            
            elif x1 < self.fingers[finger] <= x2:
                self.__u_in[self.CONTRACTED][finger] = ((self.fingers[finger] - x2) /
                                                 (x1                   - x2))
                self.__u_in[self.RELAXED]   [finger] = 1.0 - self.__u_in[self.CONTRACTED][finger]
                self.__u_in[self.STRAINED]  [finger] = 0.0

            elif x2 < self.fingers[finger] <= x3:
                self.__u_in[self.CONTRACTED][finger] = 0.0
                self.__u_in[self.RELAXED]   [finger] = 1.0
                self.__u_in[self.STRAINED]  [finger] = 0.0

            elif x3 < self.fingers[finger] <= x4:
                self.__u_in[self.CONTRACTED][finger] = 0.0
                self.__u_in[self.RELAXED]   [finger] = ((self.fingers[finger] - x4) /
                                                 (x3                   - x4))
                self.__u_in[self.STRAINED]  [finger] = 1.0 - self.__u_in[self.RELAXED][finger]

            elif x4 < self.fingers[finger]:
                self.__u_in[self.CONTRACTED][finger] = 0.0
                self.__u_in[self.RELAXED]   [finger] = 0.0
                self.__u_in[self.STRAINED]  [finger] = 1.0


        # Apenas exibe
#        print u"Pesos de entrada:"
#        NOMES = [u'Contraído', 'Relaxado', 'Esticado']
#        for inputs in range (self.INPUT_VARIABLES):
#            print "%s:" % NOMES[inputs],
#            for valor in self.__u_in[inputs]:
#                print "\t%d%%" % (valor*100),
#            print
#        print

#        print u"Pesos de saída:"

        # Calcula o peso de cada variável de saída (letras)
        u_out = {}
        max_u_out = [0.0, 0.0]
        out_letter = [None, None]
        for letter in self.MAPPING:
            # Ignora letras que não coincidiram pelos contatos
            if self.MAPPING[letter]['contacts'] == self.contacts:
#                print "%s:\t" % letter,
                u_out [letter] = 0.0
                
                for finger in range(5):
                    finger_input = self.MAPPING[letter]['fingers'][finger]
                    finger_weight = self.__u_in [finger_input][finger]
#                    print "\t%d%%" % (finger_weight*100),
                    u_out [letter] += finger_weight

                u_out [letter] /= 5.0
#                print "\t=%d%%" % (u_out[letter]*100)

                if u_out [letter] > max_u_out[0]:
                    max_u_out[1] = max_u_out[0]
                    max_u_out[0] = u_out [letter]
                    out_letter[1] = out_letter[0]
                    out_letter[0] = letter
                elif u_out [letter] > max_u_out[1]:
                    max_u_out[1] = u_out [letter]
                    out_letter[1] = letter

        
        # Chance maior de 70%
        if max_u_out[0] > 0.7:
            # Checa se deu empate em 5%
            advantage = (max_u_out[0] - max_u_out[1]) / max_u_out[0]
            if advantage <= 0.05:
#                print u"Empate entre %s e %s" % tuple(out_letter)
                out_letter[0] = None
#            else:
#                print u"Máximo: %s, %d%%" % (out_letter[0], max_u_out[0]*100)
        else:
            out_letter[0] = None
#            print u"Nenhuma letra"

#        print

        self.__result = out_letter[0]
        return self.__result

    # translate()

    
# Código de teste da classe HTTranslator
if __name__ == "__main__":
    contraido = [1, 2, 1, 1, 2]
    relaxado = [45, 30, 42, 58, 41]
    esticado = [165, 170, 172, 168, 171]

    tradutor = HTTranslator ()
    tradutor.adjust (esticado, relaxado, contraido)

    print "\n** Letra A **"
    dedos = [150, 4, 6, 3, 1]
    contatos = [False, False, True, True]
    tradutor.translate (dedos, contatos)

    print "\n** Letra B **"
    dedos = [1, 140, 164, 137, 128]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra C **"
    dedos = [50, 40, 64, 37, 28]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra D **"
    dedos = [50, 140, 64, 37, 28]
    contatos = [True, False, False, False]
    tradutor.translate (dedos, contatos)
    
    print "\n** Letra E **"              
    dedos = [5, 1, 4, 3, 2]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra F **"
    dedos = [35, 47, 147, 163, 172]
    contatos = [False, False, False, True]
    tradutor.translate (dedos, contatos)
    
    print "\n** Letra G **"
    dedos = [35, 147, 1, 3, 2]
    contatos = [False, False, False, True]
    tradutor.translate (dedos, contatos)
    
    print "\n** Letra H **"
    dedos = [35, 147, 152, 3, 2]
    contatos = [False, True, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra I **"
    dedos = [35, 4, 1, 3, 152]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra J **"
    dedos = [35, 4, 1, 3, 52]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra K **"
    dedos = [35, 154, 161, 3, 2]
    contatos = [False, True, False, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra L **"
    dedos = [135, 174, 1, 3, 5]
    contatos = [False, False, False, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra M **"
    dedos = [45, 174, 163, 138, 5]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra N **"
    dedos = [45, 174, 163, 8, 5]
    contatos = [False, False, True, True]
    tradutor.translate (dedos, contatos)

    print "\n** Letra O **"
    dedos = [53, 48, 32, 10, 59]
    contatos = [True, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra P **"
    dedos = [53, 148, 82, 1, 9]
    contatos = [False, True, False, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra Q **"
    dedos = [53, 48, 2, 1, 9]
    contatos = [False, False, False, True]
    tradutor.translate (dedos, contatos)

    print "\n** Letra R **"
    dedos = [53, 148, 68, 1, 9]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra S **"
    dedos = [53, 4, 6, 1, 9]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra T **"
    dedos = [53, 74, 163, 175, 190]
    contatos = [False, False, False, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra U **"
    dedos = [53, 174, 163, 1, 9]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra V **"
    dedos = [53, 174, 163, 1, 9]
    contatos = [False, False, False, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra W **"
    dedos = [53, 174, 163, 158, 9]
    contatos = [False, False, False, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra X **"
    dedos = [53, 74, 6, 5, 9]
    contatos = [False, False, False, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra Y **"
    dedos = [153, 4, 6, 5, 179]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra Z **"
    dedos = [53, 164, 6, 5, 1]
    contatos = [False, False, False, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra . **"
    dedos = [153, 174, 163, 175, 190]
    contatos = [True, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra , **"
    dedos = [53, 4, 1, 163, 159]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra ! **"
    dedos = [153, 174, 163, 1, 9]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra ? **"
    dedos = [157, 174, 163, 5, 9]
    contatos = [False, False, False, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra <SP> **"
    dedos = [153, 174, 163, 158, 179]
    contatos = [False, False, True, True]
    tradutor.translate (dedos, contatos)

    print "\n** Letra <BS> **"
    dedos = [153, 164, 186, 175, 179]
    contatos = [False, False, True, False]
    tradutor.translate (dedos, contatos)

    print "\n** Letra <CR> **"
    dedos = [153, 164, 6, 5, 174]
    contatos = [False, False, False, False]
    tradutor.translate (dedos, contatos)

