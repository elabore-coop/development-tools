# -*- coding: utf-8 -*-

from odoo import models, fields


class Task(models.Model):
    _inherit = "project.task"

    issue_ids = fields.One2many("git.issue", "task_id")

    def link_issue(self):
        return {
            "name": "Link a Git issue",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "link.git.issue",
            "target": "new",
        }

    def create_issue(self):
        return {
            "name": "Create a Git issue",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "create.git.issue",
            "target": "new",
        }

    def refresh_issues(self):
        for record in self:
            for issue in record.issue_ids:
                issue.refresh_data()
