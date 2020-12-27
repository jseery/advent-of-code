from pathlib import Path
import re
import itertools
from toolz import groupby
from loguru import logger


REQUIRED_FIELDS = set(
    [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # 'cid',  # 'cid' is optional
    ]
)

HCL_EXPR = re.compile(r"#[0-9a-f]{6}")


def get_puzzle_input(fname: str):
    input = Path(__file__).parent.joinpath(fname).read_text()
    return input


def parse_batch_file(puzzle_input: str):
    all_passports = []
    current_passport = []
    for line in puzzle_input.splitlines():
        if line == "":
            all_passports.append(" ".join(current_passport))
            current_passport = []
        else:
            current_passport.append(line)
    all_passports.append(" ".join(current_passport))
    return all_passports


def parse_passport(psprt: str) -> dict:
    k_v_tuples = map(lambda x: x.split(":"), psprt.split())
    result = {}
    for k, v in k_v_tuples:
        if k == "pid":
            result[k] = v
        else:
            try:
                result[k] = int(v)
            except ValueError:
                result[k] = v
    return result


def judge_passport_easy(psprt: dict) -> bool:
    if len(psprt) == 8:
        return True
    elif (len(psprt) == 7) and ("cid" not in psprt):
        return True
    return False


def judge_passport(psprt: dict) -> bool:
    if not REQUIRED_FIELDS <= psprt.keys():
        logger.error(f"{psprt.keys()=} missing required keys.")
        return False
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if not (1920 <= psprt["byr"] <= 2002):
        logger.error(f"{psprt['byr']=}")
        return False
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if not (2010 <= psprt["iyr"] <= 2020):
        logger.error(f"{psprt['iyr']=}")
        return False
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not (2020 <= psprt["eyr"] <= 2030):
        logger.error(f"{psprt['eyr']=}")
        return False
    # hgt (Height) - a number followed by either cm or in:
    try:
        hgt_val = int(psprt["hgt"][:-2])
    except ValueError:  # we tried to int() a string
        logger.error(f"{psprt['hgt']=}")
        return False
    except TypeError:  # tried to subscript an int
        logger.error(f"{psprt['hgt']=}")
        return False
    hgt_units = psprt["hgt"][-2:]
    if not hgt_units in ("cm", "in"):
        logger.error(f"{hgt_units=}")
        return False
    # If cm, the number must be at least 150 and at most 193.
    if (hgt_units == "cm") and not (150 <= hgt_val <= 193):
        return False
    # If in, the number must be at least 59 and at most 76.
    if (hgt_units == "in") and not (59 <= hgt_val <= 76):
        return False
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if not HCL_EXPR.fullmatch(psprt["hcl"]):
        logger.error(f"{psprt['hcl']=}")
        return False
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if psprt["ecl"] not in (
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    ):
        logger.error(f"{psprt['ecl']=}")
        return False
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if len(str(psprt["pid"])) != 9:
        logger.error(f"{psprt['pid']=}, {len(str(psprt['pid']))=}")
        return False
    # cid (Country ID) - ignored, missing or not.
    return True


def main():

    pz = get_puzzle_input("input.txt")

    parsed_passports = map(parse_passport, parse_batch_file(pz))

    judged = groupby(judge_passport, parsed_passports)

    for outcome in judged:
        print(outcome, len(judged[outcome]))

    return


if __name__ == "__main__":
    main()
