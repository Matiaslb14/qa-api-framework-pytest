from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    BASE_URL: str = "https://jsonplaceholder.typicode.com"
    TIMEOUT: int = 10
    DEFAULT_HEADERS: dict = None

    def __post_init__(self):
        object.__setattr__(
            self,
            "DEFAULT_HEADERS",
            {"Content-Type": "application/json; charset=UTF-8"},
        )


settings = Settings()
