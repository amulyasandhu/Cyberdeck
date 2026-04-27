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

    weather = results.get('weather', 'offline')
    quote = results.get('quote', '"Stay curious, stay dangerous." — CYBERDECK OS')

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
def command_loop():
    tasks = [
        "finish cyberdeck OS",
        "push projects to github",
        "start research organizer idea"
    ]

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
                
                console.print("    [bold white]CURRENT TASKS[/bold white]               ")
                console.print()
                for i, task in enumerate(tasks, 1):
                    padding = 27 - len(task)
                    if padding < 0:
                        padding = 0
                    console.print(f"   [cyan]{i}.[/cyan] {task}{' ' * padding} ")
                console.print()

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