from unittest.mock import patch

from django.core.management import call_command  # lets us call the function
from django.db.utils import OperationalError  # the error that appears when db is not on
from django.test import TestCase


class CommandsTestCase(TestCase):
    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""

        with patch(
            "django.db.utils.ConnectionHandler.__getitem__"
        ) as gi:  # we are mocking the getitem function
            gi.return_value = True  # whenever getitem is called in our function, it will overwrite it and return true
            call_command("wait_for_db")  # this is the management command we are calling
            self.assertEqual(gi.call_count, 1)
            # we just want to make sure that the call was called once

    @patch("time.sleep", return_value=None)  # we are using patch as a decorator
    # we mocked the time.sleep cause we dont want to wait very long in our tests
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        # we want to check the db 5 times and we dont want to slow down the test execution with each wait

        with patch("django.db.utils.ConnectionHandler.__getitem__") as gi:
            # instead of adding a return value, we add a sideeffect from the python mock module
            # we are going to make it return 5 times the operational error
            gi.side_effect = [OperationalError] * 5 + [
                True
            ]  # the first 5 times we call gi, it will raise the operational error
            call_command("wait_for_db")
            self.assertEqual(gi.call_count, 6)

