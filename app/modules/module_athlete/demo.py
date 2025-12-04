from __future__ import annotations

from tkinter.font import names

from .base import SportBranch, AthleteStatus
from .implementations import ProfessionalAthlete, AmateurAthlete, YouthAthlete
from .repository import AthleteRepository


def run_demo() -> None:
    repo = AthleteRepository()

    athlete1 = ProfessionalAthlete(
    athlete_id=1,
    name='<Yusuf Profesyonel Atlet',
    age=27,
    sport_branch=SportBranch.Football,
    status=AthleteStatus.Active,
    salary=60000,
    contract_years=3,
    )

    athlete2 = AmateurAthlete(
    athlete_id=2,
    name="Ayse Amatör Atlet",
    age=21,
    sport_branch=SportBranch.Basketball,
    status=AthleteStatus.Active,
    base_fee=350.0,
    has_student_discount=True,
    )
    athlete3 = YouthAthlete(
    athlete_id=3,
    name='<Yusuf Youth',
    age=28,
    sport_branch=SportBranch.Voleyball,
    status=AthleteStatus.Injured,
    school_name='<Anadolu Lisesi',
    parent_contact='Mehmet 0512 345 67 89',
    )
    for athlete in [athlete1, athlete2, athlete3]:
        repo.add(athlete)

    print("---Sporcularımız---")
    for athlete in repo.list_all():
        print("Aidat:", athlete.calculate_membership_fee())
        print("-" * 40)

    print("---Sadece Futbolcular---")
    for athlete in repo.filter_by_branch(SportBranch.Football):
        print(athlete.get_profile_summary())

    print("---Sadece Basketbolcular---")
    for athlete in repo.filter_by_branch(SportBranch.Basketball):
        print(athlete.get_profile_summary())

    print("---Sadece Voleybolcular---")
    for athlete in repo.filter_by_branch(SportBranch.Voleyball):
        print(athlete.get_profile_summary())

    print("---Aktif Sporcular---")
    for athlete in repo.filter_by_status(AthleteStatus.Active):
        print(athlete.get_profile_summary())

    print("---Sakat Sporcular---")
    for athlete in repo.filter_by_status(AthleteStatus.Injured):
        print(athlete.get_profile_summary())
