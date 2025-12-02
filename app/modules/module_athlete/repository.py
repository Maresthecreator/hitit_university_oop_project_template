from __future__ import annotations

from typing import List, Optional, Optional

from .base import AtletBase, SporBransi, AtletDurumu


class AtletRepo:
    """Sporcular icin bellek """

    def __init__(self) -> None:
        self.atletler:List[AtletBase] = []

    def add(self, atlet: AtletBase) -> None:
        self.atletler.append(atlet)

    def


