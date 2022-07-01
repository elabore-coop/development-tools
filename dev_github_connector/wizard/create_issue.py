# -*- coding: utf-8 -*-

from odoo import models
from github import Github


class CreateGitIssue(models.TransientModel):
    _inherit = "create.git.issue"

    def _convert_issue_status(self, status):
        if status == "open":
            return "opened"
        elif status == "closed":
            return "closed"
        else:
            return super(CreateGitIssue, self)._convert_issue_status(status)

    def _create_git_issue(self):
        values = super(CreateGitIssue, self)._create_git_issue()
        if self.issue_platform.tool == "github":
            github = Github(self.env.user.company_id.github_token)
            repo = github.get_repo(self.issue_repo.displayed_name)
            issue = repo.create_issue(
                title=self.issue_name, body=self.issue_description
            )
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
