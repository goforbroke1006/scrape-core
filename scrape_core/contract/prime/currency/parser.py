import re

from ..country_code.country_code import CountryAlpha2Code
from .currency_code import Currency3Code


def parse_or_none(text: str, country_code: CountryAlpha2Code | None = None):
    try:
        return parse(text, country_code)
    except ValueError:
        return None


def parse(text: str, country_code: CountryAlpha2Code | None = None):
    text_upper = text.upper().strip()
    
    if 'KR' == text:
        if country_code == CountryAlpha2Code.Norway:
            return Currency3Code.NorwegianKrone
        if country_code == CountryAlpha2Code.Sweden:
            return Currency3Code.SwedishKrona
    
    if 'RS' == text:
        if country_code == CountryAlpha2Code.Serbia:
            return Currency3Code.SerbianDinar
        if country_code == CountryAlpha2Code.Pakistan:
            return Currency3Code.PakistaniRupee
        if country_code == CountryAlpha2Code.Nepal:
            return Currency3Code.NepaleseRupee
    
    if 'L' == text:
        if country_code == CountryAlpha2Code.Honduras:
            return Currency3Code.HonduranLempira
    
    if 'BSD$' in text:
        return Currency3Code.BahamianDollar
    if 'TT$' in text:
        return Currency3Code.TrinidadAndTobagoDollar
    if 'RD$' in text:
        return Currency3Code.DominicanPeso
    if 'сўм' in text:
        return Currency3Code.UzbekistaniSum
    if 'KČ' in text:
        return Currency3Code.CzechKoruna
    if 'грн' in text or 'ГРН' in text:
        return Currency3Code.UkrainianHryvnia
    
    if 'US$' in text:
        return Currency3Code.UnitedStatesDollar
    elif 'EC$' in text:
        return Currency3Code.EastCaribbeanDollar
    elif 'MX$' in text:
        return Currency3Code.MexicanPeso
    elif 'U$' in text:
        return Currency3Code.UnitedStatesDollar
    elif 'J$' in text:
        return Currency3Code.JamaicanDollar
    elif 'HK$' in text:
        return Currency3Code.HongKongDollar
    elif 'KM' in text:
        return Currency3Code.BosniaConvertibleMark
    elif 'R$' in text:
        if country_code == CountryAlpha2Code.Brazil:
            return Currency3Code.BrazilianReal
    elif 'Rs.' in text:
        if country_code == CountryAlpha2Code.India or country_code == CountryAlpha2Code.UAE:
            return Currency3Code.IndianRupee
    
    if '฿' in text:
        return Currency3Code.ThaiBaht
    elif '₸' in text or '〒' in text:
        return Currency3Code.KazakhstaniTenge
    elif '₦' in text:
        return Currency3Code.NigerianNaira
    elif '₼' in text:
        return Currency3Code.AzerbaijaniManat
    elif '₩' in text:
        return Currency3Code.SouthKoreanWon
    elif '€' in text:
        return Currency3Code.Euro
    elif '₮' in text:
        return Currency3Code.MongolianTughrik
    elif '$' in text:
        if country_code == CountryAlpha2Code.Canada:
            return Currency3Code.CanadianDollar
        if country_code == CountryAlpha2Code.AntiguaBarbuda:
            return Currency3Code.EastCaribbeanDollar
        if country_code == CountryAlpha2Code.Jamaica:
            return Currency3Code.JamaicanDollar
        if country_code == CountryAlpha2Code.Australia:
            return Currency3Code.AustraliaDollar
        
        return Currency3Code.UnitedStatesDollar
    
    elif 'د.إ' in text_upper:
        return Currency3Code.EmiratesDirham
    elif '£' in text:
        return Currency3Code.GreatBritishPound
    elif '֏' in text or 'Դ' in text:
        return Currency3Code.ArmenianDram
    elif '₽' in text:
        return Currency3Code.RussianRuble
    elif 'руб.' in text:
        return Currency3Code.RussianRuble
    elif '₾' in text:
        return Currency3Code.GeorgianLari
    elif '₹' in text:
        return Currency3Code.IndianRupee
    elif '₴' in text:
        return Currency3Code.UkrainianHryvnia
    elif '₺' in text:
        return Currency3Code.TurkishLire
    elif 'TL' == text and country_code == CountryAlpha2Code.Turkey:
        return Currency3Code.TurkishLire
    elif '₡' in text:
        return Currency3Code.CostaRicanColones
    elif '¥' in text:
        if country_code == CountryAlpha2Code.Japan:
            return Currency3Code.JapaneseYen
        if country_code == CountryAlpha2Code.China:
            return Currency3Code.ChineseYuan
    elif '円' in text:
        return CountryAlpha2Code.Japan
    elif 'ZŁ' in text or 'zł' in text:
        return Currency3Code.PolishZlotych
    elif '₫' in text:
        return Currency3Code.VietnameseDongs
    elif '₪' in text:
        return Currency3Code.IsraeliNewShekels
    elif '₦' in text:
        return Currency3Code.NigerianNaira
    elif 'Ƒ' in text:
        if country_code == CountryAlpha2Code.Aruba:
            return Currency3Code.ArubanFlorin
        if country_code == CountryAlpha2Code.Curacao:
            return Currency3Code.AntilleanGuilder
    elif 'Bs' in text:
        if country_code == CountryAlpha2Code.Bolivia:
            return Currency3Code.BolivianBoliviano
    elif '₲' in text:
        return Currency3Code.ParaguayanGuarani
    elif '₱' in text:
        return Currency3Code.PhilippinePeso
    
    if 'USD' in text_upper:
        return Currency3Code.UnitedStatesDollar
    elif 'EUR' in text_upper:
        return Currency3Code.Euro
    elif 'GBP' in text_upper:
        return Currency3Code.GreatBritishPound
    elif 'QAR' in text_upper:
        return Currency3Code.QatariRiyal
    elif 'RUB' in text_upper:
        return Currency3Code.RussianRuble
    elif 'AED' in text_upper:
        return Currency3Code.EmiratesDirham
    elif 'CAD' in text_upper:
        return Currency3Code.CanadianDollar
    elif 'XCD' in text_upper:
        return Currency3Code.EastCaribbeanDollar
    elif 'MWK' in text_upper:
        return Currency3Code.MalawianKwacha
    elif 'ANG' in text_upper:
        return Currency3Code.AntilleanGuilder
    elif 'BHD' in text_upper:
        return Currency3Code.BahrainiDinar
    elif 'PKR' in text_upper:
        return Currency3Code.PakistaniRupee
    elif 'NIO' in text_upper:
        return Currency3Code.NicaraguanCordoba
    elif 'NZD' in text_upper:
        return Currency3Code.NewZealandDollar
    elif 'MOP' in text_upper:
        return Currency3Code.MacanesePataca
    elif 'DKK' in text_upper:
        return Currency3Code.DanishKrone
    elif 'OMR' in text_upper:
        return Currency3Code.OmaniRial
    elif 'GIP' in text_upper:
        return Currency3Code.GibraltarPound
    elif 'UGX' in text_upper:
        return Currency3Code.UgandanShilling
    elif 'BDT' in text_upper:
        return Currency3Code.BangladeshiTaka
    elif 'BSD' in text_upper:
        return Currency3Code.BahamianDollar
    elif 'HNL' in text_upper:
        return Currency3Code.HonduranLempira
    elif 'KES' in text_upper:
        return Currency3Code.KenyanShilling
    elif 'KYD' in text_upper:
        return Currency3Code.CaymanIslandsDollar
    elif 'BTC' in text_upper:
        return Currency3Code.BitCoin
    
    iso_code_m = re.search(r'([A-Z]{3})', text)
    if iso_code_m:
        try:
            return Currency3Code(iso_code_m.group(1))
        except ValueError:
            pass
        
        return iso_code_m.group(1)
        # return Currency3Code(iso_code_m.group(1))
    
    if len(text) == 3:
        try:
            return Currency3Code(text)
        except ValueError:
            pass
        
        if re.match(r'^[A-Z]{3}$', text):
            print(f'WARN: need to add the missed currency {text}')
        
        # return just string
        return text
    
    print(f'WARN: unknown currency {text}')
    
    return None
