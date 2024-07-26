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


class DescribeResourceGroupsAction(BaseAction):
    action = 'DescribeResourceGroups'
    command = 'describe-resource-groups'
    usage = '%(prog)s [-r <resource_groups> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-r", "--resource-groups", dest="resource_groups",
                            action="store", type=str, default=None,
                            help="an array including IDs of resource groups.")

        parser.add_argument("-w", "--search-word", dest="search_word",
                            action="store", type=str, default=None,
                            help="the search word which can be instance id and instance name.")

        parser.add_argument("-v", "--verbose", dest="verbose",
                            action="store", type=int, default=1,
                            help="Whether to return redundant message.if it is 1, return the details of the instance related other resources.")

        parser.add_argument("-k", "--sort-key", dest="sort_key",
                            action="store", type=str, default=None,
                            help="the sort key, which defaults be create_time.")

        parser.add_argument("-R", "--reverse", dest="reverse",
                            action="store", type=int, default=0,
                            help="0 for Ascending order, 1 for Descending order.")

    @classmethod
    def build_directive(cls, options):
        directive = {
            "resource_groups": explode_array(options.resource_groups),
            "search_word": options.search_word,
            "verbose": options.verbose,
            "sort_key": options.sort_key,
            "reverse": options.reverse,
            "limit": options.limit,
            "offset": options.offset
        }

        return directive
