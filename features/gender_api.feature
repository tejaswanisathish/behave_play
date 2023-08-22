Feature: Test Gender API

    Scenario: Fetch gender with name
        Given we fetch gender for mary
        When the GET request is successful
        Then the response should be
            | count   | name | gender | probability |
            | 1011867 | mary | female | 1.0         |

