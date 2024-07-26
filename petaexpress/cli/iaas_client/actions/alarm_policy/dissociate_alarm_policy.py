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

from petaexpress.cli.iaas_client.actions.base import BaseAction

from petaexpress.cli.misc.utils import explode_array


class DissociateAlarmPolicyAction(BaseAction):
    action = 'DissociateAlarmPolicy'
    command = 'dissociate-alarm-policy'
    usage = '%(prog)s [-a <alarm_policy>] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument("-a", "--alarm-policy", dest="alarm_policy",
                            action="store", type=str, default='',
                            help="the ID of alarm policy.")

        parser.add_argument("-r", "--resources", dest="resources",
                            action="store", type=str, default=None,
                            help="the ID of resources you want to dissociate with alarm policy.")

        parser.add_argument("-R", "--related-resource", dest="related_resource",
                            action="store", type=str, default=None,
                            help="when the network load balancer is bound,related_resource needs to specify a public network IP ID associated with this load balancer.")

    @classmethod
    def build_directive(cls, options):

        if options.alarm_policy == '':
            print('error: alarm_policy should be specified.')
            return None

        directive = {
            "alarm_policy": options.alarm_policy,
            "resources": explode_array(options.resources),
            "related_resource": options.related_resource
        }

        return directive