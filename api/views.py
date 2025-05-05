from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import process_message
from .serializers import MessageSerializer
from celery.result import AsyncResult

class ProcessView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            task = process_message.delay(serializer.validated_data['email'], serializer.validated_data['message'])
            return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StatusView(APIView):
    def get(self, request, task_id):
        result = AsyncResult(task_id)
        return Response({
            "task_id": task_id,
            "state": result.state,
            "result": result.result
        })
