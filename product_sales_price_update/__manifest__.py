# -*- coding: utf-8 -*-
{
    'name': 'Product Price Update',
    'summary': """Bulk Product Price Update in Percentage""",
    'version': '15.1.1',
    'author': 'Navabrind IT Solutions Pvt Ltd',
    'price': 5.0,
    'sequence': 1,
    'currency': 'EUR',
    'category': 'Sales',
    'website': 'https://www.navabrindsol.com',
    'support': 'sales@navabrindsol.com',
    'depends': ['base','product'],
    'description': """This app provide facility to bulk update of products and product variants sale prices on given percentage""",
    'data': [
        'security/ir.model.access.csv',
        'wizard/update_product_info_view.xml',
        'wizard/update_product_variant_info_view.xml',
    ],
    'installable': True,
    'application': True,
    'images': ['static/description/module_image.png'],
    'license': 'LGPL-3', 
    
}
