import allure 
import json  
from allure_commons.types import AttachmentType
from core.logger import Logger

class Helper():

    def __init__(self, logger_name='Helper'):
        self.logger = Logger(logger_name).get()

    def attach_response_to_allure(self, response):
        if response.status_code != 204 and response.content:
            try:
                formatted_response = json.dumps(response.json(), indent=4)
                allure.attach(body=formatted_response, name='API Response', attachment_type=AttachmentType.JSON)
            except Exception:
                formatted_response = response.text
                allure.attach(body=formatted_response, name='API Response', attachment_type=AttachmentType.TEXT)
        else:
            formatted_response = f"No content, status code: {response.status_code}"
            allure.attach(body=formatted_response, name='API Response', attachment_type=AttachmentType.TEXT)

    def assert_response(self, response):
        if response.status_code == 200:
            self.logger.info(f"Correct response: {response.status_code}")
            return True, response.json()
        else:
            try:
                error_body = response.json()
                error_msg = json.dumps(error_body)
            except Exception:
                error_body = response.text
                error_msg = error_body if error_body else "No error details"
            self.logger.error(f'Status code not 200. Status code - {response.status_code}, Response - {error_msg}')
            raise ValueError(f'Status code not 200. Status code - {response.status_code}, Response - {error_msg}')
        
    def assert_create_response(self, response):
        if response.status_code == 204:
            self.logger.info(f"Correct create response: {response.status_code}")
            return True, {}
        else:
            try:
                error_body = response.json()
                error_msg = json.dumps(error_body)
            except Exception:
                error_body = response.text
                error_msg = error_body if error_body else "No error details"
            self.logger.error(f'Status code not 204. Status code - {response.status_code}, Response - {error_msg}')
            raise ValueError(f'Status code not 204. Status code - {response.status_code}, Response - {error_msg}')
        
    def assert_bad_response(self, response, expected_status):
        if response.status_code != expected_status:
            try:
                error_body = response.json()
                error_msg = json.dumps(error_body)
            except Exception:
                error_body = response.text
                error_msg = error_body if error_body else "No error details"
            self.logger.error(f'Status code not equal expected status. Status code - {response.status_code}, Response - {error_msg}')
            raise ValueError(f'Status code not equal expected status. Status code - {response.status_code}, Response - {error_msg}')
        return response