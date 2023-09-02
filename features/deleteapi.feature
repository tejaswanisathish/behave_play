Feature: Testing by deleting the API

    @DeletingtheRecordsapi
    Scenario: Deleting user records
        Given user sends the api to delete user record
        Then Verify if record is deleted as following

            | message          |
            | Item # 1 deleted |

