Feature: SWAPI people
    Scenario: Verify person 1
        When I request person by number 1
        Then I am getting person Luke Skywalker

    Scenario: Verify person 2
        When I request person by number 2
        Then I am getting person C-3PO

    Scenario: Verify person 3
        When I request person by number 3
        Then I am getting person R2-D2