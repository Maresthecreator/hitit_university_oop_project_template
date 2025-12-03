from __future__ import annotations

from dataclasses import dataclass

from .base import AtletBase, SporBransi, AtletDurumu


class ProfesyonelAtlet(AtletBase):
    maas: float
    yillik_kontrat: int

    def abonelik_ucreti_hesapla(self) -> float:
        return 0.0

    def hesap_gecmisi(self) -> str:
        return (
            f"[PRO] {self.name} | Branş: {self.sport_branch.name} | "
            f"Durum: {self.status.name} | Maaş: {self.salary}"
        )

@dataclass
class AmatorAtlet(AtletBase):
    genel_tutar: float
    ogrenci_getirme_indirimi: bool = False
    def abonelik_ucreti_hesapla(self) -> float:
        ucret = self.ana_ucret
        if self.ogrenci_getirme_indirimi:
            ucret *= 0.8
        return ucret

    def hesap_gecmisi(self) -> str:
        return (
            f"[AMATOR] {self.isim} | Branş: {self.spor_bransi} | "
            f"Durum: {self.durum} | Ücret: {self.abonelik_ucreti_hesapla()}"
        )

@dataclass
class GencAtlet(AtletBase):
    okul_ismi: str
    ebebeyn_iletisim:str
    burs_orani: float = 0.5

    def abonelik_ucreti_hesapla(self) -> float:
        ana_ucret = 500.0
        return ana_ucret * self.burs_orani

    def hesap_gecmisi(self) -> str:
        return (
            f"[GENC] {self.isim} ({self.yas}) | Branş: {self.spor_bransi} | "
            f"Okul: {self.okul_ismi} | Durum: {self.durum}"
        )




