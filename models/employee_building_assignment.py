from odoo import fields, models

class Employee(models.Model):
    _name = 'employee.building.assignment'
    _description = 'employee'
    employee_id = fields.Many2one('hr.employee', 'id')
    building_id = fields.Many2one('fm.building', 'id')
    assignment_start_date = fields.Date('assignment_start_date')
    assignment_end_date = fields.Date('assignment_end_date')




    #under_roaf_area_as_mt = fields.Many2one('res.partner', string='Publisher')
    #under_roaf_area_as_feet = fields.Many2one('res.partner', string='Publisher')

    #author_ids = fields.Many2many('res.partner', string='Authors')