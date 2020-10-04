import fire

def hellp(name="world"):
    return f"Hellp {name}"

# python cli_fire.py  # Hello World!
# python cli_fire.py --name=David  # Hello David!

if __name__ == "__main__":
    fire.Fire(hello)
