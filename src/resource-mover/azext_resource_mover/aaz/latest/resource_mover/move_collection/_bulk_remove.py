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
    "resource-mover move-collection bulk-remove",
)
class BulkRemove(AAZCommand):
    """Removes the set of move resources included in the request body from move collection. The orchestration is done by service. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true.

    The 'az resource-mover move-collection bulk-remove' command remains same for both 'RegionToRegion' and 'RegionToZone' type move collections.

    :example: Remove a move-resource in a move-collection.
        az resource-mover move-collection bulk-remove --move-resources "/subscriptions/subID/resourceGroups/myRG/providers/Microsoft.Migrate/MoveCollections/movecollection1/MoveResources/moveresource1" --validate-only false --name MyMoveCollection --resource-group MyResourceGroup
    """

    _aaz_info = {
        "version": "2023-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.migrate/movecollections/{}/bulkremove", "2023-08-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.move_collection_name = AAZStrArg(
            options=["-n", "--name", "--move-collection-name"],
            help="The Move Collection Name.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.",
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.input_type = AAZStrArg(
            options=["--input-type"],
            arg_group="Body",
            help="Defines the move resource input type.",
            enum={"MoveResourceId": "MoveResourceId", "MoveResourceSourceId": "MoveResourceSourceId"},
        )
        _args_schema.move_resources = AAZListArg(
            options=["--move-resources"],
            arg_group="Body",
            help="Gets or sets the list of resource Id's, by default it accepts move resource id's unless the input type is switched via moveResourceInputType property.",
        )
        _args_schema.validate_only = AAZBoolArg(
            options=["--validate-only"],
            arg_group="Body",
            help="Gets or sets a value indicating whether the operation needs to only run pre-requisite.",
        )

        move_resources = cls._args_schema.move_resources
        move_resources.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.MoveCollectionsBulkRemove(ctx=self.ctx)()
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

    class MoveCollectionsBulkRemove(AAZHttpOperation):
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
            if session.http_response.status_code in [200]:
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/moveCollections/{moveCollectionName}/bulkRemove",
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
                    "moveCollectionName", self.ctx.args.move_collection_name,
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
                    "api-version", "2023-08-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("moveResourceInputType", AAZStrType, ".input_type")
            _builder.set_prop("moveResources", AAZListType, ".move_resources")
            _builder.set_prop("validateOnly", AAZBoolType, ".validate_only")

            move_resources = _builder.get(".moveResources")
            if move_resources is not None:
                move_resources.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

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
            _schema_on_200.end_time = AAZStrType(
                serialized_name="endTime",
                flags={"read_only": True},
            )
            _schema_on_200.error = AAZObjectType()
            _BulkRemoveHelper._build_schema_operation_status_error_read(_schema_on_200.error)
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.start_time = AAZStrType(
                serialized_name="startTime",
                flags={"read_only": True},
            )
            _schema_on_200.status = AAZStrType(
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _BulkRemoveHelper:
    """Helper class for BulkRemove"""

    _schema_affected_move_resource_read = None

    @classmethod
    def _build_schema_affected_move_resource_read(cls, _schema):
        if cls._schema_affected_move_resource_read is not None:
            _schema.id = cls._schema_affected_move_resource_read.id
            _schema.move_resources = cls._schema_affected_move_resource_read.move_resources
            _schema.source_id = cls._schema_affected_move_resource_read.source_id
            return

        cls._schema_affected_move_resource_read = _schema_affected_move_resource_read = AAZObjectType()

        affected_move_resource_read = _schema_affected_move_resource_read
        affected_move_resource_read.id = AAZStrType(
            flags={"read_only": True},
        )
        affected_move_resource_read.move_resources = AAZListType(
            serialized_name="moveResources",
            flags={"read_only": True},
        )
        affected_move_resource_read.source_id = AAZStrType(
            serialized_name="sourceId",
            flags={"read_only": True},
        )

        move_resources = _schema_affected_move_resource_read.move_resources
        move_resources.Element = AAZObjectType()
        cls._build_schema_affected_move_resource_read(move_resources.Element)

        _schema.id = cls._schema_affected_move_resource_read.id
        _schema.move_resources = cls._schema_affected_move_resource_read.move_resources
        _schema.source_id = cls._schema_affected_move_resource_read.source_id

    _schema_operation_status_error_read = None

    @classmethod
    def _build_schema_operation_status_error_read(cls, _schema):
        if cls._schema_operation_status_error_read is not None:
            _schema.additional_info = cls._schema_operation_status_error_read.additional_info
            _schema.code = cls._schema_operation_status_error_read.code
            _schema.details = cls._schema_operation_status_error_read.details
            _schema.message = cls._schema_operation_status_error_read.message
            return

        cls._schema_operation_status_error_read = _schema_operation_status_error_read = AAZObjectType()

        operation_status_error_read = _schema_operation_status_error_read
        operation_status_error_read.additional_info = AAZListType(
            serialized_name="additionalInfo",
            flags={"read_only": True},
        )
        operation_status_error_read.code = AAZStrType(
            flags={"read_only": True},
        )
        operation_status_error_read.details = AAZListType(
            flags={"read_only": True},
        )
        operation_status_error_read.message = AAZStrType(
            flags={"read_only": True},
        )

        additional_info = _schema_operation_status_error_read.additional_info
        additional_info.Element = AAZObjectType()

        _element = _schema_operation_status_error_read.additional_info.Element
        _element.info = AAZObjectType()
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        info = _schema_operation_status_error_read.additional_info.Element.info
        info.move_resources = AAZListType(
            serialized_name="moveResources",
            flags={"read_only": True},
        )

        move_resources = _schema_operation_status_error_read.additional_info.Element.info.move_resources
        move_resources.Element = AAZObjectType()
        cls._build_schema_affected_move_resource_read(move_resources.Element)

        details = _schema_operation_status_error_read.details
        details.Element = AAZObjectType()
        cls._build_schema_operation_status_error_read(details.Element)

        _schema.additional_info = cls._schema_operation_status_error_read.additional_info
        _schema.code = cls._schema_operation_status_error_read.code
        _schema.details = cls._schema_operation_status_error_read.details
        _schema.message = cls._schema_operation_status_error_read.message


__all__ = ["BulkRemove"]
