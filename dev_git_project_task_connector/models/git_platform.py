# -*- coding: utf-8 -*-

from odoo import models, fields


class GitPlatform(models.Model):
    _name = "git.platform"
    _description = "Git Platform"

    name = fields.Char(string="Name", required=True)
    tool = fields.Selection([], string="Tool", required=True)
    url = fields.Char(string="URL", required=True, copy=False)
