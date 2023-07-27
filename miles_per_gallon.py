def calc_mpg(miles, gallons):
    """Calculate miles per gallon for a single trip"""
    if gallons == 0:
        return 0.0
    return miles / gallons

def calc_total_mpg(total_miles, total_gallons):
    """Calculate combined miles per gallon for all trips"""
    if total_gallons == 0:
        return 0.0
    return total_miles / total_gallons

def main():
    total_miles = 0
    total_gallons = 0

    while True:
        miles_driven = int(input("Enter miles driven for the trip (or -1 to quit): "))
        if miles_driven == -1:
            break

        gallons_used = int(input("Enter gallons used for the trip: "))

        mpg = calc_mpg(miles_driven, gallons_used)
        total_miles += miles_driven
        total_gallons += gallons_used

        print(f"Miles per gallon for this trip: {mpg:.2f}")
        print(f"Combined miles per gallon for all trips: {calc_total_mpg(total_miles, total_gallons):.2f}\n")

if __name__ == "__main__":
    main()