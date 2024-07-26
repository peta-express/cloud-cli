# coding: utf-8

from petaexpress.cli.iaas_client.actions.base import BaseAction
from petaexpress.cli.misc.utils import explode_array

class StopLoadBalancersAction(BaseAction):

    action = 'StopLoadBalancers'
    command = 'stop-loadbalancers'
    usage = '%(prog)s -l <loadbalancers> [-f <conf_file>]'
    description = 'Stop one or more load balancers'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-l', '--loadbalancers', dest='loadbalancers',
                action='store', type=str, default='',
                help='the comma separated IDs of load balancers you want to stop.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'loadbalancers': options.loadbalancers,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
                'loadbalancers': explode_array(options.loadbalancers),
                }
