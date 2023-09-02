@GenderAPI
Feature: Test Gender API

    @GETMethod
    Scenario: Fetch gender with name from the Gender API
        Given we fetch gender for mary
        When the GET request is successful
        Then the response should be
            | count   | name | gender | probability |
            | 1011867 | mary | female | 1.0         |

