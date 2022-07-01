from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    github_token = fields.Char(
        related="company_id.github_token", string="Github token", readonly=False
    )
