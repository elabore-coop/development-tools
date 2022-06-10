# -*- coding: utf-8 -*-

from odoo import models
from github import Github


class LinkGitIssue(models.TransientModel):
    _inherit = "link.git.issue"

    def _convert_issue_status(self, status):
        if status == "open":
            return "opened"
        elif status == "closed":
            return "closed"
        else:
            return super(LinkGitIssue, self)._convert_issue_status(status)

    def _compute_issue_values(self):
        values = super(LinkGitIssue, self)._compute_issue_values()
        if self.issue_platform.tool == "github":
            github = Github()
            repo = github.get_repo(self.issue_repo.displayed_name)
            issue = repo.get_issue(number=self.issue_number)
            values = {
                "issue_id": issue.number,
                "name": issue.title,
                "platform": self.issue_platform.id,
                "repo": self.issue_repo.id,
                "status": self._convert_issue_status(issue.state),
                "url": issue.html_url,
                "task_id": self.env["project.task"]
                .browse(self._context.get("active_ids"))
                .id,
            }
        return values
