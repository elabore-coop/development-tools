# -*- coding: utf-8 -*-

from odoo import models
from github import Github


class GitIssue(models.Model):
    _inherit = "git.issue"

    def _convert_issue_status(self, status):
        if status == "open":
            return "opened"
        elif status == "closed":
            return "closed"
        else:
            return status

    def refresh_data(self):
        for record in self:
            if record.platform.tool == "github":
                github = Github()
                repo = github.get_repo(self.repo.displayed_name)
                issue = repo.get_issue(number=self.issue_id)
                record.status = self._convert_issue_status(issue.state)
