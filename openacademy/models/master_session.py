from odoo import models, fields

class mastersession(models.Model):

    _name = "mastersession.student"
    name = fields.Char(string='Master Name', required=True)
    session = fields.Selection([('1', 'session 1'), ('2', 'session 2'), ('3', 'session 3')], string='session')

