"""
//button[text()=" Sign in "]        # не используется знак @, потому что это не атрибут, а параметр!
//employee[@id=’1’]/name[text()=’John’]
(//button[text()=" Sign in "])[0]
//button[contains(@class,"btn")]
//button[@data-cy="submitButton" and @type="submit"]
"""

LOGO = ('xpath', '//a[@class="nav-link no-active"]')
ALL_TRACKS_TAB = ('xpath', '(//a[contains(@class, "btn")])[1]')
