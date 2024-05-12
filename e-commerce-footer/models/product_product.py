from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def pricelist_item_ids(self):
        data = []
        data = [
            {
                "min_quantity": 1,
                "percent_price": 0,
                "fixed_price": 0,
            },
            {
                "min_quantity": 2,
                "percent_price": 5,
                "fixed_price": 0,
            },
            {
                "min_quantity": 3,
                "percent_price": 10,
                "fixed_price": 0,
            }
        ]
        return data


class ProductTemplateProduct(models.Model):
    _inherit = 'product.template'
    pricelist_item_ids = fields.Many2many(
        comodel_name='product.pricelist.item',  # Assuming 'product.pricelist.item' is the correct model
        string='Pricelist Items',
        compute='_compute_pricelist_item_ids'
    )

    @api.depends  # No specific dependencies, so it is left empty
    def _compute_pricelist_item_ids(self):
        # For demonstration, we're using a fixed ID set, ensure these IDs exist or are handled accordingly
        dummy_ids = [1, 2, 3]  # Presuming these IDs exist in your database for 'product.pricelist.item'
        self.pricelist_item_ids = [(6, 0, dummy_ids)]
