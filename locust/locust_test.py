from locust import HttpLocust, TaskSet, task

HOST = 'https://api.github.com'
REPO_URL = '/users/paradell/repos'


class GithubLocust(TaskSet):
    @task(1)
    def get_repos(self):
        self.client.get(REPO_URL)


class WebsiteUser(HttpLocust):
    task_set = GithubLocust
    min_wait = 5000
    max_wait = 9000
    host = HOST
