# PyZoom

PyZoom is a python script that accepts user input for a school subject and opens the meeting link for said subject in zoom.us.

PyZoom currently only supports Safari, but I hope to add support for other browsers such as Chrome and FireFox.

### Prerequisites

You must have Selenium Webdriver to use this project. Learn about installing and using Selenium here:
- https://selenium-python.readthedocs.io/installation.html
- https://selenium-python.readthedocs.io/getting-started.html

NOTE: Currently, you must have Safari installed. Support for other browsers coming soon.

### Installation

Once selenium is installed properly, you may download this project through:

```
git clone https://github.com/YulkyTulky/StealMemes.git
cd StealMemes
```

Then, you must edit the file in a text editor, inputting corresponding subjects and Zoom links.
To do this, find this section of the code:
```
classrooms = {
        "art": "https://zoom.us/j/0000000000",
        "english": "https://zoom.us/j/0000000000",
        "history": "https://zoom.us/j/0000000000",
        "language": "https://zoom.us/j/0000000000",
        "math": "https://zoom.us/j/0000000000",
        "science": "https://zoom.us/j/0000000000",
    }
and change subject names and zoom links accordingly, adding more key-value pairs when necessary.
```


## Authors

* **Eamon Tracey** - *Initial work* - [YulkyTulky](https://github.com/YulkyTulky)
