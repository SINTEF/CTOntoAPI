from datetime import datetime
from typing import Dict
import json
import time
import requests
import os
from util.log import logger
from util.environment_and_configuration import (
    get_environment_variable,
    get_environment_variable_int,
)

from requests.exceptions import RequestException as ReqExc

FAST_API_HOST = get_environment_variable("FAST_API_HOST")
FAST_API_PORT = get_environment_variable_int("FAST_API_PORT")
API_URI = f"http://{FAST_API_HOST}:{FAST_API_PORT}"


def _handle_request_exception(retry_number: int = 0):
    logger.info("API not available!")
    logger.info(f"Tried to connect to {API_URI}")

    sleep_time = 5 * (2**retry_number)

    logger.info(f"Retrying in {sleep_time} seconds...")
    time.sleep(sleep_time)


def get_json(
    relative_path: str,
    retries: int = -1,
    timeout: int = 30,
    result_class=None,
    **kwargs,
):
    """
    Get request to the specified api endpoint
    :param relative_path:
    :param retries: how often to retry if the call failed. Negative numbners mean (about) unlimited.
    :return: the response json as dict
    """
    range_limit = retries + 1 if retries >= 0 else 999999999999999999999999
    for i in range(range_limit):
        try:
            resp_dict = requests.get(
                API_URI + relative_path, params=kwargs, timeout=timeout
            ).json()

            if result_class is not None:
                resp_dict = result_class.from_json(str(resp_dict))

            elif isinstance(resp_dict, str):
                # Sometimes, the json is still represented as string instead of dict
                resp_dict = json.loads(resp_dict)

            return resp_dict
        except ReqExc as e:
            logger.error(f"Failed to execute {API_URI + relative_path} with args {kwargs}")
            logger.error(e)
            if i < retries:
                _handle_request_exception(i)





def get_raw(relative_path: str, retries: int = -1, **kwargs):
    """
    Get request to the specified api endpoint
    :param relative_path:
    :param retries: how often to retry if the call failed. Negative numbners mean (about) unlimited.
    :return: the raw response
    """
    range_limit = retries + 1 if retries >= 0 else 999999999999999999999999
    for i in range(range_limit):
        try:
            return requests.get(
                API_URI + relative_path, params=kwargs, timeout=300
            ).content
        except ReqExc:
            _handle_request_exception(i)


def get_str(relative_path: str, retries: int = -1, **kwargs):
    """
    Get request to the specified api endpoint
    :param relative_path:
    :return: the response as string
    """
    range_limit = retries + 1 if retries >= 0 else 999999999999999999999999
    for i in range(range_limit):
        try:
            return requests.get(API_URI + relative_path, params=kwargs, timeout=30).text
        except ReqExc:
            _handle_request_exception(i)


def get_int(relative_path: str, retries: int = -1, **kwargs):
    """
    Get request to the specified api endpoint
    :param relative_path:
    :param retries: how often to retry if the call failed. Negative numbners mean (about) unlimited.
    :return: the response as int number
    """
    range_limit = retries + 1 if retries >= 0 else 999999999999999999999999
    for i in range(range_limit):
        try:
            return int(
                requests.get(API_URI + relative_path, params=kwargs, timeout=30).text
            )
        except ReqExc:
            _handle_request_exception(i)


def get_float(relative_path: str, retries: int = -1, **kwargs):
    """
    Get request to the specified api endpoint
    :param relative_path:
    :param retries: how often to retry if the call failed. Negative numbners mean (about) unlimited.
    :return: the response as float number
    """
    range_limit = retries + 1 if retries >= 0 else 999999999999999999999999
    for i in range(range_limit):
        try:
            return float(
                requests.get(API_URI + relative_path, params=kwargs, timeout=30).text
            )
        except ReqExc:
            _handle_request_exception(i)


def patch(relative_path: str, retries: int = -1, **kwargs):
    range_limit = retries + 1 if retries >= 0 else 999999999999999999999999
    for i in range(range_limit):
        try:
            return requests.patch(API_URI + relative_path, params=kwargs)
        except ReqExc:
            _handle_request_exception(i)


def post(
    relative_path: str,
    data: Dict = None,
    json: Dict = None,
    retries: int = -1,
    **kwargs,
):
    """Post request. Returns the response body text

    Args:
    relative_path (str): _description_
    retries: how often to retry if the call failed. Negative numbners mean (about) unlimited.
        data (Dict, optional): _description_. Defaults to None.
        json (Dict, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    range_limit = retries + 1 if retries >= 0 else 999999999999999999999999
    for i in range(range_limit):
        try:
            response = requests.post(
                API_URI + relative_path, params=kwargs, data=data, json=json
            )
            text = response.text
            if text[0] == '"' and text[-1] == '"':
                text = text[1:-1]
            return text
        except ReqExc:
            _handle_request_exception(i)


def delete(relative_path: str, retries: int = -1, **kwargs):
    """Delete request. Returns the response body text

    Args:
    relative_path (str): _description_
    retries: how often to retry if the call failed. Negative numbners mean (about) unlimited.


    Returns:
        _type_: _description_
    """
    range_limit = retries + 1 if retries >= 0 else 999999999999999999999999
    for i in range(range_limit):
        try:
            response = requests.delete(API_URI + relative_path, params=kwargs)
            text = response.text
            if text[0] == '"' and text[-1] == '"':
                text = text[1:-1]
            return text
        except ReqExc:
            _handle_request_exception(i)