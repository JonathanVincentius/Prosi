# from odoo import models, fields, api


# class prosi_kedokteran(models.Model):
#     _name = 'prosi_kedokteran.prosi_kedokteran'
#     _description = 'prosi_kedokteran.prosi_kedokteran'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

