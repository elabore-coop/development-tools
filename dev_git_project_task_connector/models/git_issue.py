# -*- coding: utf-8 -*-

from odoo import models, fields


class GitIssue(models.Model):
    _name = "git.issue"
    _description = "Issue Git"

    name = fields.Char(string="Title", required=True, copy=True)
    platform = fields.Many2one("git.platform", string="Git platform", required=True)
    repo = fields.Many2one(
        "git.repo", string="Git repository", required=True, copy=True
    )
    status = fields.Selection(
        [
            ("opened", "Opened"),
            ("closed", "Closed"),
        ],
        required=True,
        default="opened",
        copy=False,
    )
    url = fields.Char(string="Link", required=True, copy=False)

    task_id = fields.Many2one("project.task", required=True, copy=True)
