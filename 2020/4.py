import re


def process(filename):
    with open(filename, "r") as file:
        tally = 0
        current_passport = Passport()
        for l in file:
            line = l.strip()
            if line == "":
                if current_passport.is_valid():
                    tally += 1
                current_passport = Passport()
                continue
            current_passport.parse_line(line)
        return tally


class Passport(object):
    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None

    def is_valid(self):
        if(self.byr == None or
           self.iyr == None or
           self.eyr == None or
           self.hgt == None or
           self.hcl == None or
           self.ecl == None or
           self.pid == None):
            return False
        if self.validate():
            return True
        else:
            return False

    def validate(self):

        if validate_int(self.byr, 1920, 2002) == False:
            print(f"invalid byr {self.byr}")
            return False

        if validate_int(self.iyr, 2010, 2020) == False:
            print(f"invalid iyr: {self.iyr}")
            return False
        if validate_int(self.eyr, 2020, 2030) == False:
            print(f"invalid eyr: {self.eyr}")
            return False
        if self.validate_height() == False:
            print(f"invalid height: {self.hgt}")
            return False
        if self.validate_hair()  == False:
            print(f"invalid hcl: {self.hcl}")
            return False
        if self.validate_eyes()  == False:
            print(f"invalid ecl: {self.ecl}")
            return False
        if self.validate_passport() == False:
            print(f"invalid pid: {self.pid}")
            return False

        return True

    def validate_height(self):
        units, val = self.hgt[-2:], self.hgt[0:-2]
        if not val.isdigit():
            print(val)
            return False
        value = int(val)
        if units == "cm" and value >= 150 and value < 194:
            return True
        if units == "in" and value >= 59 and value < 77:
            return True
        return False

    def validate_hair(self):
        return regex_match("#[a-f0-9]{6}", self.hcl)

    def validate_eyes(self):
        if self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True
        return False

    def validate_passport(self):
        return regex_match("[0-9]{9}", self.pid)

    def parse_line(self, line):
        keyvals = line.split(" ")
        for keyval in keyvals:
            split = keyval.split(":")
            self.parse(split[0], split[1])

    def parse(self, key, val):
        if key == "byr":
            self.byr = val
        if key == "iyr":
            self.iyr = val
        if key == "eyr":
            self.eyr = val
        if key == "hgt":
            self.hgt = val
        if key == "hcl":
            self.hcl = val
        if key == "ecl":
            self.ecl = val
        if key == "pid":
            self.pid = val
        if key == "cid":
            self.cid = val


def regex_match(regexp: str, value: str):
    matches = re.fullmatch(regexp, value)
    if matches is None:
        return False
    return True


def validate_int(value: str, min: int, max: int):
    if not value.isdigit():
        return False
    asint = int(value)
    return asint >= min and asint <= max


# print("valid")
# print(process("./4_2_valid.txt"))

# print("########################")

# print("invalid")

# print(process("./4_2_invalid.txt"))

print(process("./4.txt"))