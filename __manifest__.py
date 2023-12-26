# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'MES_Hieu',
    'version': '15.0.1.0.0',
    "category": "Themes/Backend",
    'live_test_url': 'https://youtu.be/IhI7TpOAAKg',
    'sequence': 1,
    'summary': """
        Learn Odoo,
    """,
    'description': "This is module MES_Hieu",
    'author': 'MES_Hieu',
    'maintainer': 'MES_Hieu',
    'price': '150.0',
    'currency': 'EUR',
    'website': 'https://neway-solutions.com',
    'license': 'OPL-1',
    'depends': [
        'base', 'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
       'views/menuView.xml',
        'views/stdModelView.xml',
        # 'views/stdProductView.xml',
        # 'views/popup_basic_views.xml',
        # 'views/employee_inherit_views.xml',
    ],

}