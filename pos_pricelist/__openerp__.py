# -*- coding: utf-8 -*-
##############################################################################
# Point Of Sale - Pricelist for POS Odoo
# Copyright (C) 2014 Taktik (http://www.taktik.be)
# @author Adil Houmadi <ah@taktik.be>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'POS Pricelist',
    'version': '1.0.0',
    'category': 'Point Of Sale',
    'sequence': 1,
    'author': "Adil Houmadi @Taktik,Odoo Community Association (OCA)",
    'summary': 'Pricelist for Point of sale',
    'description': """
New feature for the Point Of Sale:
=============================================
    Add support for pricelist on the point of sale
    """,
    'depends': [
        "point_of_sale",
    ],
    'data': [
        "views/pos_pricelist_template.xml",
    ],
    'demo': [
        'demo/pos_pricelist_demo.yml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
