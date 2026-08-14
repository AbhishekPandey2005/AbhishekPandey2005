"""Generate Abhishek's light and dark GitHub profile SVGs."""

from __future__ import annotations

import calendar
import datetime as dt
import html
import json
import os
import urllib.request

USERNAME = "AbhishekPandey2005"
API = "https://api.github.com/graphql"

PORTRAIT = r"""::::::::::..:+===:...::-------=--=--=-:==-=----:..:.:+*==-:::::--==-:-==-:-::-==-:--=--=-:::::::::::
:::::::.:.:..++==-:::-------==-==-:===--==----:-::..:**===:-::--=----:------.:---:-==--:-:::::::::::
:::::::::.:..++=+=::----:---==--===-=:=--=--=-=-::::.**+==:--=--=----==-::::...:.::----:-:::::::::::
::::::---:-::=*++=:------:------=-------:--=--=-:-::.*#*++---===========--::.::..------:::::::::::::
::::::------:-*+++-----------::::--====::::---=-=---:*#*+=-:--=-=--=-=-===-:-::.:-:--==-:::::..:::::
::::------:.::*+++=-----------::::----:::--:-:-------+#*===---=---========----:--::=------::::::..::
:::------::.::+*++=-----------:::--:-:::--==+====----=#*===------=============--=-=-------::-::::::.
.:-----::-:.::+*+++:-----=---::::-=++***************+++++=+::----===============-------------:-::::.
:-----:--:-:::=*+++--:::------=*************************+++--:::-============-=---------------::::::
:----------:::-#+++::-.::--=+***###****##########*##***++*+++=---------=--=-------------------==+***
---------------**++-...::-**#########################***++++**+=--::-----:--:--------=+*############
---------::::-:**++=::::=*######################*######******+***++=-:.:--:-+*###############**+++==
--------::.:.::+#+++--=*########################*########**+++******++###%#########*+++=-:..:-------
-------:::::..:=#+++=+##############################*######*++++******+***++==-----:::.......:------
-------::...:::-#*++*#########%###############%############***+++*******+:....::---::.........:---=-
--------:.....::*+*############%%%%%%%%%#%##############*#******++*******=:...::::::..........::----
---------:....::=*#####%#%#%%#%%%%%%%%%%%%%%%%%#############*#*****+******-::..:--:............::::-
---------::...::=*#####%%%%%%%%%%%%%%%%%%%%%%%%%%###############**********=---:::::::...........:::-
---------==++****####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%######*###*********=-===---:::::........:::-=
==+*#######**++##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%#%########*#*###****#**+=-----=--:::-:......:::--
#**++=----::::=#%%%%#%%%%%%%%######%%%%%%%%##%%%###%######%###*#*#*****#***=----:--------::::..:---=
:::::------:::+#%%%%%%%%%%%%#####################%##%%##%##%#######**##****+--=-----=-=----------===
::::::-----::-+%%%%%%%%%%%%###################*######%%#####%#############*+=====--==========--=====
::------------=#%%%%%%%%%%%#####*****************#####%#####%%#######*####*====-----=-============--
::-------------+%%%%%%%%%%#####******+++++++++++*****#####*####*##########*=========-===-===----=-==
::-------------=%%%%%%%%%#*###***++++++=====+====++************+*#**######+================+=====--=
::-------------=#%%%%%%##********++++++=============+==++===+++++*==*####*======--======+==+===-====
::--------------*%%%%%#**##############**+++++=================---::+####+=======--=====+++=++======
:::--------------*%%%#**+#############%%%##**+++====+++*******++=--:-###*==============+++++=+=====+
:::---------------#%%*+***#######****########**++=++****####****+++==*#*=+=======-=========+=++==+=+
:::-----=---------=##%##*########*****########%##**#+++*****++++++==-+++==+=============++=++++==++*
:::------------=###%%****###%%%##%%%##########*++=**++*#####**++++=---=#+++++===========+++++++====*
::::-----------+#####+*#*###%%####%%#**######*+=-==#=+***#%#*=-+*++---=*=++==============++++*++===+
::::-----------**###*+*############******####+=---++*=+*****+====------*=++++===-========++++=++=+++
::::-----------+#*##*+*#******************#**+=-::-=+-==++**++==--:::-=+=+++++===========+++++++==++
-::::---=-------*###*******++++++++++++**##**+--:::--+---===-----::::-*==+++++=====++++==++*+*+===++
=::::--==-------=###*******##*++++++++*###**+==-:::---=---------::::-*===+++++===+=+++==+++*+++==++*
+::::-===--------*###*******+++++++++**#****+=--:::--==------:---::::=====++++===+=+===++++**+*+++++
*:::::-----------*###*********+++++++*#*++**+==-::::::===------:::--:++==-+=+--=::----=====+++=+====
#-::::-----------*##%#********+++++++*#*****++==-::::::===------::---*+===+==--:::::..:-:::=+:.:==::
#=::::-----------*##%#*#*##****++++++*#%#####*++====+=--==----------=**+++==---:::::::::::::::::::::
#+::::------------=+*######*****++++**#######****+==-::-------------=+#**++--:::::::::::::::::::::::
##-:::--------------+#######*******+**#######**#*+==---::----------=+-+#**+=:::::.::::::::::::::::::
##=::::--==---------=#########******##%%%##*++++==--====----------===-=*#*+=::::::::::::::::::::::::
*#+::::=====---------=#############%%########**+****+==+++=------=-===-=***=-:::::::::::::::::::::::
**+-:::-===-----------+##############%%%%#####***********+++----===********+=::::::::::::::::::::::-
==-----:---------------############**#####*+======----=+**+==--===:.::::-=+=:-::::::::::::::::::::::
---------:::::::::-----*############**#####**++++========++======-:.:::.::::-:::-::::::::::::-::::::
:::::::::::::::::-==-:-=##############*###########**++====+=====:....:::::::::-:-:::::::::::-:::::::
::::::::::::-==-::::::+%@@%#############*********++++++++=====+**+::::-=-:::-:::-:---:--:..:::::::::
:::-:::-==-:::::-+*###%@@@%#%#########*******+++==--=========+***##++++**+-:::-:--------:::::::::-::
****==-::::=**#####%%%@@@@@##%%######*********++===----=-==+#****#%#**+++++++=:----------:-:::-:---:
*******+*#######%%@%%@@@@@@%##%%%#######*#******++=======++#*****#%#**++++++++++=---------:---------
***++*#%%#%#%%%%@@%%@@@@@@%%%%%%%%%%%%%%%####*****++****++##*#*###%#**+++++++++++++----------::--=-:
+++*#%%%%%%%%%%@@%%@@@@@@%%%%%%%%%%%%%%%%%%%%%#%%####*++*%#######%%#**+++++++++++++++==::::---::-=--
*#%%%%%%%%%%@@@@@%@@%@@@%%%%%%%%%%#######%%%%#####**++*%%#######%%##**++++++++++++++++++=-:::::::::-
%%%%%%%%%%%@@@@@%%@@@@@@%%%%%%%%%############*******#%%%#######%%%##*********++++++++++++***+-::::::
%%%%%%%%%@@@@@@%%%@@@@@%%%%%%%%%###################%%@%#####%%%%%%%#************++++++**+******+--::
%%%%%%%@@@@@@@@%@%%@@@%%##%####%%################%%@%#####%%%%%%@%%#************++++*+**+##********+
%%%%%%@@@@@@@@%%%%@@@@%#########################%%@%%####%%%%%%%@%%#**####*********+*+*******#**#*++
@%%%@@@@@@@@@%%%%@@@@@#####****####*******######@@%#######%%%%%%@%%#########********#****##*********
%%%@@@@@@@@@@%%%@@@@@@%#*#******************###@@%#%#####%%%##%@@%%##############***#*##*#*###******
%%@@@@@@@@@@@%%%%%%@@@###*******************#%%%%#######%%%%%%%@@%%###############**#*##*##*#*##****
%@@@@@@@@@@@@@%%%@@@@%#%#******************#@@@%#######%###%%%%@@%%###############**%#%#########**#*
@%@@@@@@@@@@@%%%%%@@@*%@#****************#%%%@@@@@####%##%%##%%@@@%################*######%%######**
@@@@@@@@@@@@@%%%%%%@%+@@@#***********#%@@@%%@@@@@@@@@%%##%%%#%%@@@@%###############*%%%%##%#########
@@@@@@@@@@@@@@@%%%%%+%@@@@#*******@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@%##%#####%%%####*#%%%%#%%%%#%####
@@@@@@@@@@@@@@@@@@%+#%@@@@@*****#@@@@@@@@@@@@@%@@@@@@@@@@@@@@%@@@@@%##%#%%%%%##%%%%##%#%##%%%%%#%%%#
@@@@@@@@@@@@@@@@@@@@@%@@@@@%***#@@@@@@@@@%@@@@%@@@@@@%%%@@@@%%@@@@@%%%%%%%%%%%%%%%%%#@%%%#%%%%%%%%#%
@@@@@@@@@@@@@@@@@@@@@%@%@@@%**#@@@@@@@@@%@@@@%%@@@@@%%%%@@@@%%@@@@@%%%%%%%%%%%%%%%%%##%%%%%%%%%%%%%%
@@@@@@@@@@@@@@@@@@@@@@%%@@%%%*%@@@@@@@%%@@@@%%@@@@@@%%%%@@@@%%@@@@@@%%%%%%%%%%%%%%%%%#%%%%%@%%%%%%%%
@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%@@@@@@@%%@@@@%%%@@@@@@%%%%@@@@%%@%@@@@%%%%%%%%%%%%%%%%%%@@%%%@@@%%%%%%
@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@@@@%@@@@@%%%@@@@@@%%%%@@@@@@%%%@@@@%%%%%%%%%%%%%%%%%#%@@%%@@@%%%%%%
"""


def graphql(query: str, variables: dict) -> dict:
    token = os.environ.get("GH_STATS_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("Set GITHUB_TOKEN or GH_STATS_TOKEN before running profile.py")
    body = json.dumps({"query": query, "variables": variables}).encode()
    request = urllib.request.Request(
        API,
        data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)
    if result.get("errors"):
        raise RuntimeError(result["errors"])
    return result["data"]


def fetch_stats() -> dict[str, int | str]:
    query = """
    query($login: String!, $cursor: String) {
      user(login: $login) {
        createdAt
        followers { totalCount }
        repositories(first: 100, after: $cursor, ownerAffiliations: OWNER) {
          totalCount
          nodes { stargazerCount }
          pageInfo { hasNextPage endCursor }
        }
      }
    }
    """
    stars = 0
    cursor = None
    created_at = ""
    followers = repos = 0
    while True:
        user = graphql(query, {"login": USERNAME, "cursor": cursor})["user"]
        created_at = user["createdAt"]
        followers = user["followers"]["totalCount"]
        repo_data = user["repositories"]
        repos = repo_data["totalCount"]
        stars += sum(repo["stargazerCount"] for repo in repo_data["nodes"])
        if not repo_data["pageInfo"]["hasNextPage"]:
            break
        cursor = repo_data["pageInfo"]["endCursor"]

    contributions = 0
    start_year = int(created_at[:4])
    contribution_query = """
    query($login: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $login) {
        contributionsCollection(from: $from, to: $to) {
          contributionCalendar { totalContributions }
        }
      }
    }
    """
    now = dt.datetime.now(dt.timezone.utc)
    for year in range(start_year, now.year + 1):
        start = dt.datetime(year, 1, 1, tzinfo=dt.timezone.utc)
        end = min(dt.datetime(year, 12, 31, 23, 59, 59, tzinfo=dt.timezone.utc), now)
        data = graphql(
            contribution_query,
            {"login": USERNAME, "from": start.isoformat(), "to": end.isoformat()},
        )
        contributions += data["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    return {"repos": repos, "stars": stars, "followers": followers, "contributions": contributions}


def age_string() -> str:
    raw = os.environ.get("BIRTH_DATE", "")
    if not raw:
        return "Set BIRTH_DATE secret"
    born = dt.date.fromisoformat(raw)
    today = dt.date.today()
    years = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    anniversary_year = born.year + years
    anniversary_day = min(born.day, calendar.monthrange(anniversary_year, born.month)[1])
    anniversary = dt.date(anniversary_year, born.month, anniversary_day)
    months = 0
    cursor = anniversary
    while True:
        month = cursor.month % 12 + 1
        year = cursor.year + (cursor.month // 12)
        day = min(cursor.day, calendar.monthrange(year, month)[1])
        candidate = dt.date(year, month, day)
        if candidate > today:
            break
        cursor = candidate
        months += 1
    days = (today - cursor).days
    cake = " 🎂" if today.month == born.month and today.day == born.day else ""
    return f"{years} years, {months} months, {days} days{cake}"


def svg(theme: dict[str, str], stats: dict[str, int | str]) -> str:
    portrait_lines = "\n".join(
        f'<tspan x="10" y="{9 + i * 7.5}">{html.escape(line)}</tspan>'
        for i, line in enumerate(PORTRAIT.splitlines())
    )
    rows = [
        ("OS", "Windows 11 · Linux · Android"),
        ("Uptime", age_string()),
        ("Host", "Computer Science Undergraduate"),
        ("Focus", "AI/ML · Full-Stack · Cybersecurity"),
        ("Languages", "Python · JavaScript · C/C++ · Java"),
        ("AI", "RAG · LangChain · Machine Learning"),
        ("Web", "React.js · Node.js · Express.js · MongoDB"),
        ("Currently", "Building intelligent applications"),
    ]
    info = []
    for i, (key, value) in enumerate(rows):
        y = 55 + i * 25
        info.append(
            f'<tspan x="450" y="{y}" class="muted">. </tspan>'
            f'<tspan class="key">{html.escape(key)}</tspan>: '
            f'<tspan class="value">{html.escape(value)}</tspan>'
        )
    contact = [
        ("Email", "abhi992005@gmail.com"),
        ("LinkedIn", "abhishek-pandey-6169aa293"),
        ("X", "@Abhishekthepiro"),
        ("Portfolio", "https://abhishekpandeyy.netlify.app/"),
    ]
    contacts = []
    for i, (key, value) in enumerate(contact):
        y = 305 + i * 25
        contacts.append(
            f'<tspan x="450" y="{y}" class="muted">. </tspan>'
            f'<tspan class="key">{html.escape(key)}</tspan>: '
            f'<tspan class="value">{html.escape(value)}</tspan>'
        )
    stats_text = [
        f'<tspan x="450" y="480" class="muted">. </tspan><tspan class="key">Repositories</tspan>: <tspan class="value">{stats["repos"]:,}</tspan>  |  <tspan class="key">Stars earned</tspan>: <tspan class="value">{stats["stars"]:,}</tspan>',
        f'<tspan x="450" y="505" class="muted">. </tspan><tspan class="key">Contributions</tspan>: <tspan class="value">{stats["contributions"]:,}</tspan>  |  <tspan class="key">Followers</tspan>: <tspan class="value">{stats["followers"]:,}</tspan>',
        f'<tspan x="450" y="530" class="muted">. </tspan><tspan class="key">Profile</tspan>: <tspan class="value">github.com/{USERNAME}</tspan>',
    ]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="560" viewBox="0 0 1100 560" role="img" aria-label="Abhishek Pandey GitHub profile">
<style>
  .bg {{ fill: {theme['bg']}; }}
  text {{ font: 16px Consolas, "Liberation Mono", monospace; fill: {theme['text']}; white-space: pre; }}
  .portrait {{ font-size: 6.8px; letter-spacing: 0; fill: {theme['portrait']}; }}
  .key {{ fill: {theme['key']}; font-weight: 700; }}
  .value {{ fill: {theme['value']}; }}
  .muted {{ fill: {theme['muted']}; }}
</style>
<rect class="bg" width="1100" height="560" rx="16"/>
<text class="portrait">{portrait_lines}</text>
<text>
  <tspan x="450" y="25" class="key">abhishek@pandey</tspan><tspan> ─────────────────────────────────────</tspan>
  {''.join(info)}
  <tspan x="450" y="270">─ Contact ─────────────────────────────────────────</tspan>
  {''.join(contacts)}
  <tspan x="450" y="445">─ GitHub Stats ────────────────────────────────────</tspan>
  {''.join(stats_text)}
</text>
</svg>'''


def main() -> None:
    stats = (
        {"repos": 8, "stars": 1, "followers": 8, "contributions": 131}
        if os.environ.get("PROFILE_PREVIEW") == "1"
        else fetch_stats()
    )
    themes = {
        "light_mode.svg": {"bg": "#f6f8fa", "text": "#24292f", "portrait": "#57606a", "key": "#953800", "value": "#0a3069", "muted": "#afb8c1"},
        "dark_mode.svg": {"bg": "#0d1117", "text": "#c9d1d9", "portrait": "#8b949e", "key": "#ffa657", "value": "#58a6ff", "muted": "#30363d"},
    }
    for filename, theme in themes.items():
        with open(filename, "w", encoding="utf-8") as output:
            output.write(svg(theme, stats))


if __name__ == "__main__":
    main()
