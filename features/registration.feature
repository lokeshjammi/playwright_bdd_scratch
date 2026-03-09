Feature: Check registration feature in way2automation.com

    Feature Description
    As a user, I want to check the registration feature in way2automation.com
    So that I can ensure the feature is working correctly

    Scenario: Check registration feature in way2automation.com
        Given I am on the way2automation.com homepage
        When page title is displayed as "Welcome to the Test Sitee"
        Then Check for the display of registration form with title "Dummy Registration Form"
        Then Click on name field
        Then enter name field value as "Test"