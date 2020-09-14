import fire


def hello(name="world"):
    return f"Hello {name}"

# python cli_fire.py  # Hello World!
# python cli_fire.py --name=David  # Hello David!


if __name__ == "__main__":
    fire.Fire(hello)
