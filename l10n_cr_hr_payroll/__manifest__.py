# -*- coding: utf-8 -*-
{
    'name': 'Costa Rica Payroll',
    'version': '12.0.1.0.1',
    'category': 'Human Resources',
    'author': 'Odoo CR Team',
    'depends': [
        'hr_payroll',
        ],
    'description': """
Costa Rica Payroll Rules.
=====================
    - Configuration of hr_payroll for Costa Rica localization.
    - All main contributions rules for Costa Rica payslip.

    """,
    'data': [
        'data/hr_salary_rule_data.xml',
        'data/hr_payroll_structure_data.xml'
    ],
}
