"""Generated from contracts/device.openapi.yaml; edit the contract, policy, or generator instead."""

# 此文件由生成链维护，手改会在 generate --check 中被拒绝。

from types import MappingProxyType
from typing import (
    Final,
    Generic,
    Literal,
    NotRequired,
    Required,
    TypeAlias,
    TypeVar,
)

from typing_extensions import TypedDict

JsonScalar: TypeAlias = bool | float | int | str | None
JsonValue: TypeAlias = JsonScalar | list["JsonValue"] | dict[str, "JsonValue"]

ResponseT = TypeVar("ResponseT")


class ResponseEnvelope(TypedDict, Generic[ResponseT], total=False):
    request_id: NotRequired[str]
    client_request_id: NotRequired[str]
    data: Required[ResponseT]


class APIKey(TypedDict, total=False):
    id: Required[str]
    key_prefix: Required[str]
    name: Required[str]
    status: Required[Literal["active", "inactive"]]


class APIKeyCreateRequest(TypedDict, total=False):
    name: Required[str]
    prefix: NotRequired[str]


class APIKeyCreateResult(TypedDict, total=False):
    api_key: Required[str]
    key: Required["APIKey"]


class APIKeyStatusUpdateRequest(TypedDict, total=False):
    status: Required[Literal["active", "inactive"]]


class Account(TypedDict, total=False):
    auth_mode: NotRequired[str]
    capabilities: NotRequired[list[str]]
    id: Required[str]
    metadata: NotRequired["FreeFormObject"]
    name: Required[str]
    provider: Required["ProviderName"]
    provider_account_ref: NotRequired[str]
    provider_profile: NotRequired["ProviderProfile"]
    proxy: NotRequired["FreeFormObject"]
    region: Required[str]
    runtime_status: NotRequired["RuntimeStatus"]
    status: Required[str]


class AccountRequest(TypedDict, total=False):
    auth_mode: NotRequired[str]
    capabilities: NotRequired[list[str]]
    metadata: NotRequired["FreeFormObject"]
    name: NotRequired[str]
    provider: Required["ProviderName"]
    provider_account_ref: NotRequired[str]
    provider_data: NotRequired["FreeFormObject"]
    proxy: NotRequired["FreeFormObject"]
    region: Required[str]
    runtime_status: NotRequired["RuntimeStatus"]
    status: NotRequired[str]


class AccountSession(TypedDict, total=False):
    account_id: Required[str]
    auth_fields: NotRequired[list["AuthField"]]
    auth_payload: NotRequired["FreeFormObject"]
    expires_at: NotRequired[str]
    last_error: NotRequired[str]
    status: Required[str]


class AuthField(TypedDict, total=False):
    label: NotRequired[str]
    placeholder: NotRequired[str]
    required: Required[bool]
    type: Required[str]


class Contact(TypedDict, total=False):
    avatar_url: Required[str]
    conversation_id: Required[str]
    display_name: Required[str]
    extra: NotRequired["FreeFormObject"]
    id: Required[str]
    is_blocked: NotRequired[bool]
    provider_user_id: Required[str]


class ContactBlocklistResult(TypedDict, total=False):
    blocklist: Required[list[str]]
    dhash: NotRequired[str]


class ContactCard(TypedDict, total=False):
    emails: NotRequired[list["ContactEmail"]]
    name: Required[str]
    organization: NotRequired[str]
    phones: NotRequired[list["ContactPhone"]]
    title: NotRequired[str]


class ContactEmail(TypedDict, total=False):
    address: Required[str]
    type: NotRequired[str]


class ContactIdRequest(TypedDict, total=False):
    contact_id: Required[str]


class ContactListResult(TypedDict, total=False):
    has_more: Required[bool]
    items: Required[list["Contact"]]
    next_cursor: NotRequired[str]


class ContactNoteRequest(TypedDict, total=False):
    contact_id: Required[str]
    note: Required[str]


class ContactPhone(TypedDict, total=False):
    number: Required[str]
    type: NotRequired[str]


class Conversation(TypedDict, total=False):
    avatar_url: Required[str]
    conversation_id: Required[str]
    created_at: NotRequired[str]
    description: NotRequired[str]
    extra: NotRequired["FreeFormObject"]
    is_muted: Required[bool]
    is_pinned: Required[bool]
    last_message_at: NotRequired[str]
    last_message_text: NotRequired[str]
    members_count: NotRequired[int]
    subscribers_count: NotRequired[int]
    title: Required[str]
    type: Required["ConversationType"]
    unread_count: Required[int]
    username: NotRequired[str]


class ConversationIdRequest(TypedDict, total=False):
    conversation_id: Required[str]


class ConversationLabel(TypedDict, total=False):
    id: Required[str]
    name: Required[str]


class ConversationLabelDeleteRequest(TypedDict, total=False):
    label_id: Required[str]


class ConversationLabelDeleteResult(TypedDict, total=False):
    deleted: Required[Literal[True]]
    label_id: Required[str]


class ConversationLabelListResult(TypedDict, total=False):
    has_more: Required[bool]
    items: Required[list["ConversationLabel"]]
    next_cursor: NotRequired[str]


class ConversationLabelMembersRequest(TypedDict, total=False):
    action: Required[Literal["add", "remove"]]
    conversation_ids: Required[list[str]]
    label_id: Required[str]


class ConversationLabelMembersResult(TypedDict, total=False):
    action: Required[Literal["add", "remove"]]
    conversation_ids: Required[list[str]]
    label_id: Required[str]


class ConversationLabelUpsertRequest(TypedDict, total=False):
    label_id: NotRequired[str]
    name: Required[str]


class ConversationListResult(TypedDict, total=False):
    has_more: Required[bool]
    items: Required[list["Conversation"]]
    next_cursor: NotRequired[str]


class ConversationMember(TypedDict, total=False):
    avatar_url: Required[str]
    display_name: Required[str]
    extra: NotRequired["FreeFormObject"]
    joined_at: NotRequired[str]
    peer_id: Required[str]
    role: NotRequired[str]
    username: NotRequired[str]


class ConversationMemberListResult(TypedDict, total=False):
    has_more: Required[bool]
    items: Required[list["ConversationMember"]]
    next_cursor: NotRequired[str]


class ConversationMuteRequest(TypedDict, total=False):
    conversation_id: Required[str]
    duration: NotRequired[int]
    mute_until: NotRequired[str]


class ConversationReadRequest(TypedDict, total=False):
    conversation_id: Required[str]
    up_to_message_id: NotRequired[str]
    up_to_message_sender_id: NotRequired[str]


ConversationType: TypeAlias = Literal[
    "user",
    "group",
    "channel",
]


class Error(TypedDict, total=False):
    code: Required[str]
    message: Required[str]


class ErrorEnvelope(TypedDict, total=False):
    client_request_id: NotRequired[str]
    error: Required["Error"]
    request_id: NotRequired[str]


FreeFormObject: TypeAlias = dict[str, JsonValue]


class Group(TypedDict, total=False):
    avatar_url: Required[str]
    conversation_id: Required[str]
    created_at: NotRequired[str]
    description: NotRequired[str]
    extra: NotRequired["FreeFormObject"]
    id: Required[str]
    joined_at: NotRequired[str]
    member_count: NotRequired[int]
    name: Required[str]


class GroupCreateRequest(TypedDict, total=False):
    members: NotRequired[list[str]]
    name: Required[str]


class GroupCreateResult(TypedDict, total=False):
    id: Required[str]


class GroupIdRequest(TypedDict, total=False):
    group_id: Required[str]


class GroupInfoUpdateRequest(TypedDict, total=False):
    avatar_url: NotRequired[str]
    description: NotRequired[str]
    group_id: Required[str]
    name: NotRequired[str]


class GroupInviteCode(TypedDict, total=False):
    invite_code: Required[str]
    invite_url: Required[str]


class GroupJoinApprovalModeRequest(TypedDict, total=False):
    enabled: Required[bool]
    group_id: Required[str]


class GroupJoinRequest(TypedDict, total=False):
    id: Required[str]
    lid: NotRequired[str]
    phone: NotRequired[str]
    requested_at: NotRequired[str]


class GroupJoinRequestsResult(TypedDict, total=False):
    group_id: Required[str]
    items: Required[list["GroupJoinRequest"]]


class GroupJoinRequestsUpdateRequest(TypedDict, total=False):
    action: Required[Literal["approve", "reject"]]
    group_id: Required[str]
    member_ids: Required[list[str]]


class GroupListResult(TypedDict, total=False):
    has_more: Required[bool]
    items: Required[list["Group"]]
    next_cursor: NotRequired[str]


class GroupMemberUpdateRequest(TypedDict, total=False):
    action: Required[Literal["add", "remove", "promote", "demote"]]
    group_id: Required[str]
    member_id: Required[str]


class Mention(TypedDict, total=False):
    id: Required[str]


class MessageEditRequest(TypedDict, total=False):
    account_id: Required[str]
    content: Required[str]
    conversation_id: Required[str]
    message_id: Required[str]


class MessagePayload(TypedDict, total=False):
    caption: NotRequired[str]
    contacts: NotRequired[list["ContactCard"]]
    file_key: NotRequired[str]
    file_url: NotRequired[str]
    text: NotRequired[str]
    type: Required[Literal["text", "image", "video", "audio", "document", "file", "contact"]]
    url: NotRequired[str]


class MessagePinRequest(TypedDict, total=False):
    account_id: Required[str]
    conversation_id: Required[str]
    duration_seconds: NotRequired[int]
    message_id: Required[str]
    pinned: Required[bool]
    sender_id: NotRequired[str]


class MessageReactionRequest(TypedDict, total=False):
    account_id: Required[str]
    conversation_id: Required[str]
    emoji: NotRequired[str]
    message_id: Required[str]
    sender_id: NotRequired[str]


class MessageTargetRequest(TypedDict, total=False):
    account_id: Required[str]
    conversation_id: Required[str]
    message_id: Required[str]
    sender_id: NotRequired[str]


class OkData(TypedDict, total=False):
    ok: Required[Literal[True]]


ProviderName: TypeAlias = Literal[
    "telegram",
    "whatsapp",
    "line",
    "twitter",
    "x",
    "zalo",
    "tiktok",
]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class ProviderProfile(TypedDict, total=False, extra_items=JsonValue):  # type: ignore[call-arg, unused-ignore]
    avatar_url: NotRequired[str]
    bio: NotRequired[str]
    display_name: NotRequired[str]
    first_name: NotRequired[str]
    id: NotRequired[str]
    last_name: NotRequired[str]
    phone: NotRequired[str]
    username: NotRequired[str]


class ProviderRegionsResponse(TypedDict, total=False):
    provider: Required["ProviderName"]
    regions: Required[list["RegionAvailability"]]


class Recipient(TypedDict, total=False):
    id: Required[str]
    type: Required["ConversationType"]


class RegionAvailability(TypedDict, total=False):
    allocatable: Required[bool]
    region: Required[str]
    supported: Required[bool]


class ReplyTo(TypedDict, total=False):
    reply_token: Required[str]


class ResponseMeta(TypedDict, total=False):
    client_request_id: NotRequired[str]
    request_id: NotRequired[str]


class RuntimeActionResult(TypedDict, total=False):
    account_id: Required[str]
    action: Required[Literal["refresh_status", "start", "stop", "reconnect"]]
    operation_status: Required[str]
    provider: Required["ProviderName"]
    runtime_error: Required[str]
    runtime_status: Required["RuntimeStatus"]


RuntimeStatus: TypeAlias = Literal[
    "unknown",
    "starting",
    "running",
    "stopping",
    "stopped",
    "reconnecting",
    "disconnected",
    "error",
]


class SendMessageRequest(TypedDict, total=False):
    account_id: Required[str]
    mentions: NotRequired[list["Mention"]]
    message: Required["MessagePayload"]
    provider_data: NotRequired["FreeFormObject"]
    reply_to: NotRequired["ReplyTo"]
    to: Required["Recipient"]


class SendMessageResult(TypedDict, total=False):
    account_id: Required[str]
    message_id: Required[str]
    provider_ref: NotRequired[str]
    reply_token: NotRequired[str]
    status: Required[str]


StandardEventType: TypeAlias = Literal[
    "*",
    "message.received",
    "message.updated",
    "message.deleted",
    "message.read",
    "message.reaction",
    "message.delivered",
    "conversation.updated",
    "conversation.deleted",
    "conversation.cleared",
    "conversation.history",
    "group.updated",
    "group.join_request",
    "account.status.updated",
    "account.started",
    "account.history.synced",
    "account.auth.required",
    "account.auth.succeeded",
    "account.auth.failed",
]


class WebhookEndpoint(TypedDict, total=False):
    id: Required[str]
    retry_policy: NotRequired["FreeFormObject"]
    signing_enabled: Required[bool]
    status: Required[str]
    subscribed_events: NotRequired[list["StandardEventType"]]
    url: Required[str]


class WebhookEndpointRequest(TypedDict, total=False):
    retry_policy: NotRequired["FreeFormObject"]
    signing_secret: NotRequired[str]
    status: Required[str]
    subscribed_events: NotRequired[list["StandardEventType"]]
    url: Required[str]


class Workspace(TypedDict, total=False):
    account_quota: Required[int]
    account_quota_unlimited: Required[bool]
    metadata: NotRequired[dict[str, str]]
    name: Required[str]
    status: Required[str]


class WorkspaceUpdateRequest(TypedDict, total=False):
    metadata: NotRequired[dict[str, str]]
    name: Required[str]
    status: Required[str]


MessageRevokeRequest: TypeAlias = MessageTargetRequest


class BlockContactPath(TypedDict, total=False):
    account_id: Required[str]


class BlockContactQuery(TypedDict, total=False):
    pass


BlockContactRequestBody: TypeAlias = ContactIdRequest


BlockContactResponse: TypeAlias = ResponseEnvelope[OkData]


class CancelAccountAuthPath(TypedDict, total=False):
    account_id: Required[str]


class CancelAccountAuthQuery(TypedDict, total=False):
    pass


CancelAccountAuthRequestBody: TypeAlias = FreeFormObject


CancelAccountAuthResponse: TypeAlias = ResponseEnvelope[FreeFormObject]


class CheckAccountQrAuthPath(TypedDict, total=False):
    account_id: Required[str]


class CheckAccountQrAuthQuery(TypedDict, total=False):
    pass


CheckAccountQrAuthRequestBody: TypeAlias = FreeFormObject


CheckAccountQrAuthResponse: TypeAlias = ResponseEnvelope[FreeFormObject]


class CreateAccountPath(TypedDict, total=False):
    pass


class CreateAccountQuery(TypedDict, total=False):
    pass


CreateAccountRequestBody: TypeAlias = AccountRequest


CreateAccountResponse: TypeAlias = ResponseEnvelope[Account]


class CreateApiKeyPath(TypedDict, total=False):
    pass


class CreateApiKeyQuery(TypedDict, total=False):
    pass


CreateApiKeyRequestBody: TypeAlias = APIKeyCreateRequest


CreateApiKeyResponse: TypeAlias = ResponseEnvelope[APIKeyCreateResult]


class CreateGroupPath(TypedDict, total=False):
    account_id: Required[str]


class CreateGroupQuery(TypedDict, total=False):
    pass


CreateGroupRequestBody: TypeAlias = GroupCreateRequest


CreateGroupResponse: TypeAlias = ResponseEnvelope[GroupCreateResult]


class CreateWebhookEndpointPath(TypedDict, total=False):
    pass


class CreateWebhookEndpointQuery(TypedDict, total=False):
    pass


CreateWebhookEndpointRequestBody: TypeAlias = WebhookEndpointRequest


CreateWebhookEndpointResponse: TypeAlias = ResponseEnvelope[WebhookEndpoint]


class DeactivateWebhookEndpointPath(TypedDict, total=False):
    endpoint_id: Required[str]


class DeactivateWebhookEndpointQuery(TypedDict, total=False):
    pass


DeactivateWebhookEndpointRequestBody: TypeAlias = None


DeactivateWebhookEndpointResponse: TypeAlias = ResponseEnvelope[WebhookEndpoint]


class DeleteAccountPath(TypedDict, total=False):
    account_id: Required[str]


class DeleteAccountQuery(TypedDict, total=False):
    pass


DeleteAccountRequestBody: TypeAlias = None


DeleteAccountResponse: TypeAlias = None


class DeleteConversationLabelPath(TypedDict, total=False):
    account_id: Required[str]


class DeleteConversationLabelQuery(TypedDict, total=False):
    pass


DeleteConversationLabelRequestBody: TypeAlias = ConversationLabelDeleteRequest


DeleteConversationLabelResponse: TypeAlias = ResponseEnvelope[ConversationLabelDeleteResult]


class DeleteWebhookEndpointPath(TypedDict, total=False):
    endpoint_id: Required[str]


class DeleteWebhookEndpointQuery(TypedDict, total=False):
    pass


DeleteWebhookEndpointRequestBody: TypeAlias = None


DeleteWebhookEndpointResponse: TypeAlias = None


class EditMessagePath(TypedDict, total=False):
    pass


class EditMessageQuery(TypedDict, total=False):
    pass


EditMessageRequestBody: TypeAlias = MessageEditRequest


EditMessageResponse: TypeAlias = ResponseEnvelope[OkData]


class GetAccountPath(TypedDict, total=False):
    account_id: Required[str]


class GetAccountQuery(TypedDict, total=False):
    pass


GetAccountRequestBody: TypeAlias = None


GetAccountResponse: TypeAlias = ResponseEnvelope[Account]


class GetAccountAuthStatePath(TypedDict, total=False):
    account_id: Required[str]


class GetAccountAuthStateQuery(TypedDict, total=False):
    pass


GetAccountAuthStateRequestBody: TypeAlias = None


GetAccountAuthStateResponse: TypeAlias = ResponseEnvelope[AccountSession]


class GetContactPath(TypedDict, total=False):
    account_id: Required[str]


class GetContactQuery(TypedDict, total=False):
    contact_id: Required[str]


GetContactRequestBody: TypeAlias = None


GetContactResponse: TypeAlias = ResponseEnvelope[Contact]


class GetConversationPath(TypedDict, total=False):
    account_id: Required[str]


class GetConversationQuery(TypedDict, total=False):
    conversation_id: Required[str]
    type: NotRequired[ConversationType]


GetConversationRequestBody: TypeAlias = None


GetConversationResponse: TypeAlias = ResponseEnvelope[Conversation]


class GetGroupPath(TypedDict, total=False):
    account_id: Required[str]


class GetGroupQuery(TypedDict, total=False):
    group_id: Required[str]


GetGroupRequestBody: TypeAlias = None


GetGroupResponse: TypeAlias = ResponseEnvelope[Group]


class GetGroupInviteCodePath(TypedDict, total=False):
    account_id: Required[str]


class GetGroupInviteCodeQuery(TypedDict, total=False):
    group_id: Required[str]


GetGroupInviteCodeRequestBody: TypeAlias = None


GetGroupInviteCodeResponse: TypeAlias = ResponseEnvelope[GroupInviteCode]


class GetWebhookEndpointPath(TypedDict, total=False):
    endpoint_id: Required[str]


class GetWebhookEndpointQuery(TypedDict, total=False):
    pass


GetWebhookEndpointRequestBody: TypeAlias = None


GetWebhookEndpointResponse: TypeAlias = ResponseEnvelope[WebhookEndpoint]


class GetWorkspacePath(TypedDict, total=False):
    pass


class GetWorkspaceQuery(TypedDict, total=False):
    pass


GetWorkspaceRequestBody: TypeAlias = None


GetWorkspaceResponse: TypeAlias = ResponseEnvelope[Workspace]


class ImportAccountAuthSessionPath(TypedDict, total=False):
    account_id: Required[str]


class ImportAccountAuthSessionQuery(TypedDict, total=False):
    pass


ImportAccountAuthSessionRequestBody: TypeAlias = FreeFormObject


ImportAccountAuthSessionResponse: TypeAlias = ResponseEnvelope[FreeFormObject]


class LeaveGroupPath(TypedDict, total=False):
    account_id: Required[str]


class LeaveGroupQuery(TypedDict, total=False):
    pass


LeaveGroupRequestBody: TypeAlias = GroupIdRequest


LeaveGroupResponse: TypeAlias = ResponseEnvelope[OkData]


class ListAccountsPath(TypedDict, total=False):
    pass


class ListAccountsQuery(TypedDict, total=False):
    pass


ListAccountsRequestBody: TypeAlias = None


ListAccountsResponse: TypeAlias = ResponseEnvelope[list[Account]]


class ListApiKeysPath(TypedDict, total=False):
    pass


class ListApiKeysQuery(TypedDict, total=False):
    pass


ListApiKeysRequestBody: TypeAlias = None


ListApiKeysResponse: TypeAlias = ResponseEnvelope[list[APIKey]]


class ListContactBlocklistPath(TypedDict, total=False):
    account_id: Required[str]


class ListContactBlocklistQuery(TypedDict, total=False):
    pass


ListContactBlocklistRequestBody: TypeAlias = None


ListContactBlocklistResponse: TypeAlias = ResponseEnvelope[ContactBlocklistResult]


class ListContactsPath(TypedDict, total=False):
    account_id: Required[str]


class ListContactsQuery(TypedDict, total=False):
    cursor: NotRequired[str]
    limit: NotRequired[int]
    q: NotRequired[str]
    updated_since: NotRequired[str]


ListContactsRequestBody: TypeAlias = None


ListContactsResponse: TypeAlias = ResponseEnvelope[ContactListResult]


class ListConversationLabelsPath(TypedDict, total=False):
    account_id: Required[str]


class ListConversationLabelsQuery(TypedDict, total=False):
    cursor: NotRequired[str]
    limit: NotRequired[int]


ListConversationLabelsRequestBody: TypeAlias = None


ListConversationLabelsResponse: TypeAlias = ResponseEnvelope[ConversationLabelListResult]


class ListConversationMembersPath(TypedDict, total=False):
    account_id: Required[str]


class ListConversationMembersQuery(TypedDict, total=False):
    conversation_id: Required[str]
    type: NotRequired[ConversationType]
    cursor: NotRequired[str]
    limit: NotRequired[int]


ListConversationMembersRequestBody: TypeAlias = None


ListConversationMembersResponse: TypeAlias = ResponseEnvelope[ConversationMemberListResult]


class ListConversationsPath(TypedDict, total=False):
    account_id: Required[str]


class ListConversationsQuery(TypedDict, total=False):
    type: NotRequired[str]
    cursor: NotRequired[str]
    limit: NotRequired[int]
    label_id: NotRequired[str]


ListConversationsRequestBody: TypeAlias = None


ListConversationsResponse: TypeAlias = ResponseEnvelope[ConversationListResult]


class ListGroupJoinRequestsPath(TypedDict, total=False):
    account_id: Required[str]


class ListGroupJoinRequestsQuery(TypedDict, total=False):
    group_id: Required[str]


ListGroupJoinRequestsRequestBody: TypeAlias = None


ListGroupJoinRequestsResponse: TypeAlias = ResponseEnvelope[GroupJoinRequestsResult]


class ListGroupsPath(TypedDict, total=False):
    account_id: Required[str]


class ListGroupsQuery(TypedDict, total=False):
    cursor: NotRequired[str]
    limit: NotRequired[int]


ListGroupsRequestBody: TypeAlias = None


ListGroupsResponse: TypeAlias = ResponseEnvelope[GroupListResult]


class ListProviderRegionsPath(TypedDict, total=False):
    provider: Required[ProviderName]


class ListProviderRegionsQuery(TypedDict, total=False):
    pass


ListProviderRegionsRequestBody: TypeAlias = None


ListProviderRegionsResponse: TypeAlias = ResponseEnvelope[ProviderRegionsResponse]


class ListWebhookEndpointsPath(TypedDict, total=False):
    pass


class ListWebhookEndpointsQuery(TypedDict, total=False):
    pass


ListWebhookEndpointsRequestBody: TypeAlias = None


ListWebhookEndpointsResponse: TypeAlias = ResponseEnvelope[list[WebhookEndpoint]]


class MarkConversationReadPath(TypedDict, total=False):
    account_id: Required[str]


class MarkConversationReadQuery(TypedDict, total=False):
    pass


MarkConversationReadRequestBody: TypeAlias = ConversationReadRequest


MarkConversationReadResponse: TypeAlias = ResponseEnvelope[OkData]


class MarkConversationUnreadPath(TypedDict, total=False):
    account_id: Required[str]


class MarkConversationUnreadQuery(TypedDict, total=False):
    pass


MarkConversationUnreadRequestBody: TypeAlias = ConversationIdRequest


MarkConversationUnreadResponse: TypeAlias = ResponseEnvelope[OkData]


class MuteConversationPath(TypedDict, total=False):
    account_id: Required[str]


class MuteConversationQuery(TypedDict, total=False):
    pass


MuteConversationRequestBody: TypeAlias = ConversationMuteRequest


MuteConversationResponse: TypeAlias = ResponseEnvelope[OkData]


class PinConversationPath(TypedDict, total=False):
    account_id: Required[str]


class PinConversationQuery(TypedDict, total=False):
    pass


PinConversationRequestBody: TypeAlias = ConversationIdRequest


PinConversationResponse: TypeAlias = ResponseEnvelope[OkData]


class PinMessagePath(TypedDict, total=False):
    pass


class PinMessageQuery(TypedDict, total=False):
    pass


PinMessageRequestBody: TypeAlias = MessagePinRequest


PinMessageResponse: TypeAlias = ResponseEnvelope[OkData]


class ReactMessagePath(TypedDict, total=False):
    pass


class ReactMessageQuery(TypedDict, total=False):
    pass


ReactMessageRequestBody: TypeAlias = MessageReactionRequest


ReactMessageResponse: TypeAlias = ResponseEnvelope[OkData]


class ReconnectAccountRuntimePath(TypedDict, total=False):
    account_id: Required[str]


class ReconnectAccountRuntimeQuery(TypedDict, total=False):
    pass


ReconnectAccountRuntimeRequestBody: TypeAlias = FreeFormObject


ReconnectAccountRuntimeResponse: TypeAlias = ResponseEnvelope[RuntimeActionResult]


class RefreshAccountRuntimePath(TypedDict, total=False):
    account_id: Required[str]


class RefreshAccountRuntimeQuery(TypedDict, total=False):
    pass


RefreshAccountRuntimeRequestBody: TypeAlias = FreeFormObject


RefreshAccountRuntimeResponse: TypeAlias = ResponseEnvelope[RuntimeActionResult]


class RevokeMessagePath(TypedDict, total=False):
    pass


class RevokeMessageQuery(TypedDict, total=False):
    pass


RevokeMessageRequestBody: TypeAlias = MessageRevokeRequest


RevokeMessageResponse: TypeAlias = ResponseEnvelope[OkData]


class RotateApiKeyPath(TypedDict, total=False):
    key_id: Required[str]


class RotateApiKeyQuery(TypedDict, total=False):
    pass


RotateApiKeyRequestBody: TypeAlias = APIKeyCreateRequest


RotateApiKeyResponse: TypeAlias = ResponseEnvelope[APIKeyCreateResult]


class SendMessagePath(TypedDict, total=False):
    pass


class SendMessageQuery(TypedDict, total=False):
    pass


SendMessageRequestBody: TypeAlias = SendMessageRequest


SendMessageResponse: TypeAlias = ResponseEnvelope[SendMessageResult]


class SetContactNotePath(TypedDict, total=False):
    account_id: Required[str]


class SetContactNoteQuery(TypedDict, total=False):
    pass


SetContactNoteRequestBody: TypeAlias = ContactNoteRequest


SetContactNoteResponse: TypeAlias = ResponseEnvelope[OkData]


class SetConversationLabelMembersPath(TypedDict, total=False):
    account_id: Required[str]


class SetConversationLabelMembersQuery(TypedDict, total=False):
    pass


SetConversationLabelMembersRequestBody: TypeAlias = ConversationLabelMembersRequest


SetConversationLabelMembersResponse: TypeAlias = ResponseEnvelope[ConversationLabelMembersResult]


class SetGroupJoinApprovalModePath(TypedDict, total=False):
    account_id: Required[str]


class SetGroupJoinApprovalModeQuery(TypedDict, total=False):
    pass


SetGroupJoinApprovalModeRequestBody: TypeAlias = GroupJoinApprovalModeRequest


SetGroupJoinApprovalModeResponse: TypeAlias = ResponseEnvelope[OkData]


class StartAccountAuthPath(TypedDict, total=False):
    account_id: Required[str]


class StartAccountAuthQuery(TypedDict, total=False):
    pass


StartAccountAuthRequestBody: TypeAlias = FreeFormObject


StartAccountAuthResponse: TypeAlias = ResponseEnvelope[FreeFormObject]


class StartAccountQrAuthPath(TypedDict, total=False):
    account_id: Required[str]


class StartAccountQrAuthQuery(TypedDict, total=False):
    pass


StartAccountQrAuthRequestBody: TypeAlias = FreeFormObject


StartAccountQrAuthResponse: TypeAlias = ResponseEnvelope[FreeFormObject]


class StartAccountRuntimePath(TypedDict, total=False):
    account_id: Required[str]


class StartAccountRuntimeQuery(TypedDict, total=False):
    pass


StartAccountRuntimeRequestBody: TypeAlias = FreeFormObject


StartAccountRuntimeResponse: TypeAlias = ResponseEnvelope[RuntimeActionResult]


class StopAccountRuntimePath(TypedDict, total=False):
    account_id: Required[str]


class StopAccountRuntimeQuery(TypedDict, total=False):
    pass


StopAccountRuntimeRequestBody: TypeAlias = FreeFormObject


StopAccountRuntimeResponse: TypeAlias = ResponseEnvelope[RuntimeActionResult]


class SubmitAccountAuthCodePath(TypedDict, total=False):
    account_id: Required[str]


class SubmitAccountAuthCodeQuery(TypedDict, total=False):
    pass


SubmitAccountAuthCodeRequestBody: TypeAlias = FreeFormObject


SubmitAccountAuthCodeResponse: TypeAlias = ResponseEnvelope[FreeFormObject]


class SubmitAccountAuthPasswordPath(TypedDict, total=False):
    account_id: Required[str]


class SubmitAccountAuthPasswordQuery(TypedDict, total=False):
    pass


SubmitAccountAuthPasswordRequestBody: TypeAlias = FreeFormObject


SubmitAccountAuthPasswordResponse: TypeAlias = ResponseEnvelope[FreeFormObject]


class UnblockContactPath(TypedDict, total=False):
    account_id: Required[str]


class UnblockContactQuery(TypedDict, total=False):
    pass


UnblockContactRequestBody: TypeAlias = ContactIdRequest


UnblockContactResponse: TypeAlias = ResponseEnvelope[OkData]


class UnmuteConversationPath(TypedDict, total=False):
    account_id: Required[str]


class UnmuteConversationQuery(TypedDict, total=False):
    pass


UnmuteConversationRequestBody: TypeAlias = ConversationIdRequest


UnmuteConversationResponse: TypeAlias = ResponseEnvelope[OkData]


class UnpinConversationPath(TypedDict, total=False):
    account_id: Required[str]


class UnpinConversationQuery(TypedDict, total=False):
    pass


UnpinConversationRequestBody: TypeAlias = ConversationIdRequest


UnpinConversationResponse: TypeAlias = ResponseEnvelope[OkData]


class UpdateAccountPath(TypedDict, total=False):
    account_id: Required[str]


class UpdateAccountQuery(TypedDict, total=False):
    pass


UpdateAccountRequestBody: TypeAlias = AccountRequest


UpdateAccountResponse: TypeAlias = ResponseEnvelope[Account]


class UpdateApiKeyStatusPath(TypedDict, total=False):
    key_id: Required[str]


class UpdateApiKeyStatusQuery(TypedDict, total=False):
    pass


UpdateApiKeyStatusRequestBody: TypeAlias = APIKeyStatusUpdateRequest


UpdateApiKeyStatusResponse: TypeAlias = ResponseEnvelope[APIKey]


class UpdateGroupInfoPath(TypedDict, total=False):
    account_id: Required[str]


class UpdateGroupInfoQuery(TypedDict, total=False):
    pass


UpdateGroupInfoRequestBody: TypeAlias = GroupInfoUpdateRequest


UpdateGroupInfoResponse: TypeAlias = ResponseEnvelope[OkData]


class UpdateGroupJoinRequestsPath(TypedDict, total=False):
    account_id: Required[str]


class UpdateGroupJoinRequestsQuery(TypedDict, total=False):
    pass


UpdateGroupJoinRequestsRequestBody: TypeAlias = GroupJoinRequestsUpdateRequest


UpdateGroupJoinRequestsResponse: TypeAlias = ResponseEnvelope[OkData]


class UpdateGroupMembersPath(TypedDict, total=False):
    account_id: Required[str]


class UpdateGroupMembersQuery(TypedDict, total=False):
    pass


UpdateGroupMembersRequestBody: TypeAlias = GroupMemberUpdateRequest


UpdateGroupMembersResponse: TypeAlias = ResponseEnvelope[OkData]


class UpdateWebhookEndpointPath(TypedDict, total=False):
    endpoint_id: Required[str]


class UpdateWebhookEndpointQuery(TypedDict, total=False):
    pass


UpdateWebhookEndpointRequestBody: TypeAlias = WebhookEndpointRequest


UpdateWebhookEndpointResponse: TypeAlias = ResponseEnvelope[WebhookEndpoint]


class UpdateWorkspacePath(TypedDict, total=False):
    pass


class UpdateWorkspaceQuery(TypedDict, total=False):
    pass


UpdateWorkspaceRequestBody: TypeAlias = WorkspaceUpdateRequest


UpdateWorkspaceResponse: TypeAlias = ResponseEnvelope[Workspace]


class UpsertConversationLabelPath(TypedDict, total=False):
    account_id: Required[str]


class UpsertConversationLabelQuery(TypedDict, total=False):
    pass


UpsertConversationLabelRequestBody: TypeAlias = ConversationLabelUpsertRequest


UpsertConversationLabelResponse: TypeAlias = ResponseEnvelope[ConversationLabel]


SCHEMA_NAMES: Final = (
    "APIKey",
    "APIKeyCreateRequest",
    "APIKeyCreateResult",
    "APIKeyStatusUpdateRequest",
    "Account",
    "AccountRequest",
    "AccountSession",
    "AuthField",
    "Contact",
    "ContactBlocklistResult",
    "ContactCard",
    "ContactEmail",
    "ContactIdRequest",
    "ContactListResult",
    "ContactNoteRequest",
    "ContactPhone",
    "Conversation",
    "ConversationIdRequest",
    "ConversationLabel",
    "ConversationLabelDeleteRequest",
    "ConversationLabelDeleteResult",
    "ConversationLabelListResult",
    "ConversationLabelMembersRequest",
    "ConversationLabelMembersResult",
    "ConversationLabelUpsertRequest",
    "ConversationListResult",
    "ConversationMember",
    "ConversationMemberListResult",
    "ConversationMuteRequest",
    "ConversationReadRequest",
    "ConversationType",
    "Error",
    "ErrorEnvelope",
    "FreeFormObject",
    "Group",
    "GroupCreateRequest",
    "GroupCreateResult",
    "GroupIdRequest",
    "GroupInfoUpdateRequest",
    "GroupInviteCode",
    "GroupJoinApprovalModeRequest",
    "GroupJoinRequest",
    "GroupJoinRequestsResult",
    "GroupJoinRequestsUpdateRequest",
    "GroupListResult",
    "GroupMemberUpdateRequest",
    "Mention",
    "MessageEditRequest",
    "MessagePayload",
    "MessagePinRequest",
    "MessageReactionRequest",
    "MessageRevokeRequest",
    "MessageTargetRequest",
    "OkData",
    "ProviderName",
    "ProviderProfile",
    "ProviderRegionsResponse",
    "Recipient",
    "RegionAvailability",
    "ReplyTo",
    "ResponseMeta",
    "RuntimeActionResult",
    "RuntimeStatus",
    "SendMessageRequest",
    "SendMessageResult",
    "StandardEventType",
    "WebhookEndpoint",
    "WebhookEndpointRequest",
    "Workspace",
    "WorkspaceUpdateRequest",
)


DEPENDENT_REQUIRED: Final = MappingProxyType(
    {
        "ConversationReadRequest": MappingProxyType(
            {
                "up_to_message_id": ("up_to_message_sender_id",),
                "up_to_message_sender_id": ("up_to_message_id",),
            }
        ),
    }
)


__all__ = [
    "DEPENDENT_REQUIRED",
    "ResponseEnvelope",
    "SCHEMA_NAMES",
    "JsonScalar",
    "JsonValue",
    "APIKey",
    "APIKeyCreateRequest",
    "APIKeyCreateResult",
    "APIKeyStatusUpdateRequest",
    "Account",
    "AccountRequest",
    "AccountSession",
    "AuthField",
    "Contact",
    "ContactBlocklistResult",
    "ContactCard",
    "ContactEmail",
    "ContactIdRequest",
    "ContactListResult",
    "ContactNoteRequest",
    "ContactPhone",
    "Conversation",
    "ConversationIdRequest",
    "ConversationLabel",
    "ConversationLabelDeleteRequest",
    "ConversationLabelDeleteResult",
    "ConversationLabelListResult",
    "ConversationLabelMembersRequest",
    "ConversationLabelMembersResult",
    "ConversationLabelUpsertRequest",
    "ConversationListResult",
    "ConversationMember",
    "ConversationMemberListResult",
    "ConversationMuteRequest",
    "ConversationReadRequest",
    "ConversationType",
    "Error",
    "ErrorEnvelope",
    "FreeFormObject",
    "Group",
    "GroupCreateRequest",
    "GroupCreateResult",
    "GroupIdRequest",
    "GroupInfoUpdateRequest",
    "GroupInviteCode",
    "GroupJoinApprovalModeRequest",
    "GroupJoinRequest",
    "GroupJoinRequestsResult",
    "GroupJoinRequestsUpdateRequest",
    "GroupListResult",
    "GroupMemberUpdateRequest",
    "Mention",
    "MessageEditRequest",
    "MessagePayload",
    "MessagePinRequest",
    "MessageReactionRequest",
    "MessageRevokeRequest",
    "MessageTargetRequest",
    "OkData",
    "ProviderName",
    "ProviderProfile",
    "ProviderRegionsResponse",
    "Recipient",
    "RegionAvailability",
    "ReplyTo",
    "ResponseMeta",
    "RuntimeActionResult",
    "RuntimeStatus",
    "SendMessageRequest",
    "SendMessageResult",
    "StandardEventType",
    "WebhookEndpoint",
    "WebhookEndpointRequest",
    "Workspace",
    "WorkspaceUpdateRequest",
    "BlockContactPath",
    "BlockContactQuery",
    "BlockContactRequestBody",
    "BlockContactResponse",
    "CancelAccountAuthPath",
    "CancelAccountAuthQuery",
    "CancelAccountAuthRequestBody",
    "CancelAccountAuthResponse",
    "CheckAccountQrAuthPath",
    "CheckAccountQrAuthQuery",
    "CheckAccountQrAuthRequestBody",
    "CheckAccountQrAuthResponse",
    "CreateAccountPath",
    "CreateAccountQuery",
    "CreateAccountRequestBody",
    "CreateAccountResponse",
    "CreateApiKeyPath",
    "CreateApiKeyQuery",
    "CreateApiKeyRequestBody",
    "CreateApiKeyResponse",
    "CreateGroupPath",
    "CreateGroupQuery",
    "CreateGroupRequestBody",
    "CreateGroupResponse",
    "CreateWebhookEndpointPath",
    "CreateWebhookEndpointQuery",
    "CreateWebhookEndpointRequestBody",
    "CreateWebhookEndpointResponse",
    "DeactivateWebhookEndpointPath",
    "DeactivateWebhookEndpointQuery",
    "DeactivateWebhookEndpointRequestBody",
    "DeactivateWebhookEndpointResponse",
    "DeleteAccountPath",
    "DeleteAccountQuery",
    "DeleteAccountRequestBody",
    "DeleteAccountResponse",
    "DeleteConversationLabelPath",
    "DeleteConversationLabelQuery",
    "DeleteConversationLabelRequestBody",
    "DeleteConversationLabelResponse",
    "DeleteWebhookEndpointPath",
    "DeleteWebhookEndpointQuery",
    "DeleteWebhookEndpointRequestBody",
    "DeleteWebhookEndpointResponse",
    "EditMessagePath",
    "EditMessageQuery",
    "EditMessageRequestBody",
    "EditMessageResponse",
    "GetAccountPath",
    "GetAccountQuery",
    "GetAccountRequestBody",
    "GetAccountResponse",
    "GetAccountAuthStatePath",
    "GetAccountAuthStateQuery",
    "GetAccountAuthStateRequestBody",
    "GetAccountAuthStateResponse",
    "GetContactPath",
    "GetContactQuery",
    "GetContactRequestBody",
    "GetContactResponse",
    "GetConversationPath",
    "GetConversationQuery",
    "GetConversationRequestBody",
    "GetConversationResponse",
    "GetGroupPath",
    "GetGroupQuery",
    "GetGroupRequestBody",
    "GetGroupResponse",
    "GetGroupInviteCodePath",
    "GetGroupInviteCodeQuery",
    "GetGroupInviteCodeRequestBody",
    "GetGroupInviteCodeResponse",
    "GetWebhookEndpointPath",
    "GetWebhookEndpointQuery",
    "GetWebhookEndpointRequestBody",
    "GetWebhookEndpointResponse",
    "GetWorkspacePath",
    "GetWorkspaceQuery",
    "GetWorkspaceRequestBody",
    "GetWorkspaceResponse",
    "ImportAccountAuthSessionPath",
    "ImportAccountAuthSessionQuery",
    "ImportAccountAuthSessionRequestBody",
    "ImportAccountAuthSessionResponse",
    "LeaveGroupPath",
    "LeaveGroupQuery",
    "LeaveGroupRequestBody",
    "LeaveGroupResponse",
    "ListAccountsPath",
    "ListAccountsQuery",
    "ListAccountsRequestBody",
    "ListAccountsResponse",
    "ListApiKeysPath",
    "ListApiKeysQuery",
    "ListApiKeysRequestBody",
    "ListApiKeysResponse",
    "ListContactBlocklistPath",
    "ListContactBlocklistQuery",
    "ListContactBlocklistRequestBody",
    "ListContactBlocklistResponse",
    "ListContactsPath",
    "ListContactsQuery",
    "ListContactsRequestBody",
    "ListContactsResponse",
    "ListConversationLabelsPath",
    "ListConversationLabelsQuery",
    "ListConversationLabelsRequestBody",
    "ListConversationLabelsResponse",
    "ListConversationMembersPath",
    "ListConversationMembersQuery",
    "ListConversationMembersRequestBody",
    "ListConversationMembersResponse",
    "ListConversationsPath",
    "ListConversationsQuery",
    "ListConversationsRequestBody",
    "ListConversationsResponse",
    "ListGroupJoinRequestsPath",
    "ListGroupJoinRequestsQuery",
    "ListGroupJoinRequestsRequestBody",
    "ListGroupJoinRequestsResponse",
    "ListGroupsPath",
    "ListGroupsQuery",
    "ListGroupsRequestBody",
    "ListGroupsResponse",
    "ListProviderRegionsPath",
    "ListProviderRegionsQuery",
    "ListProviderRegionsRequestBody",
    "ListProviderRegionsResponse",
    "ListWebhookEndpointsPath",
    "ListWebhookEndpointsQuery",
    "ListWebhookEndpointsRequestBody",
    "ListWebhookEndpointsResponse",
    "MarkConversationReadPath",
    "MarkConversationReadQuery",
    "MarkConversationReadRequestBody",
    "MarkConversationReadResponse",
    "MarkConversationUnreadPath",
    "MarkConversationUnreadQuery",
    "MarkConversationUnreadRequestBody",
    "MarkConversationUnreadResponse",
    "MuteConversationPath",
    "MuteConversationQuery",
    "MuteConversationRequestBody",
    "MuteConversationResponse",
    "PinConversationPath",
    "PinConversationQuery",
    "PinConversationRequestBody",
    "PinConversationResponse",
    "PinMessagePath",
    "PinMessageQuery",
    "PinMessageRequestBody",
    "PinMessageResponse",
    "ReactMessagePath",
    "ReactMessageQuery",
    "ReactMessageRequestBody",
    "ReactMessageResponse",
    "ReconnectAccountRuntimePath",
    "ReconnectAccountRuntimeQuery",
    "ReconnectAccountRuntimeRequestBody",
    "ReconnectAccountRuntimeResponse",
    "RefreshAccountRuntimePath",
    "RefreshAccountRuntimeQuery",
    "RefreshAccountRuntimeRequestBody",
    "RefreshAccountRuntimeResponse",
    "RevokeMessagePath",
    "RevokeMessageQuery",
    "RevokeMessageRequestBody",
    "RevokeMessageResponse",
    "RotateApiKeyPath",
    "RotateApiKeyQuery",
    "RotateApiKeyRequestBody",
    "RotateApiKeyResponse",
    "SendMessagePath",
    "SendMessageQuery",
    "SendMessageRequestBody",
    "SendMessageResponse",
    "SetContactNotePath",
    "SetContactNoteQuery",
    "SetContactNoteRequestBody",
    "SetContactNoteResponse",
    "SetConversationLabelMembersPath",
    "SetConversationLabelMembersQuery",
    "SetConversationLabelMembersRequestBody",
    "SetConversationLabelMembersResponse",
    "SetGroupJoinApprovalModePath",
    "SetGroupJoinApprovalModeQuery",
    "SetGroupJoinApprovalModeRequestBody",
    "SetGroupJoinApprovalModeResponse",
    "StartAccountAuthPath",
    "StartAccountAuthQuery",
    "StartAccountAuthRequestBody",
    "StartAccountAuthResponse",
    "StartAccountQrAuthPath",
    "StartAccountQrAuthQuery",
    "StartAccountQrAuthRequestBody",
    "StartAccountQrAuthResponse",
    "StartAccountRuntimePath",
    "StartAccountRuntimeQuery",
    "StartAccountRuntimeRequestBody",
    "StartAccountRuntimeResponse",
    "StopAccountRuntimePath",
    "StopAccountRuntimeQuery",
    "StopAccountRuntimeRequestBody",
    "StopAccountRuntimeResponse",
    "SubmitAccountAuthCodePath",
    "SubmitAccountAuthCodeQuery",
    "SubmitAccountAuthCodeRequestBody",
    "SubmitAccountAuthCodeResponse",
    "SubmitAccountAuthPasswordPath",
    "SubmitAccountAuthPasswordQuery",
    "SubmitAccountAuthPasswordRequestBody",
    "SubmitAccountAuthPasswordResponse",
    "UnblockContactPath",
    "UnblockContactQuery",
    "UnblockContactRequestBody",
    "UnblockContactResponse",
    "UnmuteConversationPath",
    "UnmuteConversationQuery",
    "UnmuteConversationRequestBody",
    "UnmuteConversationResponse",
    "UnpinConversationPath",
    "UnpinConversationQuery",
    "UnpinConversationRequestBody",
    "UnpinConversationResponse",
    "UpdateAccountPath",
    "UpdateAccountQuery",
    "UpdateAccountRequestBody",
    "UpdateAccountResponse",
    "UpdateApiKeyStatusPath",
    "UpdateApiKeyStatusQuery",
    "UpdateApiKeyStatusRequestBody",
    "UpdateApiKeyStatusResponse",
    "UpdateGroupInfoPath",
    "UpdateGroupInfoQuery",
    "UpdateGroupInfoRequestBody",
    "UpdateGroupInfoResponse",
    "UpdateGroupJoinRequestsPath",
    "UpdateGroupJoinRequestsQuery",
    "UpdateGroupJoinRequestsRequestBody",
    "UpdateGroupJoinRequestsResponse",
    "UpdateGroupMembersPath",
    "UpdateGroupMembersQuery",
    "UpdateGroupMembersRequestBody",
    "UpdateGroupMembersResponse",
    "UpdateWebhookEndpointPath",
    "UpdateWebhookEndpointQuery",
    "UpdateWebhookEndpointRequestBody",
    "UpdateWebhookEndpointResponse",
    "UpdateWorkspacePath",
    "UpdateWorkspaceQuery",
    "UpdateWorkspaceRequestBody",
    "UpdateWorkspaceResponse",
    "UpsertConversationLabelPath",
    "UpsertConversationLabelQuery",
    "UpsertConversationLabelRequestBody",
    "UpsertConversationLabelResponse",
]
