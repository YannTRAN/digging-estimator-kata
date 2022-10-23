import math


class digging:

    def __init__(self,dig_per_rotation,length,days):
        self.dig_per_rotation = dig_per_rotation
        self.length = length
        self.day = days

    def miner(self):
        self.dt_miner = 0
        self.nt_miner = 0


        for i in range(0, len(self.dig_per_rotation)-1):
            if self.dig_per_rotation[i] < math.floor(self.length / self.days):
                self.self.dt_miner += 1

        if math.floor(self.length / self.days) > self.max_dig_per_rotation:
            for i in range(0, len(self.dig_per_rotation) -1):
                if self.dig_per_rotation[i] + self.max_dig_per_rotation < math.floor(self.length / self.days):
                    self.self.nt_miner += 1

        return self.dt_miner,self.nt_miner



    def healers(self):
        pass

    def smithies(self):
        pass

    def lighters(self):

        self.nbr_lighters = self.dt_miner + self.nt_miner + 1


        return self.nbr_lighters

    def inn_keepers(self):
        pass

    def guards(self):
        pass

    def guard_managers(self):
        pass

    def protectors(self):
        pass


