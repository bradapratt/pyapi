#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?"
all_cams = ["FHAZ", "RHAZ", "MAST", "CHEMCAM", "NAVCAM"]


def main():
    # first I want to grab my credentials
    with open("nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()

    # remove any newline characters from the api_key
    nasacreds = "&api_key=" + nasacreds.strip("\n")

    # get rover info
    count = 0
    roverlist = []
    for rover in requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers?" + nasacreds).json()['rovers']:
        roverlist.append((rover['name'].lower(), rover['max_sol']))
        count += rover['total_photos']
    print(f"There are {count} total photos!")

    # get just photo links
    for rover in roverlist:
        for sol in range(1, rover[1]):
            for photo in requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/" + rover[0] + "/photos?sol=" + str(sol) + nasacreds).json()['photos']:
                print(photo['img_src'])

    # get rover name & date too
    for rover in roverlist:
        for sol in range(1, rover[1]):
            for photo in requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/" + rover[0] + "/photos?sol=" + str(sol) + nasacreds).json()['photos']:
                print("ROVER: " + rover[0].capitalize())
                print("DATE: " + photo['earth_date'])
                print(photo['img_src'])
                print()

    # let user decide camera
    choice = input(f"Please enter type the name of the desired camera {all_cams}: ")
    while choice not in all_cams:
        print("Invalid entry. Camera name must match exactly.")
        choice = input(f"Please enter type the name of the desired camera {all_cams}: ")

    for rover in roverlist:
        for sol in range(1, rover[1]):
            for photo in requests.get(
                    "https://api.nasa.gov/mars-photos/api/v1/rovers/" + rover[0] + "/photos?sol=" + str(
                            sol) + nasacreds).json()['photos']:
                if photo['camera']['name'] == choice:
                    print("ROVER: " + rover[0].capitalize())
                    print("CAMERA: " + photo['camera']['name'])
                    print("DATE: " + photo['earth_date'])
                    print(photo['img_src'])
                    print()


if __name__ == "__main__":
    main()
