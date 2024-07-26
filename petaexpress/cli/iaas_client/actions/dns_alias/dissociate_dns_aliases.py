# =========================================================================
# Copyright 2012-present RAKSmart, Inc.
# -------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================

from petaexpress.cli.misc.utils import explode_array
from petaexpress.cli.iaas_client.actions.base import BaseAction

class DissociateDNSAliasesAction(BaseAction):

    action = 'DissociateDNSAliases'
    command = 'dissociate-dns-aliases'
    usage = '%(prog)s -d "dns_alias_id, ..." [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-d', '--dns_aliases', dest='dns_aliases',
                action='store', type=str, default='',
                help='the comma separated IDs of dns alias you want to dissociate.')

    @classmethod
    def build_directive(cls, options):
        dns_aliases = explode_array(options.dns_aliases)
        if not dns_aliases:
            return None

        return {'dns_aliases': dns_aliases}