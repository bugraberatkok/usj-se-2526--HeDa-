class DataAnalysisContent:
    def __init__(self, content: str):
        if not content or not content.strip():
            raise ValueError("Data analysis content cannot be empty")
        self._value = content.strip()

    def __eq__(self, other):
        return isinstance(other, DataAnalysisContent) and self._value == other._value

    def __str__(self):
        return self._value

    def value(self):
        return self._value
