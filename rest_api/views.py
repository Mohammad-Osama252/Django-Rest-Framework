from django.shortcuts import render
from .custom_auth import CustomAuthentication
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

def student_detail(request, pk):
    std = Student.objects.get(id=pk)
    serializer = StudentSerializer(std)
    # json_data = JSONRenderer().render(serializer.data)

    return JsonResponse(serializer.data, safe=True)


# Complete QuerySet of Student Model

def student_list(request):
    std_list = Student.objects.all()
    serializer = StudentSerializer(std_list, many=True)
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def createStudent(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            print('in')
            serializer.save()
            res = {'mes': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def updateStudent(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'mes': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def deleteStudent(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted'}
        json_data = JSONRenderer().render(res)
        return JsonResponse(res, content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self, request, *args, **kwargs):
        std = Student.objects.get()
        serializer = StudentSerializer(std)
        return JsonResponse(serializer.data, safe=False)


# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
class Std_viewset(viewsets.ViewSet):
    def list(self, request):
        print(self.basename)
        print(self.action)
        print(self.suffix)
        print(self.description)
        print(self.detail)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

    def create(self, request):
            st = StudentSerializer(data= request.data)
            if st.is_valid():
                st.save()
                return Response({'msg': 'Success'})
            return Response({'err': 'Error'})

    def update(self, request, pk=None):
        id = pk
        std = Student.objects.get(id=id)
        st_update = StudentSerializer(std, data=request.data, partial=True)
        if st_update.is_valid():
            st_update.save()
            return Response({'msg': 'update'})

    def destroy(self, request, pk=None):
        id = pk
        std = Student.objects.get(id=id)
        std.delete()
        return Response({'msg': 'Delete'})


class class_Api(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if pk is not None:
            std = Student.objects.get(id=id)
            serializer = StudentSerializer(std)
            return Response(serializer.data)
        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.method == 'POST':
            std = StudentSerializer(data=request.data)
            if std.is_valid():
                std.save()
                return Response({'msg': 'Created'})
            return Response(std.errors)


class StdView(ListModelMixin, CreateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StdCreate(CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class concrete_Api(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class concrete_Apis(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


### ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [TokenAuthentication]
    # authentication_classes = [CustomAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = ['city']
    filter_backends = [SearchFilter]


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'email': str(request.user.email),
            'password': str(request.user.password),
            'auth': str(request.auth),  # None
        }
        return Response(content)


