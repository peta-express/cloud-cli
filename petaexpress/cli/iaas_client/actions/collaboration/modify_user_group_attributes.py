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


class ModifyUserGroupAttributesAction(BaseAction):
    action = 'ModifyUserGroupAttributes'
    command = 'modify-user-group-attributes'
    usage = '%(prog)s [-u <user_group>] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-u", "--user-group", dest="user_group",
                            action="store", type=str, default='',
                            help="The ID of user group which attributes you want to modify.")

        parser.add_argument("-n", "--user-group-name", dest="user_group_name",
                            action="store", type=str, default=None,
                            help="The new name of the user group which will be modified.")

        parser.add_argument("-d", "--description", dest="description",
                            action="store", type=str, default=None,
                            help="The description of the user group.")

        parser.add_argument("-s", "--status", dest="status",
                            action="store", type=str, default=None,
                            help="the status of user group.")

    @classmethod
    def build_directive(cls, options):
        if options.user_group == '':
            print('error: user_group should be specified')
            return None

        directive = {
            "user_group": options.user_group,
            "user_group_name": options.user_group_name,
            "description": options.description,
            "status": options.status,
        }

        return directive
