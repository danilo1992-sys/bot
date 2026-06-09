import requests

MATCH = "https://worldcupfixtureapi.com/api/matches"
TODAY = "https://worldcupfixtureapi.com/api/matches/today"
TEAM = "https://worldcupfixtureapi.com/api/teams"
GROUP = "https://worldcupfixtureapi.com/api/groups/"


def match():
    response = requests.get(MATCH)
    response.raise_for_status()
    data = response.json()
    for m in data["matches"]:
        home = m["homeTeam"]["name"]
        away = m["awayTeam"]["name"]
        date = m["kickoff"]["local"]["date"]
        time = m["kickoff"]["local"]["time"]
        group = m.get("group", "")
        print(f"{date} {time} | {home} vs {away} | Grupo {group}")


def teams():
    response = requests.get(TEAM)
    response.raise_for_status()
    data = response.json()
    for t in data["teams"]:
        name = t["name"]
        code = t["code"]
        group = t["groups"][0]


if __name__ == "__main__":
    match()
    teams()
