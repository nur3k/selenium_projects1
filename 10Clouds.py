import unittest
import requests


class APITests(unittest.TestCase):
    def setUp(self):
        self.page_url = "https://jsonplaceholder.typicode.com"
        self.given_postid = 13
        self.desired_number_of_comments = 5
        self.post_to_delete_id = 14

    def return_comments_from_given_posts_nr_as_json(self, post_nr):
        path = self.page_url+'/comments?postId={}'.format(post_nr)
        output = requests.get(path)
        return output.json()

    def return_given_post_as_json(self, post_nr):
        path = self.page_url+'/posts/{}'.format(post_nr)
        output = requests.get(path)
        return output.json()

    def test_comment_atributes(self):
        post_comments = self.return_comments_from_given_posts_nr_as_json(self.given_postid)
        assert isinstance(post_comments[0]["postId"], int)
        assert isinstance(post_comments[0]["id"], int)
        assert isinstance(post_comments[0]["email"], str)
        assert isinstance(post_comments[0]["body"], str)

    def test_desired_number_of_comments(self):
        posted_comments = self.return_comments_from_given_posts_nr_as_json(self.given_postid)
        assert len(posted_comments) == self.desired_number_of_comments

    def test_add_post(self):
        path = self.page_url+'/posts'
        data = {"title": 'foo', "body": 'bar', "userId": 1}
        header = {"Content-type": "application/json; charset=UTF-8"}
        req = requests.post(path, data, header)
        assert self.return_given_post_as_json(req.json()["id"])

    def test_edit_post(self):
        path = self.page_url + '/posts/{}'.format(self.given_postid)
        data = {"title": 'Changed Title', "body": 'Changed Body'}
        requests.patch(path, data)
        edited_comment = self.return_given_post_as_json(self.given_postid)
        assert all([k in edited_comment.keys() and v in edited_comment[k] for k, v in data.items()])

    def test_delete_post(self):
        path = self.page_url + '/posts/{}'.format(self.post_to_delete_id)
        requests.delete(path)
        assert not self.return_given_post_as_json(self.post_to_delete_id)


if __name__ == "__main__":
    unittest.main()