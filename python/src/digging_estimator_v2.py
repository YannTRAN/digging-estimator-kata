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
    protectors = 0


class TeamComposition:
    day_team: Team = Team()
    night_team: Team = Team()

    total = 0

class DiggingEstimator:
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

        digging = Digging(max_dig_per_rotation, dig_per_rotation, length, days)

        dt.miners += digging.miner()[0]
        nt.miners += digging.miner()[1]

        dt.protectors += digging.protectors()[0]
        nt.protectors += digging.protectors()[1]

        dt.healers += digging.healers()[0]
        nt.healers += digging.healers()[1]

        dt.smithies += digging.smithies()[0]
        nt.smithies += digging.smithies()[1]

        nt.lighters += digging.lighters()

        dt.inn_keepers += digging.inn_keepers()[0]
        nt.inn_keepers += digging.inn_keepers()[1]

        dt.washers = digging.washers()[0]

        while True:
            old_washers = nt.washers
            old_guards = nt.guards
            old_chief_guard = nt.guard_managers

            nt.washers = digging.washers()[1]
            nt.guards = digging.guards()
            nt.guard_managers = digging.guard_managers()

            if old_washers == nt.washers and old_guards == nt.guards and old_chief_guard == nt.guard_managers:
                break


        composition.total = dt.miners + dt.washers + dt.healers + dt.smithies + dt.inn_keepers + dt.protectors + nt.miners + nt.washers + nt.healers + nt.smithies + nt.inn_keepers + nt.guards + nt.guard_managers + nt.lighters + nt.protectors

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
