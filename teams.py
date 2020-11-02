from selenium import webdriver
import time
import datetime


def initiate_class():
    options = webdriver.ChromeOptions()
    options.add_argument("use-fake-ui-for-media-stream")

    driver = webdriver.Chrome(options=options)
    driver.get('https://teams.microsoft.com/go#')

    def login(email_id, password):
        time.sleep(5)
        email_textfield = driver.find_element_by_css_selector('#i0116')
        email_textfield.send_keys(email_id)
        time.sleep(2)
        next_button = driver.find_element_by_css_selector('#idSIButton9')
        next_button.click()
        time.sleep(2)
        password_textfield = driver.find_element_by_css_selector('#i0118')
        password_textfield.send_keys(password)
        time.sleep(2)

        driver.find_element_by_css_selector(
            '#idSIButton9').click()  # for sign in button
        driver.find_element_by_css_selector(
            '#idSIButton9').click()  # for stay signed-in button
        time.sleep(20)

    def find_team(team_name):
        if team_name == 'DAA':
            driver.find_elements_by_xpath(
                "//*[contains(text(), 'CS1501-CSE-V-C')]")[0].click()
        elif team_name == 'SE':
            driver.find_elements_by_xpath(
                "//*[contains(text(), 'BTECH-CSE-CS1502-C')]")[0].click()
        elif team_name == 'DCOM':
            driver.find_elements_by_xpath(
                "//*[contains(text(), 'CSE5CDCOM')]")[0].click()
        elif team_name == 'ACD':
            driver.find_elements_by_xpath(
                "//*[contains(text(), 'ACD CSE (5 C)')]")[0].click()
        elif team_name == 'DE':
            driver.find_elements_by_xpath(
                "//*[contains(text(), 'Python Programming-DE-CS-B')]")[0].click()
        elif team_name == 'OE':
            driver.find_elements_by_xpath(
                "//*[contains(text(), 'SOLAR PHOTOVOLTAICS ENERGY CONVERSION')]")[0].click()
        elif team_name == 'TEST':
            driver.find_elements_by_xpath(
                "//*[contains(text(), 'test team @sgiix')]")[0].click()
        else:
            print('wrong team name')

    def run_class(team_name):

        find_team(team_name)

        time.sleep(15)
        driver.find_elements_by_xpath(
            "//*[contains(text(), 'Join')]")[-1].click()  # for join button in discussion
        time.sleep(5)
        driver.find_element_by_css_selector(
            '#page-content-wrapper > div.flex-fill > div > calling-pre-join-screen > div > div > div.ts-calling-pre-join-content > div.central-section > div.video-and-name-input > div > div > section > div.buttons-container > toggle-button:nth-child(1) > div > button > span.style-layer').click()  # to disable webcam
        # driver.find_element_by_css_selector(
        # '#preJoinAudioButton > div > button > span.style-layer').click()  # to disable mic
        time.sleep(2)
        driver.find_element_by_css_selector(
            '#page-content-wrapper > div.flex-fill > div > calling-pre-join-screen > div > div > div.ts-calling-pre-join-content > div.central-section > div.video-and-name-input > div > div > section > div.flex-fill.input-section > div > div > button').click()  # to join the class
        print('joined class : ' +
              datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        # time.sleep(10)
        # driver.find_element_by_css_selector(
        # '#toast-container > div > div > div.toast-message > div > button:nth-child(2) > div').click()  # might vary from desktop to desktop for closing pop at bottom right
        time.sleep(5)
        # driver.find_element_by_css_selector(
        # '#roster-button > ng-include > svg').click()  # for opening participants and their count
        # time.sleep(300)
        # if len(driver.find_elements_by_xpath(
        #         "//*[contains(text(), 'Suggestions')]")) != 0:
        #     driver.find_elements_by_xpath(
        #         "//*[contains(text(), 'Suggestions')]")[0].click()
        while True:
            time.sleep(2)
            print(len(driver.find_elements_by_css_selector('#page-content-wrapper > div.flex-fill > div > calling-screen > div > div.ts-calling-screen.flex-fill.call-connected.PERSISTENT.passive-bar-available.shift-up.has-meeting-info.closed-captions-hidden.PRESENTATION.show-participants-in-passive-bar.trigger-overlap > div.call-screen-main.flex-fill > div.flex-fill.call-screen-wrapper > div.call-screen-footer > div > calling-passive-bar > div > div.ts-calling-hidden-participants-count.item > div > div')))
            if len(driver.find_elements_by_css_selector('#page-content-wrapper > div.flex-fill > div > calling-screen > div > div.ts-calling-screen.flex-fill.call-connected.PERSISTENT.passive-bar-available.shift-up.has-meeting-info.closed-captions-hidden.PRESENTATION.show-participants-in-passive-bar.trigger-overlap > div.call-screen-main.flex-fill > div.flex-fill.call-screen-wrapper > div.call-screen-footer > div > calling-passive-bar > div > div.ts-calling-hidden-participants-count.item > div > div')) == 0:
                print('ab class khatam' +
                      datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                driver.quit()

                # if int(driver.find_element_by_css_selector('#page-content-wrapper > div.flex-fill > div > calling-screen > div > div.ts-calling-screen.flex-fill.call-connected.PERSISTENT.GRID.passive-bar-available.shift-up.has-meeting-info.closed-captions-hidden.show-roster.has-panel.trigger-overlap > meeting-panel-components > calling-roster > div > div.scroll-container.flex-fill > div > div.scrolling-pane > accordion > div > accordion-section:nth-child(2) > div > calling-roster-section > div > div.roster-list-title-group.has-roster-limit > button > span.toggle-number').text.strip("()")) < 15:  # comparing participant count
                # driver.find_element_by_css_selector(
                #     '#hangup-button > ng-include > svg').click()  # clicking hangup button
                # time.sleep(10)
                # print('participants when leaving : ' + driver.find_element_by_css_selector('#page-content-wrapper > div.flex-fill > div > calling-screen > div > div.ts-calling-screen.flex-fill.call-connected.PERSISTENT.GRID.passive-bar-available.shift-up.has-meeting-info.closed-captions-hidden.show-roster.has-panel.trigger-overlap > meeting-panel-components > calling-roster > div > div.scroll-container.flex-fill > div > div.scrolling-pane > accordion > div > accordion-section:nth-child(2) > div > calling-roster-section > div > div.roster-list-title-group.has-roster-limit > button > span.toggle-number').text.strip("()"))
                # driver.quit()
                # print('class finished : ' +
                #       datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                # break

    login('email@gmail.com', 'password')
    run_class('DAA')


def run_script():
    while True:
        # time.sleep(30)
        if (datetime.datetime(2020, 8, 19, 16, 15, 00) < datetime.datetime.now()):
            print('browser opened : ' +
                  datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            initiate_class()
            break


# try:
#     run_script()
# except:
#     print('error occurred : ' +
#           datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
#     # run_script()

run_script()
