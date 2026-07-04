import re

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Students(models.Model):
    _name = 'students.management'

    name = fields.Char(string=" Name")
    ref_id = fields.Char(string='Reference', required=True, copy=False, readonly=True,
                       default=lambda self: 'New')
    school_id = fields.Many2one(comodel_name="school.details", string="school name")
    street = fields.Char(string="Street")
    new_country_id = fields.Many2one(comodel_name='res.country')
    permanent_country_id = fields.Many2one(comodel_name='res.country')
    new_state_id = fields.Many2one(comodel_name='res.country.state')
    permanent_state_id = fields.Many2one(comodel_name='res.country.state')
    perment_street = fields.Char(string="Street")
    street2 = fields.Char(string="Street 2")
    perment_street2 = fields.Char(string="Street 2")
    city = fields.Char(string=" City")
    perment_city = fields.Char(string="City")
    state_id = fields.Char(string=" State ID")
    perment_state_id = fields.Char("State ID")
    zip = fields.Char(string=" Zip")
    perment_zip = fields.Char(string=" Zip")
    email = fields.Char(string=" Email Id")
    phone = fields.Char(string=" Phone Number")
    age = fields.Integer(string=" Age", compute="compute_age")
    parent_ids = fields.One2many(comodel_name="parent.details", inverse_name="student_id", string="Parent")
    date_of_birth = fields.Date(string=" DOB ")
    blood_group = fields.Selection(
        [("o_+ve", "O+ve"), ("o_-ve", "O-ve"), ("a_-ve", "A-ve"), ("a_+ve", "A+ve"), ("b_-ve", "B-ve"),
         ("b_+ve", "B+ve"), ("ab_-ve", "AB-ve"), ("ab_+ve", "AB+ve")], string="Blood Group")
    relationship = fields.Selection([("mother", "Mother"), ("father", "Father")], string=" Student Relationship")
    religion = fields.Char(string=" Religion")
    country_id = fields.Char(string=" Country ID")
    is_same_address = fields.Boolean(string="is same current address")
    perment_country_id = fields.Char(string=" Country ID")
    status = fields.Selection([
        ("draft", "Draft"),
        ("pass", "Pass"),
        ("fail", "Fail")
    ], string=" Status", default="draft")

    def action_draft(self):
        self.status = "draft"

    def action_pass(self):
        self.status = "pass"

    def action_fail(self):
        self.status = "fail"

    @api.constrains('email')
    def email_validation(self):

        for rec in self:
            pattern = r'^(\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6})$'
            if rec.email:
                email_match = re.match(pattern, rec.email)
                if email_match == None:
                    raise ValidationError("not a valid e-mail id")
    @api.constrains('phone')

    def phone_no_validation(self):
        for rec in self:
            if not rec.phone:
                raise ValidationError("phone number is mandatory")
            if not re.match(r'^\d+$', rec.phone):
                raise ValidationError("phone number must be digit")
            if not re.match(r'^\d{10}$',rec.phone):
                raise ValidationError("must have 10 digit")
    @api.depends('age')


    def compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                today = fields.Date.today()
                rec.age = relativedelta(today, rec.date_of_birth).years
            else:
                rec.age = 0

    @api.model_create_multi
    def create(self, vals_list):
        """ Create a sequence for the student model """
        for vals in vals_list:
            if vals.get('ref_id', ('New')) == ('New'):
                vals['ref_id'] = (self.env['ir.sequence'].
                                  next_by_code('students.management'))
        return super().create(vals_list)
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

    def action_view(self):
        for rec in self:
            rec.status = "pass"







