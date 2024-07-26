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


class TerminateInstancesAction(BaseAction):

    action = 'TerminateInstances'
    command = 'terminate-instances'
    usage = '%(prog)s -i "instance_id,..." [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--instances', dest='instances',
                            action='store', type=str, default='',
                            help='the comma separated IDs of instances you want to terminate.')

        parser.add_argument('-D', '--direct-cease', dest='direct_cease',
                            action='store', type=int, default=0,
                            help='whether to keep deleted resource in recycle bin (direct-cease=0) or not (direct-cease=1).')

        return parser

    @classmethod
    def build_directive(cls, options):
        instances = explode_array(options.instances)
        if not instances:
            print('error: [instances] should be specified')
            return None

        return {
            'instances': instances,
            'direct_cease': options.direct_cease,
        }
