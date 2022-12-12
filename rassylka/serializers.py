from rest_framework import serializers
from rassylka.models import Client, Links, Message


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Client

    def validate(self, value):
        if str(value)[0] != '7':
            raise serializers.ValidationError(
                'Введите номер в формате 7XXXXXXXXXX'
            )
        return value


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class LinklistSerializer(serializers.ModelSerializer):
    send_messages = serializers.SerializerMethodField()
    not_send_messages = serializers.SerializerMethodField()

    class Meta:
        model = Links
        fields = ('id', 'start_send_time', 'end_send_time', 'text', 'tag', 'code', 'send_messages', 'not_send_messages')


    def get_send_messages(self, obj):
        return obj.messages.filter(status='S').count()

    def get_not_send_messages(self, obj):
        return obj.messages.filter(status='N').count()


class LinkSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(read_only=True, many=True)

    class Meta:
        model = Links
        fields = ('id', 'start_send_time', 'end_send_time', 'text', 'tag', 'code', 'messages')

