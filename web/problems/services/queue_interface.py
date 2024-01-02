import aiohttp

from django.http import QueryDict
from django.core.files.uploadedfile import UploadedFile

from RATS.settings import QUEUE_HOST


class QueueInterface:
    '''Queue service web interface
        All methods get Querydict and UploadedFile'''
    def __init__(self) -> None:
        self.session = aiohttp.ClientSession()

    def add_solution(self, request_data: QueryDict,
                     request_file:  UploadedFile):
        data = request_data.dict()
        if request_file:
            data['code'] = request_file.read()
        return self.session.post(QUEUE_HOST+'/solving', json=data)

