import unittest

import requests
import random

class UserApiEndpointIntegration(unittest.TestCase):
    def test_scenario_retrieve_user_details_from_list(self):
        res = requests.get('http://127.0.0.1:7070/api/v0/users')

        # Check that the API returns a correct 200 OK
        self.assertEqual(res.status_code, 200, "Return status should be 200 OK not '{}'".format(res.status_code))

        out = res.json()

        # Check that all keys are present
        for item in out['items']:
            self.assertCountEqual(item.keys(), ['id', 'first_name','last_name'])

        # Use random entry in list to retrieve details
        user = random.choices(out['items'])[0]

        # Retrieve user details based on the id
        res_user_details = requests.get('http://127.0.0.1:7070/api/v0/users/{}'.format(user['id']))
        self.assertEqual(res_user_details.status_code, 200, "Return status should be 200 OK not '{}'".format(res_user_details.status_code))

        # Check that now the additonal information (age and mail) are present
        user_out = res_user_details.json()
        self.assertCountEqual(user_out.keys(), ['id', 'first_name','last_name', 'age', 'mail', 'gender'])

if __name__ == "__main__":
    unittest.main()
