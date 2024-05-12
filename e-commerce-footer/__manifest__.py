# -*- coding: utf-8 -*-
{
    'name': "e-commerce-footer",

    'summary': """E-commerce footer module""",

    'description': """
    E-commerce footer module remove odoo online and odoo enterprise links from footer
    """,

    'author': "Ruzimurodov Nodirjon",
    'website': "https://t.me/ruzimurodov_nodir",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', "website_sale", "web"],

    # always loaded
    'data': [
        'views/footer.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
