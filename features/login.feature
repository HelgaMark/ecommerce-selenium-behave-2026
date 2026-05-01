Feature: User login functionality
  As user of the e-commerce platform
  I want to be able to login with my credentials
  So that I can access my account and shop

  Background:
    Given I am on the Sauce Demo login page

  Scenario: Successful login with valid credentials
    When I enter username "standard_user"
    And I enter password "secret_sauce"
    And I click the login button
    Then I should be redirected to the products page
    And I should see the "Products" in the header

  Scenario: Login fails with invalid username
    When I enter username "invalid_user"
    And I enter password "secret_sauce"
    And I click the login button
    Then I should see an error message
    And the error message should contain "Username and password do not match"

  Scenario: Login fails with invalid password
    When I enter username "standard_user"
    And I enter password "invalid_password"
    And I click the login button
    Then I should see an error message
    And the error message should contain "Username and password do not match"

  Scenario: Login fails with empty credentials
    When I leave the username field empty
    And I leave the password field empty
    And I click the login button
    Then I should see an error message
    And the error message should contain "Username is required"

