from odoo import fields, models, api

class School(models.Model):
    _name = "school.details"

    name=fields.Char(string="school name")
    student=fields.One2many(comodel_name='students.management',inverse_name="school_id",string='student')

    count = fields.Integer(string="Total Count",compute="compute_count",defult=0)


    def compute_count(self):
        for rec in self:
            rec.count = self.env['students.management'].search_count(
                [('school_id', '=', self.id)])
    def action_get_count(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Total Count',
            'view_mode': 'list,form',
            'res_model': 'students.management',
            'domain': [('school_id', '=', self.id)],
            'context': "{'create': False}"
        }





