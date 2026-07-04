from tokenize import String

from odoo import fields, models, api


class Parent(models.Model):
    _name = "parent.details"
    _rec_name = "parent_name"

    parent_name = fields.Char(string="Parent Name")
    student_id = fields.Many2one(comodel_name='students.management')
    new_country_id = fields.Many2one(comodel_name='res.country')
    permanent_country_id = fields.Many2one(comodel_name='res.country')
    new_state_id = fields.Many2one(comodel_name='res.country.state')
    permanent_state_id = fields.Many2one(comodel_name='res.country.state')
    student_ids = fields.Many2many(comodel_name='students.management',string="Child name")
    street = fields.Char(string="Street")
    perment_street = fields.Char(string="Street")

    street2 = fields.Char(string=" Street 2")
    perment_street2 = fields.Char(string=" Street 2")
    city = fields.Char(string=" City")
    perment_city = fields.Char(string=" City")
    state_id = fields.Char(string=" State ID")
    perment_state_id = fields.Char(string=" State ID")
    zip = fields.Char(string=" Zip")
    perment_zip = fields.Char(string=" Zip")
    email = fields.Char(string=" Email Id")
    phone = fields.Integer(string=" Phone Number")
    age = fields.Integer(string=" Age")
    date_of_birth = fields.Date(string=" DOB ")
    blood_group = fields.Selection(
        [("o_+ve", "O+ve"), ("o_-ve", "O-ve"), ("a_-ve", "A-ve"), ("a_+ve", "A+ve"), ("b_-ve", "B-ve"),
         ("b_+ve", "B+ve"), ("ab_-ve", "AB-ve"), ("ab_+ve", "AB+ve")], string="Blood Group")
    relationship = fields.Selection([("mother", "Mother"), ("father", "Father")], string=" Parent Relationship")
    religion = fields.Char(string=" Religion")
    country_id = fields.Char(string=" Country ID")
    is_same_address = fields.Boolean(string="is same current address")

    @api.onchange('is_same_address')

    def address_same(self):
        if self.is_same_address:
            self.perment_street = self.street
            self.perment_street2 = self.street2
            self.perment_city = self.city
            self.perment_zip = self.zip
            self.permanent_country_id = self.new_country_id
            self.permanent_state_id = self.new_state_id
        else:
            self.perment_street = False
            self.perment_street2 = False
            self.perment_city = False
            self.perment_zip = False
            self.permanent_country_id = False
            self.permanent_state_id = False


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('student_id'):
                student = self.env['students.management'].browse(vals['student_id'])

                vals['street'] = student.street
                vals['street2'] = student.street2
                vals['city'] = student.city
                vals['zip'] = student.zip
                vals['new_country_id'] = student.new_country_id.id if student.new_country_id else False
                vals['new_state_id'] = student.new_state_id.id if student.new_state_id else False

        return super().create(vals_list)
