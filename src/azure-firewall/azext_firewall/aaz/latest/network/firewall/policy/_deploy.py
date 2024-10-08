# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network firewall policy deploy",
    is_preview=True,
)

class Deploy(AAZCommand):
    """Deploys the firewall policy draft and child rule collection group drafts.
    """

    _aaz_info = {
        "version": "2023-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/firewallpolicies/{}/deploy", "2023-11-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True


    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the Firewall Policy.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.FirewallPolicyDeploymentsDeploy(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class FirewallPolicyDeploymentsDeploy(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName}/deploy",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "firewallPolicyName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-11-01",
                    required=True,
                ),
            }
            return parameters


        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.id = AAZStrType()
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.base_policy = AAZObjectType(
                serialized_name="basePolicy",
            )
            _DeployHelper._build_schema_sub_resource_read(properties.base_policy)
            properties.child_policies = AAZListType(
                serialized_name="childPolicies",
                flags={"read_only": True},
            )
            properties.dns_settings = AAZObjectType(
                serialized_name="dnsSettings",
            )
            properties.explicit_proxy = AAZObjectType(
                serialized_name="explicitProxy",
            )
            properties.firewalls = AAZListType(
                flags={"read_only": True},
            )
            properties.insights = AAZObjectType()
            properties.intrusion_detection = AAZObjectType(
                serialized_name="intrusionDetection",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.snat = AAZObjectType()
            properties.sql = AAZObjectType()
            properties.threat_intel_mode = AAZStrType(
                serialized_name="threatIntelMode",
            )
            properties.threat_intel_whitelist = AAZObjectType(
                serialized_name="threatIntelWhitelist",
            )
            child_policies = cls._schema_on_200.properties.child_policies
            child_policies.Element = AAZObjectType()
            _DeployHelper._build_schema_sub_resource_read(child_policies.Element)

            dns_settings = cls._schema_on_200.properties.dns_settings
            dns_settings.enable_proxy = AAZBoolType(
                serialized_name="enableProxy",
            )
            dns_settings.require_proxy_for_network_rules = AAZBoolType(
                serialized_name="requireProxyForNetworkRules",
                nullable=True,
            )
            dns_settings.servers = AAZListType()

            servers = cls._schema_on_200.properties.dns_settings.servers
            servers.Element = AAZStrType()

            explicit_proxy = cls._schema_on_200.properties.explicit_proxy
            explicit_proxy.enable_explicit_proxy = AAZBoolType(
                serialized_name="enableExplicitProxy",
                nullable=True,
            )
            explicit_proxy.enable_pac_file = AAZBoolType(
                serialized_name="enablePacFile",
                nullable=True,
            )
            explicit_proxy.http_port = AAZIntType(
                serialized_name="httpPort",
            )
            explicit_proxy.https_port = AAZIntType(
                serialized_name="httpsPort",
            )
            explicit_proxy.pac_file = AAZStrType(
                serialized_name="pacFile",
            )
            explicit_proxy.pac_file_port = AAZIntType(
                serialized_name="pacFilePort",
            )

            firewalls = cls._schema_on_200.properties.firewalls
            firewalls.Element = AAZObjectType()
            _DeployHelper._build_schema_sub_resource_read(firewalls.Element)

            insights = cls._schema_on_200.properties.insights
            insights.is_enabled = AAZBoolType(
                serialized_name="isEnabled",
            )
            insights.log_analytics_resources = AAZObjectType(
                serialized_name="logAnalyticsResources",
            )
            insights.retention_days = AAZIntType(
                serialized_name="retentionDays",
            )

            log_analytics_resources = cls._schema_on_200.properties.insights.log_analytics_resources
            log_analytics_resources.default_workspace_id = AAZObjectType(
                serialized_name="defaultWorkspaceId",
            )
            _DeployHelper._build_schema_sub_resource_read(log_analytics_resources.default_workspace_id)
            log_analytics_resources.workspaces = AAZListType()

            workspaces = cls._schema_on_200.properties.insights.log_analytics_resources.workspaces
            workspaces.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.insights.log_analytics_resources.workspaces.Element
            _element.region = AAZStrType()
            _element.workspace_id = AAZObjectType(
                serialized_name="workspaceId",
            )
            _DeployHelper._build_schema_sub_resource_read(_element.workspace_id)

            intrusion_detection = cls._schema_on_200.properties.intrusion_detection
            intrusion_detection.configuration = AAZObjectType()
            intrusion_detection.mode = AAZStrType()
            intrusion_detection.profile = AAZStrType()

            configuration = cls._schema_on_200.properties.intrusion_detection.configuration
            configuration.bypass_traffic_settings = AAZListType(
                serialized_name="bypassTrafficSettings",
            )
            configuration.private_ranges = AAZListType(
                serialized_name="privateRanges",
            )
            configuration.signature_overrides = AAZListType(
                serialized_name="signatureOverrides",
            )

            bypass_traffic_settings = cls._schema_on_200.properties.intrusion_detection.configuration.bypass_traffic_settings
            bypass_traffic_settings.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.intrusion_detection.configuration.bypass_traffic_settings.Element
            _element.description = AAZStrType()
            _element.destination_addresses = AAZListType(
                serialized_name="destinationAddresses",
            )
            _element.destination_ip_groups = AAZListType(
                serialized_name="destinationIpGroups",
            )
            _element.destination_ports = AAZListType(
                serialized_name="destinationPorts",
            )
            _element.name = AAZStrType()
            _element.protocol = AAZStrType()
            _element.source_addresses = AAZListType(
                serialized_name="sourceAddresses",
            )
            _element.source_ip_groups = AAZListType(
                serialized_name="sourceIpGroups",
            )

            destination_addresses = cls._schema_on_200.properties.intrusion_detection.configuration.bypass_traffic_settings.Element.destination_addresses
            destination_addresses.Element = AAZStrType()

            destination_ip_groups = cls._schema_on_200.properties.intrusion_detection.configuration.bypass_traffic_settings.Element.destination_ip_groups
            destination_ip_groups.Element = AAZStrType()

            destination_ports = cls._schema_on_200.properties.intrusion_detection.configuration.bypass_traffic_settings.Element.destination_ports
            destination_ports.Element = AAZStrType()

            source_addresses = cls._schema_on_200.properties.intrusion_detection.configuration.bypass_traffic_settings.Element.source_addresses
            source_addresses.Element = AAZStrType()

            source_ip_groups = cls._schema_on_200.properties.intrusion_detection.configuration.bypass_traffic_settings.Element.source_ip_groups
            source_ip_groups.Element = AAZStrType()

            private_ranges = cls._schema_on_200.properties.intrusion_detection.configuration.private_ranges
            private_ranges.Element = AAZStrType()

            signature_overrides = cls._schema_on_200.properties.intrusion_detection.configuration.signature_overrides
            signature_overrides.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.intrusion_detection.configuration.signature_overrides.Element
            _element.id = AAZStrType()
            _element.mode = AAZStrType()

            snat = cls._schema_on_200.properties.snat
            snat.auto_learn_private_ranges = AAZStrType(
                serialized_name="autoLearnPrivateRanges",
            )
            snat.private_ranges = AAZListType(
                serialized_name="privateRanges",
            )

            private_ranges = cls._schema_on_200.properties.snat.private_ranges
            private_ranges.Element = AAZStrType()

            sql = cls._schema_on_200.properties.sql
            sql.allow_sql_redirect = AAZBoolType(
                serialized_name="allowSqlRedirect",
            )

            threat_intel_whitelist = cls._schema_on_200.properties.threat_intel_whitelist
            threat_intel_whitelist.fqdns = AAZListType()
            threat_intel_whitelist.ip_addresses = AAZListType(
                serialized_name="ipAddresses",
            )

            fqdns = cls._schema_on_200.properties.threat_intel_whitelist.fqdns
            fqdns.Element = AAZStrType()

            ip_addresses = cls._schema_on_200.properties.threat_intel_whitelist.ip_addresses
            ip_addresses.Element = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200       


class _DeployHelper:
    """Helper class for Deploy"""

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()
        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()
        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Deploy"]