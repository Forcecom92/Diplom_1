import pytest
from praktikum.bun import Bun
from data import BunData, IngrData
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


@pytest.fixture()
def set_data_bun():
    bun = Bun(BunData.bun_name, BunData.bun_price)

    return bun


@pytest.fixture()
def set_data_ingr():
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, IngrData.ingr_name, IngrData.ingr_price)

    return ingredient