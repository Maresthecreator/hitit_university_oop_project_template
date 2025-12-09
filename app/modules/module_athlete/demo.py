from __future__ import annotations

from tkinter.font import names

from .base import SportBranch, AthleteStatus
from .implementations import ProfessionalAthlete, AmateurAthlete, YouthAthlete
from .repository import AthleteRepository


def run_demo() -> None:
    repo = AthleteRepository()

    athlete1 = ProfessionalAthlete(
    athlete_id=1,
    name='Yusuf Profesyonel Atlet',
    age=27,
    sport_branch=SportBranch.Football,
    status=AthleteStatus.Active,
    salary=60000,
    contract_years=3,
    )

    athlete2 = AmateurAthlete(
    athlete_id=2,
    name="Ayşe Amatör Atlet",
    age=21,
    sport_branch=SportBranch.Basketball,
    status=AthleteStatus.Active,
    base_fee=350.0,
    has_student_discount=True,
    )

    athlete3 = YouthAthlete(
    athlete_id=3,
    name='Ilgın Genç Atlet',
    age=17,
    sport_branch=SportBranch.Voleyball,
    status=AthleteStatus.Injured,
    school_name='Erzurum Proje Lisesi',
    parent_contact='Mehmet 0512 345 67 89',
    )

    athlete4 = AmateurAthlete(
    athlete_id=4,
    name="Can Amatör Atlet ",
    age=23,
    sport_branch=SportBranch.Swimming,
    status=AthleteStatus.Suspended,
    base_fee=560.0,
    has_student_discount=False,
    )

    athlete5 = YouthAthlete(
    athlete_id=5,
    name="Yılmaz Genç Atlet",
    age=16,
    sport_branch=SportBranch.Golf,
    status=AthleteStatus.Active,
    school_name="Atatürk Fen Lisesi",
    parent_contact='Eylül 0555 345 67 89',
    )
    athlete6 = ProfessionalAthlete(
    athlete_id=6,
    name="Hakan Profesyonel Atlet",
    age=51,
    sport_branch=SportBranch.Tennis,
    status=AthleteStatus.Retired,
    salary=0,
    contract_years=0,
    )


    for athlete in [athlete1, athlete2, athlete3, athlete4, athlete5, athlete6]:
        repo.add(athlete)

    print("---Sporcularımız---")
    for athlete in repo.list_all():
        print("Aidat:", athlete.calculate_membership_fee())
        print("-" * 50)

    print("---Sadece Futbolcular---")
    for athlete in repo.filter_by_branch(SportBranch.Football):
        print(athlete.get_profile_summary())

    print("---Sadece Basketbolcular---")
    for athlete in repo.filter_by_branch(SportBranch.Basketball):
        print(athlete.get_profile_summary())

    print("---Sadece Voleybolcular---")
    for athlete in repo.filter_by_branch(SportBranch.Voleyball):
        print(athlete.get_profile_summary())

    print("---Sadece Tenisciler---")
    for athlete in repo.filter_by_branch(SportBranch.Tennis):
        print(athlete.get_profile_summary())

    print("---Sadece Yüzücüler---")
    for athlete in repo.filter_by_branch(SportBranch.Swimming):
        print(athlete.get_profile_summary())

    print("---Sadece Golfcü---")
    for athlete in repo.filter_by_branch(SportBranch.Golf):
        print(athlete.get_profile_summary())

    print("---Aktif Sporcular---")
    for athlete in repo.filter_by_status(AthleteStatus.Active):
        print(athlete.get_profile_summary())

    print("---Sakat Sporcular---")
    for athlete in repo.filter_by_status(AthleteStatus.Injured):
        print(athlete.get_profile_summary())

    print("---Açığa Alınmış Sporcular---")
    for athlete in repo.filter_by_status(AthleteStatus.Suspended):
        print(athlete.get_profile_summary())

    print("---Emekli Olmuş Sporcular---")
    for athlete in repo.filter_by_status(AthleteStatus.Retired):
        print(athlete.get_profile_summary())