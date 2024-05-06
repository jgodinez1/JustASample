@statements
Feature: View Statements
  Here we can list the functional areas, stories etc.  Stories can also be tags
  # Can make balance, type of card, number of statements into variables
Background:
 Given I have a customer
 And I create an account with 2000 balance
 And I create a physical card
 And I load statements for that card

  # Can make page to go to, nth statement into variables/scenario outline
@smoke
Scenario: view the first statement
  Given I am on the account summary page
  When I go to the "statement" page
  And I click on the <nth> statement
  Then I verify that the pdf of the statement is shown

@regression
Scenario: Verify the number of statements is correct
  Given I am on the account summary page
  When I go to the "statement" page
  Then I see <number> of statements

