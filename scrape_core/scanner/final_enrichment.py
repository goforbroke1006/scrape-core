import datetime
from typing import List, Any

from scrape_core.common import ScrapeResult
from scrape_core.scanner.pipeline import StandardPipeline


def result_final_enrichment(
        results: List[ScrapeResult],
        pipeline: StandardPipeline,
        driver: Any,
        datum: Any,
        group_el: Any,
        robots_txt_allows: bool = False,
) -> List[ScrapeResult]:
    """
    After method StandardPipeline::scan_card build object,
    we try to fill the gaps with some additional data if its were missed.
    
    @param results:  List[ScrapeResult] - what we found on the web page
    @param pipeline: StandardPipeline   - the scanning process metadata and instructions
    @param driver:   WebDriver          - accessor to page content
    @param datum:    Any                - accessor to scanning context
    """
    
    import copy
    from scrape_core.contract.prime.geo.address import AddressInfo
    from scrape_core.contract.prime.price.price_info import PriceInfo
    
    #
    #
    #
    
    categories_list = pipeline.load_categories(driver, datum)
    categories_list: List[str] | None = copy.deepcopy(categories_list) if categories_list is not None else []
    
    page_title = pipeline.load_page_title(driver, datum)
    if page_title is not None:
        print('INFO: load page title', f'"{page_title}"')
        categories_list.append(page_title)
    
    group_title = None
    if group_el is not None:
        group_title = pipeline.load_group_title(driver, datum, group_el)
        if group_title is not None:
            categories_list.append(group_title)
    
    if categories_list:
        print('INFO: load page categories', categories_list)
    
    #
    #
    #
    
    def is_optional_str(annotation):
        from typing import get_origin, get_args, Union
        
        if get_origin(annotation) is Union:
            args = get_args(annotation)
            return str in args and type(None) in args
        return annotation is str
    
    for res in results:
        res.provider = pipeline.get_provider()
        
        if res.scraped_at is None:
            res.scraped_at = datetime.datetime.utcnow()
        
        if res.country is None:
            res.country = pipeline.default_country(driver, datum)
        
        # custom enrichment for RealEstateListing
        if hasattr(res, 'address') and isinstance(getattr(res, 'address'), AddressInfo):
            if getattr(res, 'address').country is None:
                getattr(res, 'address').country = pipeline.default_country(driver, datum)
            
            if getattr(res, 'address').city is None:
                res.address.city = pipeline.default_city(driver, datum)
        
        if res.categories is None or len(res.categories) == 0:
            res.categories = categories_list
        
        # custom enrichment for GroceryListing
        if page_title:
            if (hasattr(res, 'category')
                    and is_optional_str(annotation=res.__class__.__annotations__.get('category'))):
                res.category = page_title
        if group_title:
            if (hasattr(res, 'subcategory')
                    and is_optional_str(annotation=res.__class__.__annotations__.get('subcategory'))):
                res.subcategory = group_title
        
        # universal enrichment for all price-info fields
        for attr in dir(res):
            if attr.startswith('__') or callable(getattr(res, attr)):
                continue
            
            if isinstance(getattr(res, attr), PriceInfo):
                if getattr(res, attr).currency is None and not getattr(res, attr).is_empty():
                    getattr(res, attr).currency = pipeline.default_currency(driver, datum)
        
        res.robots_txt_allows = robots_txt_allows
    
    return results
