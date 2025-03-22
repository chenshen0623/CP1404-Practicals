from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Load existing guitars and get new guitars, display all guitars in order, then save to file."""
    guitars = load_guitars(FILENAME)
    new_guitars = get_guitars()
    guitars += new_guitars
    guitars.sort()

