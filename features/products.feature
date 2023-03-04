Feature: Detail feature in products

  Scenario: Product details page works correctly
    Given I have launched the Flask application
    When I navigate to the product details page with a valid product type
    Then I should see the product details
    And the displayed product details should match the given product type
