@api
Feature: Check API status

Scenario: Check API status
    Given the base URL is "https://goal-tracker-api.onrender.com/api/v1/"
    When I send a GET request to "status"
    Then the response should contain "OPERATIONAL"
    And the response status code should be 200