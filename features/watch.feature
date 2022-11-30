Feature: watch

  Background: common steps

    Given Launch the browser
    When open facebook home page


  Scenario: user is able to click on the watch icon
#    And user is able to search the videos
    And watch module is selected by default
    And user is able to click on setting
    And user is able to turn on the show notification dots
    And user is able to click on custom notifications
    And user is able to turn on the allow video notifications
    And user is able to click on manage pages you follow
    And user is able to click on the cross button
    And user is able to click on the live icon
    And user is able to click on the shows icon
#    And user is able to click on the saved videos icon
    Then verify watch module working
