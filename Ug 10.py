class RakObat:
    def __init__()

    def _getHash(self, obat):
        has = 0
        for char in str(obat):
            has += ord(char)
        return has % self.size
    def add(self, key, value):
        key_hash = self._getHash(key)
        key_value = [key, value]
        if self.map=[key_hash] is None:
            self.map[key_hash] = list ([key_value])
            return True
    if __name__ == "__main__":
        rak1 = RakObat()
        rak1.tambahObat("Covid", "AstraZeneca (A01)")
        rak1.tambahObat("Flu", "UltraFlu (A02)")
        rak1.tambahObat("Sakit Kepala", "Paramex (A03)")
        rak1.tambahObat("Maag", "Pro Maag (A04)")
        rak1.tambahObat("Sakit Kepala", "Bodrex (A05)")
    else:
        print('key Hash',key_hash,'sudah penuh')
        return False
        
    rak1.tambahObat("Vitamin", "Vitacimin")
    print(rak1.lihatObat("Sakit Kepala"))
    print(rak1.lihatObat("Migraine"))
    rak1.ambilObat("Flu")
    rak1.ambilObat("Malaria")
    rak1.printAll()