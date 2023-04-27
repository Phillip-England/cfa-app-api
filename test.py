import os

import requests
from requests import Session
from dotenv import load_dotenv


load_dotenv()
base_url = os.getenv('BASE_URL')


def create_user_success(session: Session):
    url = os.path.join(base_url, 'user')
    data = {
        'email': 'phillip@gmail.com',
        'password': 'password'
    }
    response = session.post(url, json=data)
    if response.status_code != 201:
        raise Exception(response)


def create_user_prevent_duplication(session: Session):
    url = os.path.join(base_url, 'user')
    data = {
        'email': 'phillip@gmail.com',
        'password': 'password'
    }
    response = session.post(url, json=data)
    if response.status_code != 400:
        raise Exception(response)


def create_user_prevent_invalid_email(session: Session):
    url = os.path.join(base_url, 'user')
    data = {
        'email': 'invalidemail',
        'password': 'password'
    }
    response = session.post(url, json=data)
    if response.status_code != 400:
        raise Exception(response)


def create_user_prevent_long_email(session: Session):
    url = os.path.join(base_url, 'user')
    data = {
        'email': 'longemaillllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll@gmail.com',
        'password': 'password'
    }
    response = session.post(url, json=data)
    if response.status_code != 400:
        raise Exception(response)


def create_user_prevent_short_password(session: Session):
    url = os.path.join(base_url, 'user')
    data = {
        'email': 'phillip@gmail.com',
        'password': 'a'
    }
    response = session.post(url, json=data)
    if response.status_code != 400:
        raise Exception(response)


def create_user_prevent_long_password(session: Session):
    url = os.path.join(base_url, 'user')
    data = {
        'email': 'phillip@gmail.com',
        'password': 'adasdasdasdasdasdasasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdd'
    }
    response = session.post(url, json=data)
    if response.status_code != 400:
        raise Exception(response)


def login_user_success(session: Session):
    url = os.path.join(base_url, 'user/login')
    data = {
        'email': 'phillip@gmail.com',
        'password': 'password'
    }
    response = session.post(url, json=data)
    if response.status_code != 200:
        raise Exception(response.status_code, response.json())


def login_user_invalid_credentials(session: Session):
    url = os.path.join(base_url, 'user/login')
    data = {
        'email': 'invalid@gmail.com',
        'password': 'password'
    }
    response = session.post(url, json=data)
    if response.status_code != 400:
        raise Exception(response.status_code,
                        response.json())


def get_current_user_success(session: Session):
    url = os.path.join(base_url, 'user')
    response = session.get(url)
    if response.status_code != 200:
        raise Exception(response.status_code, response.json())


def get_current_user_unauthorized(session: Session):
    url = os.path.join(base_url, 'user')
    response = session.get(url)
    if response.status_code != 401:
        raise Exception(response.status_code, response.json())


def logout_user(session: Session):
    url = os.path.join(base_url, 'user/logout')
    response = session.get(url)
    if response.status_code != 200:
        raise Exception(response.status_code, response.json())


def logout_user_unauthorized(session: Session):
    url = os.path.join(base_url, 'user/logout')
    response = session.get(url)
    if response.status_code != 401:
        raise Exception(response.status_code, response.json())


def delete_current_user(session: Session):
    url = os.path.join(base_url, 'user')
    response = session.delete(url)
    if response.status_code != 200:
        raise Exception(response.status_code, response.json())


def delete_current_user_unauthorized(session: Session):
    url = os.path.join(base_url, 'user')
    response = session.delete(url)
    if response.status_code != 401:
        raise Exception(response.status_code, response.json())


try:
    session = requests.Session()

    # creating users tests
    create_user_success(session)
    create_user_prevent_duplication(session)
    create_user_prevent_invalid_email(session)
    create_user_prevent_long_email(session)
    create_user_prevent_short_password(session)
    create_user_prevent_long_password(session)

    # login user tests
    login_user_success(session)
    login_user_invalid_credentials(session)

    # getting the current users tests
    get_current_user_success(session)
    logout_user(session)
    get_current_user_unauthorized(session)
    login_user_success(session)

    # logging out the user tests
    logout_user(session)
    logout_user_unauthorized(session)

    # deleting user tests
    delete_current_user_unauthorized(session)
    login_user_success(session)
    delete_current_user(session)

except Exception as error:
    print(error.json())
