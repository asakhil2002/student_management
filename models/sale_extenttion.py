from odoo import fields, models

class Sale(models.Model):
    _inherit = "sale.order"


    note = fields.Char(string="Note")


class Extention(models.Model):
    _inherit = "sale.order.line"

    student_fee = fields.Integer(string="Student Fee")