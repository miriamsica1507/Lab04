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
                if line[0].startswith("CAB"):
                    codice_cab=line[0].strip()
                    num_letti=int(line[1])
                    num_ponte=int(line[2])
                    prezzo = int(line[3])
                    if len(line) > 4:
                        tipo = line[4].strip()
                        if tipo == "Lussuosa":
                            prezzo = prezzo*1.20
                        elif tipo.isdigit():
                            num_animali = int(tipo)
                            prezzo = prezzo*(1+0.10*num_animali)

                    cabina = Cabina(codice_cab, num_letti, num_ponte, prezzo)
                    self.cabineDisponibiliL.append(cabina)
                else:
                    passeggero = Passeggeri(
                        codice_pass=line[0].strip(),
                        nome=line[1],
                        cognome=line[2]
                        )
                    self.passeggeriTotali.append(passeggero)
            filein.close()

        except FileNotFoundError:
            print("File non trovato")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        for cab in self.cabineDisponibiliL:
            if cab.codice_cab.strip() == codice_cabina.strip():
                self.cabineOccupate.append(cab)
                break
            else:
                print("Cabina non disponibile")
        for passeg in self.passeggeriTotali:
            if passeg.codice_pass.strip() == codice_passeggero.strip():
                self.passeggeriTotali.remove(passeg)
                break
            else:
                print("Passeggero non trovato")

        self.passeggeriCabine.append([codice_cabina, codice_passeggero])

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        return sorted(self.cabineDisponibiliL, key=lambda cabina: cabina.prezzo)

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for pass_cab in self.passeggeriCabine:
            print (f"Passeggero: {pass_cab[1]}, Codice cabina: {pass_cab[0]}")




