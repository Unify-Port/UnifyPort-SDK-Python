"""Generated from contracts/device.openapi.yaml; edit the contract, policy, or generator instead."""

# 此文件由生成链维护，手改会在 generate --check 中被拒绝。

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

# public annotation 必须在运行时可解析，供 get_type_hints 等 introspection 使用。
from unifyport.config import RequestOptions
from unifyport.result import ApiResult

from . import models as _models

# recursive JsonValue 会按 method module namespace 求值，因此保留运行时名称。
from .models import JsonValue  # noqa: F401


class AsyncDeviceMethodsMixin:
    if TYPE_CHECKING:

        async def _execute_operation(
            self,
            operation_id: str,
            *,
            path_params: Mapping[str, object] | None = None,
            query: Mapping[str, object] | None = None,
            body: object | None = None,
            headers: Mapping[str, str] | None = None,
            options: RequestOptions | Mapping[str, Any] | None = None,
        ) -> ApiResult[Any]: ...

    async def block_contact(
        self,
        *,
        account_id: str,
        body: _models.BlockContactRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.BlockContactResponse]:
        """封锁联系人"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "blockContact",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def cancel_account_auth(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        body: _models.CancelAccountAuthRequestBody | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.CancelAccountAuthResponse]:
        """取消授权流程"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "cancelAccountAuth",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def check_account_qr_auth(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        body: _models.CheckAccountQrAuthRequestBody | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.CheckAccountQrAuthResponse]:
        """检查二维码授权结果"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "checkAccountQrAuth",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def create_account(
        self,
        *,
        body: _models.CreateAccountRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.CreateAccountResponse]:
        """创建账号"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "createAccount",
            path_params=None,
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def create_api_key(
        self,
        *,
        body: _models.CreateApiKeyRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.CreateApiKeyResponse]:
        """创建 API Key"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "createApiKey",
            path_params=None,
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def create_group(
        self,
        *,
        account_id: str,
        body: _models.CreateGroupRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.CreateGroupResponse]:
        """创建群组"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "createGroup",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def create_webhook_endpoint(
        self,
        *,
        body: _models.CreateWebhookEndpointRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.CreateWebhookEndpointResponse]:
        """创建 webhook endpoint"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "createWebhookEndpoint",
            path_params=None,
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def deactivate_webhook_endpoint(
        self,
        *,
        endpoint_id: str,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.DeactivateWebhookEndpointResponse]:
        """停用 webhook endpoint"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "deactivateWebhookEndpoint",
            path_params={"endpoint_id": endpoint_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def delete_account(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.DeleteAccountResponse]:
        """删除账号"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "deleteAccount",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def delete_conversation_label(
        self,
        *,
        account_id: str,
        body: _models.DeleteConversationLabelRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.DeleteConversationLabelResponse]:
        """删除会话标签"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "deleteConversationLabel",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def delete_webhook_endpoint(
        self,
        *,
        endpoint_id: str,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.DeleteWebhookEndpointResponse]:
        """删除 webhook endpoint"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "deleteWebhookEndpoint",
            path_params={"endpoint_id": endpoint_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def edit_message(
        self,
        *,
        body: _models.EditMessageRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.EditMessageResponse]:
        """编辑消息文本"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "editMessage",
            path_params=None,
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def get_account(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.GetAccountResponse]:
        """获取账号详情"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "getAccount",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def get_account_auth_state(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.GetAccountAuthStateResponse]:
        """获取账号授权状态"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "getAccountAuthState",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def get_contact(
        self,
        *,
        account_id: str,
        contact_id: str,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.GetContactResponse]:
        """获取联系人详情"""
        query = {
            "contact_id": contact_id,
        }
        query_params = {name: value for name, value in query.items() if value is not None} or None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "getContact",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def get_conversation(
        self,
        *,
        account_id: str,
        conversation_id: str,
        type: _models.ConversationType | None = None,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.GetConversationResponse]:
        """获取会话详情"""
        query = {
            "conversation_id": conversation_id,
            "type": type,
        }
        query_params = {name: value for name, value in query.items() if value is not None} or None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "getConversation",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def get_group(
        self,
        *,
        account_id: str,
        group_id: str,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.GetGroupResponse]:
        """获取群组详情"""
        query = {
            "group_id": group_id,
        }
        query_params = {name: value for name, value in query.items() if value is not None} or None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "getGroup",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def get_group_invite_code(
        self,
        *,
        account_id: str,
        group_id: str,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.GetGroupInviteCodeResponse]:
        """获取群邀请链接或邀请码"""
        query = {
            "group_id": group_id,
        }
        query_params = {name: value for name, value in query.items() if value is not None} or None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "getGroupInviteCode",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def get_webhook_endpoint(
        self,
        *,
        endpoint_id: str,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.GetWebhookEndpointResponse]:
        """获取 webhook endpoint"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "getWebhookEndpoint",
            path_params={"endpoint_id": endpoint_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def get_workspace(
        self,
        *,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.GetWorkspaceResponse]:
        """获取当前 workspace"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "getWorkspace",
            path_params=None,
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def import_account_auth_session(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        body: _models.ImportAccountAuthSessionRequestBody | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ImportAccountAuthSessionResponse]:
        """导入会话授权"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "importAccountAuthSession",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def leave_group(
        self,
        *,
        account_id: str,
        body: _models.LeaveGroupRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.LeaveGroupResponse]:
        """退出群组"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "leaveGroup",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def list_accounts(
        self,
        *,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ListAccountsResponse]:
        """列出账号"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "listAccounts",
            path_params=None,
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def list_api_keys(
        self,
        *,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ListApiKeysResponse]:
        """列出 API Key"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "listApiKeys",
            path_params=None,
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def list_contact_blocklist(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ListContactBlocklistResponse]:
        """查询联系人黑名单"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "listContactBlocklist",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def list_contacts(
        self,
        *,
        account_id: str,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        updated_since: str | None = None,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ListContactsResponse]:
        """列出联系人"""
        query = {
            "cursor": cursor,
            "limit": limit,
            "q": q,
            "updated_since": updated_since,
        }
        query_params = {name: value for name, value in query.items() if value is not None} or None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "listContacts",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def list_conversation_labels(
        self,
        *,
        account_id: str,
        cursor: str | None = None,
        limit: int | None = None,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ListConversationLabelsResponse]:
        """列出会话标签"""
        query = {
            "cursor": cursor,
            "limit": limit,
        }
        query_params = {name: value for name, value in query.items() if value is not None} or None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "listConversationLabels",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def list_conversation_members(
        self,
        *,
        account_id: str,
        conversation_id: str,
        type: _models.ConversationType | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ListConversationMembersResponse]:
        """列出会话成员"""
        query = {
            "conversation_id": conversation_id,
            "type": type,
            "cursor": cursor,
            "limit": limit,
        }
        query_params = {name: value for name, value in query.items() if value is not None} or None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "listConversationMembers",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def list_conversations(
        self,
        *,
        account_id: str,
        type: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        label_id: str | None = None,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ListConversationsResponse]:
        """列出会话"""
        query = {
            "type": type,
            "cursor": cursor,
            "limit": limit,
            "label_id": label_id,
        }
        query_params = {name: value for name, value in query.items() if value is not None} or None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "listConversations",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def list_group_join_requests(
        self,
        *,
        account_id: str,
        group_id: str,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ListGroupJoinRequestsResponse]:
        """列出待审批入群申请"""
        query = {
            "group_id": group_id,
        }
        query_params = {name: value for name, value in query.items() if value is not None} or None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "listGroupJoinRequests",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def list_groups(
        self,
        *,
        account_id: str,
        cursor: str | None = None,
        limit: int | None = None,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ListGroupsResponse]:
        """列出群组"""
        query = {
            "cursor": cursor,
            "limit": limit,
        }
        query_params = {name: value for name, value in query.items() if value is not None} or None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "listGroups",
            path_params={"account_id": account_id},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def list_provider_regions(
        self,
        *,
        provider: _models.ProviderName,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ListProviderRegionsResponse]:
        """查询 provider 地区可用性"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "listProviderRegions",
            path_params={"provider": provider},
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def list_webhook_endpoints(
        self,
        *,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ListWebhookEndpointsResponse]:
        """列出 webhook endpoint"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "listWebhookEndpoints",
            path_params=None,
            query=query_params,
            body=None,
            headers=header_params,
            options=options,
        )

    async def mark_conversation_read(
        self,
        *,
        account_id: str,
        body: _models.MarkConversationReadRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.MarkConversationReadResponse]:
        """标记会话已读"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "markConversationRead",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def mark_conversation_unread(
        self,
        *,
        account_id: str,
        body: _models.MarkConversationUnreadRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.MarkConversationUnreadResponse]:
        """标记会话未读"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "markConversationUnread",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def mute_conversation(
        self,
        *,
        account_id: str,
        body: _models.MuteConversationRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.MuteConversationResponse]:
        """静音会话"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "muteConversation",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def pin_conversation(
        self,
        *,
        account_id: str,
        body: _models.PinConversationRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.PinConversationResponse]:
        """置顶会话"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "pinConversation",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def pin_message(
        self,
        *,
        body: _models.PinMessageRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.PinMessageResponse]:
        """置顶或取消置顶消息"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "pinMessage",
            path_params=None,
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def react_message(
        self,
        *,
        body: _models.ReactMessageRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ReactMessageResponse]:
        """给消息加表情回应或取消回应"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "reactMessage",
            path_params=None,
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def reconnect_account_runtime(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        body: _models.ReconnectAccountRuntimeRequestBody | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.ReconnectAccountRuntimeResponse]:
        """重连账号运行态"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "reconnectAccountRuntime",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def refresh_account_runtime(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        body: _models.RefreshAccountRuntimeRequestBody | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.RefreshAccountRuntimeResponse]:
        """刷新账号运行态"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "refreshAccountRuntime",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def revoke_message(
        self,
        *,
        body: _models.RevokeMessageRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.RevokeMessageResponse]:
        """撤回消息"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "revokeMessage",
            path_params=None,
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def rotate_api_key(
        self,
        *,
        key_id: str,
        body: _models.RotateApiKeyRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.RotateApiKeyResponse]:
        """轮换 API Key"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "rotateApiKey",
            path_params={"key_id": key_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def send_message(
        self,
        *,
        body: _models.SendMessageRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.SendMessageResponse]:
        """发送消息"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "sendMessage",
            path_params=None,
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def set_contact_note(
        self,
        *,
        account_id: str,
        body: _models.SetContactNoteRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.SetContactNoteResponse]:
        """设置或清空联系人备注"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "setContactNote",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def set_conversation_label_members(
        self,
        *,
        account_id: str,
        body: _models.SetConversationLabelMembersRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.SetConversationLabelMembersResponse]:
        """给会话打标或移除标签"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "setConversationLabelMembers",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def set_group_join_approval_mode(
        self,
        *,
        account_id: str,
        body: _models.SetGroupJoinApprovalModeRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.SetGroupJoinApprovalModeResponse]:
        """设置入群审批模式"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "setGroupJoinApprovalMode",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def start_account_auth(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        body: _models.StartAccountAuthRequestBody | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.StartAccountAuthResponse]:
        """启动验证码类授权"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "startAccountAuth",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def start_account_qr_auth(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        body: _models.StartAccountQrAuthRequestBody | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.StartAccountQrAuthResponse]:
        """启动二维码授权"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "startAccountQrAuth",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def start_account_runtime(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        body: _models.StartAccountRuntimeRequestBody | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.StartAccountRuntimeResponse]:
        """启动账号运行态"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "startAccountRuntime",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def stop_account_runtime(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        body: _models.StopAccountRuntimeRequestBody | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.StopAccountRuntimeResponse]:
        """停止账号运行态"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "stopAccountRuntime",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def submit_account_auth_code(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        body: _models.SubmitAccountAuthCodeRequestBody | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.SubmitAccountAuthCodeResponse]:
        """提交验证码"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "submitAccountAuthCode",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def submit_account_auth_password(
        self,
        *,
        account_id: str,
        x_request_id: str | None = None,
        body: _models.SubmitAccountAuthPasswordRequestBody | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.SubmitAccountAuthPasswordResponse]:
        """提交二次密码"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "submitAccountAuthPassword",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def unblock_contact(
        self,
        *,
        account_id: str,
        body: _models.UnblockContactRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.UnblockContactResponse]:
        """解封联系人"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "unblockContact",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def unmute_conversation(
        self,
        *,
        account_id: str,
        body: _models.UnmuteConversationRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.UnmuteConversationResponse]:
        """取消静音会话"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "unmuteConversation",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def unpin_conversation(
        self,
        *,
        account_id: str,
        body: _models.UnpinConversationRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.UnpinConversationResponse]:
        """取消置顶会话"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "unpinConversation",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def update_account(
        self,
        *,
        account_id: str,
        body: _models.UpdateAccountRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.UpdateAccountResponse]:
        """更新账号"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "updateAccount",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def update_api_key_status(
        self,
        *,
        key_id: str,
        body: _models.UpdateApiKeyStatusRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.UpdateApiKeyStatusResponse]:
        """更新 API Key 状态"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "updateApiKeyStatus",
            path_params={"key_id": key_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def update_group_info(
        self,
        *,
        account_id: str,
        body: _models.UpdateGroupInfoRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.UpdateGroupInfoResponse]:
        """修改群信息"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "updateGroupInfo",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def update_group_join_requests(
        self,
        *,
        account_id: str,
        body: _models.UpdateGroupJoinRequestsRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.UpdateGroupJoinRequestsResponse]:
        """处理入群申请"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "updateGroupJoinRequests",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def update_group_members(
        self,
        *,
        account_id: str,
        body: _models.UpdateGroupMembersRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.UpdateGroupMembersResponse]:
        """管理群成员"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "updateGroupMembers",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def update_webhook_endpoint(
        self,
        *,
        endpoint_id: str,
        body: _models.UpdateWebhookEndpointRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.UpdateWebhookEndpointResponse]:
        """更新 webhook endpoint"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "updateWebhookEndpoint",
            path_params={"endpoint_id": endpoint_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def update_workspace(
        self,
        *,
        body: _models.UpdateWorkspaceRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.UpdateWorkspaceResponse]:
        """更新当前 workspace"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "updateWorkspace",
            path_params=None,
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )

    async def upsert_conversation_label(
        self,
        *,
        account_id: str,
        body: _models.UpsertConversationLabelRequestBody,
        x_request_id: str | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[_models.UpsertConversationLabelResponse]:
        """新建或更新会话标签"""
        query_params = None
        request_headers = {
            "X-Request-Id": x_request_id,
        }
        header_params = {
            name: value for name, value in request_headers.items() if value is not None
        } or None
        return await self._execute_operation(
            "upsertConversationLabel",
            path_params={"account_id": account_id},
            query=query_params,
            body=body,
            headers=header_params,
            options=options,
        )


__all__ = ["AsyncDeviceMethodsMixin"]
