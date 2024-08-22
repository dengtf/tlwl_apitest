from requests import request

from aomaker.fixture import BaseLogin
from aomaker.log import logger
import json

class Login(BaseLogin):

    def login(self) -> dict:
        """this is a login api"""
        body = {
            "loginName": self.account.get("user"),
            "password": self.account.get("pwd")
        }
        headers = {
            'a-appid': f'ae033de903c037b2fbf904beac29b05c',
            'a-uuid': f'65cd465f-65da-491f-a61b-37264d2472a4',
            'a-app-version': f'2.1.2',
            'a-version': f'1.0.0',
            'Content-Type': f'application/json'}

        url = ''.join([self.host, f"/tlwl/uc/auth/normal/login"])

        try:
            response = request("POST", url, json=body, headers=headers)
        except Exception as e:
            logger.error("登录失败")
            raise e
        # resp = {}
        resp = response.json()

        return resp

    def make_headers(self, resp_login: dict) -> dict:
        print(resp_login)
        headers = {
            'a-appid': f'ae033de903c037b2fbf904beac29b05c',
            'a-uuid': f'65cd465f-65da-491f-a61b-37264d2472a4',
            'a-app-version': f'2.1.1',
            'a-version': f'1.0.0',
            'Content-Type': f'application/json',
            'Cookie': resp_login.get("data").get("tokenValue")}
        return headers