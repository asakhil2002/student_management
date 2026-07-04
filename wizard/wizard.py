from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Wizard(models.TransientModel):
    _name = "update.phno"

    student = fields.Many2one(comodel_name='students.management', string="school name")
    update = fields.Char(string="new phone no")

    def updatephno(self):
        self.student.write({'phone':self.update})



class AgeFilter(models.TransientModel):
    _name="age.filter"

    start_date = fields.Integer(string="enter from age")
    end_date = fields.Integer(string="enter to age")



    @api.constrains("start_date","end_date")

    def _check_field(self):
        for rec in self:
            if rec.start_date > rec.end_date:
                raise ValidationError("please select correctt age")

    def filter_age(self):
        student_obj = self.env['students.management']
        students = student_obj.search([("age",">=",self.start_date),("age","<=",self.end_date)])



        return {
            'type':'ir.actions.act_window',
            'name':'filter students',
            'res_model':'students.management',
            'view_mode':'list,form',
            'domain':[('id','in',students.ids)],
            'target': 'current',
        }



