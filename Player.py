class Player():
    def __init__(self):
        self.name = "unknown"
        self.HP = 10
        self.MP = 10
        self.MHP = 10
        self.MMP = 10
        self.items = []
        self.attacks = []

    def setHP(self, newHP):
        self.HP = newHP if newHP < self.MHP else self.MHP

    def setMP(self, newMP):
        self.MP = newMP if newMP < self.MMP else self.MMP

    def print_status(self):
        print(self.name)
        print(f"HP = {self.HP}/{self.MHP}")
        print(f"MP = {self.MP}/{self.MMP}")
        print(self.items)
        print(self.attacks)
