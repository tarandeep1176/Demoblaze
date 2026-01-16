from selenium.webdriver.common.by import By

class SignupPageObjects:
    signup_btn = (By.CSS_SELECTOR,"#signin2")
    signup_username = (By.CSS_SELECTOR,"#sign-username")
    signup_password = (By.CSS_SELECTOR,"#sign-password")
    submit_btn = (By.CSS_SELECTOR,"button[onclick='register()']")
    close_btn = (By.CSS_SELECTOR,"#signInModal .btn-secondary")