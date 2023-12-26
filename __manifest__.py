# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRUD BASIC',
    'version': '15.0.1.0.0',
    "category": "Themes/Backend",
    'live_test_url': 'https://youtu.be/IhI7TpOAAKg',
    'sequence': 1,
    'summary': """
        Learn Odoo,
    """,
    'description': "This is module CRUD basic",
    'author': 'NEWAY Solutions',
    'maintainer': 'NEWAY Solutions',
    'price': '150.0',
    'currency': 'EUR',
    'website': 'https://neway-solutions.com',
    'license': 'OPL-1',
    'depends': [
        'base', 'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
       'views/menu_views.xml',
        'views/standard_model_views.xml',
        'views/standard_product_views.xml',
        'views/popup_basic_views.xml',
        'views/employee_inherit_views.xml',
    ],

}