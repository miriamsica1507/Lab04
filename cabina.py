class Cabina:
    def __init__(self, codice_cab, num_letti, num_ponte, prezzo):
        self.codiceCab = codice_cab
        self.numLetti = int(num_letti)
        self.numPonte = int(num_ponte)
        self.prezzo = int(prezzo)

    def __str__(self):
        return (f"Cabina: {self.codiceCab}, numero di letti: {self.numLetti}, numero ponte: {self.numPonte}"
                f"prezzo: {self.prezzo}")