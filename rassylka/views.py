from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Client, Links, Message
from .serializers import (ClientSerializer, LinklistSerializer, LinkSerializer, MessageSerializer)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('tag', 'code')


class LinksViewSet(viewsets.ModelViewSet):
    queryset = Links.objects.all()
    serializer_class = LinkSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return LinklistSerializer
        return LinkSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

























# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from rest_framework import generics, status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import *
# from .models import *
#
#
# @api_view(['GET'])
# def list(request):
#     w = Clients.objects.all()
#     return Response({'posts': ClientSerializer(w, many=True).data})
#
#
# @login_required
# @api_view(['POST'])
# def apiCreateClient(request, *args, **kwargs):
#     # if request.user.is_authenticated:
#     serializer = ClientSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# #update a client
# @api_view(['POST'])
# def apiUpdateClient(request, pk):
#     client = Clients.objects.get(pk=pk)
#     serializer = ClientSerializer(instance=client, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# #delete a client
# @api_view(['DELETE'])
# def apiDeleteClient(request, pk):
#     client = Clients.objects.get(pk=pk)
#     client.delete()
#
#     return Response("Clent succesfully deleted!")
#
#
# #add new link
# @api_view(['GET'])
# def LinkList(request):
#     w = Links.objects.all()
#     return Response({'posts': LinkSerializer(w, many=True).data})
#
#
# @login_required
# @api_view(['POST'])
# def apiCreateLink(request, *args, **kwargs):
#     # if request.user.is_authenticated:
#     serializer = LinkSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# # получения общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам
#
#
# #link detail view
# @api_view(['GET'])
# def apiLinkDetails(request, pk):
#     links = Messages.objects.filter(pk=pk)
#     serializer = MessageSerializer(links, many=True)
#     return Response(serializer.data)
#
#
# #update a link
# @api_view(['POST'])
# def apiUpdateLink(request, pk):
#     client = Links.objects.get(pk=pk)
#     serializer = LinkSerializer(instance=client, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# #delete a link
# @api_view(['DELETE'])
# def apiDeleteLink(request, pk):
#     client = Links.objects.get(pk=pk)
#     client.delete()
#
#     return Response("Link succesfully deleted!")
#
#
# #обработки активных рассылок и отправки сообщений клиентам
#
#
#
#
#
#
# # #add new Client
# # class ClientListView(generics.ListCreateAPIView):
# #     queryset = Clients.objects.all()
# #     serializer_class = ClientSerializer
# #
# #
# # #update and delete Clients
# # class ClientUDView(generics.RetrieveDestroyAPIView,
# #                    generics.RetrieveUpdateAPIView):
# #     queryset = Clients.objects.all()
# #     serializer_class = ClientSerializer
# #
# #
# # #add new link
# # class LinkListView(generics.ListCreateAPIView):
# #     queryset = Links.objects.all()
# #     serializer_class = LinkSerializer
# #
# # # получения общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам
# #
# #
# # #link detail view
# #
# #
# # #update and delete links
# # class LinkUDView(generics.RetrieveDestroyAPIView,
# #                  generics.RetrieveUpdateAPIView):
# #     queryset = Links.objects.all()
# #     serializer_class = LinkSerializer
# #
# #
# # #обработки активных рассылок и отправки сообщений клиентам
#
#
