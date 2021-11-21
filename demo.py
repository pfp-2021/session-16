from time import sleep
from rich import status
from rich.console import Console

console = Console()

with console.status("[magenta]this is doing some cool stuff") as status:
    sleep(1)
    console.log("doing some more fancy things")
    sleep(1)
    status.update("[blue] this is other message", spinner="earth")
    sleep(1)
    status.update("[green] this is other message", spinner="earth")
    sleep(1)
    status.update("[yellow] this is other message", spinner="earth")
    sleep(3)