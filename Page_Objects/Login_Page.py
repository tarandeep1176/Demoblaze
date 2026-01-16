from selenium.webdriver.common.by import By

class LoginPageObjects:
        login_btn = (By.CSS_SELECTOR,"#login2")
        login_username = (By.CSS_SELECTOR,"#loginusername")
        login_password = (By.CSS_SELECTOR,"#loginpassword")
        submit = (By.CSS_SELECTOR,"button[onclick='logIn()']")
        welcome_text = (By.CSS_SELECTOR,"#nameofuser")
        close_btn = (By.CSS_SELECTOR,"#logInModal .btn-secondary")