Feature: showing off behave

  Scenario: Performing simple math calculations
     Given we have 2 numbers to calculate
      When we add them together
      Then the result will be 7

  Scenario Outline: Adding 2 numbers
    Given A calculator
    Then The sum of <a> and <b> is <sum>

    Examples:
      | a | b | sum |
      | 2 | 5 |   7 |
      | 3 | 5 |   8 |
