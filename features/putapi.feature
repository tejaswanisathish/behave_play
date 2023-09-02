@TestAPI
Feature: Testing by updating user records using user PUT API

    @PUTMethod
    Scenario: Updating user records on TestAPI
        Given user sends the api to update user record
        Then Verify if record is updated with following

            | name | price | description        | tax  | item_id     |
            | Test | 20.0  | Testing PUT Method | 20.0 | 1 |
