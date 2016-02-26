import unittest


def multiply(a, b):
    return a + b

# Muss mit Test... beginnen!


class TestMyTestName(unittest.TestCase):
    # Zum "vorbereiten" des Tests

    def setUp(self):
        pass
    # Muss mit test... beginnen

    def test_MyFirstTest(self):
        # Arrange
        # Act
        result = multiply(7, 5)
        # Assert
        self.assertEqual(35, result)

# Falls diese Datei direkt aufgerufen wird: Unittest starten
if __name__ == "__main__":
    unittest.main()
