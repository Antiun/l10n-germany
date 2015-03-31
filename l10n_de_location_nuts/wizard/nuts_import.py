# -*- coding: utf-8 -*-
# Python source code encoding : https://www.python.org/dev/peps/pep-0263/
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright :
#        (c) 2015 Antiun Ingenieria, SL (Madrid, Spain, http://www.antiun.com)
#                 Antonio Espinosa <antonioea@antiun.com>
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

from openerp import models, api
import logging

logger = logging.getLogger(__name__)


class NutsImport(models.TransientModel):
    _inherit = 'nuts.import'
    _de_state_map = {
        'DE1': 'l10n_de_country_states.res_country_state_BW',  # BADEN-WÜRTTEMBERG
        'DE2': 'l10n_de_country_states.res_country_state_BY',  # BAYERN
        'DE3': 'l10n_de_country_states.res_country_state_BE',  # BERLIN
        'DE4': 'l10n_de_country_states.res_country_state_BB',  # BRANDENBURG
        'DE5': 'l10n_de_country_states.res_country_state_HB',  # BREMEN
        'DE6': 'l10n_de_country_states.res_country_state_HH',  # HAMBURG
        'DE7': 'l10n_de_country_states.res_country_state_HE',  # HESSEN
        'DE8': 'l10n_de_country_states.res_country_state_MV',  # MECKLENBURG-VORPOMMERN
        'DE9': 'l10n_de_country_states.res_country_state_NI',  # NIEDERSACHSEN
        'DEA': 'l10n_de_country_states.res_country_state_NW',  # NORDRHEIN-WESTFALEN
        'DEB': 'l10n_de_country_states.res_country_state_RP',  # RHEINLAND-PFALZ
        'DEC': 'l10n_de_country_states.res_country_state_SL',  # SAARLAND
        'DED': 'l10n_de_country_states.res_country_state_SN',  # SACHSEN
        'DEE': 'l10n_de_country_states.res_country_state_ST',  # SACHSEN-ANHALT
        'DEF': 'l10n_de_country_states.res_country_state_SH',  # SCHLESWIG-HOLSTEIN
        'DEG': 'l10n_de_country_states.res_country_state_TH',  # THÜRINGEN
        'DEZ': False,  # EXTRA-REGIO NUTS 1
    }

    @api.model
    def state_mapping(self, data, node):
        mapping = super(NutsImport, self).state_mapping(data, node)
        level = data.get('level', 0)
        code = data.get('code', '')
        if self._current_country.code == 'DE' and level == 2:
            toponyms = self._de_state_map.get(code, False)
            if toponyms:
                state = self.env.ref(toponyms)
                if state:
                    mapping['state_id'] = state.id
        return mapping
