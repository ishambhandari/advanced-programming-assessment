Feature: Pagination and detail feature in customers

  Scenario: Pagination works correctly in Customers page
    Given I have launched the Flask application
    When I navigate to the Customers page with pagination parameters
    Then I should see all the customers with pagination links 

 Scenario: Customer details page works correctly
    Given I have launched the Flask application
    When I navigate to the customer details page with a valid customer id as parameter
    Then I should see the customer details page

