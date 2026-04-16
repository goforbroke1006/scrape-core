from abc import ABC, abstractmethod
from typing import List, Tuple, Any, Generator

from scrape_core.common import ScrapeResult
from scrape_core.contract.prime.country_code.country_code import CountryAlpha2Code
from scrape_core.contract.prime.currency.currency_code import Currency3Code


class StandardPipeline(ABC):
    
    @abstractmethod
    def get_domain(self) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def get_provider(self) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def threshold_empty_pages(self) -> int:
        return 5
    
    @abstractmethod
    def default_country(self, driver, datum) -> CountryAlpha2Code | None:
        return None
    
    @abstractmethod
    def default_city(self, driver, datum) -> str | None:
        return None
    
    def default_district(self, driver, datum) -> str | None:
        return None
    
    def default_neighborhood(self, driver, datum) -> str | None:
        return None
    
    @abstractmethod
    def default_currency(self, driver, datum) -> Currency3Code | None:
        return None
    
    @abstractmethod
    def http_user_agent(self) -> str | None:
        return None
    
    @abstractmethod
    def main_page_link(self) -> str | None:
        return None
    
    @abstractmethod
    def get_robots_txt_content(self) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def before_scanning(self, driver) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def get_data(self) -> List[str | Tuple[Any] | List[Any]]:
        raise NotImplementedError()
    
    @abstractmethod
    def before_datum(self, driver, datum: Any) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def apply_datum(self, driver, datum: Any) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def after_datum(self, driver, datum: Any) -> None:
        return None
    
    @abstractmethod
    def load_categories(self, driver, datum: Any) -> List[str] | None:
        return None
    
    @abstractmethod
    def load_page_title(self, driver, datum: Any) -> str | None:
        return None
    
    @abstractmethod
    def load_groups(self, driver, datum: Any) -> List[Any] | None:
        return None
    
    @abstractmethod
    def load_group_title(self, driver, datum: Any, group) -> str | None:
        return None
    
    @abstractmethod
    def load_cards(self, driver, datum: Any, group) -> List[Any]:
        raise NotImplementedError()
    
    @abstractmethod
    def scan_card(self, driver, datum, group, card) -> ScrapeResult | None:
        raise NotImplementedError()
    
    @abstractmethod
    def go_to_next_page(self, driver, datum: Any) -> Generator[bool, Any, None]:
        yield False
