# -*- coding: utf-8 -*-

"""Akvo RSR is covered by the GNU Affero General Public License.
See more details in the license.txt file located at the root folder of the
Akvo RSR module. For additional details on the GNU license please
see < http://www.gnu.org/licenses/agpl.html >.
"""

M49_CODES = (
    (
        u"",
        u"World"
    ),
    (
        u"2",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Africa"
    ),
    (
        u"14",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Eastern Africa"
    ),
    (
        u"108",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Burundi"
    ),
    (
        u"174",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Comoros"
    ),
    (
        u"262",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Djibouti"
    ),
    (
        u"232",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Eritrea"
    ),
    (
        u"231",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Ethiopia"
    ),
    (
        u"404",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Kenya"
    ),
    (
        u"450",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Madagascar"
    ),
    (
        u"454",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Malawi"
    ),
    (
        u"480",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Mauritius"
    ),
    (
        u"175",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Mayotte"
    ),
    (
        u"508",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Mozambique"
    ),
    (
        u"638",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Réunion"
    ),
    (
        u"646",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Rwanda"
    ),
    (
        u"690",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Seychelles"
    ),
    (
        u"706",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Somalia"
    ),
    (
        u"728",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"South Sudan"
    ),
    (
        u"800",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Uganda"
    ),
    (
        u"834",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"United Republic of Tanzania"
    ),
    (
        u"894",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Zambia"
    ),
    (
        u"716",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Zimbabwe"
    ),
    (
        u"17",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Middle Africa"
    ),
    (
        u"24",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Angola"
    ),
    (
        u"120",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Cameroon"
    ),
    (
        u"140",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Central African Republic"
    ),
    (
        u"148",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Chad"
    ),
    (
        u"178",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Congo"
    ),
    (
        u"180",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Democratic Republic of the Congo"
    ),
    (
        u"226",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Equatorial Guinea"
    ),
    (
        u"266",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Gabon"
    ),
    (
        u"678",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Sao Tome and Principe"
    ),
    (
        u"15",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Northern Africa"
    ),
    (
        u"12",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Algeria"
    ),
    (
        u"818",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Egypt"
    ),
    (
        u"434",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Libya"
    ),
    (
        u"504",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Morocco"
    ),
    (
        u"729",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Sudan"
    ),
    (
        u"788",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Tunisia"
    ),
    (
        u"732",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Western Sahara"
    ),
    (
        u"18",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Southern Africa"
    ),
    (
        u"72",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Botswana"
    ),
    (
        u"426",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Lesotho"
    ),
    (
        u"516",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Namibia"
    ),
    (
        u"710",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"South Africa"
    ),
    (
        u"748",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Swaziland"
    ),
    (
        u"11",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Western Africa"
    ),
    (
        u"204",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Benin"
    ),
    (
        u"854",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Burkina Faso"
    ),
    (
        u"132",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Cabo Verde"
    ),
    (
        u"384",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Cote d'Ivoire"
    ),
    (
        u"270",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Gambia"
    ),
    (
        u"288",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Ghana"
    ),
    (
        u"324",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Guinea"
    ),
    (
        u"624",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Guinea-Bissau"
    ),
    (
        u"430",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Liberia"
    ),
    (
        u"466",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Mali"
    ),
    (
        u"478",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Mauritania"
    ),
    (
        u"562",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Niger"
    ),
    (
        u"566",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Nigeria"
    ),
    (
        u"654",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Saint Helena"
    ),
    (
        u"686",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Senegal"
    ),
    (
        u"694",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Sierra Leone"
    ),
    (
        u"768",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Togo"
    ),
    (
        u"19",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Americas"
    ),
    # Continent of North America consists of the Caribbean and Northern America, doesn't fit in hierarchy
    #
    # (
    #     u"3",
    #     u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"North America"
    # ),
    (
        u"419",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Latin America and the Caribbean"
    ),
    (
        u"29",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Caribbean"
    ),
    (
        u"660",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Anguilla"
    ),
    (
        u"28",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Antigua and Barbuda"
    ),
    (
        u"533",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Aruba"
    ),
    (
        u"44",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Bahamas"
    ),
    (
        u"52",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Barbados"
    ),
    (
        u"535",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Bonaire, Sint Eustatius and Saba"
    ),
    (
        u"92",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"British Virgin Islands"
    ),
    (
        u"136",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Cayman Islands"
    ),
    (
        u"192",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Cuba"
    ),
    (
        u"531",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Curaçao"
    ),
    (
        u"212",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Dominica"
    ),
    (
        u"214",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Dominican Republic"
    ),
    (
        u"308",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Grenada"
    ),
    (
        u"312",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Guadeloupe"
    ),
    (
        u"332",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Haiti"
    ),
    (
        u"388",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Jamaica"
    ),
    (
        u"474",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Martinique"
    ),
    (
        u"500",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Montserrat"
    ),
    (
        u"630",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Puerto Rico"
    ),
    (
        u"652",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Saint-Barthélemy"
    ),
    (
        u"659",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Saint Kitts and Nevis"
    ),
    (
        u"662",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Saint Lucia"
    ),
    (
        u"663",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Saint Martin (French part)"
    ),
    (
        u"670",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Saint Vincent and the Grenadines"
    ),
    (
        u"534",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Sint Maarten (Dutch part)"
    ),
    (
        u"780",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Trinidad and Tobago"
    ),
    (
        u"796",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Turks and Caicos Islands"
    ),
    (
        u"850",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"United States Virgin Islands"
    ),
    (
        u"13",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Central America"
    ),
    (
        u"84",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Belize"
    ),
    (
        u"188",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Costa Rica"
    ),
    (
        u"222",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"El Salvador"
    ),
    (
        u"320",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Guatemala"
    ),
    (
        u"340",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Honduras"
    ),
    (
        u"484",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Mexico"
    ),
    (
        u"558",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Nicaragua"
    ),
    (
        u"591",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Panama"
    ),
    (
        u"5",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"South America"
    ),
    (
        u"32",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Argentina"
    ),
    (
        u"68",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Bolivia (Plurinational State of)"
    ),
    (
        u"76",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Brazil"
    ),
    (
        u"152",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Chile"
    ),
    (
        u"170",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Colombia"
    ),
    (
        u"218",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Ecuador"
    ),
    (
        u"238",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Falkland Islands (Malvinas)"
    ),
    (
        u"254",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"French Guiana"
    ),
    (
        u"328",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Guyana"
    ),
    (
        u"600",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Paraguay"
    ),
    (
        u"604",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Peru"
    ),
    (
        u"740",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Suriname"
    ),
    (
        u"858",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Uruguay"
    ),
    (
        u"862",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Venezuela (Bolivarian Republic of)"
    ),
    (
        u"21",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Northern America"
    ),
    (
        u"60",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Bermuda"
    ),
    (
        u"124",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Canada"
    ),
    (
        u"304",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Greenland"
    ),
    (
        u"666",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Saint Pierre and Miquelon"
    ),
    (
        u"840",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"United States of America"
    ),
    (
        u"142",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Asia"
    ),
    (
        u"143",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Central Asia"
    ),
    (
        u"398",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Kazakhstan"
    ),
    (
        u"417",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Kyrgyzstan"
    ),
    (
        u"762",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Tajikistan"
    ),
    (
        u"795",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Turkmenistan"
    ),
    (
        u"860",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Uzbekistan"
    ),
    (
        u"30",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Eastern Asia"
    ),
    (
        u"156",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"China"
    ),
    (
        u"344",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"China, Hong Kong Special Administrative Region"
    ),
    (
        u"446",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"China, Macao Special Administrative Region"
    ),
    (
        u"408",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Democratic People's Republic of Korea"
    ),
    (
        u"392",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Japan"
    ),
    (
        u"496",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Mongolia"
    ),
    (
        u"410",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Republic of Korea"
    ),
    (
        u"34",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Southern Asia"
    ),
    (
        u"4",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Afghanistan"
    ),
    (
        u"50",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Bangladesh"
    ),
    (
        u"64",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Bhutan"
    ),
    (
        u"356",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"India"
    ),
    (
        u"364",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Iran (Islamic Republic of)"
    ),
    (
        u"462",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Maldives"
    ),
    (
        u"524",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Nepal"
    ),
    (
        u"586",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Pakistan"
    ),
    (
        u"144",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Sri Lanka"
    ),
    (
        u"35",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"South-Eastern Asia"
    ),
    (
        u"96",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Brunei Darussalam"
    ),
    (
        u"116",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Cambodia"
    ),
    (
        u"360",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Indonesia"
    ),
    (
        u"418",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Lao People's Democratic Republic"
    ),
    (
        u"458",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Malaysia"
    ),
    (
        u"104",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Myanmar"
    ),
    (
        u"608",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Philippines"
    ),
    (
        u"702",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Singapore"
    ),
    (
        u"764",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Thailand"
    ),
    (
        u"626",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Timor-Leste"
    ),
    (
        u"704",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Viet Nam"
    ),
    (
        u"145",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Western Asia"
    ),
    (
        u"51",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Armenia"
    ),
    (
        u"31",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Azerbaijan"
    ),
    (
        u"48",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Bahrain"
    ),
    (
        u"196",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Cyprus"
    ),
    (
        u"268",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Georgia"
    ),
    (
        u"368",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Iraq"
    ),
    (
        u"376",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Israel"
    ),
    (
        u"400",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Jordan"
    ),
    (
        u"414",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Kuwait"
    ),
    (
        u"422",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Lebanon"
    ),
    (
        u"512",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Oman"
    ),
    (
        u"634",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Qatar"
    ),
    (
        u"682",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Saudi Arabia"
    ),
    (
        u"275",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"State of Palestine"
    ),
    (
        u"760",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Syrian Arab Republic"
    ),
    (
        u"792",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Turkey"
    ),
    (
        u"784",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"United Arab Emirates"
    ),
    (
        u"887",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Yemen"
    ),
    (
        u"150",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Europe"
    ),
    (
        u"151",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Eastern Europe"
    ),
    (
        u"112",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Belarus"
    ),
    (
        u"100",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Bulgaria"
    ),
    (
        u"203",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Czech Republic"
    ),
    (
        u"348",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Hungary"
    ),
    (
        u"616",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Poland"
    ),
    (
        u"498",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Republic of Moldova"
    ),
    (
        u"642",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Romania"
    ),
    (
        u"643",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Russian Federation"
    ),
    (
        u"703",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Slovakia"
    ),
    (
        u"804",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Ukraine"
    ),
    (
        u"154",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Northern Europe"
    ),
    (
        u"248",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Åland Islands"
    ),
    (
        u"208",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Denmark"
    ),
    (
        u"233",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Estonia"
    ),
    (
        u"234",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Faeroe Islands"
    ),
    (
        u"246",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Finland"
    ),
    (
        u"831",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Guernsey"
    ),
    (
        u"352",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Iceland"
    ),
    (
        u"372",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Ireland"
    ),
    (
        u"833",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Isle of Man"
    ),
    (
        u"832",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Jersey"
    ),
    (
        u"428",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Latvia"
    ),
    (
        u"440",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Lithuania"
    ),
    (
        u"578",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Norway"
    ),
    (
        u"744",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Svalbard and Jan Mayen Islands"
    ),
    (
        u"752",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Sweden"
    ),
    (
        u"826",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"United Kingdom of Great Britain and Northern Ireland"
    ),
    (
        u"39",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Southern Europe"
    ),
    (
        u"8",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Albania"
    ),
    (
        u"20",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Andorra"
    ),
    (
        u"70",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Bosnia and Herzegovina"
    ),
    (
        u"191",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Croatia"
    ),
    (
        u"292",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Gibraltar"
    ),
    (
        u"300",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Greece"
    ),
    (
        u"336",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Holy See"
    ),
    (
        u"380",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Italy"
    ),
    (
        u"470",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Malta"
    ),
    (
        u"499",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Montenegro"
    ),
    (
        u"620",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Portugal"
    ),
    (
        u"674",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"San Marino"
    ),
    (
        u"688",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Serbia"
    ),
    (
        u"705",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Slovenia"
    ),
    (
        u"724",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Spain"
    ),
    (
        u"807",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"The former Yugoslav Republic of Macedonia"
    ),
    (
        u"155",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Western Europe"
    ),
    (
        u"40",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Austria"
    ),
    (
        u"56",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Belgium"
    ),
    (
        u"250",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"France"
    ),
    (
        u"276",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Germany"
    ),
    (
        u"438",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Liechtenstein"
    ),
    (
        u"442",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Luxembourg"
    ),
    (
        u"492",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Monaco"
    ),
    (
        u"528",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Netherlands"
    ),
    (
        u"756",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Switzerland"
    ),
    (
        u"9",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Oceania"
    ),
    (
        u"53",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Australia and New Zealand"
    ),
    (
        u"36",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Australia"
    ),
    (
        u"554",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"New Zealand"
    ),
    (
        u"574",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Norfolk Island"
    ),
    (
        u"54",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Melanesia"
    ),
    (
        u"242",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Fiji"
    ),
    (
        u"540",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"New Caledonia"
    ),
    (
        u"598",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Papua New Guinea"
    ),
    (
        u"90",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Solomon Islands"
    ),
    (
        u"548",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Vanuatu"
    ),
    (
        u"57",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Micronesia"
    ),
    (
        u"316",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Guam"
    ),
    (
        u"296",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Kiribati"
    ),
    (
        u"584",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Marshall Islands"
    ),
    (
        u"583",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Micronesia (Federated States of)"
    ),
    (
        u"520",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Nauru"
    ),
    (
        u"580",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Northern Mariana Islands"
    ),
    (
        u"585",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Palau"
    ),
    (
        u"61",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Polynesia"
    ),
    (
        u"16",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"American Samoa"
    ),
    (
        u"184",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Cook Islands"
    ),
    (
        u"258",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"French Polynesia"
    ),
    (
        u"570",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Niue"
    ),
    (
        u"612",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Pitcairn"
    ),
    (
        u"882",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Samoa"
    ),
    (
        u"772",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Tokelau"
    ),
    (
        u"776",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Tonga"
    ),
    (
        u"798",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Tuvalu"
    ),
    (
        u"876",
        u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"\u00A0" + u"Wallis and Futuna Islands"
    ),
)


# Dictionary of M.49 Alpha country and region codes, based on http://unstats.un.org/unsd/methods/m49/m49regin.htm

M49_HIERARCHY = {
    1: [2, 19, 142, 150, 9],
    2: [14, 17, 15, 18, 11],
    3: [21, 29, 13],
    4: ["AF", ],
    5: [32, 68, 76, 152, 170, 218, 238, 254, 328, 600, 604, 740, 858, 862],
    8: ["AL", ],
    9: [53, 54, 57, 61],
    11: [204, 854, 132, 384, 270, 288, 324, 624, 430, 466, 478, 562, 566, 654, 686, 694, 768],
    12: ["DZ", ],
    13: [84, 188, 222, 320, 340, 484, 558, 591],
    14: [108, 174, 262, 232, 231, 404, 450, 454, 480, 175, 508, 638, 646, 690, 706, 728, 800, 834, 894, 716],
    15: [12, 818, 434, 504, 729, 788, 732],
    16: ["AS", ],
    17: [24, 120, 140, 148, 178, 180, 226, 266, 678],
    18: [72, 426, 516, 710, 748],
    19: [419, 21],
    20: ["AD", ],
    21: [60, 124, 304, 666, 840],
    24: ["AO", ],
    28: ["AG", ],
    29: [660, 28, 533, 44, 52, 535, 92, 136, 192, 531, 212, 214, 308, 312, 332, 388, 474, 500, 630, 652, 659, 662, 663,
         670, 534, 780, 796, 850],
    30: [156, 344, 446, 408, 392, 496, 410],
    31: ["AZ", ],
    32: ["AR", ],
    34: [4, 50, 64, 356, 364, 462, 524, 586, 144],
    35: [96, 116, 360, 418, 458, 104, 608, 702, 764, 626, 704],
    36: ["AU", ],
    39: [8, 20, 70, 191, 292, 300, 336, 380, 470, 499, 620, 674, 688, 705, 724, 807],
    40: ["AT", ],
    44: ["BS", ],
    48: ["BH", ],
    50: ["BD", ],
    51: ["AM", ],
    52: ["BB", ],
    53: [36, 554, 574],
    54: [242, 540, 598, 90, 548],
    56: ["BE", ],
    57: [316, 296, 584, 583, 520, 580, 585],
    60: ["BM", ],
    61: [16, 184, 258, 570, 612, 882, 772, 776, 798, 876],
    64: ["BT", ],
    68: ["BO", ],
    70: ["BA", ],
    72: ["BW", ],
    76: ["BR", ],
    84: ["BZ", ],
    90: ["SB", ],
    92: ["VG", ],
    96: ["BN", ],
    100: ["BG", ],
    104: ["MM", ],
    108: ["BI", ],
    112: ["BY", ],
    116: ["KH", ],
    120: ["CM", ],
    124: ["CA", ],
    132: ["CV", ],
    136: ["KY", ],
    140: ["CF", ],
    142: [143, 30, 34, 35, 145],
    143: [398, 417, 762, 795, 860],
    144: ["LK", ],
    145: [51, 31, 48, 196, 268, 368, 376, 400, 414, 422, 512, 634, 682, 275, 760, 792, 784, 887],
    148: ["TD", ],
    150: [151, 154, 39, 155],
    151: [112, 100, 203, 348, 616, 498, 642, 643, 703, 804],
    152: ["CL", ],
    154: [248, 208, 233, 234, 246, 831, 352, 372, 833, 832, 428, 440, 578, 744, 752, 826],
    155: [40, 56, 250, 276, 438, 442, 492, 528, 756],
    156: ["CN", ],
    170: ["CO", ],
    174: ["KM", ],
    175: ["YT", ],
    178: ["CG", ],
    180: ["CD", ],
    184: ["CK", ],
    188: ["CR", ],
    191: ["HR", ],
    192: ["CU", ],
    196: ["CY", ],
    203: ["CZ", ],
    204: ["BJ", ],
    208: ["DK", ],
    212: ["DM", ],
    214: ["DO", ],
    218: ["EC", ],
    222: ["SV", ],
    226: ["GQ", ],
    231: ["ET", ],
    232: ["ER", ],
    233: ["EE", ],
    234: ["FO", ],
    238: ["FK", ],
    242: ["FJ", ],
    246: ["FI", ],
    248: ["AX", ],
    250: ["FR", ],
    254: ["GF", ],
    258: ["PF", ],
    262: ["DJ", ],
    266: ["GA", ],
    268: ["GE", ],
    270: ["GM", ],
    275: ["PS", ],
    276: ["DE", ],
    288: ["GH", ],
    292: ["GI", ],
    296: ["KI", ],
    300: ["GR", ],
    304: ["GL", ],
    308: ["GD", ],
    312: ["GP", ],
    316: ["GU", ],
    320: ["GT", ],
    324: ["GN", ],
    328: ["GY", ],
    332: ["HT", ],
    336: ["VA", ],
    340: ["HN", ],
    344: ["HK", ],
    348: ["HU", ],
    352: ["IS", ],
    356: ["IN", ],
    360: ["ID", ],
    364: ["IR", ],
    368: ["IQ", ],
    372: ["IE", ],
    376: ["IL", ],
    380: ["IT", ],
    384: ["CI", ],
    388: ["JM", ],
    392: ["JP", ],
    398: ["KZ", ],
    400: ["JO", ],
    404: ["KE", ],
    408: ["KP", ],
    410: ["KR", ],
    414: ["KW", ],
    417: ["KG", ],
    418: ["LA", ],
    419: [29, 13, 5],
    422: ["LB", ],
    426: ["LS", ],
    428: ["LV", ],
    430: ["LR", ],
    434: ["LY", ],
    438: ["LI", ],
    440: ["LT", ],
    442: ["LU", ],
    446: ["MO", ],
    450: ["MG", ],
    454: ["MW", ],
    458: ["MY", ],
    462: ["MV", ],
    466: ["ML", ],
    470: ["MT", ],
    474: ["MQ", ],
    478: ["MR", ],
    480: ["MU", ],
    484: ["MX", ],
    492: ["MC", ],
    496: ["MN", ],
    498: ["MD", ],
    499: ["ME", ],
    500: ["MS", ],
    504: ["MA", ],
    508: ["MZ", ],
    512: ["OM", ],
    516: ["NA", ],
    520: ["NR", ],
    524: ["NP", ],
    528: ["NL", ],
    531: ["CW", ],
    533: ["AW", ],
    534: ["SX", ],
    535: ["BQ", ],
    540: ["NC", ],
    548: ["VU", ],
    554: ["NZ", ],
    558: ["NI", ],
    562: ["NE", ],
    566: ["NG", ],
    570: ["NU", ],
    574: ["NF", ],
    578: ["NO", ],
    580: ["MP", ],
    583: ["FM", ],
    584: ["MH", ],
    585: ["PW", ],
    586: ["PK", ],
    591: ["PA", ],
    598: ["PG", ],
    600: ["PY", ],
    604: ["PE", ],
    608: ["PH", ],
    612: ["PN", ],
    616: ["PL", ],
    620: ["PT", ],
    624: ["GW", ],
    626: ["TL", ],
    630: ["PR", ],
    634: ["QA", ],
    638: ["RE", ],
    642: ["RO", ],
    643: ["RU", ],
    646: ["RW", ],
    652: ["BL", ],
    654: ["SH", ],
    659: ["KN", ],
    660: ["AI", ],
    662: ["LC", ],
    663: ["MF", ],
    666: ["PM", ],
    670: ["VC", ],
    674: ["SM", ],
    678: ["ST", ],
    682: ["SA", ],
    686: ["SN", ],
    688: ["RS", ],
    690: ["SC", ],
    694: ["SL", ],
    702: ["SG", ],
    703: ["SK", ],
    704: ["VN", ],
    705: ["SI", ],
    706: ["SO", ],
    710: ["ZA", ],
    716: ["ZW", ],
    724: ["ES", ],
    728: ["SS", ],
    729: ["SD", ],
    732: ["EH", ],
    740: ["SR", ],
    744: ["SJ", ],
    748: ["SZ", ],
    752: ["SE", ],
    756: ["CH", ],
    760: ["SY", ],
    762: ["TJ", ],
    764: ["TH", ],
    768: ["TG", ],
    772: ["TK", ],
    776: ["TO", ],
    780: ["TT", ],
    784: ["AE", ],
    788: ["TN", ],
    792: ["TR", ],
    795: ["TM", ],
    796: ["TC", ],
    798: ["TV", ],
    800: ["UG", ],
    804: ["UA", ],
    807: ["MK", ],
    818: ["EG", ],
    826: ["GB", ],
    831: ["GG", ],
    832: ["JE", ],
    833: ["IM", ],
    834: ["TZ", ],
    840: ["US", ],
    850: ["VI", ],
    854: ["BF", ],
    858: ["UY", ],
    860: ["UZ", ],
    862: ["VE", ],
    876: ["WF", ],
    882: ["WS", ],
    887: ["YE", ],
    894: ["ZM", ],
}