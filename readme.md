# Window Seat


This software will allow a photo to be uploaded to a webservice along with a
- flight number
- seat number

The webservice will then return a location that the plane was at when the photo was taken. 
This location should be in the form of a google maps link.

The goal is to allow people to take photos and then figure out what they were taking a photo of.

- No data from the user needs to be stored long term
- Using an existing service to locate the geocoords of the flight path

Extra for experts
- Time zone information should be incorporated, generally peoples phones will be set to 
the timezone they start with
- Different planes will have different seat letters, row F on an A320 will be different from a 787

## Setup requirements
heif library requires some additional steps as it's a wrapper

https://pypi.org/project/pyheif/

### MacOS
```
brew install libffi libheif
pip install git+https://github.com/carsales/pyheif.git
```