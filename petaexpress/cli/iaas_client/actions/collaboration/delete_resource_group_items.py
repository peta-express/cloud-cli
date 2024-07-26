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


class DeleteResourceGroupItemsAction(BaseAction):
    action = 'DeleteResourceGroupItems'
    command = 'delete-resource-group-items'
    usage = '%(prog)s [-g <resource_group> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-g", "--resource-group", dest="resource_group",
                            action="store", type=str, default='',
                            help="the ID of the resource group.")

        parser.add_argument("-r", "--resources", dest="resources",
                            action="store", type=str, default='',
                            help="An array including IDs of resources which you want to delete.")

    @classmethod
    def build_directive(cls, options):
        if options.resource_group == '':
            print('error: resource_group should be specified')
            return None
        resources = explode_array(options.resources)
        if not resources:
            print('error: resources should be specified')
            return None

        directive = {
            "resource_group": options.resource_group,
            "resources": resources
        }

        return directive
