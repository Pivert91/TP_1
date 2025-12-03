# test_app.py
from app import addition

# Vérifie l'addition de nombres positifs
def test_addition_positive():
    assert addition(2, 3) == 5 [cite: 35, 36]

# Vérifie l'addition de nombres négatifs
def test_addition_negative():
    assert addition(-1, -2) == -3 [cite: 37, 38]
