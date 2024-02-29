import pytest
from httpx import Response, AsyncClient


@pytest.mark.anyio
async def test_hello_world(client: AsyncClient):
    response = await client.get('/')
    assert response.status_code == 200


@pytest.mark.anyio
async def test_register_then_login_with_success(client: AsyncClient):
    # TODO Delete user if exists before

    user_data = {
        'username': 'test_user',
        'email': 'test@example.com',
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 200:
        print(vars(register_response))
        raise AssertionError

    user_data = {
        'username': 'test@example.com',
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    login_response = await client.post('/login', data=user_data)

    if login_response.status_code != 200:
        print(vars(login_response))
        raise AssertionError
    
@pytest.mark.anyio
async def test_register_with_too_short_username(client: AsyncClient):
    user_data = {
        'username': 'A',
        'email': 'test@example.com',
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 400:
        print(vars(register_response))
        raise AssertionError

@pytest.mark.anyio
async def test_register_with_bad_email(client: AsyncClient):
    user_data = {
        'username': 'test_user',
        'email': 'test@example',
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 400:
        print(vars(register_response))
        raise AssertionError
    
@pytest.mark.anyio
async def test_register_with_too_short_password(client: AsyncClient):
    user_data = {
        'username': 'test_user',
        'email': 'test@example.com',
        'password': 'D2D7z!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 400:
        print(vars(register_response))
        raise AssertionError

@pytest.mark.anyio
async def test_register_with_missing_upper_password(client: AsyncClient):
    user_data = {
        'username': 'test_user',
        'email': 'test@example.com',
        'password': 'abcde12345!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 400:
        print(vars(register_response))
        raise AssertionError

@pytest.mark.anyio
async def test_register_with_missing_lower_password(client: AsyncClient):
    user_data = {
        'username': 'test_user',
        'email': 'test@example.com',
        'password': 'ABCDE12345!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 400:
        print(vars(register_response))
        raise AssertionError
    
@pytest.mark.anyio
async def test_register_with_no_symbols_password(client: AsyncClient):
    user_data = {
        'username': 'test_user',
        'email': 'test@example.com',
        'password': 'DCL2D7zi6y8Q7a6Ib'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 400:
        print(vars(register_response))
        raise AssertionError
    
@pytest.mark.anyio
async def test_register_then_try_login_with_wrong_email(client: AsyncClient):
    user_data = {
        'username': 'test_user',
        'email': 'test@example.com',
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 200:
        print(vars(register_response))
        raise AssertionError

    user_data = {
        'username': 'test2@example.com',
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    login_response = await client.post('/login', data=user_data)

    if login_response.status_code != 401:
        print(vars(login_response))
        raise AssertionError
    
@pytest.mark.anyio
async def test_register_then_try_login_with_wrong_password(client: AsyncClient):
    user_data = {
        'username': 'test_user',
        'email': 'test@example.com',
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 200:
        print(vars(register_response))
        raise AssertionError

    user_data = {
        'username': 'test@example.com',
        'password': 'LCD2D7zi6y8Q7a6Ib!'
    }

    login_response = await client.post('/login', data=user_data)

    if login_response.status_code != 401:
        print(vars(login_response))
        raise AssertionError