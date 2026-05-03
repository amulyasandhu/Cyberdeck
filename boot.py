import time
import os
from rich.console import Console
from rich.text import Text
from rich.align import Align

console = Console()

OPERATOR = "OREXIA"
VERSION = "2.1.7"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_out(text, color="green", delay=0.03):
    for char in text:
        console.print(char, style=color, end="")
        time.sleep(delay)
    print()

def fake_load(task, duration=1.2):
    console.print(f"  [cyan]>[/cyan] {task}", end="")
    steps = 20
    for i in range(steps):
        time.sleep(duration / steps)
        console.print(".", end="", style="green")
    console.print(" [bold green]OK[/bold green]")

def boot_sequence():
    clear()
    time.sleep(0.3)

    # ASCII logo
    logo = """
   ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██████╗ ███████╗ ██████╗██╗  ██╗
  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║ ██╔╝
  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║  ██║█████╗  ██║     █████╔╝ 
  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║  ██║██╔══╝  ██║     ██╔═██╗ 
  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║██████╔╝███████╗╚██████╗██║  ██╗
   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝
    """
    console.print(logo, style="bold green")
    console.print(Align.center(f"[dim]OS v{VERSION} — OPERATOR SYSTEM[/dim]"))
    console.print()
    time.sleep(0.5)

    # Boot messages
    type_out(f"  INITIALIZING CYBERDECK OS v{VERSION}...", "bold green", 0.04)
    console.print()
    time.sleep(0.3)

    fake_load("mounting file systems")
    fake_load("initializing neural interface")
    fake_load("scanning network nodes")
    fake_load("loading operator profile")
    fake_load("establishing secure channel")
    fake_load("calibrating sensors")

    console.print()
    time.sleep(0.4)

    type_out(f"  ACCESS GRANTED.", "bold green", 0.05)
    time.sleep(0.3)
    type_out(f"  WELCOME BACK, {OPERATOR}.", "bold cyan", 0.05)
    console.print()
    time.sleep(0.8)

import datetime
import requests

def get_weather():
    try:
        res = requests.get(
            "https://wttr.in/Chandigarh?format=%C+%t",
            timeout=5,
            headers={"User-Agent": "curl/7.68.0"}
        )
        res.encoding = 'utf-8'
        import re
        clean = re.sub(r'[^\x00-\x7F]+', '', res.text.strip())
        return clean.strip()
    except:
        return "weather: offline"
    
def get_quote():
    try:
        res = requests.get("https://api.quotable.io/random?tags=technology,science", timeout=3)
        data = res.json()
        return f'"{data["content"]}" — {data["author"]}'
    except:
        return '"Stay curious, stay dangerous." — CYBERDECK OS'
    
def loading_cat(message="LOADING", duration=2.5):
    frames = [
        r" /\_/\  ",
        r"( o.o ) ",
        r" > ^ <  ",
        r"/\_/\   ",
        r"( -.o ) ",
        r" > ^ <  ",
        r" /\_/\  ",
        r"( o.- ) ",
        r" > ^ <  ",
    ]

    cat_walk = [
        r"  /\_/\  ----",
        r" ( o.o )  ---",
        r"  > ^ <  ----",
        r"  /\_/\   ---",
        r" ( -.o )  ---",
        r"  > ^ <   ---",
    ]

    run_frames = [
        ["  /\\_/\\  ", " ( o.o ) ~", "  >>--> ~~ "],
        ["  /\\_/\\  ", " ( -.o ) ~", "  ~~-->  ~ "],
        ["  /\\_/\\  ", " ( o.- ) ~", "  >>-->~~  "],
        ["  /\\_/\\  ", " ( o.o ) ~", " ~~--> ~~  "],
    ]

    total_steps = 30
    bar_width = 30
    start = time.time()

    for step in range(total_steps + 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        progress = step / total_steps
        filled = int(bar_width * progress)
        bar = "█" * filled + "░" * (bar_width - filled)
        percent = int(progress * 100)

        # cat position across screen
        cat_pos = int(progress * 35)
        frame = run_frames[step % len(run_frames)]

        console.print()
        console.print()
        console.print(f"  [bold green]CYBERDECK OS v{VERSION}[/bold green]")
        console.print(f"  [dim]{message}[/dim]")
        console.print()

        # running cat
        for line in frame:
            console.print(f"  [white]{' ' * cat_pos}{line}[/white]")

        console.print()
        console.print(f"  [green][{bar}][/green] [cyan]{percent}%[/cyan]")
        console.print()

        elapsed = time.time() - start
        remaining_time = duration - elapsed
        if remaining_time <= 0:
            break
        time.sleep(duration / total_steps)

    os.system('cls' if os.name == 'nt' else 'clear')

def dashboard():
    clear()
    import re

    # show cat while fetching
    import threading
    results = {}

    def fetch():
        results['weather'] = get_weather()
        results['quote'] = get_quote()

    t = threading.Thread(target=fetch)
    t.start()
    loading_cat("FETCHING OPERATOR DATA...", duration=3.0)
    t.join()


    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%A, %d %B %Y")
    weather = get_weather()
    quote = get_quote()

    W = 52

    def row(content=""):
        visible = re.sub(r'\[.*?\]', '', content)
        padding = W - 2 - len(visible)
        if padding < 0:
            padding = 0
        console.print(f"  [bold green]║[/bold green] {content}{' ' * padding} [bold green]║[/bold green]")

    console.print()
    console.print(f"  [bold green]╔{'═' * W}╗[/bold green]")
    row(f"[bold cyan]CYBERDECK OS v{VERSION}[/bold cyan]  —  OPERATOR: [bold magenta]{OPERATOR}[/bold magenta]")
    console.print(f"  [bold green]╠{'═' * W}╣[/bold green]")
    # temperature color logic
    try:
        temp = int(''.join(filter(lambda c: c.isdigit() or c == '-', weather.split('+')[-1].split('C')[0])))
        temp_color = "red" if temp >= 28 else "cyan"
    except:
        temp_color = "yellow"

    row(f"[green]<t>[/green] [cyan]{time_str}[/cyan]  |  [dim]{date_str}[/dim]")
    row(f"[green]<w>[/green] [{temp_color}]{weather}[/{temp_color}]")
    console.print(f"  [bold green]╠{'═' * W}╣[/bold green]")
    row("[bold white]TASKS:[/bold white]")
    row("  ▸ finish cyberdeck OS")
    row("  ▸ push projects to github")
    row("  ▸ start research organizer idea")
    console.print(f"  [bold green]╠{'═' * W}╣[/bold green]")
    row("[bold white]QUOTE:[/bold white]")

    # wrap quote
    words = quote.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 > W - 4:
            row(f"[italic dim]{line.strip()}[/italic dim]")
            line = word + " "
        else:
            line += word + " "
    if line.strip():
        row(f"[italic dim]{line.strip()}[/italic dim]")

    console.print(f"  [bold green]╚{'═' * W}╝[/bold green]")
    console.print()
    console.print("  [dim]type [/dim][cyan]nexus[/cyan][dim] for commands | [/dim][cyan]exit[/cyan][dim] to shutdown[/dim]")
    console.print() 
def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except:
        return [
            "finish cyberdeck OS",
            "push projects to github",
            "start research organizer idea"
        ]

def cmd_flights():
    console.print()
    type_out("  SCANNING AIRSPACE...", "bold green", 0.03)
    time.sleep(0.5)
    try:
        # Chandigarh area coordinates
        lat1, lat2 = 30.5, 31.0
        lon1, lon2 = 76.5, 77.0
        res = requests.get(
            f"https://opensky-network.org/api/states/all?lamin={lat1}&lomin={lon1}&lamax={lat2}&lomax={lon2}",
            timeout=8
        )
        data = res.json()
        states = data.get("states", [])

        console.print()
        console.print("  [bold white]// AIRSPACE — CHANDIGARH SECTOR[/bold white]")
        console.print()

        if not states:
            console.print("  [dim]no aircraft detected in sector[/dim]")
        else:
            console.print(f"  [dim]callsign        country         alt(m)   speed[/dim]")
            console.print(f"  [dim]{'─'*48}[/dim]")
            for s in states[:8]:
                callsign = (s[1] or "UNKNOWN").strip() or "UNKNOWN"
                country  = (s[2] or "???")[:14]
                alt      = int(s[7]) if s[7] else 0
                speed    = int(s[9]) if s[9] else 0
                console.print(f"  [cyan]{callsign:<16}[/cyan][dim]{country:<16}{alt:<9}{speed} kts[/dim]")
        console.print()
    except:
        console.print()
        console.print("  [red]airspace feed offline[/red] — [dim]try again later[/dim]")
        console.print()
def cmd_news():
    console.print()
    type_out("  INTERCEPTING GLOBAL SIGNALS...", "bold green", 0.03)
    time.sleep(0.5)
    import xml.etree.ElementTree as ET

    feeds = [
        ("WORLD",       "https://feeds.bbci.co.uk/news/world/rss.xml"),
        ("TECH",        "https://feeds.bbci.co.uk/news/technology/rss.xml"),
        ("SCIENCE",     "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml"),
        ("BUSINESS",    "https://feeds.bbci.co.uk/news/business/rss.xml"),
        ("SPORT",       "https://feeds.bbci.co.uk/sport/rss.xml"),
    ]

    headlines = []
    for category, url in feeds:
        try:
            res = requests.get(url, timeout=5)
            root = ET.fromstring(res.content)
            items = root.findall('./channel/item')[:3]
            for item in items:
                title = item.find('title').text
                headlines.append((category, title))
        except:
            pass

    # thought of the day
    try:
        res = requests.get("https://api.quotable.io/random?tags=inspirational,wisdom", timeout=3)
        data = res.json()
        thought = f'"{data["content"]}" — {data["author"]}'
    except:
        thought = '"The people who are crazy enough to think they can change the world are the ones who do." — Steve Jobs'

    console.print()
    console.print("  [bold white]// GLOBAL FEED[/bold white]")
    console.print()

    current_cat = ""
    count = 0
    for category, title in headlines[:12]:
        if category != current_cat:
            if current_cat != "":
                console.print()
            console.print(f"  [bold green][ {category} ][/bold green]")
            current_cat = category
        console.print(f"  [dim]▸[/dim] {title}")
        count += 1

    console.print()
    console.print("  [bold green][ THOUGHT OF THE DAY ][/bold green]")
    console.print(f"  [italic dim]{thought}[/italic dim]")
    console.print()
def command_loop():
    tasks = load_tasks()
    while True:
        try:
            cmd = console.input("  [bold green]OREXIA@cyberdeck[/bold green][cyan]>[/cyan] ").strip().lower()

            if cmd == "exit":
                console.print()
                type_out("  SHUTTING DOWN CYBERDECK OS...", "bold red", 0.04)
                time.sleep(0.3)
                fake_load("saving operator state")
                fake_load("closing secure channels")
                fake_load("powering down")
                console.print()
                type_out("  GOODBYE, OREXIA.", "bold cyan", 0.05)
                console.print()
                break

            elif cmd == "clear":
                dashboard()

            elif cmd == "nexus":
                console.print()
                console.print("  [bold green] /|\\  ^._.^  /|\\ [/bold green]  [dim]i know the way[/dim]")
                console.print()
                console.print("  [bold white]// NEXUS[/bold white]")
                console.print()
                console.print("  [cyan]tasks[/cyan]    — manage tasks")
                console.print("  [cyan]news[/cyan]     — global headlines")
                console.print("  [cyan]scan[/cyan]     — network scan")
                console.print("  [cyan]ghost[/cyan]    — ghost protocol")
                console.print("  [cyan]signal[/cyan]   — incoming signal")
                console.print("  [cyan]mission[/cyan]  — mission briefing")
                console.print("  [cyan]flights[/cyan]  — live departures")
                console.print("  [cyan]log[/cyan]      — system log")
                console.print("  [cyan]exit[/cyan]     — shutdown")
                console.print()
            elif cmd == "tasks":
                console.print()
                console.print("  [bold white]// TASKS[/bold white]")
                console.print()
                for i, task in enumerate(tasks, 1):
                    console.print(f"  [cyan]{i}.[/cyan] {task}")
                console.print()
                console.print("  [dim]add <task>  |  done <number>  |  edit <number> <new>[/dim]")
                console.print()

            elif cmd.startswith("add "):
                new_task = cmd[4:].strip()
                if new_task:
                    tasks.append(new_task)
                    save_tasks(tasks)
                    console.print(f"  [green]task added:[/green] {new_task}")
                    console.print()

            elif cmd.startswith("done "):
                try:
                    idx = int(cmd[5:].strip()) - 1
                    if 0 <= idx < len(tasks):
                        removed = tasks.pop(idx)
                        save_tasks(tasks)
                        console.print(f"  [green]completed:[/green] [dim]{removed}[/dim]")
                        console.print()
                    else:
                        console.print("  [red]invalid task number[/red]")
                        console.print()
                except:
                    console.print("  [red]usage: done <number>[/red]")
                    console.print()

            elif cmd.startswith("edit "):
                try:
                    parts = cmd[5:].strip().split(" ", 1)
                    idx = int(parts[0]) - 1
                    new_text = parts[1].strip()
                    if 0 <= idx < len(tasks):
                        old = tasks[idx]
                        tasks[idx] = new_text
                        save_tasks(tasks)
                        console.print(f"  [green]updated:[/green] [dim]{old}[/dim] → {new_text}")
                        console.print()
                    else:
                        console.print("  [red]invalid task number[/red]")
                        console.print()
                except:
                    console.print("  [red]usage: edit <number> <new task>[/red]")
                    console.print()
            elif cmd == "news":
                cmd_news()
            elif cmd == "flights":
                cmd_flights()

            elif cmd == "":
                pass
            elif cmd == "":
                pass

            else:
                console.print(f"  [red]unknown command:[/red] [dim]{cmd}[/dim] — type [cyan]nexus[/cyan] for commands")
                console.print()

           

        except KeyboardInterrupt:
            console.print()
            type_out("  GOODBYE, OREXIA.", "bold cyan", 0.05)
            console.print()
            break
if __name__ == "__main__":
    boot_sequence()
    dashboard()
    command_loop()