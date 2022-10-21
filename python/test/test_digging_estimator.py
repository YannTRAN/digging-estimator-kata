from python.src.digging_estimator import DiggingEstimator
import unittest
from unittest.mock import MagicMock


class DiggingEstimatorTest(unittest.TestCase):

    def test_returns_as_doctor_Pockosky_says(self):

        estimator = DiggingEstimator()
        estimator.get= MagicMock(return_value=[0, 3, 5.5, 7])
        result = estimator.tunnel(28, 2, "granite")
        assert result.total == 48