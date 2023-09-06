
from pygal.i18n import COUNTRIES

def get_country_code():

    """Return country code"""
    for code,name in COUNTRIES.items(country_name):
        if name ==country_name:
            return code

    return None

print(get_country_code("Kenya"))
