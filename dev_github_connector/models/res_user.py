# -*- coding: utf-8 -*-

from odoo import models, fields


class Users(models.Model):
    _inherit = "res.users"

    github_token = fields.Char(string="Github token")
