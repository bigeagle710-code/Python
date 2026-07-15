class RomanConverter:
    _ROMAN_MAP = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    def __init__(self, number: int):
        """Initializes the converter with a specific integer."""
        if not isinstance(number, int) or number <= 0 or number > 3999:
            raise ValueError("Roman numerals only support integers between 1 and 3999.")
        self.number = number

    def to_roman(self) -> str:
        """Converts the stored integer value to a Roman numeral string."""
        result = []
        temp_num = self.number
        for value, symbol in self._ROMAN_MAP:
            count = temp_num // value
            if count > 0:
                result.append(symbol * count)
                temp_num %= value  # Keep the remainder for the next loops

        return "".join(result)

if __name__ == "__main__":
    converter = RomanConverter(1998)
    
    print(f"Integer: {converter.number} -> Roman Numeral: {converter.to_roman()}")
