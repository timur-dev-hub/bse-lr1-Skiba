from datetime import datetime


class Review:
    VALID_SOURCES = {"google", "yelp"}

    def __init__(self, review_id: int, createdAt: datetime, score: int, author_Name: str, source: str):
        self.review_id = review_id
        self.createdAt = createdAt
        self.score = score
        self.author_Name = author_Name
        self.source = source

    def validate(self) -> bool:
        """Перевіряє коректність відгуку."""
        if not (1 <= self.score <= 5):
            raise ValueError("Score must be between 1 and 5")
        if not self.author_Name or not self.author_Name.strip():
            raise ValueError("Author name cannot be empty")
        if self.source.lower() not in self.VALID_SOURCES:
            raise ValueError(f"Source must be one of {self.VALID_SOURCES}")
        return True

    def is_recent(self, days: int = 30) -> bool:
        """Повертає True якщо відгук не старший за days днів."""
        if days < 0:
            raise ValueError("Days cannot be negative")
        delta = datetime.now() - self.createdAt
        return delta.days <= days

    def to_dict(self) -> dict:
        """Повертає дані відгуку у вигляді словника."""
        return {
            "review_id": self.review_id,
            "createdAt": self.createdAt.isoformat(),
            "score": self.score,
            "author_Name": self.author_Name,
            "source": self.source
        }
    
    