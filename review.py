from datetime import datetime


class Review:
    VALID_SOURCES = {"google", "yelp"}

    def __init__(self, review_id: int, created_at: datetime, score: int, author_name: str, source: str):
        self.review_id = review_id
        self.created_at = created_at
        self.score = score
        self.author_name = author_name
        self.source = source

    def validate(self) -> bool:
        """Перевіряє коректність відгуку."""
        if not (1 <= self.score <= 5):
            raise ValueError("Score must be between 1 and 5")
        if not self.author_name or not self.author_name.strip():
            raise ValueError("Author name cannot be empty")
        if self.source.lower() not in self.VALID_SOURCES:
            raise ValueError(f"Source must be one of {self.VALID_SOURCES}")
        return True

    def is_recent(self, days: int = 30) -> bool:
        """Повертає True якщо відгук не старший за days днів."""
        if days < 0:
            raise ValueError("Days cannot be negative")
        delta = datetime.now() - self.created_at
        return delta.days <= days

    def to_dict(self) -> dict:
        """Повертає дані відгуку у вигляді словника."""
        return {
            "review_id": self.review_id,
            "created_at": self.created_at.isoformat(),
            "score": self.score,
            "author_name": self.author_name,
            "source": self.source
        }