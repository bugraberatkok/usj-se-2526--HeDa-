class ConversationData:
    def __init__(self, data: str):
        if not data or not data.strip():
            raise ValueError("Conversation data cannot be empty")
        self._value = data.strip()

    def __eq__(self, other):
        return isinstance(other, ConversationData) and self._value == other._value

    def __str__(self):
        return self._value

    def value(self):
        return self._value
