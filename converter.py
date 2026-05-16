"""
Unit converter CLI - supports multiple unit categories.
"""
import argparse
import sys

CONVERSIONS = {
    "c2f": ("Celsius", "Fahrenheit", lambda x: x * 9/5 + 32),
    "f2c": ("Fahrenheit", "Celsius", lambda x: (x - 32) * 5/9),
    "c2k": ("Celsius", "Kelvin", lambda x: x + 273.15),
    "k2c": ("Kelvin", "Celsius", lambda x: x - 273.15),
    "km2mi": ("Kilometers", "Miles", lambda x: x * 0.621371),
    "mi2km": ("Miles", "Kilometers", lambda x: x / 0.621371),
    "m2ft": ("Meters", "Feet", lambda x: x * 3.28084),
    "ft2m": ("Feet", "Meters", lambda x: x / 3.28084),
    "cm2in": ("Centimeters", "Inches", lambda x: x / 2.54),
    "in2cm": ("Inches", "Centimeters", lambda x: x * 2.54),
    "kg2lb": ("Kilograms", "Pounds", lambda x: x * 2.20462),
    "lb2kg": ("Pounds", "Kilograms", lambda x: x / 2.20462),
    "g2oz": ("Grams", "Ounces", lambda x: x / 28.3495),
    "oz2g": ("Ounces", "Grams", lambda x: x * 28.3495),
    "l2gal": ("Liters", "Gallons", lambda x: x * 0.264172),
    "gal2l": ("Gallons", "Liters", lambda x: x / 0.264172),
    "ml2floz": ("Milliliters", "Fl Ounces", lambda x: x / 29.5735),
    "floz2ml": ("Fl Ounces", "Milliliters", lambda x: x * 29.5735),
    "sqm2sqft": ("Sq Meters", "Sq Feet", lambda x: x * 10.7639),
    "sqft2sqm": ("Sq Feet", "Sq Meters", lambda x: x / 10.7639),
    "ha2ac": ("Hectares", "Acres", lambda x: x * 2.47105),
    "ac2ha": ("Acres", "Hectares", lambda x: x / 2.47105),
}

def convert(conversion, value, precision=4):
    if conversion not in CONVERSIONS:
        return None
    from_u, to_u, func = CONVERSIONS[conversion]
    result = func(value)
    return round(result, precision)

def list_conversions():
    print("Available conversions:\n")
    for key in sorted(CONVERSIONS.keys()):
        from_u, to_u, _ = CONVERSIONS[key]
        print(f"  {key:<12} {from_u} -> {to_u}")

def main():
    parser = argparse.ArgumentParser(description="Unit Converter")
    subparsers = parser.add_subparsers(dest="command")

    conv_p = subparsers.add_parser("convert", help="Convert a value")
    conv_p.add_argument("type", help="Conversion type (e.g., c2f, km2mi)")
    conv_p.add_argument("value", type=float, help="Value to convert")
    conv_p.add_argument("-p", "--precision", type=int, default=4, help="Decimal places")

    list_p = subparsers.add_parser("list", help="List conversions")

    args = parser.parse_args()

    if args.command == "convert":
        result = convert(args.type, args.value, args.precision)
        if result is None:
            print(f"Unknown conversion: {args.type}", file=sys.stderr)
            sys.exit(1)
        from_u, to_u, _ = CONVERSIONS[args.type]
        print(f"{args.value} {from_u} = {result} {to_u}")
    elif args.command == "list":
        list_conversions()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
