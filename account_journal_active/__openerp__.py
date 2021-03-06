# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
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
    "name": "Account Journal Active",
    "version": "8.0.1.2.0",
    'author':  'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    "category": "Accounting",
    "description": """
Account Journal Active Field
============================
Adds active field on account journal
    """,
    'depends': [
        # we add dependency of account_voucher because we change voucher
        # action views to make voucher visible when journal inactive
        'account_voucher'
        ],
    'data': [
        'account_journal_view.xml',
        'account_voucher_view.xml',
        ],
    'demo': [],
    'test': [],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
