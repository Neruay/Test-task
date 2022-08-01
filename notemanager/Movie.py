import csv
import os

def add_note(path, film_name, film_note, rating): # adding entry in csv in the following format "Movie name, description, rating"
    try:
        with open(path, "a", newline = "") as f:
            wrtr = csv.writer(f, delimiter = ",")
            data = [film_name,film_note,rating]
            wrtr.writerow(data)
    except:
        print("Invalid input")


def remove_note(path, film_name): # removing entry about certain movie in csv file. As we can't delete entry from csv file, we rebuild the whole csv from the scratch, skipping only one certain entry
    try:
        data = []
        with open(path, "r", newline = "") as f:
            rdr = csv.reader(f, delimiter = ",")
            for row in rdr:
                data.append(row)
        os.remove(path)
        with open(path, "w+", newline = "") as f:
            wrtr = csv.writer(f, delimiter = ",")
            for row in data:
                if row[0] != film_name:
                    wrtr.writerow(row)
    except:
        print("Invalid input")

def print_notes(path): # printing all existing entries in readable format
    try:
        with open(path, "r", newline = "") as f:
            rdr = csv.reader(f, delimiter = ",")
            for row in rdr:
                print(" / ".join(row))
    except:
        print("Invalid input")

def best_rated(path, number_of_entries): # sorting all entries by rating column and printing best number_of_enties of them
    try:
        with open(path, "r", newline = "") as f:
            rdr = csv.reader(f, delimiter = ",")
            data = sorted(rdr, key=lambda row: int(row[2]), reverse = True)
        if number_of_entries > 0:
            print("Top {} best films by rating:".format(number_of_entries))
        for entry in range(number_of_entries):
            print("{}. ".format(entry + 1) + data[entry][0], "-", data[entry][2])
    except:
        print("Invalid input")

def worst_rated(path, number_of_entries): # sorting all entries by rating column and printing worst number_of_enties of them
    try:
        with open(path, "r", newline = "") as f:
            rdr = csv.reader(f, delimiter = ",")
            data = sorted(rdr, key=lambda row: int(row[2]))
        if number_of_entries > 0:
            print("Top {} worst films by rating:".format(number_of_entries))
        for entry in range(number_of_entries):
            print("{}. ".format(entry + 1) + data[entry][0], "-", data[entry][2])
    except:
        print("Invalid input")

def get_average_rating(path): # calculating arithmetical mean of all entries
    row_counter = 0
    total_rating = 0
    with open(path, "r", newline = "") as f:
        rdr = csv.reader(f, delimiter = ",")
        for row in rdr:
            total_rating += int(row[2])
            row_counter += 1
    print("Average rating -", round(total_rating / row_counter, 1))