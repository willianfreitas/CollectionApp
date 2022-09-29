from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from CollectionApp.models import *
from rest_framework.permissions import IsAuthenticated
import json
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ReturnCollections(APIView):
    permission_classes = [IsAuthenticated,]

    @swagger_auto_schema(
        operation_description="Get all collections of base from user."
    )

    def get(self, request) -> JsonResponse:
        '''
        Get all collections of base from user.
        '''
        user = request.user.id

        queryset = list(Collection.objects.filter(owner=user).values())

        return JsonResponse(queryset, safe=False)

class EditCollection(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'collection_id': openapi.Schema(description="Collection ID", type=openapi.TYPE_INTEGER),
                'new_content': openapi.Schema(description="New Content", type=openapi.TYPE_STRING),
            }
        ),
        operation_description="Edit a collection."
    )

    def post(self, request) -> HttpResponse:
        '''
        Edit a Collection.
        '''
        user = request.user.id
        owner = User.objects.get(id=user)
        post_json = json.loads(request.body)
        collection_id = post_json.get("collection_id")
        new_content = post_json.get("new_content")

        if user == Collection.objects.filter(id=collection_id, owner=owner):
            Collection.objects.filter(id=collection_id).update(content=new_content)
            return HttpResponse(json.dumps("Atualizado com sucesso."), content_type="charset=utf-8")
        else:
            return HttpResponse(json.dumps("Usuario sem permissao."), content_type="charset=utf-8")

class DeleteCollection(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'collection_id': openapi.Schema(description="Collection ID", type=openapi.TYPE_INTEGER),
            }
        ),
        operation_description="Delete a collection."
    )

    def post(self, request) -> HttpResponse:
        '''
        Delete a Collection.
        '''
        user = request.user.id
        owner = User.objects.get(id=user)
        post_json = json.loads(request.body)
        collection_id = post_json.get("collection_id")

        if user == Collection.objects.filter(id=collection_id, owner=owner):
            Collection.objects.filter(id=collection_id).delete()
            return HttpResponse(json.dumps("Deletado com sucesso."), content_type="charset=utf-8")
        else:
            return HttpResponse(json.dumps("Usuario sem permissao."), content_type="charset=utf-8")

class InsertCollection(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(description="Name of Collection", type=openapi.TYPE_STRING),
                'content': openapi.Schema(description="Content", type=openapi.TYPE_STRING),
            }
        ),
        operation_description="Insert a collection."
    )

    def post(self, request) -> HttpResponse:
        '''
        Insert a Collection
        '''

        post_json=json.loads(request.body)
        name_collection = post_json.get("name")
        content_collection = post_json.get("content")
        user_id = request.user.id
        owner_collection = User.objects.get(id=user_id)

        Collection.objects.create(
            name = name_collection,
            content = content_collection,
            owner = owner_collection,
        )

        return HttpResponse(json.dumps("Inserido com sucesso."), content_type="charset=utf-8")
