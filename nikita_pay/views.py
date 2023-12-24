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
        request_id = request.data.get('id')
        if request_id == None:
            return Response({'error': 'No request id'}, status=403)
        # answer 200 and do work
        executor.submit(do_work, request_id)
        return Response({'message': 'OK'}, status=200)
    
def do_work(request_id):
    sleep(7)
    result = 'Оплачено' if random.uniform(0, 1) < 0.7 else 'Ошибка при оплате'
    request = api.put('http://localhost:8080/travelrequests/change-paidstatus', json={
        'key': "12345",
        'id': str(request_id),
        'paidstatus': result
    })
    print(result)
    print(request.text)
    return result