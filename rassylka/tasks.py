import logging
import os
import time
import sys
from datetime import datetime

import requests

from .models import Client, Links, Message


logging.basicConfig(
    format='%(asctime)s %(name)s %(levelname)s  %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)],
    level=logging.ERROR
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

RETRY_TIME = 10
TIME_FORMAT = "%Y-%m-%d - %H:%M:%S"
SENDING_API_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDIwMzU5ODcsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6ImFza2VyYmt2diJ9.LjMsppO-oXzTn8cwMqTZ9WslEko7h9DdBQcDXUIci5E'


class MissingValueException(Exception):
    """ """


class GetAPIException(Exception):
    """ """


def send_api_message(message_id, client, message):
    headers = {'Authorization': f'Bearer {SENDING_API_TOKEN}'}
    json = {
        "phone": client,
        "text": message
    }
    try:
        response = requests.post(
            f'https://probe.fbrq.cloud/v1/send/{message_id}'.format(
                message_id=message_id), headers=headers, json=json)
        logger.info('Сообщение отправлено через венешний API')
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as error:
        logger.error(f'Сбой при отправке сообщения: {error}')
        return False


def start_links():
    logger.debug('-----------------')
    message_id = [1]
    finished_link_id = []
    if SENDING_API_TOKEN is None:
        logger.critical('Отсутствуют переменные окружения!')
        raise MissingValueException('Отсутствуют переменные окружения!')
    while True:
        try:
            logger.debug('Начало иттерации')
            links = Links.objects.all()
            for link in links:
                current_datetime = datetime.now()
                if (datetime.strptime(link['start_send_time'], TIME_FORMAT) <= current_datetime
                        and datetime.strptime(link['end_send_time'], TIME_FORMAT) >= current_datetime
                        and link['id'] not in finished_link_id):
                    link_id = link['id']
                    tag = link['tag']
                    code = link['code']
                    text = link['text']
                    clients = Client.objects.filter(tag=tag).filter(code=code)
                    for client in clients:
                        current_datetime = datetime.now()
                        client_id = client['id']
                        if (current_datetime <= datetime.strptime(link['end_send_time'], TIME_FORMAT) and
                                send_api_message(message_id[0], client, text)):
                            Message.objects.create(status='S', link=link_id, client=client_id)
                        else:
                            Message.objects.create(status='N', link=link_id, client=client_id)
                        message_id[0] += 1
                    finished_link_id.append(link_id)
            logger.debug('Иттерация закончена')
            logger.debug('-----------------')
            time.sleep(RETRY_TIME)
        except Exception as error:
            logger.error(f'Сбой в работе: {error}')
            logger.debug('-----------------')
            time.sleep(RETRY_TIME)


