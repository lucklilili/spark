#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import unittest

from pyspark.pandas.tests.data_type_ops.test_binary_ops import BinaryOpsTestsMixin
from pyspark.pandas.tests.connect.data_type_ops.testing_utils import OpsTestBase
from pyspark.testing.pandasutils import PandasOnSparkTestUtils
from pyspark.testing.connectutils import ReusedConnectTestCase


class BinaryOpsParityTests(
    BinaryOpsTestsMixin, PandasOnSparkTestUtils, OpsTestBase, ReusedConnectTestCase
):
    @unittest.skip("TODO(SPARK-43620): Support `Column` for SparkConnectColumn.__getitem__.")
    def test_astype(self):
        super().test_astype()

    @unittest.skip("TODO(SPARK-43666): Fix BinaryOps.ge to work with Spark Connect Column.")
    def test_ge(self):
        super().test_ge()

    @unittest.skip("TODO(SPARK-43667): Fix BinaryOps.gt to work with Spark Connect Column.")
    def test_gt(self):
        super().test_gt()

    @unittest.skip("TODO(SPARK-43667): Fix BinaryOps.le to work with Spark Connect Column.")
    def test_le(self):
        super().test_le()

    @unittest.skip("TODO(SPARK-43667): Fix BinaryOps.lt to work with Spark Connect Column.")
    def test_lt(self):
        super().test_lt()


if __name__ == "__main__":
    from pyspark.pandas.tests.connect.data_type_ops.test_parity_binary_ops import *  # noqa: F401

    try:
        import xmlrunner  # type: ignore[import]

        testRunner = xmlrunner.XMLTestRunner(output="target/test-reports", verbosity=2)
    except ImportError:
        testRunner = None
    unittest.main(testRunner=testRunner, verbosity=2)
