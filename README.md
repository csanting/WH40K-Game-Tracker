# WH40K-Game-Tracker

A simple, lightweight, self-hosted Python+Flask web app that tracks Primary Victory, Secondary Victory and Command Points for standard 10th ed WH40K matches.

Created as a refresher and practice side project.

## Dependencies/Versions

Written in Python 3.11.11 with flask 3.1.0

Virtual environment created using conda. Only package install is:

`conda install flask`

## Usage

Navigate to wherever the project is cloned and simply run:

`python .\main.py`

## TODO

Desired features with no particular order and no timeline:

- [x] Ability to save and load games in progress
- [ ] Database of mission scenarios and secondary objectives to streamline point tracking
- [ ] Provide (free) instances to individuals who do not want to run locally
- [ ] Allow multiple devices to edit a singular game instance
- [ ] Cleaner look

Always open for additional feedback, drop an issue.

## Preview
Home Screen:

![Home Screen](https://github.com/csanting/WH40K-Game-Tracker/blob/main/components/preview/home_page_preview.PNG "Home Screen")

Game Screen:

![Game Screen](https://github.com/csanting/WH40K-Game-Tracker/blob/main/components/preview/game_page_preview.PNG "Game Screen")

## Acknowledgements

All logo image files found on [drawshield.net](https://drawshield.net/catalog/charges/warhammer/).

James Workshop for creating the vast [40K](https://warhammer40000.com/) universe that has captivated millions.

The [Flask Project](https://flask.palletsprojects.com/en/stable/#).

