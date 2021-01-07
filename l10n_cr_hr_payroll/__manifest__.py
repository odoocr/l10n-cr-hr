# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Costa Rica Payroll',
    'version': '12.0.1.0.1',
    'category': 'Human Resources',
    'author': 'Odoo CR Team',
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'sumary': 'Costa Rica Payroll Rules'
    'depends': [
        'hr_payroll',
    ],

    'data': [
        'data/hr_salary_rule_data.xml',
        'data/hr_payroll_structure_data.xml'
    ],
}
