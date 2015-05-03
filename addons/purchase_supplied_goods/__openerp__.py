# -*- coding: utf-8 -*-
##############################################################################
#
#    Purchase Supplied Goods - OpenERP Module
#    Copyright (C) 2013 Shine IT (<http://www.openerp.cn).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Purchase Supplied Goods',
    'version': '1.1',
    'author': 'Shine IT',
    'website': 'http://www.openerp.cn',
    'category': 'Purchase Management',
    'depends': ['product', 'purchase'],
    'description': """
    This module will limit the selection of goods according to the supplier
    specified when creating purchase order.

    The goods available for selection will be determined by:
    products whose 'supplier info' includes the supplier specified on 
    puchase order, or
    products without providing any 'supplier info'

    本模块将限制用户在开采购订单时只能选择由该供应商供货的产品。

    产品选择列表中将只列示：
    1. 产品的供应商列表中包含采购订单上所选择的供应商的产品；
    2. 产品的供应商列表为空的产品
    """,
    'data': [
            'purchase_supplied_goods_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
