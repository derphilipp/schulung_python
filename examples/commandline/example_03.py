import click
import time


def fake_ping(address):
    click.echo(f"Ping sent to {address}... ")
    time.sleep(1)


@click.command()
@click.option("--count", default=1, help="How many pings to send.")
@click.option("--address", prompt="IP address", help="IP address to send the ping to.")
def hello(count, address):
    """Programm to send a ping"""
    for x in range(count):
        fake_ping(address)


if __name__ == "__main__":
    hello()
