from odoo import fields, api, models, _
from odoo.exceptions import UserError


class UpdateProductInfo(models.TransientModel):
    _name = "update.product.variants.info"
    _description = "Update Product Variant Info"

    percent = fields.Float(string="Percentage")
    variant_extra_price_percent = fields.Float(string='Variant Extra Price Percentage')
    is_product_template_update_ok = fields.Boolean('Base Price', default=True)
    is_variant_extra_price_ok = fields.Boolean('Variant Extra Price')

    def update_product_variants_sales_price(self):
        print(self._context)
        active_model = self._context.get('active_model')
        active_ids = self._context.get('active_ids')
        if active_model != 'product.product':
            raise UserError(_('You can only apply this action from a Product Variant.'))
        if not active_ids:
            raise UserError(_('Please select some records !!'))
        selected_product_template_ids = self.env['product.product'].sudo().browse(active_ids).mapped('product_tmpl_id')
        selected_product_variant_ids = self.env['product.product'].sudo().browse(active_ids)
        for rec in selected_product_template_ids:
            if self.is_product_template_update_ok:
                incremented_list_price = float((rec.list_price * self.percent / 100)) + rec.list_price
                rec.list_price = incremented_list_price
        for rec in selected_product_variant_ids:
            if self.is_variant_extra_price_ok:
                # ptavs = rec.attribute_line_ids.product_template_value_ids
                ptavs = rec.product_template_variant_value_ids
                for value in ptavs:
                    if value.price_extra:
                        incremented_extra_price = float((value.price_extra * self.variant_extra_price_percent / 100)) + value.price_extra
                        value.price_extra = incremented_extra_price

