from __future__ import annotations

from dataclasses import dataclass

from .base import AthleteBase, SportBranch, AthleteStatus

@dataclass
class ProfessionalAthlete(AthleteBase):
    salary: float
    contract_years: int
    sponsor_count: int=0

    def calculate_membership_fee(self) -> float:
        return 0.0

    def get_profile_summary(self) -> str:
        return (
            f"[PRO] {self.name} | Branş: {self.sport_branch.name} | "
            f"Durum: {self.status.name} | Maaş: {self.salary}"
        )
@dataclass
class AmateurAthlete(AthleteBase):
    base_fee: float
    has_student_discount: bool = False
    def calculate_membership_fee(self) -> float:
        fee = self.base_fee
        if self.has_student_discount:
            fee *= 0.8
        return fee

    def get_profile_summary(self) -> str:
        return (
            f"[AMATEUR] {self.name} | Branş: {self.sport_branch.name} | "
            f"Durum: {self.status.name} | Ücret: {self.calculate_membership_fee()}"
        )

@dataclass
class YouthAthlete(AthleteBase):
    school_name: str
    parent_contact : str
    scholarship_rate : float = 0.5

    def calculate_membership_fee(self) -> float:
        base_fee = 500.0
        return base_fee * self.scholarship_rate

    def get_profile_summary(self) -> str:
        return (
            f"[YOUTH] {self.name} ({self.age}) | Branş: {self.sport_branch.name} | "
            f"Okul: {self.school_name} | Durum: {self.status.name}"
        )




