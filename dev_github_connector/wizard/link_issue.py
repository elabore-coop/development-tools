# -*- coding: utf-8 -*-

from odoo import models
from github import Github


class LinkGitIssue(models.TransientModel):
    _inherit = "link.git.issue"

    def _compute_issue_values(self):
        values = super(LinkGitIssue, self)._compute_issue_values()
        github = Github()
        repo = github.get_repo(self.issue_repo.displayed_name)
        issue = repo.get_issue(number=self.issue_number)
        values = {
            "name": issue.title,
            "repo": self.issue_repo.id,
            "status": issue.state,
            "url": issue.html_url,
            "task_id": self.env["project.task"]
            .browse(self._context.get("active_ids"))
            .id,
        }
        return values
