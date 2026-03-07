from enum import Enum


class EmployeeGrade(Enum):
    TRAINEE = 'trainee'
    JUNIOR = 'junior'
    MIDDLE = 'middle'
    SENIOR = 'senior'
    STAFF = 'staff'
    
    def __str__(self) -> str:
        return self.value
