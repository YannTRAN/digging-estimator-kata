import math
from python.src.digging import *

class TunnelTooLongForDelayException(Exception):
    pass


class InvalidFormatException(Exception):
    pass


class Team:
    miners = 0
    healers = 0
    smithies = 0
    lighters = 0
    inn_keepers = 0
    guards = 0
    guard_managers = 0
    washers = 0


class TeamComposition:
    day_team: Team = Team()
    night_team: Team = Team()

    total = 0


class DiggingEstimator2:
    def tunnel(self, length, days, rock_type):
        dig_per_rotation = self.get(rock_type)
        max_dig_per_rotation = dig_per_rotation[len(dig_per_rotation) - 1]
        max_dig_per_day = 2 * max_dig_per_rotation

        if math.floor(length) != length or math.floor(days) != days or length < 0 or days < 0:
            raise InvalidFormatException()
        if math.floor(length / days) > max_dig_per_day:
            raise TunnelTooLongForDelayException()

        composition = TeamComposition()


        # Miners
        dt = composition.day_team
        nt = composition.night_team

        digginh = digging(max_dig_per_rotation,dig_per_rotation,length,days)


        dt.miners += digginh.miner()[0]
        nt.miners += digginh.miner()[1]

        dt.healers += digginh.healers()[0]
        nt.healers += digginh.healers()[1]

        dt.smithies += digginh.smithies()[0]
        nt.smithies += digginh.smithies()[1]

        nt.lighters += digginh.lighters()

        dt.inn_keepers += digginh.inn_keepers()[0]
        nt.inn_keepers += digginh.inn_keepers()[1]




        dt.washers = digginh.washers()[0]




        while True:
            old_washers = nt.washers
            old_guards = nt.guards
            old_chief_guard = nt.guard_managers

            nt.washers = digginh.washers()[1]
            nt.guards = digginh.guards()
            nt.guard_managers = digginh.guard_managers()

            if old_washers == nt.washers and old_guards == nt.guards and old_chief_guard == nt.guard_managers:
                break

        print("nt whasher:", nt.washers)
        print("nt inn_keeper:", nt.inn_keepers)
        print('nt.guards:',nt.guards)

        print(dt)
        composition.total = dt.miners + dt.washers + dt.healers + dt.smithies + dt.inn_keepers + nt.miners + nt.washers + nt.healers + nt.smithies + nt.inn_keepers + nt.guards + nt.guard_managers + nt.lighters

        return composition

    def get(self, rock_type):
        # for example for granite it returns [0, 3, 5.5, 7]
        # if you put 0 dwarf, you dig 0m / d / team
        # if you put 1 dwarf, you dig 3m / d / team
        # 2 dwarves = 5.5 m / d / team
        # so a day team on 2 miners and a night team of 1 miner dig 8.5 m / d
        url = "dtp://research.vin.co/digging-rate/" + rock_type
        print("Trying to fetch" + url)
        raise Exception("Does not work in test mode")



