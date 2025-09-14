from unittest.mock import Mock
from praktikum.burger import Burger
from data import BunData, IngrData, Receipt


class TestBurger:
    def test_set_burger(self):
        mock_bun = Mock()
        cheeseburger = Burger()
        cheeseburger.set_buns(mock_bun)
        assert cheeseburger.bun == mock_bun


    def test_get_price(self):
        mock_bun = Mock()
        cheeseburger = Burger()
        mock_bun.get_price.return_value = 500
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 250
        cheeseburger.bun = mock_bun
        cheeseburger.ingredients = [mock_ingredient]
        assert cheeseburger.get_price() == 500*2+250



    def test_add_ingredient(self):
        mock_ingredient = Mock()
        cheeseburger = Burger()
        cheeseburger.add_ingredient(mock_ingredient)
        assert cheeseburger.ingredients == [mock_ingredient]



    def test_move_ingredient(self):
        mock_ingredient = Mock()
        royalcheese = Burger()
        royalcheese.add_ingredient(mock_ingredient)
        royalcheese.add_ingredient(mock_ingredient)
        royalcheese.add_ingredient(mock_ingredient)
        royalcheese.add_ingredient(mock_ingredient)
        royalcheese.move_ingredient(0, 1)
        assert len(royalcheese.ingredients) == 4



    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        cheeseburger = Burger()
        cheeseburger.add_ingredient(mock_ingredient)
        cheeseburger.remove_ingredient(0)
        assert cheeseburger.ingredients == []



    def test_get_receipt(self):
        bigmak = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = BunData.bun_name
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = IngrData.ingr_type
        mock_ingredient.get_name.return_value = IngrData.ingr_name
        mock_bun.get_price.return_value = 75
        mock_ingredient.get_price.return_value = 30
        bigmak.bun = mock_bun
        bigmak.ingredients = [mock_ingredient]
        expected_receipt = Receipt.receipt_body
        assert bigmak.get_receipt() == expected_receipt







