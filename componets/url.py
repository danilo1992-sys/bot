import requests
from datetime import datetime
from componets.utils import flag

MATCH = "https://worldcupfixtureapi.com/api/matches"
TEAM = "https://worldcupfixtureapi.com/api/teams"
GROUP = "https://worldcupfixtureapi.com/api/groups"


def get_groups(group=None):
    response = requests.get(GROUP)
    response.raise_for_status()
    data = response.json()
    grouped = {}
    for g in data["groups"]:
        name = g["name"]
        if group and group.upper() not in name.upper():
            continue
        teams_list = g.get("teams") or []
        if not teams_list:
            continue
        for t in teams_list:
            grouped.setdefault(name, []).append(f"{flag(t['code'])} {t['name']}")
    result = []
    for g in sorted(grouped):
        lines = [f"⚽ {g}"] + grouped[g]
        result.append((g, "\n".join(lines)))
    return result


def match(group=None):
    response = requests.get(MATCH)
    response.raise_for_status()
    data = response.json()
    grouped = {}
    for m in data["matches"]:
        home = m["homeTeam"]["name"]
        away = m["awayTeam"]["name"]
        date = datetime.strptime(m["kickoff"]["local"]["date"], "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        time = m["kickoff"]["local"]["time"]
        g = m.get("group") or ""
        if not g:
            continue
        if group and g.upper() != group.upper():
            continue
        grouped.setdefault(g, []).append(f"{date} {time} | {home} vs {away}")
    result = []
    for g in sorted(grouped):
        lines = [f"⚽ Grupo {g}"] + grouped[g]
        result.append((g, "\n".join(lines)))
    return result


def teams(team=None):
    response = requests.get(TEAM)
    response.raise_for_status()
    data = response.json()
    grouped = {}
    for t in data["teams"]:
        name = t["name"]
        code = t["code"]
        g = t["groups"][0]
        if team and team.lower() not in name.lower():
            continue
        grouped.setdefault(g, []).append(f"{flag(code)} {name}")
    result = []
    for g in sorted(grouped):
        lines = [f"⚽ Grupo {g}"] + grouped[g]
        result.append((g, "\n".join(lines)))
    return result


if __name__ == "__main__":
    match()
    teams()
    get_groups()
