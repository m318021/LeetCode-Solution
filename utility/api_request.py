from sqlite3 import adapters
import time
import requests
from urllib.parse import urljoin
import json
import logging

import rich.status
from urllib3 import Retry
from requests.adapters import HTTPAdapter
logging.basicConfig(level=logging.INFO)

class API_Request():

    def __init__(self, server, default_status_code=200, retry_limit=20):
        self.server = server
        self.default_status_code = default_status_code
        self.retry_limit = retry_limit
        self.method_get = "get"
        self.method_post = "post"
        self.method_delete = "delete"
        self.retry_strategy =  Retry(
            total=20,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "OPTIONS"]
        )
        self.adapter = HTTPAdapter(max_retries=self.retry_strategy)


    def call_api(self, method="get", path="/", headers=[], params=[], data=[], check_status_code=True):
        url = urljoin(self.server, path)
        result = None
        adapter = HTTPAdapter(max_retries=self.retry_strategy)

        api = requests.Session()
        api.mount("https://", adapter=self.adapter)
        api.mount("http://", adapter=self.adapter)

        if method == self.method_get:
            response = api.get(url, headers=headers, params=params)
        elif method == self.method_post:
            response = api.post(url, data=data, headers=headers)
        elif method == self.method_delete:
            response = api.delete(url, data=data, headers=headers)

        logging.info("{} {}".format(response.request.method,response.request.url))
        logging.debug("Headers : {}".format(response.request.headers))
        logging.debug("Request Data/parameters:{}".format(data))
        logging.debug("Status Code : {}".format(response.status_code))
        if response.status_code == 200:
            logging.debug("Response : {}".format(response.content))
        else:
            logging.info("Response : {}".format(response.content))
        if check_status_code:
            assert response.status_code == self.default_status_code
        result = response


        return result


    def get(self, path, headers=[], params=[], check_status_code=True):
        return self.call_api(method="get", path=path, headers=headers, params=params, check_status_code=check_status_code)


    def post(self, path, headers=[], data=[], check_status_code=True):
        return self.call_api(method="post", path=path, headers=headers, data=data, check_status_code=check_status_code)


    def delete(self, path, headers=[], data=[], check_status_code=True):
        return self.call_api(method="delete", path=path, headers=headers, data=data, check_status_code=check_status_code)


if __name__ == '__main__':

    logging.info("test")