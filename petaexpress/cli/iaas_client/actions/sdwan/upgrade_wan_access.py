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


class UpgradeWanAccessAction(BaseAction):

    action = 'UpgradeWanAccess'
    command = 'upgrade-wan-access'
    usage = '%(prog)s -a "wan_access_id, ..." -b <bandwidth> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-a', '--wan_accesss', dest='wan_accesss',
                            action='store', type=str, default=None,
                            help='the IDs of wan_access you want to upgrade.')

        parser.add_argument('-b', '--bandwidth', dest='bandwidth',
                            action="store", type=int,  default=0,
                            help='the new bandwidth for wan_access, unit in Mbps.')

    @classmethod
    def build_directive(cls, options):
        if options.wan_accesss is None:
            print('error: wan_accesss should be specified.')
            return None

        return {
            'wan_accesss': explode_array(options.wan_accesss),
            'bandwidth': options.bandwidth,
        }
