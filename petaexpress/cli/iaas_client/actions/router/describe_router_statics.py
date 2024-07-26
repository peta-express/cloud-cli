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

class DescribeRouterStaticsAction(BaseAction):

    action = 'DescribeRouterStatics'
    command = 'describe-router-statics'
    usage = '%(prog)s [-s "router_static_id, ..."] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-s', '--router_statics', dest='router_statics',
                action='store', type=str, default='',
                help='the comma separated IDs of router_statics you want to list. ')

        parser.add_argument('-r', '--router', dest='router',
                action='store', type=str, default='',
                help='filter by router. ')

        parser.add_argument('-v', '--vxnet', dest='vxnet',
                action='store', type=str, default='',
                help='filter by vxnet. ')

        parser.add_argument('-t', '--static_type', dest='static_type',
                action='store', type=str, default=None,
                help='the static type. 1: port forwarding; 2: VPN; 3: DHCP options; 4: tunnels')

    @classmethod
    def build_directive(cls, options):
        directive = {
                'router_statics': explode_array(options.router_statics),
                'router': options.router,
                'vxnet': options.vxnet,
                'offset':options.offset,
                'limit': options.limit,
                }
        if options.static_type is not None:
            directive.update({'static_type': options.static_type})

        return directive
