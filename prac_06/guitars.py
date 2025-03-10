from prac_06.guitar import Guitar

print("My guitars!")

guitars = []
name = input("Name: ")
while name != '':
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $"))
    guitar = Guitar(name, guitar_year, guitar_cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    print()
    name = input("Name: ")

print("\n... snip ...\n")

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name} ({guitar.year}), "
            f"worth ${guitar.cost:,.2f}{vintage_string}")

