import argparse
import csv
import getpass
import pymongo
from datetime import date

myclient = pymongo.MongoClient(
    "mongodb+srv://burrutia:<password>@seniorproject-west.ralsx.mongodb.net/test")

mydb = myclient["mydatabase"]
col1 = mydb["mycollection1"]
col2 = mydb["mycollection2"]

parser = argparse.ArgumentParser(
    description="import and count text file lines")
parser.add_argument("-f", "--files", type=str,
                    help="name of the files", nargs="+")
parser.add_argument("-x", "--xytech", type=str, help="name of the xytech file")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="show verbose")
parser.add_argument("-o", "--output", type=str, help="CSV or Database output")
args = parser.parse_args()

if args.verbose:
    print("verbose")

csv_header1 = ["script_user", "machine", "file_username",
               "file_date", "date"]
csv_header2 = ["file_username", "file_date",
               "location", "frame_ranges"]
csv_data1 = []
csv_data2 = []

# source: https://csun.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f5a20e3b-b5de-4c82-9742-afd30026a429
xytech_file_location = args.xytech
xytech_folders = []

read_xytech_file = open(xytech_file_location, "r")
for line in read_xytech_file:
    if "/" in line:
        xytech_folders.append(line)

for baselight_or_flame_file in args.files:
    file_location = baselight_or_flame_file
    read_file = open(file_location, "r")
    parse_file_name = baselight_or_flame_file
    parse_file_name = parse_file_name.replace("_", " ")
    parse_file_name = parse_file_name.replace(".txt", "")
    parse_file_name = parse_file_name.split()
    file_machine = parse_file_name.pop(0)
    file_user = parse_file_name.pop(0)
    file_date = parse_file_name.pop(0)
    if args.output == "DB":
        col1.insert_one({"script_user": getpass.getuser(), "machine": file_machine, "file_username": file_user,
                        "file_date": file_date, "date": str(date.today()).replace("-", "")})
    elif args.output == "CSV":
        csv_data1.append({"script_user": getpass.getuser(), "machine": file_machine, "file_username": file_user,
                          "file_date": file_date, "date": str(date.today()).replace("-", "")})

    for line in read_file:
        line_parse = line.split(" ")
        if "Baselight" in file_location:
            current_folder = line_parse.pop(0)
            sub_folder = current_folder.replace("/images1/Avatar", "")
        elif "Flame" in file_location:
            line_parse.pop(0)
            current_folder = line_parse.pop(0)
            sub_folder = current_folder.replace("Avatar", "")
        for xytech_line in xytech_folders:
            if sub_folder in xytech_line:
                new_location = xytech_line.strip()
        first = ""
        pointer = ""
        last = ""
        for numeral in line_parse:
            if not numeral.strip().isnumeric():
                continue
            if first == "":
                first = int(numeral)
                pointer = first
                continue
            if int(numeral) == (pointer + 1):
                pointer = int(numeral)
                continue
            else:
                last = pointer
                if first == last:
                    # print("%s %s" % (new_location, first))
                    if args.output == "DB":
                        col2.insert_one({"file_username": file_user, "file_date": file_date,
                                        "location": new_location, "frame_ranges": str(first)})
                    elif args.output == "CSV":
                        csv_data2.append({"file_username": file_user, "file_date": file_date,
                                          "location": new_location, "frame_ranges": str(first)})
                else:
                    # print("%s %s-%s" % (new_location, first, last))
                    if args.output == "DB":
                        col2.insert_one({"file_username": file_user, "file_date": file_date,
                                        "location": new_location, "frame_ranges": str(first)+"-"+str(last)})
                    elif args.output == "CSV":
                        csv_data2.append({"file_username": file_user, "file_date": file_date,
                                          "location": new_location, "frame_ranges": str(first)+"-"+str(last)})
                first = int(numeral)
                pointer = first
                last = ""
        last = pointer
        if first != "":
            if first == last:
                # print("%s %s" % (new_location, first))
                if args.output == "DB":
                    col2.insert_one({"file_username": file_user, "file_date": file_date,
                                    "location": new_location, "frame_ranges": str(first)})
                elif args.output == "CSV":
                    csv_data2.append({"file_username": file_user, "file_date": file_date,
                                      "location": new_location, "frame_ranges": str(first)})
            else:
                # print("%s %s-%s" % (new_location, first, last))
                if args.output == "DB":
                    col2.insert_one({"file_username": file_user, "file_date": file_date,
                                    "location": new_location, "frame_ranges": str(first)+"-"+str(last)})
                elif args.output == "CSV":
                    csv_data2.append({"file_username": file_user, "file_date": file_date,
                                      "location": new_location, "frame_ranges": str(first)+"-"+str(last)})

# source: https://www.pythontutorial.net/python-basics/python-write-csv-file/
if args.output == "CSV":
    with open("mycollection1.csv", "w", encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=csv_header1)
        writer.writeheader()
        writer.writerows(csv_data1)
    with open("mycollection2.csv", "w", encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=csv_header2)
        writer.writeheader()
        writer.writerows(csv_data2)
