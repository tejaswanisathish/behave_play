Feature: Testing by creating user records using user api

@Creatinguserrecordapi
    Scenario: creating user records
        Given user sends the api to create user record
        When the POST request is successful
        Then verify if the user record is created as following

            | name            | job      |
            | Test Automation | Engineer |


