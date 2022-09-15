import json
import jsonschema
import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from mymodels.models import Item
import api.serializers

@api_view(['GET'])
def getData(request):
    return Response({'msg': 'hello'})

@api_view(['GET'])
def getItem(request, object_id=''):
    try:
        item = Item.objects.get(object_id=object_id)
        serializer = api.serializers.ItemSerializer(item, many=False)
        return Response(serializer.data)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def postData(request):
    pwd = os.path.dirname(__file__)
    file_path = os.path.join(pwd, 'schema.json')
    f = open(file_path)
    schema = json.load(f)
    data = request.data
    try:
        jsonschema.validate(data, schema)
    except jsonschema.exceptions.ValidationError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        for obj in data['objects']:
            Item.objects.create(object_id=obj['object_id'], data=obj['data'])
    except Exception:
        # validation above sometimes doesn't catch all validation errors
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def searchData(request):
    search = {}
    key = request.GET.get('key', '')
    if key:
        search['key'] = key
    value = request.GET.get('value', '')
    if value:
        search['value'] = value
    items = Item.objects.filter(data__contains=[search])
    serializer = api.serializers.ItemSerializer(items, many=True)
    return Response(serializer.data)

