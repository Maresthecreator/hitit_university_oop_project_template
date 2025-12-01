from __future__ import annotations

from dataclasses import dataclass

from .base import AthleteBase, SporBransi, AtletDurumu


class ProfesyonelAtlet(AthleteBase):
    maas: float
    yillik_kontrat: int

    def abonelik_ucreti_hesapla(self) -> float:
        return 0.0

    def hesap_gecmisi(self) -> str:
