#!/usr/bin/env python3

# This program is for .JPG and .TIFF format files.
# Installation and usage instructions:
# 1. Install Pillow (Pillow will not work if you have PIL installed):
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow
# 2. Add .jpg images  to subfolder ./images from where the script is stored.
# Note most social media sites strip exif data from uploaded photos.




import os
import os
import sys
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS


def create_google_maps_url(gps_coord):

    dec_deg_lat = convert_decimal_to_degree(float(gps_coord["lat"][0]), float(gps_coord["lat"][1]), gps_coord["lat_ref"])
    dec_deg_lon = convert_decimal_to_degree(float(gps_coord["lat"][0]), float(gps_coord["lat"][1]), gps_coord["lon_ref"])

    return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"


    



def convert_decimal_to_degree(degree, minute, second, direction):

    decimal_degree = degree + minute / 60 + second / 3600

# 'S' for south and 'W' for west
    if direction == 'S' or direction == 'W' :
        decimal_degree *= -1

    return decimal_degree



while True :
    output_choice = input("how do you to receive the ouput:\n\n1-file\n2-Terminal\n-chice here: ")

    try :
        choice = int(output_choice)

        if choice == 1:
            sys.stdout = open("exif_data.txt", "w")
            break
        elif choice == 2:
            break
        else :
            print("You entered an incorrect option, plese try again")
    except:
        print("You entered an invalid option, please try again.")


    


    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, "images"))
    files = os.listdir()


    if len(files) == 0:
        print("You don't have files in the ./images folder.")
        exit

    for file in files:

        try:
            image =Image.open(file)

            print("****************************************{file}************************************************")
            gps_coord = {}

            if image._getexif() == None:
                print(f"{file} contained no exif data.")

            else:
                for tag, value in image._getexif().items():

                    tag_name = TAGS.get(tag)

                    if tag_name == 'GPSinfo' :
                        for key, val in value.items():
                            print(f"{GPSTAGS.get(key} - {val})")

                            if GPSTAGS.get(key) == "GPSLatitude":
                                gps_coord["lat"] = val
                            elif GPSTAGS.get(key) == "GPSLongitude":
                                gps_coord["lon"] = val
                            elif GPSTAGS.get(key) == "GPSLatitudeRef":
                                gps_coord["lat_ref"] = val
                            elif GPSTAGS.get(key) == "GPSLongitudeRef":
                                gps_coord["lon_ref"] = val
                    else:
                        print(f" {tag_name} - {value}")
                
                if gps_coord:
                    print(create_google_maps_url(gps_coord))

                
        except IOError:
            print("file format not supported")

    
    if output_choice == 1:
        sys.stdout.close()
    os.chdir(cwd)



                        








