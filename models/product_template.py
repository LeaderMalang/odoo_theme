from odoo import api, fields, models
from odoo.http import request

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_new_item = fields.Boolean('New Item')
