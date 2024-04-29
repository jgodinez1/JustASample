Feature File
Given I login to website with user and password
When I goto my payment page
Then I see a list of my recent payments

Steps
Common.py
    @given(u'I load the website')
    def step_impl_load_website(context):
        print('I load the website')

    @when(u'I go to "{page}" page')
    def step_impl_goto_page(context, page):
        print('I go to {} page'.format(page)

Payment.py
    @then(u'I see a list of my recent payments')
    def step_impl_list_recent_payments
        print('Here's the list of payments')

Pages
loginPage
    #imports at top

    class Login():
        instance = None

        @classmethod
        def get_instance(cls):
            if cls.instance is None:
                cls.instance = Login()
            return cls.instance

        def __init__(self):
            self.driver = webapp.get_driver

    login = Login.get_instance()
    

paymentPage


Locaters.py
    # for login page
   uname = self.driver.find_element_by_id('user_name').text
   pword = self.driver.find_element_by_id('pass_word').text

    #for payment page
   transactions = self.driver.find_element_by_class('table payment list')
   





