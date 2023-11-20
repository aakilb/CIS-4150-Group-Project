Feature: Controlling Monsters
  Scenario Outline: Initialize Pre-set Monster
    Given give_monster <species>
    Then the monster <name> should have HP=<hp> DMG=<dmg> Action=<action>

  Examples: Monster Species
    | species | name | hp | dmg | action |
    | chicken | Chicken | 1 | 1 | pinched |
    | guard | Guard | 2 | 2 | punched |
    | bear | Bear | 4 | 2 | slashed at |
    | pbag | Punching-Bag | 10 | 0 | N/A |

  @wip
  Scenario: Initialize Pre-set Monster with Special Name
    Given give special monster chicken
    Then the monster Chicken should have special name

  Scenario: Monster attacks an opponent
    Given give_monster chicken
    And an opponent pbag
    When monster attacks opponent
    Then opponent took 1 DMG

  Scenario: Monster kills an opponent
    Given give_monster guard
    And an opponent chicken
    When monster attacks opponent
    Then opponent took 2 DMG
    And the opponent died
