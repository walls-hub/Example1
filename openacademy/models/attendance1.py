from odoo import models, fields


class att(models.Model):
    _name = "att.student"
    name = fields.Many2one('master.student', 'name')
    attendance= fields.Selection([('Y', 'Present'), ('N', 'Absent')], string='Attendance')
    date = fields.Date(string="Date")
    master_name = fields.Many2one('mastersession.student', 'name')

