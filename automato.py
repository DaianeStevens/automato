class Automato:
    def __init__(self):
        self.etapa_inicial = '0'
        self.etapa_final = '3'
        # dicionário em python para representar o autômato
        self.etapas = {
            '0': {'ç': '1'},
            '1': {'ã': '2'},
            '2': {'o': '3'}
        }

    def verificar_palavra(self, palavra):
        estado_atual = self.etapa_inicial
        for simbolo in palavra[-3::]:

            if simbolo in self.etapas[estado_atual]:
                # troca de estados
                estado_atual = self.etapas[estado_atual][simbolo]
            else:
                estado_atual = self.etapa_inicial

        # vai retornar true quando todo os estados passaram pelo if e a palavra foi verificada 
        return estado_atual in self.etapa_final
    
