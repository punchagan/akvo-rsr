# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import akvo.rsr.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rsr', '0071_auto_20160525_1036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipientcountry',
            options={'ordering': ('-percentage', 'country'), 'verbose_name': 'recipient country', 'verbose_name_plural': 'recipient countries'},
        ),
        migrations.RemoveField(
            model_name='projectupdatelocation',
            name='country',
        ),
        migrations.AddField(
            model_name='organisationlocation',
            name='iati_country',
            field=akvo.rsr.fields.ValidXMLCharField(blank=True, help_text='The country in which the organisation is located.', max_length=2, verbose_name='country', choices=[('AF', 'AF - Afghanistan'), ('AX', 'AX - \xc5land Islands'), ('AL', 'AL - Albania'), ('DZ', 'DZ - Algeria'), ('AS', 'AS - American Samoa'), ('AD', 'AD - Andorra'), ('AO', 'AO - Angola'), ('AI', 'AI - Anguilla'), ('AQ', 'AQ - Antarctica'), ('AG', 'AG - Antigua and Barbuda'), ('AR', 'AR - Argentina'), ('AM', 'AM - Armenia'), ('AW', 'AW - Aruba'), ('AU', 'AU - Australia'), ('AT', 'AT - Austria'), ('AZ', 'AZ - Azerbaijan'), ('BS', 'BS - Bahamas (The)'), ('BH', 'BH - Bahrain'), ('BD', 'BD - Bangladesh'), ('BB', 'BB - Barbados'), ('BY', 'BY - Belarus'), ('BE', 'BE - Belgium'), ('BZ', 'BZ - Belize'), ('BJ', 'BJ - Benin'), ('BM', 'BM - Bermuda'), ('BT', 'BT - Bhutan'), ('BO', 'BO - Bolivia (Plurinational State Of)'), ('BQ', 'BQ - Bonaire, Saint Eustatius and Saba'), ('BA', 'BA - Bosnia and Herzegovina'), ('BW', 'BW - Botswana'), ('BV', 'BV - Bouvet Island'), ('BR', 'BR - Brazil'), ('IO', 'IO - British Indian Ocean Territory (The)'), ('BN', 'BN - Brunei Darussalam'), ('BG', 'BG - Bulgaria'), ('BF', 'BF - Burkina Faso'), ('BI', 'BI - Burundi'), ('KH', 'KH - Cambodia'), ('CM', 'CM - Cameroon'), ('CA', 'CA - Canada'), ('CV', 'CV - Cape Verde'), ('KY', 'KY - Cayman Islands (The)'), ('CF', 'CF - Central African Republic (The)'), ('TD', 'TD - Chad'), ('CL', 'CL - Chile'), ('CN', 'CN - China'), ('CX', 'CX - Christmas Island'), ('CC', 'CC - Cocos (Keeling) Islands (The)'), ('CO', 'CO - Colombia'), ('KM', 'KM - Comoros (The)'), ('CG', 'CG - Congo (The)'), ('CD', 'CD - Congo, The Democratic Republic of the'), ('CK', 'CK - Cook Islands (The)'), ('CR', 'CR - Costa Rica'), ('CI', 'CI - C\xf4te Divoire'), ('HR', 'HR - Croatia'), ('CU', 'CU - Cuba'), ('CW', 'CW - Cura\xe7ao'), ('CY', 'CY - Cyprus'), ('CZ', 'CZ - Czech Republic (The)'), ('DK', 'DK - Denmark'), ('DJ', 'DJ - Djibouti'), ('DM', 'DM - Dominica'), ('DO', 'DO - Dominican Republic (The)'), ('EC', 'EC - Ecuador'), ('EG', 'EG - Egypt'), ('SV', 'SV - El Salvador'), ('GQ', 'GQ - Equatorial Guinea'), ('ER', 'ER - Eritrea'), ('EE', 'EE - Estonia'), ('ET', 'ET - Ethiopia'), ('FK', 'FK - Falkland Islands (The) [malvinas]'), ('FO', 'FO - Faroe Islands (The)'), ('FJ', 'FJ - Fiji'), ('FI', 'FI - Finland'), ('FR', 'FR - France'), ('GF', 'GF - French Guiana'), ('PF', 'PF - French Polynesia'), ('TF', 'TF - French Southern Territories (The)'), ('GA', 'GA - Gabon'), ('GM', 'GM - Gambia (The)'), ('GE', 'GE - Georgia'), ('DE', 'DE - Germany'), ('GH', 'GH - Ghana'), ('GI', 'GI - Gibraltar'), ('GR', 'GR - Greece'), ('GL', 'GL - Greenland'), ('GD', 'GD - Grenada'), ('GP', 'GP - Guadeloupe'), ('GU', 'GU - Guam'), ('GT', 'GT - Guatemala'), ('GG', 'GG - Guernsey'), ('GN', 'GN - Guinea'), ('GW', 'GW - Guinea-Bissau'), ('GY', 'GY - Guyana'), ('HT', 'HT - Haiti'), ('HM', 'HM - Heard Island and Mcdonald Islands'), ('VA', 'VA - Holy See (The)'), ('HN', 'HN - Honduras'), ('HK', 'HK - Hong Kong'), ('HU', 'HU - Hungary'), ('IS', 'IS - Iceland'), ('IN', 'IN - India'), ('ID', 'ID - Indonesia'), ('IR', 'IR - Iran (Islamic Republic Of)'), ('IQ', 'IQ - Iraq'), ('IE', 'IE - Ireland'), ('IM', 'IM - Isle of Man'), ('IL', 'IL - Israel'), ('IT', 'IT - Italy'), ('JM', 'JM - Jamaica'), ('JP', 'JP - Japan'), ('JE', 'JE - Jersey'), ('JO', 'JO - Jordan'), ('KZ', 'KZ - Kazakhstan'), ('KE', 'KE - Kenya'), ('KI', 'KI - Kiribati'), ('KP', 'KP - Korea (Democratic Peoples Republic Of)'), ('KR', 'KR - Korea (Republic Of)'), ('XK', 'XK - Kosovo'), ('KW', 'KW - Kuwait'), ('KG', 'KG - Kyrgyzstan'), ('LA', 'LA - Lao Peoples Democratic Republic (The)'), ('LV', 'LV - Latvia'), ('LB', 'LB - Lebanon'), ('LS', 'LS - Lesotho'), ('LR', 'LR - Liberia'), ('LY', 'LY - Libyan Arab Jamahiriya'), ('LI', 'LI - Liechtenstein'), ('LT', 'LT - Lithuania'), ('LU', 'LU - Luxembourg'), ('MO', 'MO - Macao'), ('MK', 'MK - Macedonia (The Former Yugoslav Republic Of)'), ('MG', 'MG - Madagascar'), ('MW', 'MW - Malawi'), ('MY', 'MY - Malaysia'), ('MV', 'MV - Maldives'), ('ML', 'ML - Mali'), ('MT', 'MT - Malta'), ('MH', 'MH - Marshall Islands (The)'), ('MQ', 'MQ - Martinique'), ('MR', 'MR - Mauritania'), ('MU', 'MU - Mauritius'), ('YT', 'YT - Mayotte'), ('MX', 'MX - Mexico'), ('FM', 'FM - Micronesia (Federated States Of)'), ('MD', 'MD - Moldova (Republic Of)'), ('MC', 'MC - Monaco'), ('MN', 'MN - Mongolia'), ('ME', 'ME - Montenegro'), ('MS', 'MS - Montserrat'), ('MA', 'MA - Morocco'), ('MZ', 'MZ - Mozambique'), ('MM', 'MM - Myanmar'), ('NA', 'NA - Namibia'), ('NR', 'NR - Nauru'), ('NP', 'NP - Nepal'), ('NL', 'NL - Netherlands (The)'), ('AN', 'AN - Netherland Antilles'), ('NC', 'NC - New Caledonia'), ('NZ', 'NZ - New Zealand'), ('NI', 'NI - Nicaragua'), ('NE', 'NE - Niger (The)'), ('NG', 'NG - Nigeria'), ('NU', 'NU - Niue'), ('NF', 'NF - Norfolk Island'), ('MP', 'MP - Northern Mariana Islands (The)'), ('NO', 'NO - Norway'), ('OM', 'OM - Oman'), ('PK', 'PK - Pakistan'), ('PW', 'PW - Palau'), ('PS', 'PS - Palestinian Territory, Occupied'), ('PA', 'PA - Panama'), ('PG', 'PG - Papua New Guinea'), ('PY', 'PY - Paraguay'), ('PE', 'PE - Peru'), ('PH', 'PH - Philippines (The)'), ('PN', 'PN - Pitcairn'), ('PL', 'PL - Poland'), ('PT', 'PT - Portugal'), ('PR', 'PR - Puerto Rico'), ('QA', 'QA - Qatar'), ('RE', 'RE - Reunion'), ('RO', 'RO - Romania'), ('RU', 'RU - Russian Federation (The)'), ('RW', 'RW - Rwanda'), ('BL', 'BL - Saint Barth\xe9lemy'), ('SH', 'SH - Saint Helena, Ascension and Tristan da Cunha'), ('KN', 'KN - Saint Kitts and Nevis'), ('LC', 'LC - Saint Lucia'), ('MF', 'MF - Saint Martin (French Part)'), ('PM', 'PM - Saint Pierre and Miquelon'), ('VC', 'VC - Saint Vincent and the Grenadines'), ('WS', 'WS - Samoa'), ('SM', 'SM - San Marino'), ('ST', 'ST - Sao Tome and Principe'), ('SA', 'SA - Saudi Arabia'), ('SN', 'SN - Senegal'), ('RS', 'RS - Serbia'), ('SC', 'SC - Seychelles'), ('SL', 'SL - Sierra Leone'), ('SG', 'SG - Singapore'), ('SX', 'SX - Sint Maarten (Dutch Part)'), ('SK', 'SK - Slovakia'), ('SI', 'SI - Slovenia'), ('SB', 'SB - Solomon Islands'), ('SO', 'SO - Somalia'), ('ZA', 'ZA - South Africa'), ('GS', 'GS - South Georgia and the South Sandwich Islands'), ('SS', 'SS - South Sudan'), ('ES', 'ES - Spain'), ('LK', 'LK - Sri Lanka'), ('SD', 'SD - Sudan (The)'), ('SR', 'SR - Suriname'), ('SJ', 'SJ - Svalbard and Jan Mayen'), ('SZ', 'SZ - Swaziland'), ('SE', 'SE - Sweden'), ('CH', 'CH - Switzerland'), ('SY', 'SY - Syrian Arab Republic'), ('TW', 'TW - Taiwan (Province of China)'), ('TJ', 'TJ - Tajikistan'), ('TZ', 'TZ - Tanzania, United Republic of'), ('TH', 'TH - Thailand'), ('TL', 'TL - Timor-Leste'), ('TG', 'TG - Togo'), ('TK', 'TK - Tokelau'), ('TO', 'TO - Tonga'), ('TT', 'TT - Trinidad and Tobago'), ('TN', 'TN - Tunisia'), ('TR', 'TR - Turkey'), ('TM', 'TM - Turkmenistan'), ('TC', 'TC - Turks and Caicos Islands (The)'), ('TV', 'TV - Tuvalu'), ('UG', 'UG - Uganda'), ('UA', 'UA - Ukraine'), ('AE', 'AE - United Arab Emirates (The)'), ('GB', 'GB - United Kingdom of Great Britain and Northern Ireland (The)'), ('US', 'US - United States of America (The)'), ('UM', 'UM - United States Minor Outlying Islands (The)'), ('UY', 'UY - Uruguay'), ('UZ', 'UZ - Uzbekistan'), ('VU', 'VU - Vanuatu'), ('VE', 'VE - Venezuela (Bolivarian Republic Of)'), ('VN', 'VN - Viet Nam'), ('VG', 'VG - Virgin Islands (British)'), ('VI', 'VI - Virgin Islands (U.s.)'), ('WF', 'WF - Wallis and Futuna'), ('EH', 'EH - Western Sahara'), ('YE', 'YE - Yemen'), ('ZM', 'ZM - Zambia'), ('ZW', 'ZW - Zimbabwe')]),
            preserve_default=True,
        ),
    ]
