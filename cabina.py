class Cabina:
    def __init__(self, codice_cab, num_letti, num_ponte, prezzo):
        self.codiceCab = codice_cab
        self.numLetti = int(num_letti)
        self.numPonte = int(num_ponte)
        self.prezzo = int(prezzo)

    def __str__(self):
        return f"Cabina: {self.codiceCab}| letti: {self.numLetti} | ponte: {self.numPonte} | prezzo: {self.prezzo}"

    def __repr__(self):
        return f"Cabina: {self.codiceCab}| letti: {self.numLetti} | ponte: {self.numPonte} | prezzo: {self.prezzo}"