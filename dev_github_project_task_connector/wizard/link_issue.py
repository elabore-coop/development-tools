# -*- coding: utf-8 -*-

from odoo import models, fields
from github import Github


class LinkGitIssue(models.TransientModel):
    _name = "link.git.issue"
    _description = "Link a Git Issue to a project task"

    issue_repo = fields.Many2one("git.repo", string="Repository", required=True)
    issue_number = fields.Integer("Issue number", required=True)

    def link_issue(self):
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
        self.env["git.issue"].create(values)
