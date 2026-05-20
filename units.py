"""
Conversion registry and utilities.
"""

class ConversionRegistry:
    """Registry of unit conversions."""

    def __init__(self):
        self._conversions = {}
        self._categories = {}

    def register(self, key, from_unit, to_unit, func, category="Other"):
        self._conversions[key] = (from_unit, to_unit, func)
        if category not in self._categories:
            self._categories[category] = []
        self._categories[category].append(key)

    def convert(self, key, value):
        if key not in self._conversions:
            raise KeyError(f"Unknown conversion: {key}")
        _, _, func = self._conversions[key]
        return func(value)

    def get_info(self, key):
        if key not in self._conversions:
            return None
        from_u, to_u, _ = self._conversions[key]
        return from_u, to_u

    def list_all(self):
        return dict(self._conversions)

    def list_by_category(self):
        result = {}
        for cat, keys in self._categories.items():
            result[cat] = []
            for key in keys:
                from_u, to_u, _ = self._conversions[key]
                result[cat].append((key, from_u, to_u))
        return result

    def find(self, query):
        """Search for conversions by keyword."""
        query = query.lower()
        results = []
        for key, (from_u, to_u, _) in self._conversions.items():
            if query in key.lower() or query in from_u.lower() or query in to_u.lower():
                results.append((key, from_u, to_u))
        return results


def create_default_registry():
    """Create registry with all default conversions."""
    reg = ConversionRegistry()

    # Temperature
    reg.register("c2f", "Celsius", "Fahrenheit", lambda x: x * 9/5 + 32, "Temperature")
    reg.register("f2c", "Fahrenheit", "Celsius", lambda x: (x - 32) * 5/9, "Temperature")
    reg.register("c2k", "Celsius", "Kelvin", lambda x: x + 273.15, "Temperature")
    reg.register("k2c", "Kelvin", "Celsius", lambda x: x - 273.15, "Temperature")

    # Distance
    reg.register("km2mi", "Kilometers", "Miles", lambda x: x * 0.621371, "Distance")
    reg.register("mi2km", "Miles", "Kilometers", lambda x: x / 0.621371, "Distance")
    reg.register("m2ft", "Meters", "Feet", lambda x: x * 3.28084, "Distance")
    reg.register("ft2m", "Feet", "Meters", lambda x: x / 3.28084, "Distance")
    reg.register("cm2in", "Centimeters", "Inches", lambda x: x / 2.54, "Distance")
    reg.register("in2cm", "Inches", "Centimeters", lambda x: x * 2.54, "Distance")

    # Weight
    reg.register("kg2lb", "Kilograms", "Pounds", lambda x: x * 2.20462, "Weight")
    reg.register("lb2kg", "Pounds", "Kilograms", lambda x: x / 2.20462, "Weight")
    reg.register("g2oz", "Grams", "Ounces", lambda x: x / 28.3495, "Weight")
    reg.register("oz2g", "Ounces", "Grams", lambda x: x * 28.3495, "Weight")

    # Volume
    reg.register("l2gal", "Liters", "Gallons", lambda x: x * 0.264172, "Volume")
    reg.register("gal2l", "Gallons", "Liters", lambda x: x / 0.264172, "Volume")

    # Area
    reg.register("sqm2sqft", "Sq Meters", "Sq Feet", lambda x: x * 10.7639, "Area")
    reg.register("sqft2sqm", "Sq Feet", "Sq Meters", lambda x: x / 10.7639, "Area")
    reg.register("ha2ac", "Hectares", "Acres", lambda x: x * 2.47105, "Area")
    reg.register("ac2ha", "Acres", "Hectares", lambda x: x / 2.47105, "Area")

    return reg
