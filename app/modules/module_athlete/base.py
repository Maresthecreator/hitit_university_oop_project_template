from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto


class SporBransi(Enum):
    Futbol = auto()
    Basketbol = auto()
    Voleybol = auto()
    Yuzme = auto()
    Tenis = auto()
    Golf = auto()

class AtletDurumu(Enum):
    Aktif = auto()
    Sakat = auto()
    Aciga_Alindi = auto()
    Emekli = auto()

@dataclass
class AthleteBase(ABC):
    atlet_numara: int
    isim = str
    yas : int
    spor_bransi : SporBransi
    durum : AtletDurumu

    @abstractmethod
    def abonelik_ucreti_hesapla(self) -> float:
        """Her alt sinif ucreti hesapla"""

    @abstractmethod
    def hesap_gecmisi(self) -> str:
        """Hesap gecmisini gosterir"""

    def durum_guncelle(self, yeni_durum: AtletDurumu) -> float:
        """ Sporcunun durumunu guncelle"""


