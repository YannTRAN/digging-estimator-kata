from python.src.digging_estimator_v2 import *
from python.src.digging_estimator import *

from unittest.mock import MagicMock



estimator = DiggingEstimator()
estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
result = estimator.tunnel(28, 2, "Granite")


estimator = DiggingEstimator2()
estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])
result = estimator.tunnel(28, 2, "Granite")
