# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class MyAccountHub(http.Controller):

    # @http.route('/my/hub/category', type='http', auth="public", website=True)
    # def get_categories(self, **kw):
    #     categories = request.env['product.category'].sudo().search([])
    #     category_list = []
    #     for category in categories:
    #         data = {
    #             'id': category.id,
    #             'name': category.name
    #         }
    #         category_list.append(data)
    #     res = {
    #         'data': category_list
    #     }
    #     return json.dumps(res)

    @http.route(['/','/home','/home/page/<int:page>'], type='http', auth="public", website=True)
    def home_page(self,page=0, **kw):
        url = "/home"
        ppg = 6
        products_count = len(request.env['product.template'].sudo().search([]))
        pager = request.website.pager(url=url, total=products_count, page=page, step=ppg)
        categories = request.env['product.public.category'].sudo().search([])
        products = request.env['product.template'].sudo().search([], limit=ppg, offset=pager['offset'])
        categ = request.env['product.template'].sudo().search([('is_new_item', '=', True)])
        print("home page========",categ)
        return request.render('odoo_theme.home_template',{'categories':categories,
                                                          'products':products,
                                                          'products_count':products_count,
                                                          'pager': pager,
                                                          'categ': categ,
                                                          })
