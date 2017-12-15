Feature: menu

  Background: login
    Given I am on 'http://localhost/litecart/admin' page
    When I type 'admin' in 'username' input field
    When I type 'admin' in 'password' input field
    When I click '.footer [type="submit"]' button
    Then I am on new page with title 'My Store'

 Scenario: 
    And I am browsing menu
    Then I get header of subpage