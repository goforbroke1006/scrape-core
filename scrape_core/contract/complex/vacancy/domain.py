import datetime
from typing import List

from currency.obj_value_currency_code import Currency3Code
from geography.obj_value import CountryAlpha2Code
from obj_aggregate_unified import UnifiedObject
from opt_type import OptionalType
from .obj_value_employee_grade import EmployeeGrade
from .obj_value_salary_period import SalaryPeriod
from .obj_value_salary_type import SalaryType


class VacancyObject(UnifiedObject):
    def __init__(
            self,
            provider_name: str = None,
            
            country: str | CountryAlpha2Code = None,
            
            internal_id: str = None,
            title: str = '',
            link_detail_page: str | None = None,
            content: str | None = None,
            
            recruiter_name: str = None,
            company_name: str = None,
            department_names: List[str] = None,
            domain_names: List[str] = None,
            team_name: str | None = None,
            
            salary_text: str | None = None,
            salary_min: float = None,
            salary_max: float = None,
            salary_type: SalaryType | str = None,
            salary_currency: Currency3Code | str | None = None,
            salary_period: SalaryPeriod | str | None = None,
            
            publish_text: str = None,
            publish_dt: datetime.datetime | datetime.date = None,
            
            start_at_text: str | None = None,
            start_at_dt: datetime.datetime | datetime.date = None,
            deadline_text: str | None = None,
            deadline_dt: datetime.datetime | datetime.date = None,
            
            countries: List[CountryAlpha2Code | str] = None,
            city: str = None,
            locations: List[str] = None,
            
            remote_allowed: OptionalType | str | None = OptionalType.UNKNOWN,
            hybrid_allowed: OptionalType | str | None = OptionalType.UNKNOWN,
            onsite_allowed: OptionalType | str | None = OptionalType.UNKNOWN,
            worldwide_allowed: OptionalType | str | None = OptionalType.UNKNOWN,
            relocation_package: OptionalType | str | None = OptionalType.UNKNOWN,
            visa_sponsorship: OptionalType | str | None = OptionalType.UNKNOWN,
            
            tech_stack: List[str] = None,
            employee_grade: EmployeeGrade | str | None = None,
            experience_text: str = None,
            job_format_text: str = None,
            contract_type_text: str = None,
            
            number_of_views: int | None = None,
            
            attributes=None,
    ):
        super().__init__(
            object_code='vacancy',
            provider_name=provider_name,
            
            country=country,
            
            internal_id=internal_id,
            title=title,
            link_detail_page=link_detail_page,
            content=content,
        )
        
        countries = [str(c) for c in countries]
        
        self.recruiter_name = recruiter_name
        self.company_name = company_name
        self.department_names = department_names
        self.domain_names = domain_names
        self.team_name = team_name
        
        self.salary_text = salary_text
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.salary_type = salary_type
        self.salary_currency = salary_currency
        self.salary_period = salary_period
        
        self.publish_text = publish_text
        self.publish_dt = publish_dt
        
        self.start_at_text = start_at_text
        self.start_at_dt = start_at_dt
        self.deadline_text = deadline_text
        self.deadline_dt = deadline_dt
        
        self.country = country
        self.countries = countries
        self.city = city
        self.locations = locations
        
        self.remote_allowed = remote_allowed
        self.hybrid_allowed = hybrid_allowed
        self.onsite_allowed = onsite_allowed
        self.worldwide_allowed = worldwide_allowed
        self.relocation_package = relocation_package
        self.visa_sponsorship = visa_sponsorship
        
        self.tech_stack = tech_stack
        self.employee_grade = employee_grade
        self.experience_text = experience_text
        self.job_format_text = job_format_text
        self.contract_type_text = contract_type_text
        
        self.number_of_views = number_of_views
        
        self.scanned_at = datetime.datetime.now()
        
        self.attributes = attributes
