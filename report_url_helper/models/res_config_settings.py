# Copyright 2024 Mihran Thalhath <https://github.com/MihranThalhath>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    is_show_print_url_cog_menu = fields.Boolean(
        string="Show Print URL in Cog Menu (All Users)",
        help="Show Print URL in Cog Menu for all users",
        config_parameter="report_url_helper.is_show_print_url_cog_menu",
        default=False,
    )
    is_hide_default_print_cog_menu = fields.Boolean(
        string="Hide Default Print in Cog Menu (All Users)",
        help="Hide Default Print in Cog Menu for all users",
        config_parameter="report_url_helper.is_hide_default_print_cog_menu",
        default=False,
    )
