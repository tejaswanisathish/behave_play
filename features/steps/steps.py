"""This file contains step definitions to test the Gender API - https://api.genderize.io"""
from behave import given, then, when
import httpx
from http import HTTPStatus

@given("we fetch gender for {name}")
def fetch_gender_details(context, name: str):
    """Fetches gender details

    Args:
        context (Behave): Behave context
        name (str): Name of the test user
    """
    response = httpx.get(url=f"https://api.genderize.io", params={"name":name})
    context.request_status_code = response.status_code
    context.get_gender_response = response.json()

@when("the {request_type} request is successful")
def validate_request_status_code(context, request_type):
    actual = getattr(context, "request_status_code", None)
    if actual is None:
        raise ValueError("Unable to fetch status code of the request that fetched gender from Gender API")
    match request_type:
        case "GET":
            assert actual == HTTPStatus.OK
        case "POST":
            assert actual == HTTPStatus.CREATED
    delattr(context, "request_status_code")

@then("the response should be")
def validate_api_response(context):
    expected = dict(context.table.rows[0].as_dict())
    
    actual = getattr(context, "get_gender_response", None)
    if actual is None:
        raise ValueError("Fetch gender API request response not found in Behave context")
    
    for expected_key, expected_value in expected.items():
        assert str(actual[expected_key]) == expected_value

    delattr(context, "get_gender_response")

@given("user sends the api to create user record")
def create_user_record(context):
    url = 'https://reqres.in/api/users'
    data = {'name': 'Test Automation','job': 'Engineer'}
    response =httpx.post(url, json=data)
    context.request_status_code = response.status_code
    context.created_user_record = response.json()

@then("verify if the user record is created as following")
def verifying_created_record(context):
    expected = dict(context.table.rows[0].as_dict())
    actual = getattr(context, "created_user_record", None)
    if actual is None:
        raise ValueError("record is not created")
    
    for expected_key, expected_value in expected.items():
        assert str(actual[expected_key]) == expected_value

@given("user sends the api to update user record")
def update_user_record(context):
    item_id = 1
    url = f'http://127.0.0.1:8000/items/{item_id}'
    data = {'name': 'Test','price': '20','description': 'Testing PUT Method', 'tax': '20','item_id': '1'}
    response = httpx.put(url, json=data)
    context.request_status_code = response.status_code
    context.update_user_record = response.json()


@then("Verify if record is updated with following")
def verifying_updated_record(context):
    expected =dict(context.table.rows[0].as_dict())
    actual = getattr(context, "update_user_record", None)
    if actual is None:
        raise ValueError("record is not updated")
    
    for expected_key, expected_value in expected.items():
        assert str(actual[expected_key]) == expected_value


@given("user sends the api to delete user record")
def delete_record(context):
 item_id = 1
 url = f'http://127.0.0.1:8000/items/{item_id}'
 response = httpx.delete(url)
 context.request_status_code = response.status_code
 context.delete_record = response.json()

@then("Verify if record is deleted as following")
def verifying_deleted_message(context):
    expected =dict(context.table.rows[0].as_dict())
    actual = getattr(context, "delete_record", None)

    if actual is None:
        raise ValueError("record is not deleted or the message is incorrect")
    
    for expected_key, expected_value in expected.items():
        assert str(actual[expected_key]) == expected_value
