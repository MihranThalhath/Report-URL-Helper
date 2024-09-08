# Odoo - Report URL Helper

QWeb development is always a pain since we might have to generate the PDF multiple times while we create a new QWeb report
or make changes to an existing QWeb report. The best method to make sure that we don't spam our Downloads folder is to use
direct URL of the report we are generating along with the record for which we are generating the report. [Source](https://www.odoo.com/documentation/17.0/developer/reference/backend/reports.html#reports-are-web-pages)

I have been using the above method to make my life easier, but whenever I need to make a change in any existing report, I
need to go and find out the ID of the report and this will become irritating very quick if we are making changes every now
and then.

This module adds a new option under Actions Cog Menu, which shows all the reports in existing Print menu, but when clicking
the items in the new cog menu, it will open the reports in their predefind URL instead of downloading them.<br/> Couple this with 
`--dev=xml`([source](https://www.odoo.com/documentation/17.0/developer/reference/cli.html#developer-features)) option while running Odoo and a page refresh is enough to view your new changes.

You can find a small video of how it works below:



https://github.com/user-attachments/assets/4496e435-401c-4c25-a6d8-6e95605ffeff


This will not work with all the reports in Odoo since some reports are getting data dynamically from Python.
Also there maybe small alignment issues when you open both Print submenu in Actions Cog menu. I haven't bothered to fix it.
