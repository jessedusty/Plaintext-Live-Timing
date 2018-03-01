import urllib.request
from operator import itemgetter

DNF_time = 9999


def parse_time(time):
    if "DSQ" in time or "DNF" in time or "DNS" in time:
        return DNF_time
    if ":" in time:
        parts = time.split(":")
        return int(parts[0]) * 60 + float(parts[1])
    return float(time)


def get_text(url):
    with urllib.request.urlopen(url) as f:
        return f.read().decode("UTF-8")


def print_person(person):
    print(person["name"] + " #" + str(person["place"]))
    print(" r1: " + person["r1"])
    print(" r2: " + person["r2"])
    print(" c: " + person["tt"])


def string_person(person):
    a = person["name"] + " #" + str(person["place"]) + "\n"
    if "r1" in person:
        a += " r1: " + person["r1"] + "\n"
    if "r2" in person:
        a += " r2: " + person["r2"] + "\n"
    if "tt" in person:
        a += " c: " + person["tt"] + "\n"
    return a


def retrieve_times(id): # 185595
    url = "http://www.live-timing.com/includes/aj_race.php?r={}&&m=1&&u=5".format(id)
    content = get_text(url)

    racer = {"s_tt": DNF_time}
    racers = []
    for a in content.split("|"):
        b = a.split("=")
        if b[0] == "m":
            if "name" in racer:
                racers.append(racer)
            racer = {"s_tt": DNF_time}
            racer["name"] = b[1]
        elif b[0] == "t":
            racer["team"] = b[1]
        elif b[0] == "r1":
            racer["r1"] = b[1]
            racer["s_r1"] = parse_time(b[1])
        elif b[0] == "r2":
            racer["r2"] = b[1]
            racer["s_r2"] = parse_time(b[1])
        elif b[0] == "tt":
            racer["tt"] = b[1]
            racer["s_tt"] = parse_time(b[1])

    newlist = sorted(racers, key=itemgetter("s_tt"))

    for i, n in enumerate(newlist):
        n["place"] = i + 1

    return newlist


def stringify_racers(times_list):
    result = ""
    for i in times_list:
        result += string_person(i)
    return result


def show_team(times_list, team="SIT"):
    return filter(lambda x: x["team"] == team.upper(), times_list)
