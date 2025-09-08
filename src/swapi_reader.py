import os
from typing import List, Type
import requests

from crypto_utils import JSONKeyEncryptor
from data_classes import Person
from api_reader import APIReader


class SWAPIReader(APIReader):
    """Generic SWAPI reader with optional debug logging."""

    def __init__(self, dataclass_type: Type[Person], resource: str, debug: bool = False):
        super().__init__(debug=debug)
        self.dataclass_type = dataclass_type
        self._resource = resource
        self._base_url = "https://swapi.info/api"
        self.logger.info(f"SWAPIReader initialized for endpoint '{self._resource}'")
        if self.debug:
            self.logger.debug(f"dataclass_type={dataclass_type.__name__}, resource={resource}")

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def resource(self) -> str:
        return self._resource

    def fetch(self) -> List[Person]:
        url = f"{self.base_url.rstrip('/')}/{self.resource}"
        self.logger.info(f"Fetching data from {url}")
        self.logger.debug(f"Sending GET request to {url}")
        try:
            resp = requests.get(url, timeout=20)
            resp.raise_for_status()
            results = resp.json()
            self.logger.info(f"Fetched {len(results)} records from {self.resource}")
            if self.debug and results:
                self.logger.debug(f"First record preview: {results[0]}")
            encryptor = JSONKeyEncryptor(key=os.getenv("FERNET_KEY"))
            encrypted_results = []
            for item in results:
                if "birth_year" in item:
                    item["birth_year"] = encryptor.encrypt_value(item.pop("birth_year"))
                encrypted_results.append(item)
            return [self.dataclass_type(**item) for item in encrypted_results]
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch {self.resource}: {e}")
            return []