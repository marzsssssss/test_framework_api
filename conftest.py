import os
import httpx
import pytest_asyncio

from dotenv import load_dotenv, set_key

from core.headers import Headers
from config.base_test import BaseTest

load_dotenv()

@pytest_asyncio.fixture()
async def base():
    htx = httpx.AsyncClient()
    client = BaseTest(htx)
    yield client
    await htx.aclose()

# Только если запуск локальная перезаписать .env 
@pytest_asyncio.fixture(scope='session', autouse=True)
async def init_tokens():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"{os.getenv('HOST')}/auth/refresh/",
            json = {'refresh_token': os.getenv('REFRESH_TOKEN')}
        )
    assert response.status_code == 200, f"Failed requests {response.text}"

    access_token = response.json().get('tokens', {}).get('access', {}).get('token')
    refresh_token = response.json().get('tokens', {}).get('refresh', {}).get('token')
    set_key(".env", "ACCESS_TOKEN", access_token)
    set_key(".env", "REFRESH_TOKEN", refresh_token)
    return response


@pytest_asyncio.fixture(scope='session')
async def get_currency_id():
    async with httpx.AsyncClient(headers = Headers().basic) as client:
        response = await client.get(
            url = f"{os.getenv('HOST')}/currencies/",
        )
    assert response.status_code == 200, f"Failed requests {response.text}"

    currencies = response.json()
    cur_jpy = next((c for c in currencies if c.get('code') == 'JPY'), None)
    assert cur_jpy is not None, "Currency with code 'JPY' not found "
    return cur_jpy['id']

@pytest_asyncio.fixture(scope='session')
async def get_ewallet_id():
    async with httpx.AsyncClient(headers = Headers().basic) as client:
        response = await client.get(
            url=f"{os.getenv('HOST')}/accounts/ewallets/",
        )
    assert response.status_code == 200, f"Failed requests {response.text}"
    
    data = response.json().get('data',[])
    ewallet_usd = next((c for c in data if c.get('currency', {}).get('code') == 'USD'), None)
    assert ewallet_usd is not None, "Currency with code 'USD' not found"
    return ewallet_usd['id']