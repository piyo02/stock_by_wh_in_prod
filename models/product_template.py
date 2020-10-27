from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = "product.template"

    stock_in_store = fields.Float(string="Stok di Toko", compute='count_stock_in_store')
    stock_in_warehouse = fields.Float(string="Stok di Gudang", compute='count_stock_in_warehouse')
    stock_in_canvas_car = fields.Float(string="Stok di Mobil Canvas", compute='count_stock_in_canvas_car')

    @api.one
    def count_stock_in_store(self):
        qty = 0
        stocks = self.env['stock.quant'].search([
            ('product_id.name', '=', self.name),
            ('location_id.location_id.name', '=', 'TKTAS')
        ])

        for stock in stocks:
            qty += stock.qty
        self.stock_in_store = qty
    
    @api.one
    def count_stock_in_warehouse(self):
        qty = 0
        stocks = self.env['stock.quant'].search([
            ('product_id.name', '=', self.name),
            ('location_id.location_id.name', '=', 'GDTAS')
        ])

        for stock in stocks:
            qty += stock.qty
        
        self.stock_in_warehouse = qty

    @api.one
    def count_stock_in_canvas_car(self):
        qty = 0
        stocks = self.env['stock.quant'].search([
            ('product_id.name', '=', self.name),
            ('location_id.location_id.name', '=', 'MBCV')
        ])

        for stock in stocks:
            qty += stock.qty
        
        self.stock_in_canvas_car = qty
        