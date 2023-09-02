@TestAPI
Feature: Testing by deleting the API

    @DELETEMethod
    Scenario: Deleting user records on TestAPI
        Given user sends the api to delete user record
        Then Verify if record is deleted as following

            | message          |
            | Item # 1 deleted |

