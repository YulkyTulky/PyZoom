from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import sys


def main():
    """The user must patch the values in the classrooms dictionary.

    Simply insert a string key representing a subject and make its value
    a string representing the appropriate zoom link. A template is
    currently given.
    """

    classrooms = {
        "art": "https://zoom.us/j/0000000000",
        "english": "https://zoom.us/j/0000000000",
        "history": "https://zoom.us/j/0000000000",
        "language": "https://zoom.us/j/0000000000",
        "math": "https://zoom.us/j/0000000000",
        "science": "https://zoom.us/j/0000000000",
    }

    try:
        room = sys.argv[1]
    except IndexError:
        room = input("Class: ").lower()

    if room not in classrooms:
        print("Invalid Classroom.")
        return
    else:
        driver = webdriver.Safari()
        driver.get(classrooms[room])
        try:
            WebDriverWait(driver, 5).until(ec.alert_is_present())
        except TimeoutException:
            print("The pop-up alert did not load. Please check your internet connection and try again.")
        else:
            driver.switch_to.alert.accept()
        finally:
            driver.quit()


main()
