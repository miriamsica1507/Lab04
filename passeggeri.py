class Passeggeri:
    def __init__(self, codice_pass, nome, cognome):
        self.codicaPass = codice_pass
        self.nomeP = nome
        self.cognomeP = cognome

    def __str__(self):
        return f"Passeggero: {self.codicaPass} | Nome: {self.nomeP} | Cognome: {self.cognomeP}"

    def __repr__(self):
        return f"Passeggero: {self.codicaPass} | Nome: {self.nomeP} | Cognome: {self.cognomeP}"