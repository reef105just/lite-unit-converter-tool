"""
Unit converter - supports temperature, distance, weight, volume, and area.
"""

CONVERSIONS = {
    # Temperature
    "c2f": ("Celsius", "Fahrenheit", lambda x: x * 9/5 + 32),
    "f2c": ("Fahrenheit", "Celsius", lambda x: (x - 32) * 5/9),
    "c2k": ("Celsius", "Kelvin", lambda x: x + 273.15),
    "k2c": ("Kelvin", "Celsius", lambda x: x - 273.15),
    # Distance
    "km2mi": ("Kilometers", "Miles", lambda x: x * 0.621371),
    "mi2km": ("Miles", "Kilometers", lambda x: x / 0.621371),
    "m2ft": ("Meters", "Feet", lambda x: x * 3.28084),
    "ft2m": ("Feet", "Meters", lambda x: x / 3.28084),
    "cm2in": ("Centimeters", "Inches", lambda x: x / 2.54),
    "in2cm": ("Inches", "Centimeters", lambda x: x * 2.54),
    # Weight
    "kg2lb": ("Kilograms", "Pounds", lambda x: x * 2.20462),
    "lb2kg": ("Pounds", "Kilograms", lambda x: x / 2.20462),
    "g2oz": ("Grams", "Ounces", lambda x: x / 28.3495),
    "oz2g": ("Ounces", "Grams", lambda x: x * 28.3495),
    # Volume
    "l2gal": ("Liters", "Gallons", lambda x: x * 0.264172),
    "gal2l": ("Gallons", "Liters", lambda x: x / 0.264172),
    "ml2floz": ("Milliliters", "Fluid Ounces", lambda x: x / 29.5735),
    "floz2ml": ("Fluid Ounces", "Milliliters", lambda x: x * 29.5735),
    # Area
    "sqm2sqft": ("Sq Meters", "Sq Feet", lambda x: x * 10.7639),
    "sqft2sqm": ("Sq Feet", "Sq Meters", lambda x: x / 10.7639),
    "ha2ac": ("Hectares", "Acres", lambda x: x * 2.47105),
    "ac2ha": ("Acres", "Hectares", lambda x: x / 2.47105),
}

def convert(conversion, value):
    if conversion not in CONVERSIONS:
        print(f"Unknown conversion: {conversion}")
        print(f"Available: {', '.join(sorted(CONVERSIONS.keys()))}")
        return None
    from_u, to_u, func = CONVERSIONS[conversion]
    result = func(value)
    return result

def list_conversions():
    categories = {"Temperature": [], "Distance": [], "Weight": [], "Volume": [], "Area": []}
    cat_map = {
        "c2f": "Temperature", "f2c": "Temperature", "c2k": "Temperature", "k2c": "Temperature",
        "km2mi": "Distance", "mi2km": "Distance", "m2ft": "Distance", "ft2m": "Distance",
        "cm2in": "Distance", "in2cm": "Distance",
        "kg2lb": "Weight", "lb2kg": "Weight", "g2oz": "Weight", "oz2g": "Weight",
        "l2gal": "Volume", "gal2l": "Volume", "ml2floz": "Volume", "floz2ml": "Volume",
        "sqm2sqft": "Area", "sqft2sqm": "Area", "ha2ac": "Area", "ac2ha": "Area",
    }
    for key, cat in cat_map.items():
        from_u, to_u, _ = CONVERSIONS[key]
        categories[cat].append(f"  {key:<12} {from_u} -> {to_u}")
    for cat, items in categories.items():
        print(f"\n{cat}:")
        for item in items:
            print(item)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1 or sys.argv[1] == "list":
        list_conversions()
    elif len(sys.argv) == 3:
        result = convert(sys.argv[1], float(sys.argv[2]))
        if result is not None:
            from_u, to_u, _ = CONVERSIONS[sys.argv[1]]
            print(f"{float(sys.argv[2])} {from_u} = {result:.4f} {to_u}")
