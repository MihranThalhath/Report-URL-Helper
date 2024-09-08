# Copyright 2024 Mihran Thalhath <https://github.com/MihranThalhath>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Report URL helper",
    "summary": """QWeb development made easier.""",
    "author": "Mihran Thalhath",
    "website": "https://github.com/MihranThalhath",
    "version": "15.0.1.0.0",
    "depends": [
        "base",
        "base_setup",
        "web",
    ],
    "data": [
        "security/groups.xml",
        "views/ir_actions_report.xml",
        "views/res_config_settings.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "report_url_helper/static/src/js/*.js",
        ],
        "web.assets_qweb": [
            "report_url_helper/static/src/xml/*.xml",
        ],
    },
    "installable": True,
    "license": "AGPL-3",
}
