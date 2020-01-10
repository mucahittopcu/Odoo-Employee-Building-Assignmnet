from odoo import fields, models, api


class Building(models.Model):
    _name = 'fm.building'
    _description = 'Buildings'
    _rec_name = 'building_name'

    building_name = fields.Char('building_name', required=True)
    building_no = fields.Char('building_no', required=True)
    building_dimension = fields.Char('building_dimension')
    construction_year = fields.Integer('construction_year')
    structural_system = fields.Char('structural_system')
    office_area_as_mt_square = fields.Float('offici_area_as_mt_sqare')
    under_roof_area_as_mt = fields.Float('under_roaf_area_as_mt')
    under_roof_area_as_feet = fields.Float('under_roaf_area_as_feet', compute='set_age_group')

    @api.depends('under_roof_area_as_mt')
    def set_age_group(self):
        for rec in self:
            rec.under_roof_area_as_feet = rec.under_roof_area_as_mt * 3.28

