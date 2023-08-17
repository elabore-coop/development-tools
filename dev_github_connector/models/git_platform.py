# -*- coding: utf-8 -*-

from odoo import models, fields


class GitPlatform(models.Model):
    _inherit = "git.platform"

    tool = fields.Selection(selection_add=[("github", "Github")], ondelete={'github':'cascade'})
