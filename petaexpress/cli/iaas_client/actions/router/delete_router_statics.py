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

class DeleteRouterStaticsAction(BaseAction):

    action = 'DeleteRouterStatics'
    command = 'delete-router-statics'
    usage = '%(prog)s -s "router_static_id, ..." [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-s', '--router_statics', dest='router_statics',
                action='store', type=str, default='',
                help='the comma separated IDs of router_statics you want to delete. ')

    @classmethod
    def build_directive(cls, options):
        router_statics = explode_array(options.router_statics)
        if not router_statics:
            return None

        return {
            'router_statics': router_statics,
        }
