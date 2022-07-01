from odoo import models, fields


class Company(models.Model):
    _inherit = "res.company"

    github_token = fields.Char(string="Github token")
