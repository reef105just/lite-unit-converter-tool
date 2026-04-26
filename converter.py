def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs / 2.20462

if __name__ == "__main__":
    print("Unit Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. KM to Miles")
    print("4. Miles to KM")
    print("5. KG to LBS")
    print("6. LBS to KG")

    choice = input("\nSelect (1-6): ")
    value = float(input("Enter value: "))

    funcs = {
        "1": ("Celsius", "Fahrenheit", celsius_to_fahrenheit),
        "2": ("Fahrenheit", "Celsius", fahrenheit_to_celsius),
        "3": ("KM", "Miles", km_to_miles),
        "4": ("Miles", "KM", miles_to_km),
        "5": ("KG", "LBS", kg_to_lbs),
        "6": ("LBS", "KG", lbs_to_kg),
    }

    if choice in funcs:
        from_u, to_u, func = funcs[choice]
        result = func(value)
        print(f"\n{value} {from_u} = {result:.2f} {to_u}")
