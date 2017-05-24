from locust import HttpLocust, TaskSet, task

class GithubLocust(TaskSet):
    @task(1)
    def get_repos(self):
        self.client.get('/users/paradell/repos')

class WebsiteUser(HttpLocust):
    task_set = GithubLocust
    min_wait = 5000
    max_wait = 9000

