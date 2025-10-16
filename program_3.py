# Program #3: US_Population, Griffin Corniea, 10/14/25
def main():

    all_entered_values = []

    print("Enter state population data. Type 'done' when finished.\n")

    while True:
        year_input = input("Enter year (or 'done' to stop): ")
        if year_input.lower() == "done":
            break

        try:
            year = int(year_input)
        except ValueError:
            print("Please enter a valid year")
            continue

        state = input("Enter state name: ")
        pop_input = input("Enter population: ")

        try:
            population = int(pop_input)
        except ValueError:
            print("Population must be an integer.")
            continue

        all_entered_values.append([year, state, population])

    if not all_entered_values:
        print("\nNo data entered. Exiting program.")
        return

    year_to_sum_input = input("\nEnter a year to calculate total U.S. population: ")
    try:
        year_to_sum = int(year_to_sum_input)
    except ValueError:
        print("Invalid year entered.")
        return

    sum_population_for_year(all_entered_values, year_to_sum)




def sum_population_for_year(all_entered_values, year_to_sum):
    total = 0
    for entry in all_entered_values:
        year, state, population = entry
        if year == year_to_sum:
            total += population

    print(f"\nTotal population for {year_to_sum}: {total:,}")


if __name__ == '__main__':
    main()