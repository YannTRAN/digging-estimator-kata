from python.src.digging_estimator_v2 import *
from python.src.digging_estimator_v2 import InvalidFormatException as InvalidFormatException_v2, TunnelTooLongForDelayException as TunnelTooLongForDelayException_v2
import pytest
import unittest
from unittest.mock import MagicMock


class DiggingEstimatorTest(unittest.TestCase):

    def test_error_negative_day(self):
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        with pytest.raises(InvalidFormatException_v2):
            estimator.tunnel(28, -100, "Granite")

    def test_error_impossible_digging(self):
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        with pytest.raises(TunnelTooLongForDelayException_v2):
            estimator.tunnel(50, 1, "Granite")

    def test_max_dw_miner_dt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        self.assertEqual(result.day_team.miners, 3)

    def test_max_dw_miner_nt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        self.assertEqual(result.night_team.miners, 3)

    def test_min_dw_miner_dt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(20, 2000, "Granite")
        self.assertEqual(result.day_team.miners, 0)

    def test_min_dw_miner_nt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(20, 2000, "Granite")
        self.assertEqual(result.night_team.miners, 0)

    def test_max_dw_guard_manager_total_nt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.night_team.guard_managers
        self.assertEqual(total_nt, 2)

    def test_max_dw_guard_total_nt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.night_team.guards
        self.assertEqual(total_nt, 6)

    def test_max_dw_healer_dt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.day_team.healers
        self.assertEqual(total_nt, 1)

    def test_max_dw_healer_nt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.night_team.healers
        self.assertEqual(total_nt, 1)

    def test_max_dw_smithies_dt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.day_team.smithies
        self.assertEqual(total_nt, 2)

    def test_max_dw_smithies_nt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.night_team.smithies
        self.assertEqual(total_nt, 2)

    def test_max_dw_washer_total_dt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.day_team.washers
        self.assertEqual(total_nt, 2)

    # Tests impactés par la nouvelle feature

    def test_max_dw_innkeeper_total_nt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.night_team.inn_keepers
        self.assertEqual(total_nt, 16)

    def test_max_dw_washer_total_nt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.night_team.washers
        self.assertEqual(total_nt, 4)

    def test_max_dw_lighter_total_nt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.night_team.lighters
        self.assertEqual(total_nt, 6)

    def test_max_dw_compo_total(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        self.assertEqual(result.total, 60)

    def test_max_dw_compo_total_nt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.night_team.miners + result.night_team.healers + result.night_team.smithies + result.night_team.lighters + result.night_team.inn_keepers + result.night_team.guards + result.night_team.guard_managers + result.night_team.washers + result.night_team.protectors
        self.assertEqual(total_nt, 42)

    def test_max_dw_compo_total_dt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_dt = result.day_team.miners + result.day_team.healers + result.day_team.smithies + result.day_team.lighters + result.day_team.inn_keepers + result.day_team.guards + result.day_team.guard_managers + result.day_team.washers +result.night_team.protectors
        self.assertEqual(total_dt, 18)

#  tests pour la nouvelle feature

    def test_max_dw_protector_dt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.day_team.protectors
        self.assertEqual(total_nt, 2)


    def test_max_dw_protector_nt(self):
        dig = Digging
        dig.gob = MagicMock(return_value=True)
        estimator = DiggingEstimator()
        estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "Granite")
        total_nt = result.night_team.protectors
        self.assertEqual(total_nt, 2)