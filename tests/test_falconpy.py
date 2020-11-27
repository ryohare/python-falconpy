
from falconpy.api_complete import APIHarness
from falconpy.services import oauth2
from falconpy.services import hosts
from falconpy.services import user_management
from falconpy.services import spotlight_vulnerabilities
from falconpy.services import sensor_update_policy
from falconpy.services import real_time_response
from falconpy.services import real_time_response_admin
from falconpy.services import prevention_policy
from falconpy.services import iocs
from falconpy.services import intel
from falconpy.services import incidents
from falconpy.services import host_group
from falconpy.services import firewall_policies
from falconpy.services import falconx_sandbox
from falconpy.services import event_streams
from falconpy.services import device_control_policies
from falconpy.services import detects
from falconpy.services import cloud_connect_aws

def test_classes():
    oauth2.OAuth2(creds={})
    access_token = ""
    hosts.Hosts(access_token)
    APIHarness(creds={})
