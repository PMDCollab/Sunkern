from typing import Optional, Dict

from sunkern.provider.abstract import AbstractProvider


class ProviderPool:
    _loaded_providers: Optional[Dict[str, AbstractProvider]] = None

    @classmethod
    def lst(cls) -> Dict[str, AbstractProvider]:
        pass

    @classmethod
    def get(cls, name: str) -> AbstractProvider:
        return cls.lst()[name]  # may raise an IndexError!
