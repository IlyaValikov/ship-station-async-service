from time import sleep
from rest_framework.views import APIView
from rest_framework.response import Response
import random
import secrets
import requests as api
from concurrent import futures

executor = futures.ThreadPoolExecutor(max_workers=10)

class ProbabilityView(APIView):
    # answer 200 and do work
    def post(self, request):
        request_id = request.data.get('requestID')
        token = request.data.get('token')  # Получаем токен из тела запроса
        if request_id is None or token is None:
            return Response({'error': 'No request id or token'}, status=403)
        # answer 200 and do work
        executor.submit(do_work, request_id, token)
        return Response({'message': 'OK'}, status=200)
    
def do_work(request_id, token):
    sleep(7)
    result = 'Одобрено' if random.uniform(0, 1) < 0.7 else 'Запрещено'
    headers = {'Authorization': token}  
    request = api.put('http://localhost:8080/request/check', json={
        'key': "12345",
        'requestID': int(request_id),
        'paidstatus': result
    }, headers=headers)  # Передаем заголовки с токеном
    print(result)
    print(request.text)
    return result
