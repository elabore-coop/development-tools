# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateGitIssue(models.TransientModel):
    _name = "create.git.issue"
    _description = "Create a Git Issue"

    issue_name = fields.Char(string="Title", required=True)
    issue_description = fields.Html(string="Description", required=False)
    issue_repo = fields.Many2one("git.repo", required=True)

    # Function to inherit in Git platform connector addons
    def _convert_issue_status(self, status):
        return status

    # Function to inherit in Git platform connector addons
    def _create_git_issue(self):
        return {}

    def create_issue(self):
        values = self._create_git_issue()
        self.env["git.issue"].create(values)
