import pytest
from datetime import datetime, timedelta
from review import Review



# функція для створення коректного відгуку

def make_review(score=3, author="John Doe", source="google", days_ago=5):
    created = datetime.now() - timedelta(days=days_ago)
    return Review(1, created, score, author, source)

# Тести методу validate()


def test_validate_valid_review():
    # Arrange
    review = make_review(score=3, author="Alice", source="google")
    # Act
    result = review.validate()
    # Assert
    assert result # EP: позитивний — всі поля коректні


def test_validate_score_minimum():
    # Arrange
    review = make_review(score=1)
    # Act
    result = review.validate()
    # Assert
    assert result # BVA: межа знизу — score=1 є допустимим


def test_validate_score_maximum():
    # Arrange
    review = make_review(score=5)
    # Act
    result = review.validate()
    # Assert
    assert result # BVA: межа зверху — score=5 є допустимим


def test_validate_score_below_minimum():
    # Arrange
    review = make_review(score=0)
    # Act + Assert
    with pytest.raises(ValueError):
        review.validate()  # BVA: score=0 нижче межі → помилка


def test_validate_score_above_maximum():
    # Arrange
    review = make_review(score=6)
    # Act + Assert
    with pytest.raises(ValueError):
        review.validate()  # BVA: score=6 вище межі → помилка


def test_validate_score_negative():
    # Arrange
    review = make_review(score=-1)
    # Act + Assert
    with pytest.raises(ValueError):
        review.validate()  # EP: негативний — від'ємний score → помилка


def test_validate_empty_author_name():
    # Arrange
    review = make_review(author="")
    # Act + Assert
    with pytest.raises(ValueError):
        review.validate()  # EP: негативний — порожнє ім'я → помилка


def test_validate_whitespace_author_name():
    # Arrange
    review = make_review(author="   ")
    # Act + Assert
    with pytest.raises(ValueError):
        review.validate()  # EP: негативний — ім'я з пробілів → помилка


def test_validate_invalid_source():
    # Arrange
    review = make_review(source="facebook")
    # Act + Assert
    with pytest.raises(ValueError):
        review.validate()  # EP: негативний — недопустиме джерело → помилка


def test_validate_valid_source_yelp():
    # Arrange
    review = make_review(source="yelp")
    # Act
    result = review.validate()
    # Assert
    assert result # EP: позитивний — "yelp" є допустимим джерелом


# Тести методу is_recent()

def test_is_recent_new_review():
    # Arrange
    review = make_review(days_ago=5)
    # Act
    result = review.is_recent(days=30)
    # Assert
    assert result # EP: позитивний — свіжий відгук


def test_is_recent_old_review():
    # Arrange
    review = make_review(days_ago=31)
    # Act
    result = review.is_recent(days=30)
    # Assert
    assert not result   # BVA: days_ago=31 > межі 30 → не свіжий


def test_is_recent_exactly_on_boundary():
    # Arrange
    review = make_review(days_ago=30)
    # Act
    result = review.is_recent(days=30)
    # Assert
    assert result # BVA: межа — рівно 30 днів → ще свіжий


def test_is_recent_negative_days():
    # Arrange
    review = make_review(days_ago=1)
    # Act + Assert
    with pytest.raises(ValueError):
        review.is_recent(days=-1)  # EP: негативний — days=-1 → помилка



# Тести методу to_dict()

def test_to_dict_returns_correct_keys():
    # Arrange
    review = make_review()
    # Act
    result = review.to_dict()
    # Assert
    assert set(result.keys()) == {
        "review_id", "created_at", "score", "author_name", "source"
    }  # EP: позитивний — словник містить всі потрібні ключі


def test_to_dict_returns_correct_values():
    # Arrange
    created = datetime(2024, 6, 15, 12, 0, 0)
    review = Review(42, created, 4, "Bob", "tripadvisor")
    # Act
    result = review.to_dict()
    # Assert
    assert result["review_id"] == 42
    assert result["score"] == 4
    assert result["author_name"] == "Bob"
    assert result["source"] == "tripadvisor"
    assert result["created_at"] == "2024-06-15T12:00:00"  # EP: позитивний — значення коректні

    