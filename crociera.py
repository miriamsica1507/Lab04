import csv
from cabina import Cabina
from passeggeri import Passeggeri

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.cabineDisponibili = []
        self.cabineOccupate = []
        self.passeggeriTotali = []
        self.passeggeriCabine = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def cabineDisponibili(self,animali):
        pass

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        filein = open(file_path)
        reader = csv.reader(filein)
        for line in reader:
            if "CAB" in line[0]:
                cabina = Cabina(
                    codice_cab=line[0],
                    num_letti=line[1],
                    num_ponte=line[2],
                    prezzo=line[3]
                )
                self.cabineDisponibili.append(cabina)
            else:
                passeggero = Passeggeri(
                    codice_pass=line[0],
                    nome=line[1],
                    cognome=line[2]
                )
                self.passeggeriTotali.append(passeggero)
        filein.close()
        try:
            filein = open(file_path,"r", encoding="utf-8")
        except FileNotFoundError:
            print("File non trovato")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        if codice_cabina not in self.cabineDisponibili:
            if codice_passeggero in self.passeggeriTotali:
                self.cabineOccupate.append(codice_cabina)
                self.passeggeriTotali.remove(codice_passeggero)
                self.passeggeriCabine.append([codice_cabina,codice_passeggero])
            else:
                print("Passegero non trovato")
        else:
            print("Cabina non trovato")

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        cabine_ordinate = []
        for cabina in self.cabineDisponibili:
            cabine_ordinate.append(cabina)
        cabine_ordinate.sort(key=lambda cabina: cabina.prezzo)
        return cabine_ordinate


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for pass_cab in self.passeggeriCabine:
            if pass_cab[1] == self.passeggeriTotali[0]:
                print(f"Passeggero: {pass_cab[1]}, Nome: {self.passeggeriTotali[1]}"
                      f"Cognome: {self.passeggeriTotali[2]} ha la cabina {pass_cab[0]}")
            else:
                print("Qualcosa è andato storto!")



