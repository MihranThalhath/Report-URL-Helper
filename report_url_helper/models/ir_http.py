# Copyright 2024 Mihran Thalhath <https://github.com/MihranThalhath>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        result = super(IrHttp, self).session_info()
        ICP = self.env["ir.config_parameter"].sudo()
        if show_print_url_cog_menu := bool(
            ICP.get_param("report_url_helper.is_show_print_url_cog_menu", False)
        ):
            result.update(
                {
                    "is_show_print_url_cog_menu": show_print_url_cog_menu,
                    "is_hide_default_print_cog_menu": bool(
                        ICP.get_param(
                            "report_url_helper.is_hide_default_print_cog_menu", False
                        )
                    ),
                }
            )
        else:
            result.update(
                {
                    "is_show_print_url_cog_menu": self.env.user.has_group(
                        "report_url_helper.group_report_url"
                    ),
                    "is_hide_default_print_cog_menu": False,
                }
            )
        return result
