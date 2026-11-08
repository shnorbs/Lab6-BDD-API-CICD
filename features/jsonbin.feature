Feature: JSONBin bins

  Background:
    Given the JSONBin base URL is "https://api.jsonbin.io/v3"
    And I have a valid master key

  @tag1
  Scenario Outline: Create a bin
    When I create a bin with data '<payload>'
    Then the response status code should be 200
    And the response should contain a bin id

    Examples:
      | payload                 |
      | {"item": "apple"}       |
      | {"item": "pear"}        |

  @tag1
  Scenario: Read a bin
    Given a bin exists with data '{"hello": "world"}'
    When I read the bin
    Then the response status code should be 200
    And the record should equal '{"hello": "world"}'

  @tag2
  Scenario: Delete a bin
    Given a bin exists with data '{"temp": true}'
    When I delete the bin
    Then the response status code should be 200

  @tag2
  Scenario Outline: Deleted bin cannot be read
    Given a bin exists with data '<payload>'
    And I delete the bin
    When I read the bin
    Then the response status code should be 404

    Examples:
      | payload        |
      | {"a": 1}       |
      | {"b": 2}       |