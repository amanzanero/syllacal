# syllacal ![CI status](https://img.shields.io/badge/not%20running-red.svg)

## Pitch
Syllacal is a web service that imports all the vital exam dates and deadlines from your syllabus into your calendar. First, Syllacal scans your given PDF. Then, it exports relevant information surrounding a date (ex. 09/10, 09-10, September 10) to an .ics file. This can be added to your calendar (iCalendar, Google Calendar, and more).

More information available at [https://devpost.com/software/syllacal](https://devpost.com/software/syllacal). Presentation available at [https://docs.google.com/presentation/d/1PvxCvDMlyIk1RdIqbW5Fx7ui24Ad_m77D7VIbkph2I0/edit?usp=sharing](https://docs.google.com/presentation/d/1PvxCvDMlyIk1RdIqbW5Fx7ui24Ad_m77D7VIbkph2I0/edit?usp=sharing).

## Description
This repo contains the full stack for a 24-hour long hackathon project by four students at University of Southern California. The event was TrojanHacks on October 13-14th. The project vision is not fully implemented; as of October 14th, the back-end is able to identify text and output it to a terminal. The front-end supplies appealing visuals and allows the user to select a file to be uploaded and the submit button prompts the back-end functionality. The file type is not limited and no calendar features have been implemented.

## Languages
- Python (with Django)
- HTML (with Bootstrap)
- CSS

## Setup
Prerequisites:
* python 3.6

Cloning
```
$ git clone https://github.com/amanzanero/syllacal
```
```
pip install -r requirements.txt
```
to get dependencies.
Run with: 
```
python3 manage.py runserver
```

## Credits
Web template take from [https://github.com/BlackrockDigital/startbootstrap-creative](https://github.com/BlackrockDigital/startbootstrap-creative).
