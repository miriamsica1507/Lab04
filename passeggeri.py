class Passeggeri:
    def __init__(self, codice_pass, nome, cognome):
        self.codice_pass = codice_pass
        self.nomeP = nome
        self.cognomeP = cognome

    def __str__(self):
        return f"Passeggero: {self.codice_pass} | Nome: {self.nomeP} | Cognome: {self.cognomeP}"

    def __repr__(self):
        return f"Passeggero: {self.codice_pass} | Nome: {self.nomeP} | Cognome: {self.cognomeP}"