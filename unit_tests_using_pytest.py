import pytest
from pokemon_attributes import PokeMon


# top row is base stats, bottom row is expected stats after setting stats and IVs
# (Pokédex ID, Name, Type1, Type2, Total, HP, ATK, DEF, SPATK, SPDEF, SPD, Gen, Legendary)
# (Lv. 100 for all for consistency, to be randomized later)
@pytest.mark.parametrize('DexID, Name, Type1, Type2, Total, HP, ATK, DEF, SPATK, SPDEF, SPD, gen, legendary, \
                          eDexID, eName, eType1, eType2, eTotal, eHP, eATK, eDEF, eSPATK, eSPDEF, eSPD, egen, elegendary',
                         [
                             (7, 'Squirtle', 'Water', '', 314, 44, 48, 65, 50, 64, 43, 1, 'False',
                              7, 'Squirtle', 'Water', '', 825, 205, 102, 152, 120, 147, 99, 1, 'False'),
                             (384, 'Rayquaza', 'Dragon', 'Flying', 680, 105, 150, 90, 150, 90, 95, 3, 'True',
                              384, 'Rayquaza', 'Dragon', 'Flying', 1541, 326, 310, 212, 307, 186, 200, 3, 'True'),
                             (36, 'Clefable', 'Fairy', '', 483, 95, 70, 73, 95, 90, 60, 1, 'False',
                              36, 'Clefable', 'Fairy', '', 1181, 313, 159, 152, 207, 211, 139, 1, 'False'),
                             (350, 'Milotic', 'Water', '', 540, 95, 60, 79, 100, 125, 81, 3, 'False',
                              350, 'Milotic', 'Water', '', 1318, 328, 142, 163, 215, 282, 188, 3, 'False'),
                             (445, 'Garchomp', 'Dragon', 'Ground', 600, 108, 130, 95, 80, 85, 102, 4, 'False',
                              445, 'Garchomp', 'Dragon', 'Ground', 1406, 343, 274, 208, 186, 181, 214, 4, 'False'),
                             (376, 'Metagross', 'Steel', 'Psychic', 600, 80, 135, 130, 95, 90, 70, 3, 'False',
                              376, 'Metagross', 'Steel', 'Psychic', 1427, 294, 281, 287, 217, 201, 147, 3, 'False')
                         ])
def test_set_stats_ivs(DexID, Name, Type1, Type2, Total, HP, ATK, DEF, SPATK, SPDEF, SPD, gen, legendary,
                          eDexID, eName, eType1, eType2, eTotal, eHP, eATK, eDEF, eSPATK, eSPDEF, eSPD, egen, elegendary):

    temp = PokeMon((DexID, Name, Type1, Type2, Total, HP, ATK, DEF, SPATK, SPDEF, SPD, gen, legendary))
    actual = (temp.id, temp.name, temp.type1, temp.type2, temp.total, temp.hp, temp.attack, temp.defense, temp.special_attack, temp.special_defense, temp.speed, temp.generation, temp.isLegendary)
    expected = (eDexID, eName, eType1, eType2, eTotal, eHP, eATK, eDEF, eSPATK, eSPDEF, eSPD, egen, elegendary)
    assert actual == expected


@pytest.mark.parametrize('DexID, Name, Type1, Type2, Total, HP, ATK, DEF, SPATK, SPDEF, SPD, gen, legendary, \
                          eDexID, eName, eType1, eType2, eTotal, eHP, eATK, eDEF, eSPATK, eSPDEF, eSPD, egen, elegendary',
                         [
                             (7, 'Squirtle', 'Water', '', 314, 44, 48, 65, 50, 64, 43, 1, 'False',
                              7, 'Squirtle', 'Water', '', 825, 205, 112, 152, 108, 147, 99, 1, 'False'),
                             (384, 'Rayquaza', 'Dragon', 'Flying', 680, 105, 150, 90, 150, 90, 95, 3, 'True',
                              384, 'Rayquaza', 'Dragon', 'Flying', 1541, 326, 341, 212, 276, 186, 200, 3, 'True'),
                             (36, 'Clefable', 'Fairy', '', 483, 95, 70, 73, 95, 90, 60, 1, 'False',
                              36, 'Clefable', 'Fairy', '', 1181, 313, 174, 152, 186, 211, 139, 1, 'False'),
                             (350, 'Milotic', 'Water', '', 540, 95, 60, 79, 100, 125, 81, 3, 'False',
                              350, 'Milotic', 'Water', '', 1318, 328, 156, 163, 193, 282, 188, 3, 'False'),
                             (445, 'Garchomp', 'Dragon', 'Ground', 600, 108, 130, 95, 80, 85, 102, 4, 'False',
                              445, 'Garchomp', 'Dragon', 'Ground', 1406, 343, 301, 208, 167, 181, 214, 4, 'False'),
                             (376, 'Metagross', 'Steel', 'Psychic', 600, 80, 135, 130, 95, 90, 70, 3, 'False',
                              376, 'Metagross', 'Steel', 'Psychic', 1427, 294, 309, 287, 195, 201, 147, 3, 'False')
                         ])
def test_set_nature(DexID, Name, Type1, Type2, Total, HP, ATK, DEF, SPATK, SPDEF, SPD, gen, legendary,
                          eDexID, eName, eType1, eType2, eTotal, eHP, eATK, eDEF, eSPATK, eSPDEF, eSPD, egen, elegendary):
    temp = PokeMon((DexID, Name, Type1, Type2, Total, HP, ATK, DEF, SPATK, SPDEF, SPD, gen, legendary))
    temp.update_nature_stats(3)
    actual = (temp.id, temp.name, temp.type1, temp.type2, temp.total, temp.hp, temp.attack, temp.defense, temp.special_attack, temp.special_defense, temp.speed, temp.generation, temp.isLegendary)
    expected = (eDexID, eName, eType1, eType2, eTotal, eHP, eATK, eDEF, eSPATK, eSPDEF, eSPD, egen, elegendary)
    assert actual == expected
