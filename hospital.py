# Libraries
from pickle import *

# Data structures
date = dict(day=int, month=int, year=int)
doctor = dict(code=int, name=str, birthdate=date, specialty=str, status=str)

# Functions
def fill(f):
    cont = "Y"
    while cont.upper() == "Y":
        d = dict(doctor)
        d["code"] = int(input("Doctor Code = "))
        while d["code"] <= 0:
            d["code"] = int(input("Doctor Code (must be > 0) = "))

        d["name"] = input("Name = ")

        d["birthdate"]["day"] = int(input("Day of Birth = "))
        while not (1 <= d["birthdate"]["day"] <= 31):
            d["birthdate"]["day"] = int(input("Day of Birth (1-31) = "))

        d["birthdate"]["month"] = int(input("Month of Birth = "))
        while not (1 <= d["birthdate"]["month"] <= 12):
            d["birthdate"]["month"] = int(input("Month of Birth (1-12) = "))

        d["birthdate"]["year"] = int(input("Year of Birth = "))
        while not (1950 <= d["birthdate"]["year"] <= 2000):
            d["birthdate"]["year"] = int(input("Year of Birth (1950-2000) = "))

        d["specialty"] = input("Specialty = ")
        while len(d["specialty"]) > 20:
            d["specialty"] = input("Specialty (max 20 chars) = ")

        d["status"] = input("Marital Status (S=Single, M=Married) = ")
        while d["status"] not in ["S", "M"]:
            d["status"] = input("Marital Status (S=Single, M=Married) = ")

        dump(d, f)
        cont = input("Do you want to continue? (Y/N): ")
        while cont.upper() not in ["Y", "N"]:
            cont = input("Do you want to continue? (Y/N): ")


def add(f):
    d = dict(doctor)
    d["code"] = int(input("Doctor Code = "))
    while d["code"] <= 0:
        d["code"] = int(input("Doctor Code (must be > 0) = "))

    d["name"] = input("Name = ")

    d["birthdate"]["day"] = int(input("Day of Birth = "))
    while not (1 <= d["birthdate"]["day"] <= 31):
        d["birthdate"]["day"] = int(input("Day of Birth (1-31) = "))

    d["birthdate"]["month"] = int(input("Month of Birth = "))
    while not (1 <= d["birthdate"]["month"] <= 12):
        d["birthdate"]["month"] = int(input("Month of Birth (1-12) = "))

    d["birthdate"]["year"] = int(input("Year of Birth = "))
    while not (1950 <= d["birthdate"]["year"] <= 2000):
        d["birthdate"]["year"] = int(input("Year of Birth (1950-2000) = "))

    d["specialty"] = input("Specialty = ")
    while len(d["specialty"]) > 20:
        d["specialty"] = input("Specialty (max 20 chars) = ")

    d["status"] = input("Marital Status (S=Single, M=Married) = ")
    while d["status"] not in ["S", "M"]:
        d["status"] = input("Marital Status (S=Single, M=Married) = ")

    dump(d, f)


def display_all(f):
    try:
        while True:
            d = load(f)
            print("---- Doctor ----")
            print(f"Code: {d['code']}")
            print(f"Name: {d['name']}")
            print(f"Birthdate: {d['birthdate']['day']}/"
                  f"{d['birthdate']['month']}/"
                  f"{d['birthdate']['year']}")
            print(f"Specialty: {d['specialty']}")
            print(f"Marital Status: {d['status']}")
    except EOFError:
        pass


def married_doctors(f, f1):
    """Show married doctors AND save them in a file."""
    found = False
    try:
        while True:
            d = load(f)
            if d["status"] == "M":
                found = True
                print("---- Married Doctor ----")
                print(f"Name: {d['name']}")
                print(f"Specialty: {d['specialty']}")
                f1.write(f"Name: {d['name']}, Specialty: {d['specialty']}\n")
    except EOFError:
        pass

    if not found:
        print("No married doctors found.")


# ---------------- MAIN PROGRAM ----------------

print("---- Doctor Management Menu ----")
print("1. Add a new doctor")
print("2. Show all doctors")
print("3. Show married doctors")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    f = open("doctor.dat", "ab")
    add(f)
    f.close()
elif choice == 2:
    f = open("doctor.dat", "rb")
    display_all(f)
    f.close()
elif choice == 3:
    f = open("doctor.dat", "rb")
    f1 = open("married_doctors.txt", "w")
    married_doctors(f, f1)
    f.close()
    f1.close()
else:
    print("Invalid choice! Please run the program again.")
