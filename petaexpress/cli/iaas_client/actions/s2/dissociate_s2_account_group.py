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

class DissociateS2AccountGroupAction(BaseAction):
    action = 'DissociateS2AccountGroup'
    command = 'dissociate-s2-account-group'
    usage = '%(prog)s -s <s2_groups> -S <s2_accounts>  [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-s", "--s2-groups", dest="s2_groups",
                            action="store", type=str, default=None,
                            help="the IDs of groups.")

        parser.add_argument("-S", "--s2-accounts", dest="s2_accounts",
                            action="store", type=str, default=None,
                            help="the IDs of accounts.")


    @classmethod
    def build_directive(cls, options):
        for key in ['s2_groups', 's2_accounts']:
            if not hasattr(options, key):
                print("error: [%s] should be specified." % key)
                return None
        
        directive = {
            "s2_groups": explode_array(options.s2_groups),
            "s2_accounts": explode_array(options.s2_accounts),
        }
        
        return directive
