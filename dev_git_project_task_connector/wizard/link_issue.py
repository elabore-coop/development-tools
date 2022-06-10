# -*- coding: utf-8 -*-

from odoo import models, fields


class LinkGitIssue(models.TransientModel):
    _name = "link.git.issue"
    _description = "Link a Git Issue to a project task"

    issue_repo = fields.Many2one("git.repo", string="Repository", required=True)
    issue_number = fields.Integer("Issue number", required=True)

    # Function to inherit in Git platform connector addons
    def _compute_issue_values(self):
        return {}

    def link_issue(self):
        values = self._compute_issue_values()
        self.env["git.issue"].create(values)
