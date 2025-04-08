# devrock on top
import sys
import time
import subprocess
import os
from rich.console import Console
from rich.panel import Panel

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_screen():
    clear()
    console.print(Panel.fit(
        "[bold magenta]🚀 RockCloner v1.0.1[/bold magenta]\n[green]Launching... Please wait[/green]",
        border_style="magenta"
    ))
    time.sleep(2)

def launch_cloner():
    # Re-run THIS script with an extra argument to skip the loading screen
    subprocess.call([sys.executable, __file__, "run"])

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        import rockcloner
        rockcloner.main()
    else:
        loading_screen()
        launch_cloner()

if __name__ == "__main__":
    main()
