import csv
from cabina import Cabina
from passeggeri import Passeggeri

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self.cabineDisponibiliL = []
        self.cabineOccupate = []
        self.passeggeriTotali = []
        self.passeggeriCabine = []

    def elenco_passeggeri(self, passeggeri):
        if passeggeri in self.passeggeriCabine:
            for passegger in self.passeggeriCabine:
                print(f"Passeggero: {passegger[1]} ha la cabina: {passegger[0]}")
        else:
            print(f"Passeggero: {passeggeri} non abbinato a una cabina")

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nuovo_nome):
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try :
            filein = open(file_path, newline='', encoding='utf-8')
            reader = csv.reader(filein)
            for line in reader:
                if "CAB" in line[0]:
                    if line[4] == "Lussuosa":
                        prezzof = int(line[3])*1.20
                    elif line[4].strip().isdigit():
                        num_animali = int(line[4])
                        prezzof = int(line[3])*(1 + 0.10*num_animali)
                    else:
                        prezzof = int(line[3])
                    cabina = Cabina(
                        codice_cab=line[0],
                        num_letti=line[1],
                        num_ponte=line[2],
                        prezzo=prezzof
                        )
                    self.cabineDisponibiliL.append(cabina)
                else:
                    passeggero = Passeggeri(
                        codice_pass=line[0],
                        nome=line[1],
                        cognome=line[2]
                        )
                    self.passeggeriTotali.append(passeggero)
            filein.close()

        except FileNotFoundError:
            print("File non trovato")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        if codice_cabina in self.cabineDisponibiliL:
            if codice_passeggero in self.passeggeriTotali:
                self.cabineOccupate.append(codice_cabina)
                self.passeggeriTotali.remove(codice_passeggero)
                self.passeggeriCabine.append([codice_cabina,codice_passeggero])
            else:
                print("Passegero non trovato")
        else:
            print("Cabina non disponibile")

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        return sorted(self.cabineOccupate, key=lambda cabina: cabina.prezzo)

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for pass_cab in self.passeggeriCabine:
            if pass_cab[1] == self.passeggeriTotali[0]:
                print(f"Passeggero: {pass_cab[1]}, Nome: {self.passeggeriTotali[1]}"
                      f"Cognome: {self.passeggeriTotali[2]} ha la cabina {pass_cab[0]}")
            else:
                print("Qualcosa è andato storto!")



