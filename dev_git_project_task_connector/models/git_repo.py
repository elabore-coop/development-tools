# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GitRepository(models.Model):
    _name = "git.repo"
    _description = "Repository Git"

    platform_id = fields.Many2one("git.platform", string="Git platform", required=True)
    name = fields.Char(string="Name", required=True)
    owner = fields.Char(string="Owner", required=True)
    displayed_name = fields.Char(
        string="Displayed name", compute="_compute_displayed_name"
    )

    @api.depends("owner", "name")
    def _compute_displayed_name(self):
        for record in self:
            displayed_name = []            
            if record.owner:
                displayed_name.append(record.owner)
            if record.name:
                displayed_name.append(record.name)
            record.displayed_name = '/'.join(displayed_name)                
