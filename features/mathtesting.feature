Feature: Performing simple math calculations

  Scenario Outline: Adding Two Numbers
    Given we have 2 numbers to calculate: <a> and <b>
    And a calculator
    When we add them together
    Then the result will be <sum>
    Examples:
      |  a |  b | sum |
      |  2 |  5 |   7 |
      |  3 |  5 |   8 |
      | 15 | 45 |  60 |

  Scenario Outline: Multiplying 2 numbers
    Given we have 2 numbers to calculate: <a> and <b>
    And a calculator
    When we multiply them together
    Then the result will be <product>
    Examples:
      | a |  b | product |
      | 2 |  5 |      10 |
      | 3 |  5 |      15 |
      | 5 | 10 |      50 |
