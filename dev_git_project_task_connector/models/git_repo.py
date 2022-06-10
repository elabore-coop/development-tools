# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GitRepository(models.Model):
    _name = "git.repo"
    _description = "Repository Git"

    name = fields.Char(string="Name", required=True)
    owner = fields.Char(string="Owner", required=True)
    displayed_name = fields.Char(
        string="Displayed name", compute="_compute_displayed_name"
    )

    @api.multi
    @api.depends("owner", "name")
    def _compute_displayed_name(self):
        for record in self:
            if record.name and record.owner:
                record.displayed_name = record.owner + "/" + record.name
