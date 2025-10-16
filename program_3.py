# Program #3: US_Population, Griffin Corniea, 10/14/25
def main():

    all_values = []

    print("Enter state population data. Type 'done' when finished.\n")

    while True:
        year_input = input("Enter year (or 'done' to stop): ")
        if year_input.lower() == "done":
            break

        year = int(year_input)
        state = input("Enter state name: ")
        population = int(input("Enter population: "))

        all_values.append([year, state, population])

    if not all_values:
        print("\nNo data entered. Exiting program.")
        return

    year_to_sum = int(input("\nEnter a year to calculate total U.S. population: "))
    sum_population_for_year(all_values, year_to_sum)


def sum_population_for_year(all_entered_values, year_to_sum):
    total = 0
    for entry in all_entered_values:
        year, state, population = entry
        if year == year_to_sum:
            total += population

    print(f"\nTotal population for {year_to_sum}: {total:,}")


if __name__ == '__main__':
    main()