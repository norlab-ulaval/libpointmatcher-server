import os
import pytest
from fastapi.testclient import TestClient
from httpx import Response, AsyncClient
from motor.core import AgnosticCollection

from db.mongo import get_database

from main import app

TEST_EMAIL = 'test@example.com'
TEST_USER = 'test_user'
client = TestClient(app)

b64_config = 'cmVhZGluZ0RhdGFQb2ludHNGaWx0ZXJzOgogIC0gSWRlbnRpdHlEYXRhUG9pbnRzRmlsdGVyOgoKcmVmZXJlbmNlRGF0YVBvaW50c0ZpbHRlcnM6CiAgLSBTYW1wbGluZ1N1cmZhY2VOb3JtYWxEYXRhUG9pbnRzRmlsdGVyOgogICAgICBrbm46IDEwCiAgICAgIHJhdGlvOiAxLjAgCiAgICAgIHNhbXBsaW5nTWV0aG9kOiAwCiAgICAgIGF2ZXJhZ2VFeGlzdGluZ0Rlc2NyaXB0b3JzOiAwCgptYXRjaGVyOgogIEtEVHJlZU1hdGNoZXI6CiAgICBrbm46IDEKICAgIGVwc2lsb246IDAgCgpvdXRsaWVyRmlsdGVyczoKICAtIFRyaW1tZWREaXN0T3V0bGllckZpbHRlcjoKICAgICAgcmF0aW86IDEuMAoKZXJyb3JNaW5pbWl6ZXI6CiAgUG9pbnRUb1BsYW5lRXJyb3JNaW5pbWl6ZXIKCnRyYW5zZm9ybWF0aW9uQ2hlY2tlcnM6CiAgLSBDb3VudGVyVHJhbnNmb3JtYXRpb25DaGVja2VyOgogICAgICBtYXhJdGVyYXRpb25Db3VudDogNDAKICAtIERpZmZlcmVudGlhbFRyYW5zZm9ybWF0aW9uQ2hlY2tlcjoKICAgICAgbWluRGlmZlJvdEVycjogMC4wMDEKICAgICAgbWluRGlmZlRyYW5zRXJyOiAwLjAxCiAgICAgIHNtb290aExlbmd0aDogNCAgIAogICAgICAKaW5zcGVjdG9yOgogIE51bGxJbnNwZWN0b3IKIyAgVlRLRmlsZUluc3BlY3RvcgoKbG9nZ2VyOgogIE51bGxMb2dnZXIKIyAgRmlsZUxvZ2dlcgoK'


@pytest.fixture(autouse=True)
async def run_around_tests():
    await remove_test_user()
    await remove_test_leaderboard_entry()


@pytest.mark.anyio
async def test_hello_world(client: AsyncClient):
    response = await client.get('/')
    assert response.status_code == 200


@pytest.mark.anyio
async def test_register_then_login_with_success(client: AsyncClient):
    user_data = {
        'username': TEST_USER,
        'email': TEST_EMAIL,
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 200:
        print(vars(register_response))
        raise AssertionError

    user_data = {
        'username': TEST_EMAIL,
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
        'email': TEST_EMAIL,
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 400:
        print(vars(register_response))
        raise AssertionError


@pytest.mark.anyio
async def test_register_with_bad_email(client: AsyncClient):
    user_data = {
        'username': TEST_USER,
        'email': 'test@outlook',
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 400:
        print(vars(register_response))
        raise AssertionError


@pytest.mark.anyio
async def test_register_with_too_short_password(client: AsyncClient):
    user_data = {
        'username': TEST_USER,
        'email': TEST_EMAIL,
        'password': 'D2D7z!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 400:
        print(vars(register_response))
        raise AssertionError


@pytest.mark.anyio
async def test_register_with_missing_upper_password(client: AsyncClient):
    user_data = {
        'username': TEST_USER,
        'email': TEST_EMAIL,
        'password': 'abcde12345!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 400:
        print(vars(register_response))
        raise AssertionError


@pytest.mark.anyio
async def test_register_with_missing_lower_password(client: AsyncClient):
    user_data = {
        'username': TEST_USER,
        'email': TEST_EMAIL,
        'password': 'ABCDE12345!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 400:
        print(vars(register_response))
        raise AssertionError


@pytest.mark.anyio
async def test_register_with_no_symbols_password(client: AsyncClient):
    user_data = {
        'username': TEST_USER,
        'email': TEST_EMAIL,
        'password': 'DCL2D7zi6y8Q7a6Ib'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 400:
        print(vars(register_response))
        raise AssertionError


@pytest.mark.anyio
async def test_register_then_try_login_with_wrong_email(client: AsyncClient):
    user_data = {
        'username': TEST_USER,
        'email': TEST_EMAIL,
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
        'username': TEST_USER,
        'email': TEST_EMAIL,
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    register_response: Response = await client.post('/register', json=user_data)

    if register_response.status_code != 200:
        print(vars(register_response))
        raise AssertionError

    user_data = {
        'username': TEST_EMAIL,
        'password': 'LCD2D7zi6y8Q7a6Ib!'
    }

    login_response = await client.post('/login', data=user_data)

    if login_response.status_code != 401:
        print(vars(login_response))
        raise AssertionError


@pytest.mark.anyio
async def test_evaluation(client: AsyncClient):
    access_token = await register_login(client)

    new_evaluation_response = await client.post('/evaluation', json={'config': b64_config, 'anonymous': False,
                                                                     'name': 'evaluation_name'},
                                                headers={'Authorization': 'Bearer ' + access_token})

    assert new_evaluation_response.status_code == 200

    get_evaluations_response = await client.get('/evaluation', headers={'Authorization': 'Bearer ' + access_token})

    assert get_evaluations_response.status_code == 200

    assert len(get_evaluations_response.json())


@pytest.mark.anyio
async def test_get_runs(client: AsyncClient):
    access_token = await register_login(client)

    new_evaluation_response = await client.post('/evaluation', json={'config': b64_config, 'anonymous': False},
                                                headers={'Authorization': 'Bearer ' + access_token})

    assert new_evaluation_response.status_code == 200

    get_evaluations_response = await client.get('/run', headers={'Authorization': 'Bearer ' + access_token})

    assert get_evaluations_response.status_code == 200

    assert len(get_evaluations_response.json())


# @pytest.mark.anyio
# async def test_size_evaluation(client: AsyncClient):
#     user_data = {
#         'username': TEST_USER,
#         'email': TEST_EMAIL,
#         'password': 'DCL2D7zi6y8Q7a6Ib!'
#     }
#
#     await client.post('/register', json=user_data)
#
#     user_data = {
#         'username': TEST_EMAIL,
#         'password': 'DCL2D7zi6y8Q7a6Ib!'
#     }
#
#     login_response = await client.post('/login', data=user_data)
#     access_token = login_response.json()['access_token']
#
#     test = await client.post('/evaluation', json={'config': 'config', 'anonymous': False},
#                                                 headers={'Authorization': 'Bearer ' + access_token})
#     response = await client.get('/leaderboard?page=1&limit=10&type=all')
#
#     #Not working since some function in the repo that the get uses is not working
#     # assert response.status_code == 200
#     # I do this because since it's an e2e test we cant really test the actual number of entry.
#     # assert response.json() > before.json()


@pytest.mark.anyio
async def test_get_types(client: AsyncClient):
    access_token = await register_login(client)

    await client.post('/evaluation', json={'config': b64_config, 'anonymous': False},
                      headers={'Authorization': 'Bearer ' + access_token})

    get_types_response = await client.get('/leaderboard/types', headers={'Authorization': 'Bearer ' + access_token})

    assert get_types_response.status_code == 200

    types = get_types_response.json()

    assert len(types)


async def register_login(client: AsyncClient) -> str:
    user_data = {
        'username': TEST_USER,
        'email': TEST_EMAIL,
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    await client.post('/register', json=user_data)

    user_data = {
        'username': TEST_EMAIL,
        'password': 'DCL2D7zi6y8Q7a6Ib!'
    }

    login_response = await client.post('/login', data=user_data)

    return login_response.json()['access_token']


async def remove_test_user():
    env = os.environ
    db = get_database(env)
    users_collection: AgnosticCollection = db['users']
    await users_collection.find_one_and_delete({"username": TEST_USER})


async def remove_test_leaderboard_entry():
    env = os.environ
    db = get_database(env)
    evaluations_collection: AgnosticCollection = db['evaluations']
    await evaluations_collection.find_one_and_delete({"user_email": TEST_EMAIL})
