from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class StockMove(models.Model):
    _inherit = "stock.move"

    stock_in_store = fields.Float(string="Stok di Toko")
    stock_in_warehouse = fields.Float(string="Stok di Gudang")
    stock_in_canvas_car = fields.Float(string="Stok di Mobil Canvas")

    @api.onchange('product_id')
    def product_id_change(self):
        if self.product_id:
            product = self.env['product.template'].search([
                ('name', '=', self.product_id.name)
            ])
            self.stock_in_store = product.stock_in_store
            self.stock_in_warehouse = product.stock_in_warehouse
            self.stock_in_canvas_car = product.stock_in_canvas_car