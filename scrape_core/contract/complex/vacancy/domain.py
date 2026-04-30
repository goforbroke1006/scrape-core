from dataclasses import dataclass, field
from fractions import Fraction
from typing import List, Optional

from scrape_core.common import ScrapeResult
from .obj_value_employee_grade import EmployeeGrade
from .obj_value_salary_period import SalaryPeriod
from .obj_value_salary_type import SalaryType
from ...prime.count_info import CountInfo
from ...prime.currency.currency_code import Currency3Code
from ...prime.datetime import DateTimeInfo
from ...prime.geo.address import AddressInfo


@dataclass
class SalaryInfo:
    text: Optional[str] = None
    amount: Optional[Fraction | float | int] = None
    amount_min: Optional[Fraction | float | int] = None
    amount_max: Optional[Fraction | float | int] = None
    currency: Optional[Currency3Code] = None
    type: Optional[SalaryType] = None  # NET, GROSS
    period: Optional[SalaryPeriod] = None


@dataclass
class Experience:
    text: Optional[str] = None
    years_min: Optional[str] = None


@dataclass
class Education:
    text: Optional[str] = None
    # TODO:


@dataclass
class VacancyListing(ScrapeResult):
    locations: List[AddressInfo] = field(default_factory=list)
    
    salary: SalaryInfo = field(default_factory=SalaryInfo)
    
    recruiter_name: Optional[str] = None
    company_name: Optional[str] = None
    department_names: List[str] = field(default_factory=list)
    domain_names: List[str] = field(default_factory=list)
    team_names: List[str] = field(default_factory=list)
    
    remote_allowed: Optional[bool] = None
    hybrid_allowed: Optional[bool] = None
    onsite_allowed: Optional[bool] = None
    worldwide_allowed: Optional[bool] = None
    relocation_package: Optional[bool] = None
    visa_sponsorship: Optional[bool] = None
    
    deadline_at: DateTimeInfo = field(default_factory=DateTimeInfo)
    
    tech_stack: List[str] = field(default_factory=list)
    employee_grade: Optional[EmployeeGrade] = None
    experience: Experience = field(default_factory=Experience)
    education: Education = field(default_factory=Education)
    job_format_text: Optional[str] = None
    contract_type_text: Optional[str] = None
    
    views: CountInfo = field(default_factory=CountInfo)
