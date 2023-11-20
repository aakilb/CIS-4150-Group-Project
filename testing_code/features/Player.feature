Feature: Controlling the Player
  Scenario: Initialize a Player with a bow
    Given a new Player with a bow
    Then the player should be initialized with a bow

  Scenario: Initialize a Player with a fist
    Given a new Player with a fist
    Then the player should be initialized with a fist

  Scenario: Initialize a Player with nothing
    Given a new Player with a invalid_weapon
    Then throw a "KeyError" for invalid weapon
