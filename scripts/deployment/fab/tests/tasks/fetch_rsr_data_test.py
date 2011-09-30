#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import mox

from testing.helpers.execution import TestSuiteLoader, TestRunner

from fab.helpers.dataretriever import DataRetriever
from fab.tasks.dataretriever import FetchRSRData


class FetchRSRDataTest(mox.MoxTestBase):

    def setUp(self):
        super(FetchRSRDataTest, self).setUp()
        self.mock_data_retriever = self.mox.CreateMock(DataRetriever)

        self.fetch_rsr_data_task = FetchRSRData(self.mock_data_retriever)

    def test_has_expected_task_name(self):
        """fab.tests.tasks.fetch_rsr_data_test  Has expected task name"""

        self.assertEqual("fetch_rsr_data", FetchRSRData.name)

    def test_can_create_task_instance(self):
        """fab.tests.tasks.fetch_rsr_data_test  Can create task instance"""

        self.assertTrue(isinstance(FetchRSRData.create_task_instance(), FetchRSRData))

    def test_can_(self):
        """fab.tests.tasks.fetch_rsr_data_test  Can fetch RSR data from database server"""

        self.mock_data_retriever.fetch_data_from_database()
        self.mox.ReplayAll()

        self.fetch_rsr_data_task.run()


def suite():
    return TestSuiteLoader().load_tests_from(FetchRSRDataTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())