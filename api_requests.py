import requests
import urls


class RequestsApi:

    def create_user(self, payload):
        return requests.post(urls.user_create_url, json = payload)

    def delete_user(self, headers):
        return requests.delete(urls.user_delete_url, headers = headers)