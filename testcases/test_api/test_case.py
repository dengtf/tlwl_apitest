# --coding:utf-8--
import pytest

from aomaker.base.base_testcase import BaseTestcase
from aomaker import aomaker
from apis.student import StudentDetails

import apis

test_data_file_path = "data/api_data/case_data.yaml"


@pytest.mark.usefixtures("clear_resource")
class TestCase(BaseTestcase):
    @pytest.mark.case
    @pytest.mark.parametrize("test_data", aomaker.data_maker(test_data_file_path, "case", "student_case"))
    def test_student_account(self):
        res = apis.student.StudentDetails.account_data(280)
        self.assert_eq(res['code'], 0)