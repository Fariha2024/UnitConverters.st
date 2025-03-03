from pint import UnitRegistry

def convert_units(value, from_unit, to_unit, ureg):
    quantity = value * ureg(from_unit)
    converted = quantity.to(to_unit)
    return converted.magnitude