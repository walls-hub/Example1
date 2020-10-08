from odoo import models, fields

class books(models.Model):

    _name = "books.book"
    name = fields.Char(string='Book Name', required=True)
    author = fields.Char(string='Author', required=True)
    editor = fields.Char(string='Editor', required=True)
    year_of_edition = fields.Char(string='Year of Edition', required=True)
    isbn = fields.Integer(string='ISBN')
