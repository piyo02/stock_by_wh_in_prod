from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class StockMove(models.Model):
    _inherit = "stock.move"

    stock_in_store = fields.Float(string="Stok di Toko")
    stock_in_warehouse = fields.Float(string="Stok di Gudang")
    stock_in_canvas_car = fields.Float(string="Stok di Mobil Canvas")