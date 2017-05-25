import requests
import time

HOST = 'https://api.github.com'
README_URL = '/repos/paradell/performance-backbone/readme'


class Transaction(object):
    def __init__(self):
        pass

    def run(self):
        # start the timer
        start_timer = time.time()
        response = requests.get(HOST+README_URL)
        response.raw.read()
        latency = time.time() - start_timer

        # store time spent in request in custom_timers, to make multi-mechanize show it properly in the output
        self.custom_timers['Get Repository Readme'] = latency

        # Assert that the API has returned a 200-OK http response
        assert (response.status_code == 200), 'Bad Response: HTTP %s' % response.status_code
