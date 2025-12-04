from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto


class SportBranch(Enum):
    Football = auto()
    Basketball = auto()
    Voleyball = auto()
    Swimming = auto()
    Tennis = auto()
    Golf = auto()

class AthleteStatus(Enum):
    Active = auto()
    Injured = auto()
    Suspended = auto()
    Retired = auto()

@dataclass
class AthleteBase(ABC):
    athlete_id: int
    name: str
    age : int
    sport_branch : SportBranch
    status : AthleteStatus

    @abstractmethod
    def calculate_membership_fee(self) -> float:
        """Her alt sinif ucreti hesapla"""

    @abstractmethod
    def get_profile_summary(self) -> str:
        """Hesap gecmisini gosterir"""

    def update_status(self, new_status: AthleteStatus) -> None:
        """ Sporcunun durumunu guncelle"""


