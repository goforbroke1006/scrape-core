import re
from fractions import Fraction

from scrape_core.contract.prime.currency.parser import parse as currency_parse
from scrape_core.contract.prime.country_code.country_code import CountryAlpha2Code
from scrape_core.contract.prime.price.price_info import PriceInfo
from scrape_core.html_entity import SYMBOL_NBSP, SYMBOL_NNBSP, SYMBOL_THSP


def parse(text: str, country_code: CountryAlpha2Code = None) -> PriceInfo:
    """
    :param text:
    :param country_code:
    :return:
    
    "11 DT 500"         -> PriceInfo("11 DT 500",           11.500,     Currency3Code.TunisianDinar)        ???
    "EGP 490"           -> PriceInfo("EGP 490",             490,        Currency3Code.EgyptianPound)
    "1,040.00 dh"       -> PriceInfo("EGP 490",             490,        Currency3Code.MoroccanDirham)       ???
    "€2.17"             -> PriceInfo("€2.17",               2.17,       Currency3Code.Euro)
    "4.860,00&nbsp;CFA" -> PriceInfo("4.860,00&nbsp;CFA",   4860.00,    Currency3Code.CFAFranc)
    "₦ 6,179.00"        -> PriceInfo("₦ 6,179.00",          6179.00,    Currency3Code.NigerianNaira)
    "SCR390.00"         -> PriceInfo("SCR390.00",           390.00,     Currency3Code.SeychelloisRupee)
    "R79.95"            -> PriceInfo("R79.95",              79.95,      Currency3Code.SouthAfricanRand)
    "R50,00"            -> PriceInfo("R50,00",              50.00,      Currency3Code.SouthAfricanRand)
    "R 70.00"           -> PriceInfo("R 70.00",             70.00,      Currency3Code.SouthAfricanRand)
    "R 59.99 ZAR"       -> PriceInfo("R 59.99 ZAR",         59.99,      Currency3Code.SouthAfricanRand)
    "R1,609.99"         -> PriceInfo("R1,609.99",           1609.99,    Currency3Code.SouthAfricanRand)
    "9.99 ₼"            -> PriceInfo("9.99 ₼",              9.99,       Currency3Code.AzerbaijaniManat)
    "Rs. 185.00"        -> PriceInfo("Rs. 185.00",          185.00,     Currency3Code.SriLankanRupee)
    "₨194.70"           -> PriceInfo("₨194.70",             194.70,     Currency3Code.MauritianRupee)
    "RM 17.95"          -> PriceInfo("RM 17.95",            17.95,      Currency3Code.MalaysianRinggit)
    "50 000 сум"        -> PriceInfo("50 000 сум",          50000,      Currency3Code.UzbekistaniSum)
    "$1.75"             -> PriceInfo("$1.75",               1.75,       Currency3Code.UnitedStatesDollar)
    "$10.00"            -> PriceInfo("$10.00",              10.00,      Currency3Code.AustraliaDollar)
    
    "109.00"            -> PriceInfo("109.00",              109.00,     None)
    "29 950"            -> PriceInfo("29 950",              29950,      None)
    
    """
    
    text = text.replace(SYMBOL_NBSP, ' ')
    text = text.replace(SYMBOL_NNBSP, ' ')
    text = text.replace(SYMBOL_THSP, ' ')
    
    amount_m = re.search(r'(([\d,]+)(\.(\d+))*)', text)
    if amount_m:
        amount = Fraction(amount_m.group(1).replace(',', ''))
        price_info = PriceInfo()
        price_info.text = text
        price_info.amount = amount
        text_without_amount = text.replace(amount_m.group(1), '').strip()
        price_info.currency = currency_parse(text_without_amount, country_code)
        return price_info
    
    # TODO:
    
    raise ValueError(f'unexpected text: {text}')
