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
    "baremetalinstance show",
)
class Show(AAZCommand):
    """Get an Azure Bare Metal Instance for the specified subscription, resource group, and instance name.

    :example: Get an Azure Bare Metal Instance
        az baremetalinstance show -g myResourceGroup -n myAzureBareMetalInstance
    """

    _aaz_info = {
        "version": "2024-08-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.baremetalinfrastructure/baremetalinstances/{}", "2024-08-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.instance_name = AAZStrArg(
            options=["-n", "--instance-name"],
            help="Name of the Azure Bare Metal Instance, also known as the ResourceName.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9]+$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AzureBareMetalInstancesGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AzureBareMetalInstancesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BareMetalInfrastructure/bareMetalInstances/{azureBareMetalInstanceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "azureBareMetalInstanceName", self.ctx.args.instance_name,
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
                    "api-version", "2024-08-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.azure_bare_metal_instance_id = AAZStrType(
                serialized_name="azureBareMetalInstanceId",
            )
            properties.hardware_profile = AAZObjectType(
                serialized_name="hardwareProfile",
            )
            properties.hw_revision = AAZStrType(
                serialized_name="hwRevision",
            )
            properties.network_profile = AAZObjectType(
                serialized_name="networkProfile",
            )
            properties.os_profile = AAZObjectType(
                serialized_name="osProfile",
            )
            properties.partner_node_id = AAZStrType(
                serialized_name="partnerNodeId",
            )
            properties.power_state = AAZStrType(
                serialized_name="powerState",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.proximity_placement_group = AAZStrType(
                serialized_name="proximityPlacementGroup",
            )
            properties.storage_profile = AAZObjectType(
                serialized_name="storageProfile",
            )

            hardware_profile = cls._schema_on_200.properties.hardware_profile
            hardware_profile.azure_bare_metal_instance_size = AAZStrType(
                serialized_name="azureBareMetalInstanceSize",
            )
            hardware_profile.hardware_type = AAZStrType(
                serialized_name="hardwareType",
            )

            network_profile = cls._schema_on_200.properties.network_profile
            network_profile.circuit_id = AAZStrType(
                serialized_name="circuitId",
            )
            network_profile.network_interfaces = AAZListType(
                serialized_name="networkInterfaces",
            )

            network_interfaces = cls._schema_on_200.properties.network_profile.network_interfaces
            network_interfaces.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.network_profile.network_interfaces.Element
            _element.ip_address = AAZStrType(
                serialized_name="ipAddress",
            )

            os_profile = cls._schema_on_200.properties.os_profile
            os_profile.computer_name = AAZStrType(
                serialized_name="computerName",
            )
            os_profile.os_type = AAZStrType(
                serialized_name="osType",
            )
            os_profile.ssh_public_key = AAZStrType(
                serialized_name="sshPublicKey",
            )
            os_profile.version = AAZStrType()

            storage_profile = cls._schema_on_200.properties.storage_profile
            storage_profile.nfs_ip_address = AAZStrType(
                serialized_name="nfsIpAddress",
            )
            storage_profile.os_disks = AAZListType(
                serialized_name="osDisks",
            )

            os_disks = cls._schema_on_200.properties.storage_profile.os_disks
            os_disks.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.storage_profile.os_disks.Element
            _element.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            _element.lun = AAZIntType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
