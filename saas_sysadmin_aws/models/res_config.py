# -*- coding: utf-8 -*-
from odoo import models, fields


class SaasPortalConfigWizard(models.TransientModel):
    _inherit = 'saas_portal.config.settings'

    saas_route53_aws_accessid = fields.Char('AWS Access ID')
    saas_route53_aws_accesskey = fields.Char('AWS Secret Key')

    def get_default_saas_route53_aws_accessid(self):
        saas_route53_aws_accessid = self.env["ir.config_parameter"].get_param("saas_route53.saas_route53_aws_accessid", default=None)
        return {'saas_route53_aws_accessid': saas_route53_aws_accessid or False}

    def set_saas_route53_aws_accessid(self):
        config_parameters = self.env["ir.config_parameter"]
        for record in self:
            config_parameters.set_param("saas_route53.saas_route53_aws_accessid", record.saas_route53_aws_accessid or '')

    def get_default_saas_route53_aws_accesskey(self):
        saas_route53_aws_accesskey = self.env["ir.config_parameter"].get_param("saas_route53.saas_route53_aws_accesskey", default=None)
        return {'saas_route53_aws_accesskey': saas_route53_aws_accesskey or False}

    def set_saas_route53_aws_accesskey(self):
        config_parameters = self.env["ir.config_parameter"]
        for record in self:
            config_parameters.set_param("saas_route53.saas_route53_aws_accesskey", record.saas_route53_aws_accesskey or '')
