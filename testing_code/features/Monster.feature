Feature: Controlling Monsters
  @WIP
  Scenario Outline: Initialize Pre-set Monster
    Given give_monster <species>
    Then the monster <name> should have HP=<hp> DMG=<dmg> Action=<action>

  Examples: Monster Species
    | species | name | hp | dmg | action |
    | chicken | Chicken | 1 | 1 | pinched |
    | guard | Guard | 2 | 2 | punched |
    | bear | Bear | 4 | 2 | slashed at |
