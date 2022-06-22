from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()

def test_check_mix_snippet_postgrex():
    driver = webdriver.Firefox(executable_path='/home/hoffmann/Downloads/geckodriver',options=options)
    
    driver.get('http://localhost:4000/')
    driver.find_element_by_xpath("//a[contains( text(), 'Packages')]").click()
    driver.find_element_by_xpath("//a[contains( text(), 'postgrex')]").click()
    
    mix_snippet = driver.find_element_by_id("mix-snippet").get_attribute("value")
    mix_snippet_expected = '{:postgrex, "~> 0.1.0"}'
    assert mix_snippet == mix_snippet_expected

    driver.quit()


def test_redirect_to_rebar_documentation():
    driver = webdriver.Firefox(executable_path='/home/hoffmann/Downloads/geckodriver',options=options)
    
    driver.get('http://localhost:4000/')
    driver.find_element_by_xpath("//a[contains( text(), 'Using with Elixir')]").click()
    driver.find_element_by_xpath("//a[@href='/docs/rebar3_usage']").click()
    driver.find_element_by_xpath("//a[contains( text(), 'rebar3 documentation')]").click()
    
    url = driver.current_url
    url_expected = 'https://rebar3.org/docs/configuration/dependencies/'
    assert url == url_expected
    
    driver.quit()


def test_redirect_to_mail_suport():
    driver = webdriver.Firefox(executable_path='/home/hoffmann/Downloads/geckodriver',options=options)
    
    driver.get('http://localhost:4000/')
    driver.find_element_by_xpath("//a[@href='https://github.com/hexpm']").click()
    driver.find_element_by_xpath("//a[@href='/hexpm/hexpm']").click()
    
    url = driver.current_url
    url_expected = 'https://github.com/hexpm/hexpm'
    assert url == url_expected
    
    driver.quit()


def test_invalid_login():
    driver = webdriver.Firefox(executable_path='/home/hoffmann/Downloads/geckodriver',options=options)
    
    driver.get('http://localhost:4000/')
    driver.find_element_by_xpath("//a[@href='/login']").click()
    driver.find_element_by_id("username").send_keys("saas")
    driver.find_element_by_id("password").send_keys("suus")
    driver.find_element_by_xpath("/html/body/section/div[2]/form/button").click()
    
    url = driver.current_url
    url_expected = 'http://localhost:4000/login'
    assert url == url_expected
    
    alert = driver.find_element_by_xpath("/html/body/section/div[1]/div")
    alert_expected = 'Invalid username, email or password.'
    assert alert.text == alert_expected
    
    driver.quit()