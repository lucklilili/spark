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

from pyspark.pandas.tests.data_type_ops.test_udt_ops import UDTOpsTestsMixin
from pyspark.pandas.tests.connect.data_type_ops.testing_utils import OpsTestBase
from pyspark.testing.pandasutils import PandasOnSparkTestUtils
from pyspark.testing.connectutils import ReusedConnectTestCase


class UDTOpsParityTests(
    UDTOpsTestsMixin, PandasOnSparkTestUtils, OpsTestBase, ReusedConnectTestCase
):
    @unittest.skip(
        "TODO(SPARK-43702): Fix pyspark.sql.pandas.types.to_arrow_type to work with Spark Connect."
    )
    def test_eq(self):
        super().test_eq()

    @unittest.skip(
        "TODO(SPARK-43702): Fix pyspark.sql.pandas.types.to_arrow_type to work with Spark Connect."
    )
    def test_from_to_pandas(self):
        super().test_from_to_pandas()

    @unittest.skip(
        "TODO(SPARK-43702): Fix pyspark.sql.pandas.types.to_arrow_type to work with Spark Connect."
    )
    def test_ge(self):
        super().test_ge()

    @unittest.skip(
        "TODO(SPARK-43702): Fix pyspark.sql.pandas.types.to_arrow_type to work with Spark Connect."
    )
    def test_gt(self):
        super().test_gt()

    @unittest.skip(
        "TODO(SPARK-43702): Fix pyspark.sql.pandas.types.to_arrow_type to work with Spark Connect."
    )
    def test_isnull(self):
        super().test_isnull()

    @unittest.skip(
        "TODO(SPARK-43702): Fix pyspark.sql.pandas.types.to_arrow_type to work with Spark Connect."
    )
    def test_le(self):
        super().test_le()

    @unittest.skip(
        "TODO(SPARK-43702): Fix pyspark.sql.pandas.types.to_arrow_type to work with Spark Connect."
    )
    def test_lt(self):
        super().test_lt()

    @unittest.skip(
        "TODO(SPARK-43702): Fix pyspark.sql.pandas.types.to_arrow_type to work with Spark Connect."
    )
    def test_ne(self):
        super().test_ne()


if __name__ == "__main__":
    from pyspark.pandas.tests.connect.data_type_ops.test_parity_udt_ops import *  # noqa: F401

    try:
        import xmlrunner  # type: ignore[import]

        testRunner = xmlrunner.XMLTestRunner(output="target/test-reports", verbosity=2)
    except ImportError:
        testRunner = None
    unittest.main(testRunner=testRunner, verbosity=2)
