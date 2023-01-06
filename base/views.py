from django.http import HttpResponse
from django.views import View


from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import TaskSerializer
from .models import Task


@api_view(['GET','POST','DELETE','PUT','PATCH'])
def tasks(req,id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_task=Task.objects.get(id=id)
                return Response (TaskSerializer(temp_task,many=False).data)
            except Task.DoesNotExist:
                return Response ("not found") 
        all_tasks=TaskSerializer(Task.objects.all(),many=True).data
        return Response ( all_tasks)
    if req.method =='POST':
        tsk_serializer = TaskSerializer(data=req.data)
        if tsk_serializer.is_valid():
            tsk_serializer.save()
            return Response ("post...")
        else:
            return Response (tsk_serializer.error_messages)
    if req.method =='DELETE':
        try:
            temp_task=Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response ("not found")    
        
        temp_task.delete()
        return Response ("del...")
    if req.method =='PUT':
        try:
            temp_task=Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response ("not found")
        
        ser = TaskSerializer(data=req.data)
        old_task = Task.objects.get(id=id)
        res = ser.update(old_task, req.data)
        return Response(res)




# class Tasks(View):
#     def get(self, req):
#         all_tasks=TaskSerializer(Task.objects.all(),many=True).data
#         return HttpResponse ( all_tasks)
#     def post(self, req):
#         print(dir(req))
#         tsk_serializer = TaskSerializer(data=req)
#         tsk_serializer.is_valid()
#         tsk_serializer.save()
#         return HttpResponse ( "data was created")

    

class GreetingView(View):
    greeting = "Good Day"
    def get(self, request):
        return HttpResponse(self.greeting)