from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('处理了请求')
        ua = request.headers.get('User-Agent')
        if 'python' in ua:
            return HttpResponse('非法请求')
        return self.get_response(request)

    def process_response(self, request, response):
        print('请求了响应')
        return response
