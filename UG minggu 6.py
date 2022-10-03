class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None
    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None
class SLNC:
    def __init__(self):
        super()._init__()
        self._head = None
        self._tail = None
        self._size = 0 
    
    def isEmpty(self):
        return self._size == 0

    def insert_head(self, Node):
        baru = Node (e, None)
        if self.isEmpty() == True:
            self._head = baru
            self._tail = baru
            self._size = 1
        else:
            baru._next = self._head
            self._head = baru
            self._size += 1
    def delete(self, find):
        now = self._head
        before = Node (None, now)
        temu = False
        for i in range (0, self._size):
            if now._element == find:
                temu = True
                before._next = now._next
                self._size -= 1
                break
            else:
                now = now._next
                before._next = now
        if not temu:
            print('Tidak ditemukan', find)
    def print(self):
        listprint = list()
        now = self._head
        for i in range(0, self._size):
            listprint.append(now._element)
            now = now._next
        print(listprint)
slnc = SLNC()
    slnc.insert_head(201,"Hanif", 250000)
    slnc.insert_head(110,"Yudha", 150000)
    slnc.print()
    slnc.filter(100)
    slnc.print()
    slnc.update(200)
    slnc.update(50)
    slnc.print()
