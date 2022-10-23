import math


class digging:

    def __init__(self,max_dig_per_rotation,dig_per_rotation,length,days):
        self.max_dig_per_rotation =max_dig_per_rotation
        self.dig_per_rotation = dig_per_rotation
        self.length = length
        self.days = days

        self.nt_guards = 0
        self.nt_guard_managers = 0

    def miner(self):
        self.dt_miners = 0
        self.nt_miners = 0

        for i in range(0, len(self.dig_per_rotation)-1):
            if self.dig_per_rotation[i] < math.floor(self.length / self.days):
                self.dt_miners += 1

        if math.floor(self.length / self.days) > self.max_dig_per_rotation:
            for i in range(0, len(self.dig_per_rotation) -1):
                if self.dig_per_rotation[i] + self.max_dig_per_rotation < math.floor(self.length / self.days):
                    self.nt_miners += 1

        return self.dt_miners,self.nt_miners



    def healers(self):
        self.dt_healers = 1
        self.nt_healers = 1

        return self.dt_healers,self.nt_healers


    def smithies(self):
        self.dt_smithies = 2
        self.nt_smithies = 2

        return self.dt_smithies,self.nt_smithies



    def lighters(self):
        self.nt_lighters = self.nt_miners + 1


        return self.nt_lighters


    def inn_keepers(self):
        self.dt_inn_keepers = math.ceil((self.dt_miners + self.dt_healers + self.dt_smithies) / 4.0) * 4
        self.nt_inn_keepers = math.ceil((self.nt_miners + self.nt_healers + self.nt_smithies + self.nt_lighters) / 4.0) * 4

        return self.dt_inn_keepers, self.nt_inn_keepers


    def guards(self):

        self.nt_guards = math.ceil((self.nt_healers + self.nt_miners + self.nt_smithies + self.nt_lighters + self.nt_washers) / 3.0)

        return self.nt_guards

    def guard_managers(self):
        self.nt_guard_managers = math.ceil((self.nt_guards) / 3.0)

        return self.nt_guard_managers

    def washers(self):
        self.dt_washers = math.ceil((self.dt_miners + self.dt_healers + self.dt_smithies + self.dt_inn_keepers) / 10.0)
        self.nt_washers = math.ceil((self.nt_miners + self.nt_healers + self.nt_smithies + self.nt_inn_keepers + self.nt_lighters + self.nt_guards + self.nt_guard_managers) / 10.0)

        return self.dt_washers,self.nt_washers




    def protectors(self):
        pass
