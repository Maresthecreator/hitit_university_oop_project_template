from __future__ import annotations

from typing import List, Optional, Optional

from .base import AthleteBase, SportBranch, AthleteStatus


class AthleteRepository:
    """Sporcular icin bellek """

    def __init__(self) -> None:
        self.athletes:List[AthleteBase] = []

    def add(self, athlete: AthleteBase) -> None:
        self.athletes.append(athlete)

    def list_all(self) -> List[AthleteBase]:
        return list(self.athletes)

    def get_by_id(self, athlete_id: int) -> Optional[AthleteBase]:
        for athlete in self.athletes:
            if athlete.athlete.id == athlete_id:
                return athlete
            return None

    def filter_by_branch(self, branch: SportBranch) -> Optional[AthleteBase]:
        return[a for a in self.athletes if a.sport_branch == branch]

    def filter_by_status(self, status: AthleteStatus) -> Optional[AthleteBase]:
        return [a for a in self.athletes if a.status == status]

    def search_by_name(self, keyword: str) -> List[AthleteBase]:
        keyword = keyword.lower()
        return [a for a in self.athletes if keyword in a.name.lower()]





