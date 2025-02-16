class HomePageTopNav:
    # These are Xpath
    HRango = '//*[@id="et-boc"]/header/div/div/div[1]/div[1]/div/div/div[1]/div/a/img'
    loginBtn = '//*[@id="header-btn"]/div/a'
    homeBtn = '//*[@id="menu-main-menu"]/li[1]/a'
    pricingBtn = '//*[@id="menu-main-menu"]/li[2]/a'
    contactBtn = '//*[@id="menu-main-menu"]/li[3]/a'
    featuresBtn = '//*[@id="menu-main-menu"]/li[4]/a'
    helpBtn = '//*[@id="menu-main-menu"]/li[6]/a'

class signupform():

    email_signup = '//*[@id="user-email"]'
    company_name = '//*[@id="user-company-name"]'
    full_name = '//*[@id="user-fullname"]'
    phone_number = '//*[@id="user-phone-number"]'
    country_code = '//*[@id="wpcf7-f277799-p70-o1"]/form/p[4]/span/div/div/div'
    submit_Btn = '//*[@id="wpcf7-f277799-p70-o1"]/form/p[5]/button'

class LoginPage:
    # these are CSS selector
    logo = 'body > div.page.responsive-log.relative.error-page3 > div > div:nth-child(2) > div > div > div.pt-4.pb-2.px-0 > a > img.header-brand-img.custom-logo'
    cardText = 'body > div.page.responsive-log.relative.error-page3 > div > div.d-none.d-md-block.col-md-6.col-lg-6.col-xl-6.bg-white > div > div > h2'
    formText = 'body > div.page.responsive-log.relative.error-page3 > div > div:nth-child(2) > div > div > div.pb-4.px-0.pt-6 > h1'
    # these are Xpath
    labelEmail = '//*[@id="myform"]/div[1]/label'
    labelPassword = '//*[@id="myform"]/div[2]/label'
    emailInput = '//*[@id="UserName"]'
    passwordInput = '//*[@id="Password"]'
    emailIcon = '//*[@id="myform"]/div[1]/div/div/span/i'
    passwordIcon = '//*[@id="Password-toggle"]/a/i'
    loginBtn = '//*[@id="loadingid"]'


