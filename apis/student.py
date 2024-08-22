from aomaker.base.base_api import BaseApi
from aomaker.cache import cache


class StudentDetails(BaseApi):
    
    def account_data(self, studentID):
        """获取学员-账户中心数据"""
        http_data = {
            'api_path': '/tlwl/std/accounts/',
            'method': 'get',
            'params': {"studentId":studentID}
        }
        response = self.send_http(http_data)
        headers = self.cache.get("headers")
        print(headers)
        return response
    
    # def demo_post(self):
    #     """this is a demo post api"""
    #     body = {
    #         'name': 'aomaker',
    #         'version': 'v2'
    #     }
    #     http_data = {
    #         'api_path': '/test',
    #         'method': 'get',
    #         'params': {'name': 'aomaker'},
    #         'data': body
    #     }
    #     response = self.send_http(http_data)
    #     return response
    