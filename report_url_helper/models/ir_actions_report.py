# Copyright 2024 Mihran Thalhath <https://github.com/MihranThalhath>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    report_url = fields.Char(string="Report URL", compute="_compute_report_url")

    @api.depends("report_name")
    def _compute_report_url(self) -> None:
        for report in self:
            report.report_url = f"/report/pdf/{report.report_name}/"

    @api.model
    def get_report_url(self, report_id: int) -> str:
        try:
            report = self.env["ir.actions.report"].browse(report_id)
        except Exception:
            _logger.error("Failed to get report with id %s", report_id)
            return False
        return report.report_url
