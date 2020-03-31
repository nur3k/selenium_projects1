import json
import unittest
import requests


class LambdaTests(unittest.TestCase):
    def setUp(self):
        self.url = 'https://3k0lkwvsw7.execute-api.eu-central-1.amazonaws.com/Prod/Objects/'
        self.path_create_obj_req = '#/components/schemas/CreateObjectRequest'
        self.headers = {'content': 'application/json'}

    def return_post_create_obj_req_reponse(self, test_data):
        post_data = json.dumps(test_data)
        response = requests.post(url=self.url + self.path_create_obj_req, data=post_data, headers=self.headers)
        return response

    def test_name_no_string(self):
        data = {'Name': 12}
        request = self.return_post_create_obj_req_reponse(data)
        assert not request.ok

    def test_description_no_string(self):
        data = {'Description': 12}
        request = self.return_post_create_obj_req_reponse(data)
        assert not request.ok

    def test_name_left_border_fail(self):
        data = {'Name': 'a'}
        request = self.return_post_create_obj_req_reponse(data)
        assert not request.ok

    def test_name_left_border_pass(self):
        data = {'Name': 'ab'}
        request = self.return_post_create_obj_req_reponse(data)
        assert request.ok

    def test_name_right_border_pass(self):
        data = {'Name': '10CharsStr'}
        request = self.return_post_create_obj_req_reponse(data)
        assert request.ok

    def test_name_right_border_fail(self):
        data = {'Name': '11CharsStrg'}
        request = self.return_post_create_obj_req_reponse(data)
        assert not request.ok

    def test_description_right_border_pass(self):
        data = {'Name': 'Admin',
                'Description': "200CharStr" * 20}
        request = self.return_post_create_obj_req_reponse(data)
        assert request.ok

    def test_description_right_border_fail(self):
        data = {'Name': 'Admin',
                'Description': "200CharStr" * 20 + 'X'}
        request = self.return_post_create_obj_req_reponse(data)
        assert not request.ok

    def test_no_valid_params(self):
        data = {'name': 'name', 'Name': 'name'}
        desired_resp = {'Errors': {'name': ['unknown field']}}
        request = self.return_post_create_obj_req_reponse(data)
        assert request.status_code == 400 and request.json() == desired_resp

    def test_invalid_json(self):
        data = {'Name': 'name'}
        response = requests.post(url=self.url + self.path_create_obj_req, data=data, headers=self.headers)
        assert response.status_code == 415

    def test_invalid_header(self):
        data = {'Name': 'name'}
        headers = {'content': 'text/html'}
        response = requests.post(url=self.url + self.path_create_obj_req, data=data, headers=headers)
        print(response)
        assert response.status_code == 415

    def test_create_object_response(self):
        data = {'Name': 'ab', 'Description': 'Example Description'}
        request = self.return_post_create_obj_req_reponse(data)
        rep_json = request.json()
        assert all([k in rep_json.keys() and v in rep_json[k] for k, v in data.items()]) and 'Id' in rep_json.keys()


if __name__ == "__main__":
    unittest.main()
