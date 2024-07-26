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

class DetachKeyPairsAction(BaseAction):

    action = 'DetachKeyPairs'
    command = 'detach-keypairs'
    usage = '%(prog)s --instances "instance_id, ..." --keypairs "kp_id, ..." [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        
        parser.add_argument('-k', '--keypairs', dest='keypairs',
                action='store', type=str, default='',
                help='the comma separated IDs of keypairs you want to detach from instances. ')

        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='the IDs of instances the keypairs will be detached from.')

    @classmethod
    def build_directive(cls, options):
        keypairs = explode_array(options.keypairs)
        instances = explode_array(options.instances)
        if not keypairs or not instances:
            return None

        return {
                'keypairs': keypairs,
                'instances': instances,
                }
