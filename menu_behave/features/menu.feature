Feature: menu
  Scenario: menu retriving
    Given I am on store page
    When I am logged in as admin
    And I am browsing menu
    Then I get header of subpage