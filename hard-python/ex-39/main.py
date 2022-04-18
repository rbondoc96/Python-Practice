#!/usr/bin/env python3

def main():
    states = {
        "Oregon": "OR",
        "Florida": "FL",
        "California": "CA",
        "New York": "NY",
        "Michigan": "MI",
    }

    cities = {
        "CA": "San Francisco",
        "MI": "Detroit",
        "FL": "Jacksonville",
    }

    cities["NY"] = "New York"
    cities["OR"] = "Portland"

    separator = "".center(10, "-")
    print(separator)
    print("NY state has:", cities["NY"])
    print("OR state has:", cities["OR"])

    print(separator)
    print("Michigan's abbreviation is:", states["Michigan"])
    print("Florida's abbreviation is:", states["Florida"])

    print(separator)
    print("Michigan has:", cities[states["Michigan"]])
    print("Florida has:", cities[states["Florida"]])

    print(separator)
    for state, abbrev in states.items():
        print(f"{state} is abbreviated {abbrev}")

    print(separator)
    for abbrev, city in cities.items():
        print(f"{abbrev} has the city {city}")

    print(separator)
    for state, abbrev in states.items():
        print(f"{state} state is abbreviated {abbrev}", end=" ")
        print(f"and has city {cities[abbrev]}")

    print(separator)
    state = states.get("Texas")

    if not state:
        print("Sorry, no Texas")

    city = cities.get("TX", "Does Not Exist")
    print(f"The city for the state 'TX' is {city}")


if __name__ == "__main__":
    main()