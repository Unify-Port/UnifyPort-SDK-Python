"""Generated from contracts/device.openapi.yaml; edit the contract, policy, or generator instead."""

# 此文件由生成链维护，手改会在 generate --check 中被拒绝。

from types import MappingProxyType
from typing import (
    Final,
    Generic,
    Literal,
    Never,
    NotRequired,
    Required,
    TypeAlias,
    TypeVar,
    Union,
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
    billing: NotRequired["AccountBilling"]
    capabilities: NotRequired[list[str]]
    id: Required[str]
    metadata: NotRequired["FreeFormObject"]
    name: Required[str]
    provider: Required["ProviderName"]
    provider_account_ref: NotRequired[str]
    provider_profile: NotRequired["ProviderProfile"]
    proxy: NotRequired["FreeFormObject"]
    region: Required[str]
    runtime_status: Required["RuntimeStatus"]
    status: Required[str]


class AccountBilling(TypedDict, total=False):
    amount_minor: Required[int]
    currency: Required[Literal["USD"]]
    operation_id: Required[str]
    period_end_at: Required[str]
    period_start_at: Required[str]
    state: Required[Literal["ACTIVE", "DELETING", "DELETED", "COMPENSATED", "REVIEW"]]


class AccountCreateRequest(TypedDict, total=False):
    auth_mode: Required[Literal["qrcode", "code", "session"]]
    capabilities: NotRequired[list[str]]
    metadata: NotRequired["FreeFormObject"]
    name: NotRequired[str]
    provider: Required["ProviderInputName"]
    provider_account_ref: NotRequired[str]
    provider_data: NotRequired["FreeFormObject"]
    proxy: NotRequired["FreeFormObject"]
    region: Required[str]
    runtime_status: NotRequired["RuntimeStatus"]
    status: NotRequired[str]


class AccountListResult(TypedDict, total=False):
    has_more: Required[bool]
    items: Required[list["Account"]]
    next_cursor: NotRequired[str]


class AccountOperation(TypedDict, total=False):
    account_id: NotRequired[str]
    kind: Required[Literal["QUOTE", "CREATE", "DELETE", "COMPENSATE"]]
    last_error_code: NotRequired[str]
    operation_id: Required[str]
    state: Required[
        Literal[
            "QUOTED",
            "CONSUMED",
            "EXPIRED",
            "PENDING",
            "PROCESSING",
            "SUCCEEDED",
            "FAILED",
            "REVIEW",
        ]
    ]


class AccountProfileUpdatedWebhookEvent(TypedDict, total=False):
    account_id: Required[str]
    data: Required["_AccountProfileUpdatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["account.profile.updated"]]


class AccountSession(TypedDict, total=False):
    account_id: Required[str]
    auth_fields: NotRequired[list["AuthField"]]
    auth_payload: NotRequired["_AccountSessionAuthPayload"]
    expires_at: NotRequired[str]
    last_error: NotRequired[str]
    status: Required[str]


class AccountStartedWebhookEvent(TypedDict, total=False):
    account_id: Required[str]
    data: Required["_AccountStartedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["account.started"]]


class AccountUpdateRequest(TypedDict, total=False):
    auth_mode: NotRequired[Literal["qrcode", "code", "session"]]
    capabilities: NotRequired[list[str]]
    metadata: NotRequired["FreeFormObject"]
    name: NotRequired[str]
    provider: NotRequired["ProviderInputName"]
    provider_account_ref: NotRequired[str]
    provider_data: NotRequired["FreeFormObject"]
    proxy: NotRequired["FreeFormObject"]
    region: NotRequired[str]
    runtime_status: NotRequired["RuntimeStatus"]
    status: NotRequired[str]


class AccountWebhookError(TypedDict, total=False):
    code: Required[Literal["account_auth_failed", "account_logged_out", "account_restricted"]]
    message: Required[str]
    numeric_code: Required[Literal["20100", "20101", "20102"]]


class ActiveCallData(TypedDict, total=False):
    call_id: Required[str]
    direction: Required[Literal["inbound", "outbound"]]
    media_type: Required[Literal["voice", "video"]]
    state: Required[Literal["preparing", "dialing", "ringing", "connecting", "active"]]


class AuthField(TypedDict, total=False):
    label: NotRequired[str]
    placeholder: NotRequired[str]
    required: Required[bool]
    type: Required[str]


class CallAnsweredWebhookEvent(TypedDict, total=False):
    account_id: Required[str]
    data: Required["_CallAnsweredWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["call.answered"]]


class CallEndedWebhookEvent(TypedDict, total=False):
    account_id: Required[str]
    data: Required["_CallEndedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["call.ended"]]


class CallEventCall(TypedDict, total=False):
    direction: Required[Literal["inbound", "outbound"]]
    id: Required[str]
    media_type: Required[Literal["voice", "video"]]
    state: Required[Literal["ringing", "active", "ended"]]


class CallEventSender(TypedDict, total=False):
    display_name: NotRequired[str]
    id: Required[str]


class CallIncomingWebhookEvent(TypedDict, total=False):
    account_id: Required[str]
    data: Required["_CallIncomingWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["call.incoming"]]


class CallMessage(TypedDict, total=False):
    call: Required["CallMessageCall"]
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: Required[str]
    sent_at: NotRequired[str]
    type: Required[Literal["call"]]


class CallMessageCallVariant1(TypedDict, total=False):
    accepted_at: NotRequired[str]
    end_reason: NotRequired[Never]
    ended_by: NotRequired[Literal["remote"]]
    id: Required[str]
    media_type: NotRequired[Literal["audio", "video"]]
    status: Required[Literal["offered", "accepted", "ended"]]


class CallMessageCallVariant2(TypedDict, total=False):
    accepted_at: NotRequired[str]
    end_reason: NotRequired[Literal["timeout", "rejected_elsewhere"]]
    ended_by: NotRequired[Never]
    id: Required[str]
    media_type: NotRequired[Literal["audio", "video"]]
    status: Required[Literal["offered", "accepted", "ended"]]


class CallMessageReceivedWebhookEvent(TypedDict, total=False):
    account_id: Required[str]
    data: Required["_CallMessageReceivedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required[Literal["whatsapp"]]
    type: Required[Literal["message.received"]]


class CallMessageUpdatedWebhookEvent(TypedDict, total=False):
    account_id: Required[str]
    data: Required["_CallMessageUpdatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required[Literal["whatsapp"]]
    type: Required[Literal["message.updated"]]


class CallMessageWebhookEvent(TypedDict, total=False):
    account_id: Required[str]
    data: Required["_CallMessageWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required[Literal["whatsapp"]]
    type: Required[Literal["message.received", "message.updated"]]


class Contact(TypedDict, total=False):
    avatar_url: Required[str]
    conversation_id: Required[str]
    display_name: Required[str]
    extra: NotRequired["ContactExtra"]
    id: Required[str]
    is_blocked: NotRequired[bool]
    provider_user_id: Required[str]


class ContactAddressBook(TypedDict, total=False):
    first_name: NotRequired[str]
    full_name: NotRequired[str]


class ContactBlocklistResult(TypedDict, total=False):
    blocklist: Required[list[str]]
    dhash: NotRequired[str]


class ContactCard(TypedDict, total=False):
    emails: NotRequired[list["ContactEmail"]]
    name: Required[str]
    organization: NotRequired[str]
    phones: NotRequired[list["ContactPhone"]]
    title: NotRequired[str]


class ContactCreateRequestVariant1(TypedDict, total=False):
    phone_number: Required[str]
    username: NotRequired[str]
    whatsapp_options: NotRequired["WhatsAppContactCreateOptions"]


class ContactCreateRequestVariant2(TypedDict, total=False):
    phone_number: NotRequired[str]
    username: Required[str]
    whatsapp_options: NotRequired["WhatsAppContactCreateOptions"]


class ContactEmail(TypedDict, total=False):
    address: Required[str]
    type: NotRequired[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class ContactExtra(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    business_name: NotRequired[str]
    first_name: NotRequired[str]
    full_name: NotRequired[str]
    phone: NotRequired[str]
    push_name: NotRequired[str]
    redacted_phone: NotRequired[str]
    username: NotRequired[str]


class ContactIdRequest(TypedDict, total=False):
    contact_id: Required[str]


class ContactListResult(TypedDict, total=False):
    has_more: Required[bool]
    items: Required[list["Contact"]]
    next_cursor: NotRequired[str]


class ContactMembership(TypedDict, total=False):
    contact_id: Required[str]
    is_in_contacts: Required[bool]


class ContactMessagePayload(TypedDict, total=False):
    contacts: Required[list["ContactCard"]]
    type: Required[Literal["contact"]]


class ContactNoteRequest(TypedDict, total=False):
    contact_id: Required[str]
    note: Required[str]


class ContactPhone(TypedDict, total=False):
    number: Required[str]
    type: NotRequired[str]


class ContactUpdateChange(TypedDict, total=False):
    changed_at: NotRequired[str]
    changed_fields: Required[list[Literal["address_book.full_name", "address_book.first_name"]]]
    kind: Required[Literal["contact_updated"]]
    source: Required[Literal["address_book", "full_sync"]]


class ContactUpdateReference(TypedDict, total=False):
    address_book: Required["ContactAddressBook"]
    conversation_id: NotRequired[str]
    id: Required[str]


class ContactUpdatedData(TypedDict, total=False):
    account: NotRequired["ConversationStateAccount"]
    contact: Required["ContactUpdateReference"]
    event: Required["ContactUpdateChange"]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class ContactUpdatedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["ContactUpdatedData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["contact.updated"]]


class Conversation(TypedDict, total=False):
    avatar_url: Required[str]
    conversation_id: Required[str]
    created_at: NotRequired[str]
    description: NotRequired[str]
    extra: NotRequired["_ConversationExtra"]
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


class ConversationDisappearingMessagesChange(TypedDict, total=False):
    change_type: Required[Literal["disappearing_messages"]]
    changed_at: NotRequired[str]
    kind: Required[Literal["conversation_updated"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class ConversationDisappearingMessagesStateVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    duration_seconds: Required[Literal[0]]
    enabled: Required[Literal[False]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class ConversationDisappearingMessagesStateVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    duration_seconds: Required[int]
    enabled: Required[Literal[True]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class ConversationDisappearingMessagesUpdatedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_ConversationDisappearingMessagesUpdatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["conversation.updated"]]


class ConversationHistoryAccepted(TypedDict, total=False):
    conversation_id: Required[str]
    limit: Required[int]
    status: Required[Literal["accepted"]]


class ConversationHistoryBefore(TypedDict, total=False):
    direction: Required[Literal["inbound", "outbound"]]
    message_id: Required[str]
    sent_at: Required[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class ConversationHistoryMessage(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: NotRequired[str]
    referral: NotRequired["MessageReferral"]
    sent_at: NotRequired[str]
    text: NotRequired[str]
    type: NotRequired[str]


class ConversationHistoryRequest(TypedDict, total=False):
    before: Required["ConversationHistoryBefore"]
    conversation_id: Required[str]
    limit: NotRequired[int]


class ConversationHistorySource(TypedDict, total=False):
    source: Required[Literal["on_demand"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class ConversationHistoryWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_ConversationHistoryWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["conversation.history"]]


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
    role: NotRequired[Literal["member", "admin", "superadmin"]]
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


class ConversationStateAccount(TypedDict, total=False):
    provider_account_ref: Required[str]


class ConversationStateActor(TypedDict, total=False):
    id: Required[str]
    name: NotRequired[str]
    type: NotRequired[Literal["user"]]


class ConversationStateReference(TypedDict, total=False):
    id: Required[str]
    type: Required["ConversationType"]


ConversationType: TypeAlias = Literal[
    "user",
    "group",
    "channel",
]


class CreateCallData(TypedDict, total=False):
    call_id: Required[str]
    direction: Required[Literal["outbound"]]
    expires_at: Required[str]
    join_url: Required[str]
    media_type: Required[Literal["voice", "video"]]
    state: Required[Literal["preparing"]]


class CreateCallRequest(TypedDict, total=False):
    account_id: Required[str]
    media_type: Required[Literal["voice", "video"]]
    to: Required["_CreateCallRequestTo"]


class EndedCallData(TypedDict, total=False):
    call_id: Required[str]
    direction: Required[Literal["inbound", "outbound"]]
    media_type: Required[Literal["voice", "video"]]
    state: Required[Literal["ended", "failed"]]


class Error(TypedDict, total=False):
    code: Required[str]
    message: Required[str]
    numeric_code: Required[str]


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
    extra: NotRequired["_GroupExtra"]
    id: Required[str]
    joined_at: NotRequired[str]
    member_count: NotRequired[int]
    name: Required[str]
    permissions: NotRequired["GroupPermissions"]


class GroupAnnouncementChange(TypedDict, total=False):
    admins_only: Required[bool]
    kind: Required[Literal["announcement_changed"]]


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


class GroupInviteLinkChange(TypedDict, total=False):
    kind: Required[Literal["invite_link_changed"]]


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


class GroupPermissions(TypedDict, total=False):
    admins_only: NotRequired[bool]


class GroupSettingsEvent(TypedDict, total=False):
    changed_at: NotRequired[str]
    kind: Required[Literal["group_updated"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class GroupSettingsUpdatedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_GroupSettingsUpdatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["group.updated"]]


class GroupUpdatedChangeVariant1(TypedDict, total=False):
    admins_only: Required[bool]
    kind: Required[Literal["announcement_changed"]]


class GroupUpdatedChangeVariant2(TypedDict, total=False):
    kind: Required[Literal["invite_link_changed"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class GroupUpdatedChangeVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    kind: Required[str]


class LinkPreviewMessagePayload(TypedDict, total=False):
    link_preview: Required["SendMessageLinkPreview"]
    text: Required[str]
    type: Required[Literal["link_preview"]]


class MediaMessagePayloadVariant1(TypedDict, total=False):
    caption: NotRequired[str]
    file_key: NotRequired[str]
    file_url: NotRequired[str]
    type: Required[Literal["image", "video", "audio", "document", "file"]]
    url: Required[str]


class MediaMessagePayloadVariant2(TypedDict, total=False):
    caption: NotRequired[str]
    file_key: NotRequired[str]
    file_url: Required[str]
    type: Required[Literal["image", "video", "audio", "document", "file"]]
    url: NotRequired[str]


class MediaMessagePayloadVariant3(TypedDict, total=False):
    caption: NotRequired[str]
    file_key: Required[str]
    file_url: NotRequired[str]
    type: Required[Literal["image", "video", "audio", "document", "file"]]
    url: NotRequired[str]


class MentionVariant1(TypedDict, total=False):
    id: Required[str]
    type: NotRequired[Literal["member"]]


class MentionVariant2(TypedDict, total=False):
    id: NotRequired[Never]
    type: Required[Literal["member", "all"]]


MessageCommerceHTTPURL: TypeAlias = str


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageCommerceHistoryWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageCommerceHistoryWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["conversation.history"]]


class MessageCommerceMoney(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageCommerceReceivedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageCommerceReceivedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.received"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageCommerceUpdatedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageCommerceUpdatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.updated"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageCommerceVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: NotRequired[Never]
    product: Required["_MessageCommerceVariant1Product"]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageCommerceVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: Required["_MessageCommerceVariant2Order"]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageCommerceWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageCommerceWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.received", "message.updated", "conversation.history"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageContactCardsHistoryWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageContactCardsHistoryWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["conversation.history"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageContactCardsReceivedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageContactCardsReceivedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.received"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageContactCardsUpdatedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageContactCardsUpdatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.updated"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageContactCardsVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    contacts: Required[list["ReceivedContactCard"]]
    id: NotRequired[str]
    text: Required[str]
    type: NotRequired[Literal["contact"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageContactCardsVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    contacts: Required[list["ReceivedContactCard"]]
    id: Required[str]
    reply_token: NotRequired[Never]
    text: NotRequired[Never]
    type: Required[Literal["contact"]]


class MessageEditRequest(TypedDict, total=False):
    account_id: Required[str]
    content: Required[str]
    conversation_id: Required[str]
    message_id: Required[str]


class MessageInteractiveAttachment(TypedDict, total=False):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired["MessageInteractiveAttachmentMetadata"]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired["MessageCommerceHTTPURL"]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired["MessageCommerceHTTPURL"]


class MessageInteractiveAttachmentMetadata(TypedDict, total=False):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class MessageInteractiveButtonVariant1(TypedDict, total=False):
    id: Required[str]
    index: NotRequired[int]
    phone_number: NotRequired[Never]
    title: NotRequired[str]
    type: Required[Literal["reply", "url", "phone"]]
    url: NotRequired[Never]


class MessageInteractiveButtonVariant2(TypedDict, total=False):
    id: NotRequired[str]
    index: NotRequired[int]
    phone_number: NotRequired[Never]
    title: Required[str]
    type: Required[Literal["reply", "url", "phone"]]
    url: NotRequired[Never]


class MessageInteractiveButtonVariant3(TypedDict, total=False):
    id: NotRequired[Never]
    index: NotRequired[int]
    phone_number: NotRequired[Never]
    title: Required[str]
    type: Required[Literal["reply", "url", "phone"]]
    url: NotRequired["MessageCommerceHTTPURL"]


class MessageInteractiveButtonVariant4(TypedDict, total=False):
    id: NotRequired[Never]
    index: NotRequired[int]
    phone_number: NotRequired[Never]
    title: NotRequired[str]
    type: Required[Literal["reply", "url", "phone"]]
    url: Required["MessageCommerceHTTPURL"]


class MessageInteractiveButtonVariant5(TypedDict, total=False):
    id: NotRequired[Never]
    index: NotRequired[int]
    phone_number: NotRequired[str]
    title: Required[str]
    type: Required[Literal["reply", "url", "phone"]]
    url: NotRequired[Never]


class MessageInteractiveButtonVariant6(TypedDict, total=False):
    id: NotRequired[Never]
    index: NotRequired[int]
    phone_number: Required[str]
    title: NotRequired[str]
    type: Required[Literal["reply", "url", "phone"]]
    url: NotRequired[Never]


class MessageInteractiveHeaderVariant1(TypedDict, total=False):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class MessageInteractiveHeaderVariant2(TypedDict, total=False):
    attachment: Required["_MessageInteractiveHeaderVariant2Attachment"]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class MessageInteractiveHeaderVariant3(TypedDict, total=False):
    attachment: Required["_MessageInteractiveHeaderVariant3Attachment"]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class MessageInteractiveHeaderVariant4(TypedDict, total=False):
    attachment: Required["_MessageInteractiveHeaderVariant4Attachment"]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageInteractiveHistoryWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageInteractiveHistoryWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["conversation.history"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageInteractiveMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required["_MessageInteractiveMessageVariant1Interactive"]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageInteractiveMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required["_MessageInteractiveMessageVariant2InteractiveResponse"]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageInteractiveReceivedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageInteractiveReceivedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.received"]]


class MessageInteractiveResponseVariant1(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class MessageInteractiveResponseVariant2(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class MessageInteractiveResponseVariant3(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageInteractiveUpdatedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageInteractiveUpdatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.updated"]]


class MessageInteractiveVariant1(TypedDict, total=False):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required["MessageInteractiveHeader"]
    kind: Required[Literal["buttons", "template"]]


class MessageInteractiveVariant2(TypedDict, total=False):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired["MessageInteractiveHeader"]
    kind: Required[Literal["buttons", "template"]]


class MessageInteractiveVariant3(TypedDict, total=False):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired["MessageInteractiveHeader"]
    kind: Required[Literal["buttons", "template"]]


class MessageInteractiveVariant4(TypedDict, total=False):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired["MessageInteractiveHeader"]
    kind: Required[Literal["buttons", "template"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageInteractiveWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageInteractiveWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.received", "message.updated", "conversation.history"]]


class MessageLinkPreview(TypedDict, total=False):
    description: NotRequired["_MessageLinkPreviewDescription"]
    image_url: NotRequired["_MessageLinkPreviewImageUrl"]
    title: NotRequired["_MessageLinkPreviewTitle"]
    url: Required["MessageLinkPreviewHTTPURL"]


MessageLinkPreviewHTTPURL: TypeAlias = str


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageLinkPreviewHistoryWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageLinkPreviewHistoryWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["conversation.history"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageLinkPreviewMessage(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required["MessageLinkPreview"]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    text: NotRequired[str]
    type: Required[Literal["link_preview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageLinkPreviewReceivedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageLinkPreviewReceivedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.received"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageLinkPreviewTextUpdate(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    text: NotRequired[str]
    type: Required[Literal["text"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageLinkPreviewUpdatedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageLinkPreviewUpdatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.updated"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageLinkPreviewWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageLinkPreviewWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.received", "message.updated", "conversation.history"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageLiveLocation(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    duration_seconds: NotRequired[Never]
    ended_at: NotRequired[Never]
    id: Required[str]
    latitude: NotRequired[Never]
    location: NotRequired[Never]
    longitude: NotRequired[Never]
    reply_token: NotRequired[Never]
    text: NotRequired[Never]
    type: Required[Literal["live_location"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageLiveLocationHistoryWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageLiveLocationHistoryWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["conversation.history"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageLiveLocationReceivedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageLiveLocationReceivedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.received"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageLiveLocationUpdatedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageLiveLocationUpdatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.updated"]]


class MessageOrder(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired["MessageCommerceHTTPURL"]
    title: NotRequired[str]
    total: NotRequired["MessageCommerceMoney"]


class MessagePayloadVariant1(TypedDict, total=False):
    caption: NotRequired[str]
    text: Required[str]
    type: Required[Literal["text"]]


class MessagePayloadVariant10(TypedDict, total=False):
    file_key: Required[str]
    file_url: NotRequired[str]
    type: Required[Literal["sticker"]]
    url: NotRequired[str]


class MessagePayloadVariant2(TypedDict, total=False):
    caption: NotRequired[str]
    file_key: NotRequired[str]
    file_url: NotRequired[str]
    type: Required[Literal["image", "video", "audio", "document", "file"]]
    url: Required[str]


class MessagePayloadVariant3(TypedDict, total=False):
    caption: NotRequired[str]
    file_key: NotRequired[str]
    file_url: Required[str]
    type: Required[Literal["image", "video", "audio", "document", "file"]]
    url: NotRequired[str]


class MessagePayloadVariant4(TypedDict, total=False):
    caption: NotRequired[str]
    file_key: Required[str]
    file_url: NotRequired[str]
    type: Required[Literal["image", "video", "audio", "document", "file"]]
    url: NotRequired[str]


class MessagePayloadVariant5(TypedDict, total=False):
    contacts: Required[list["ContactCard"]]
    type: Required[Literal["contact"]]


class MessagePayloadVariant6(TypedDict, total=False):
    link_preview: Required["SendMessageLinkPreview"]
    text: Required[str]
    type: Required[Literal["link_preview"]]


class MessagePayloadVariant7(TypedDict, total=False):
    poll: Required["SendMessagePoll"]
    type: Required[Literal["poll"]]


class MessagePayloadVariant8(TypedDict, total=False):
    file_key: NotRequired[str]
    file_url: NotRequired[str]
    type: Required[Literal["sticker"]]
    url: Required[str]


class MessagePayloadVariant9(TypedDict, total=False):
    file_key: NotRequired[str]
    file_url: Required[str]
    type: Required[Literal["sticker"]]
    url: NotRequired[str]


class MessagePinChange(TypedDict, total=False):
    change_type: Required[Literal["message_pin"]]
    changed_at: NotRequired[str]
    kind: Required[Literal["message_updated"]]


class MessagePinMessage(TypedDict, total=False):
    id: Required[str]
    pin: Required["MessagePinState"]


class MessagePinParticipant(TypedDict, total=False):
    id: Required[str]
    name: NotRequired[str]
    type: NotRequired[Literal["user"]]


class MessagePinRequest(TypedDict, total=False):
    account_id: Required[str]
    conversation_id: Required[str]
    duration_seconds: NotRequired[int]
    message_id: Required[str]
    pinned: Required[bool]
    sender_id: NotRequired[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessagePinStateVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    duration_seconds: NotRequired[Never]
    expires_at: NotRequired[Never]
    pinned: Required[Literal[False]]


class MessagePinStateVariant2(TypedDict, total=False):
    duration_seconds: NotRequired[int]
    expires_at: NotRequired[str]
    pinned: Required[Literal[True]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessagePinUpdatedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessagePinUpdatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.updated"]]


class MessagePoll(TypedDict, total=False):
    max_selections: Required[int]
    options: Required[list["MessagePollOption"]]
    question: Required[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessagePollHistoryWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessagePollHistoryWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["conversation.history"]]


class MessagePollMessage(TypedDict, total=False):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: Required[str]
    mentions: NotRequired[list["Mention"]]
    poll: Required["MessagePoll"]
    referral: NotRequired["MessageReferral"]
    reply_to_message_id: NotRequired[str]
    sender: NotRequired["ConversationStateActor"]
    sent_at: NotRequired[str]
    type: Required[Literal["poll"]]


class MessagePollOption(TypedDict, total=False):
    id: Required[str]
    title: Required[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessagePollReceivedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessagePollReceivedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.received"]]


class MessagePollVoteChange(TypedDict, total=False):
    change_type: Required[Literal["poll_vote"]]
    kind: Required[Literal["message_updated"]]


class MessagePollVoteMessage(TypedDict, total=False):
    id: Required[str]
    poll_vote: Required["MessagePollVote"]
    type: Required[Literal["poll"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessagePollVoteUpdatedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessagePollVoteUpdatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.updated"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessagePollVoteVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    reason: NotRequired[Never]
    selected_option_ids: Required[list[str]]
    status: Required[Literal["decoded"]]
    voted_at: NotRequired[str]
    voter_id: Required[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessagePollVoteVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    reason: NotRequired[Literal["decryption_failed", "missing_poll_context", "unknown"]]
    selected_option_ids: NotRequired[Never]
    status: Required[Literal["unavailable"]]
    voted_at: NotRequired[str]
    voter_id: Required[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessagePollWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessagePollWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.received", "message.updated", "conversation.history"]]


class MessageProduct(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired["MessageCommerceHTTPURL"]
    price: NotRequired["MessageCommerceMoney"]
    title: NotRequired[str]
    url: NotRequired["MessageCommerceHTTPURL"]


class MessageReactionRequest(TypedDict, total=False):
    account_id: Required[str]
    conversation_id: Required[str]
    emoji: NotRequired[str]
    message_id: Required[str]
    sender_id: NotRequired[str]


class MessageReferral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired["MessageReferralProviderExtensions"]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageReferralHistoryWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageReferralHistoryWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["conversation.history"]]


class MessageReferralProviderExtensions(TypedDict, total=False):
    whatsapp: Required["WhatsAppMessageReferralExtension"]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageReferralReceivedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageReferralReceivedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.received"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageReferralUpdatedWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageReferralUpdatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.updated"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageReferralWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_MessageReferralWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required["ProviderName"]
    type: Required[Literal["message.received", "message.updated", "conversation.history"]]


class MessageRevokeRequest(TypedDict, total=False):
    account_id: Required[str]
    conversation_id: Required[str]
    message_id: Required[str]
    sender_id: NotRequired[str]


class MessageTargetRequest(TypedDict, total=False):
    account_id: Required[str]
    conversation_id: Required[str]
    message_id: Required[str]
    sender_id: NotRequired[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalCommerceVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: NotRequired[Never]
    product: Required["_MessageWithOptionalCommerceVariant1Product"]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalCommerceVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: Required["_MessageWithOptionalCommerceVariant2Order"]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalCommerceVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: NotRequired[JsonValue]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalContactCards(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    contacts: NotRequired[list["ReceivedContactCard"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalInteractiveVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required["_MessageWithOptionalInteractiveVariant1Interactive"]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalInteractiveVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required["_MessageWithOptionalInteractiveVariant2InteractiveResponse"]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalInteractiveVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: Required["_MessageWithOptionalInteractiveVariant3Product"]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalInteractiveVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    order: Required["_MessageWithOptionalInteractiveVariant4Order"]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalInteractiveVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: NotRequired[JsonValue]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalLinkPreviewVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required["MessageLinkPreview"]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    text: NotRequired[str]
    type: Required[Literal["link_preview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalLinkPreviewVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required["_MessageWithOptionalLinkPreviewVariant2Interactive"]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalLinkPreviewVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required["_MessageWithOptionalLinkPreviewVariant3InteractiveResponse"]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalLinkPreviewVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: Required["_MessageWithOptionalLinkPreviewVariant4Product"]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalLinkPreviewVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: Required["_MessageWithOptionalLinkPreviewVariant5Order"]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalLinkPreviewVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: NotRequired[JsonValue]


MessageWithOptionalLiveLocation: TypeAlias = dict[str, JsonValue]


class MessageWithOptionalPollVariant1(TypedDict, total=False):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: Required[str]
    mentions: NotRequired[list["Mention"]]
    poll: Required["MessagePoll"]
    referral: NotRequired["MessageReferral"]
    reply_to_message_id: NotRequired[str]
    sender: NotRequired["ConversationStateActor"]
    sent_at: NotRequired[str]
    type: Required[Literal["poll"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalPollVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required["MessageLinkPreview"]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    text: NotRequired[str]
    type: Required[Literal["link_preview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalPollVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required["_MessageWithOptionalPollVariant3Interactive"]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalPollVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required["_MessageWithOptionalPollVariant4InteractiveResponse"]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalPollVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: Required["_MessageWithOptionalPollVariant5Product"]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalPollVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: Required["_MessageWithOptionalPollVariant6Order"]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalPollVariant7(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    type: NotRequired[JsonValue]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class MessageWithOptionalReferral(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    referral: NotRequired["MessageReferral"]


class OkData(TypedDict, total=False):
    ok: Required[Literal[True]]


class PasskeyResponseRequest(TypedDict, total=False):
    webauthn_response: Required[str]


class PollMessagePayload(TypedDict, total=False):
    poll: Required["SendMessagePoll"]
    type: Required[Literal["poll"]]


class Post(TypedDict, total=False):
    author: NotRequired["PostAuthor"]
    created_at: NotRequired[str]
    id: Required["PostResourceID"]
    text: NotRequired[str]


class PostAuthor(TypedDict, total=False):
    avatar_url: NotRequired[str]
    display_name: NotRequired[str]
    id: Required["PostResourceID"]


class PostComment(TypedDict, total=False):
    author: NotRequired["PostAuthor"]
    created_at: NotRequired[str]
    id: Required["PostResourceID"]
    parent_comment_id: NotRequired["PostResourceID"]
    post_id: Required["PostResourceID"]
    text: NotRequired[str]


class PostCommentCreatedWebhookEvent(TypedDict, total=False):
    account_id: Required[str]
    data: Required["_PostCommentCreatedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required[Literal["tiktok"]]
    type: Required[Literal["post.comment.created"]]


class PostCommentListRequest(TypedDict, total=False):
    cursor: NotRequired[str]
    limit: NotRequired[int]
    post_id: Required["PostResourceID"]


class PostCommentListResultVariant1(TypedDict, total=False):
    has_more: Required[Literal[True]]
    items: Required[list["PostComment"]]
    next_cursor: Required[str]


class PostCommentListResultVariant2(TypedDict, total=False):
    has_more: Required[Literal[False]]
    items: Required[list["PostComment"]]
    next_cursor: NotRequired[Never]


class PostCommentReplyRequest(TypedDict, total=False):
    comment_id: NotRequired["PostResourceID"]
    post_id: Required["PostResourceID"]
    text: Required[str]


class PostCommentReplyResult(TypedDict, total=False):
    comment: NotRequired["PostComment"]
    status: Required[Literal["accepted"]]


class PostInfoRequest(TypedDict, total=False):
    post_id: Required["PostResourceID"]


class PostListResultVariant1(TypedDict, total=False):
    has_more: Required[Literal[True]]
    items: Required[list["Post"]]
    next_cursor: Required[str]


class PostListResultVariant2(TypedDict, total=False):
    has_more: Required[Literal[False]]
    items: Required[list["Post"]]
    next_cursor: NotRequired[Never]


PostResourceID: TypeAlias = str


class ProviderAuthSession(TypedDict, total=False):
    account_id: Required[str]
    auth_mode: Required[str]
    auth_payload: NotRequired["_ProviderAuthSessionAuthPayload"]
    authorize_url: Required[str]
    available_auth_modes: Required[list[str]]
    expires_at: Required[str]
    provider: Required["ProviderName"]
    status: Required[str]
    switchable: Required[bool]


ProviderInputName: TypeAlias = Literal[
    "telegram",
    "whatsapp",
    "line",
    "twitter",
    "zalo",
    "tiktok",
    "whatsapp-protocol",
    "x",
    "x_client",
    "twitter_client",
]


ProviderName: TypeAlias = Literal[
    "telegram",
    "whatsapp",
    "line",
    "twitter",
    "zalo",
    "tiktok",
    "whatsapp-protocol",
]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class ProviderProfile(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    avatar_url: NotRequired[str]
    bio: NotRequired[str]
    business_name: NotRequired[str]
    device_id: NotRequired["WhatsAppDeviceID"]
    display_name: NotRequired[str]
    first_name: NotRequired[str]
    id: NotRequired[str]
    last_name: NotRequired[str]
    phone: NotRequired[str]
    platform: NotRequired[str]
    push_name: NotRequired[str]
    username: NotRequired[str]


class ProviderRegionsResponse(TypedDict, total=False):
    provider: Required["ProviderName"]
    regions: Required[list["RegionAvailability"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class QRAuthCheckData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    action: NotRequired[Literal["check_qr_auth"]]
    auth_payload: NotRequired["QRAuthCheckPayload"]
    auth_status: NotRequired[str]
    provider: NotRequired["ProviderName"]
    status: NotRequired[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class QRAuthCheckPayload(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    public_key: NotRequired["FreeFormObject"]
    qr_code: NotRequired[str]
    type: NotRequired[str]


class ReceivedContactCard(TypedDict, total=False):
    name: NotRequired[str]
    vcard: Required[str]


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
    auth_required: NotRequired[bool]
    auth_status: NotRequired[str]
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


class SendMessageLinkPreview(TypedDict, total=False):
    description: NotRequired[str]
    image_url: NotRequired["MessageLinkPreviewHTTPURL"]
    title: NotRequired[str]
    url: Required["MessageLinkPreviewHTTPURL"]


class SendMessagePoll(TypedDict, total=False):
    max_selections: Required[int]
    options: Required[list["SendMessagePollOption"]]
    question: Required[str]


class SendMessagePollOption(TypedDict, total=False):
    title: Required[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class SendMessageProviderData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    seconds: NotRequired[int]
    waveform: NotRequired[str]


class SendMessageRequest(TypedDict, total=False):
    account_id: Required[str]
    mentions: NotRequired[list["Mention"]]
    message: Required["MessagePayload"]
    provider_data: NotRequired[dict[str, JsonValue]]
    reply_to: NotRequired["ReplyTo"]
    to: Required["Recipient"]


class SendMessageResult(TypedDict, total=False):
    account_id: Required[str]
    message_id: Required[str]
    provider_ref: NotRequired[str]
    reply_token: NotRequired[str]
    status: Required[str]


SessionImportRequest = TypedDict(
    "SessionImportRequest",
    {
        "session_url": NotRequired[str],
        "whatsapp-protocol": NotRequired["WhatsAppProtocolSessionImportParams"],
    },
    total=False,
)


StandardEventType: TypeAlias = Literal[
    "*",
    "contact.updated",
    "post.comment.created",
    "message.received",
    "message.updated",
    "message.deleted",
    "message.read",
    "message.reaction",
    "message.delivered",
    "call.incoming",
    "call.answered",
    "call.ended",
    "conversation.updated",
    "conversation.deleted",
    "conversation.cleared",
    "conversation.history",
    "group.updated",
    "group.join_request",
    "account.status.updated",
    "account.profile.updated",
    "account.started",
    "account.history.synced",
    "account.auth.required",
    "account.auth.succeeded",
    "account.auth.failed",
]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class StartCodeAuthData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    action: Required[Literal["start_auth"]]
    auth_payload: NotRequired["_StartCodeAuthDataAuthPayload"]
    auth_status: NotRequired[str]
    provider: Required["ProviderName"]
    status: NotRequired[str]
    verify_code: NotRequired[str]


class StickerMessagePayloadVariant1(TypedDict, total=False):
    file_key: NotRequired[str]
    file_url: NotRequired[str]
    type: Required[Literal["sticker"]]
    url: Required[str]


class StickerMessagePayloadVariant2(TypedDict, total=False):
    file_key: NotRequired[str]
    file_url: Required[str]
    type: Required[Literal["sticker"]]
    url: NotRequired[str]


class StickerMessagePayloadVariant3(TypedDict, total=False):
    file_key: Required[str]
    file_url: NotRequired[str]
    type: Required[Literal["sticker"]]
    url: NotRequired[str]


class TextMessagePayload(TypedDict, total=False):
    caption: NotRequired[str]
    text: Required[str]
    type: Required[Literal["text"]]


class WebhookEndpoint(TypedDict, total=False):
    account_id: NotRequired[str]
    id: Required[str]
    retry_policy: NotRequired["FreeFormObject"]
    signing_enabled: Required[bool]
    status: Required[Literal["active", "inactive"]]
    subscribed_events: NotRequired[list["StandardEventType"]]
    url: Required[str]


class WebhookEndpointRequest(TypedDict, total=False):
    account_id: NotRequired[str]
    retry_policy: NotRequired["FreeFormObject"]
    signing_secret: NotRequired[str]
    status: Required[Literal["active", "inactive"]]
    subscribed_events: NotRequired[list["StandardEventType"]]
    url: Required[str]


class WhatsAppAccountAuthFailedWebhookEvent(TypedDict, total=False):
    account_id: Required[str]
    data: Required["_WhatsAppAccountAuthFailedWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required[Literal["whatsapp"]]
    type: Required[Literal["account.auth.failed"]]


class WhatsAppContactCreateOptions(TypedDict, total=False):
    first_name: NotRequired[str]
    full_name: NotRequired[str]
    sync_to_device_contacts: NotRequired[bool]


WhatsAppDeviceID: TypeAlias = int


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class WhatsAppMessageDeviceSender(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    device_id: NotRequired["WhatsAppDeviceID"]
    id: NotRequired[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class WhatsAppMessageDeviceWebhookEvent(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account_id: Required[str]
    data: Required["_WhatsAppMessageDeviceWebhookEventData"]
    id: Required[str]
    occurred_at: Required[str]
    provider: Required[Literal["whatsapp"]]
    type: Required[Literal["message.received", "message.updated"]]


class WhatsAppMessageReferralExtension(TypedDict, total=False):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class WhatsAppProtocolSessionImportParams(TypedDict, total=False):
    app_version: NotRequired[str]
    auth_hex_data: NotRequired[str]
    authhexdata: NotRequired[str]
    country: NotRequired[str]
    device: NotRequired[int]
    fallback_server_addresses: NotRequired[list[str]]
    hash: NotRequired[str]
    identity_pri_key: Required[str]
    identity_pub_key: Required[str]
    peer_kem_public: NotRequired[str]
    phone: Required[str]
    platform: NotRequired[int]
    pq_handshake_mode: NotRequired[str]
    server_address: NotRequired[str]
    static_pri_key: Required[str]
    static_pub_key: Required[str]
    use_xxkem_handshake: NotRequired[bool]


class Workspace(TypedDict, total=False):
    account_quota: Required[int]
    account_quota_unlimited: Required[bool]
    account_quota_used: Required[int]
    is_beta: Required[bool]
    metadata: NotRequired[dict[str, str]]
    name: Required[str]
    status: Required["WorkspaceStatus"]


WorkspaceStatus: TypeAlias = Literal[
    "active",
    "inactive",
]


class WorkspaceUpdateRequest(TypedDict, total=False):
    is_beta: NotRequired[Never]
    metadata: NotRequired[dict[str, str]]
    name: Required[str]
    status: Required["WorkspaceStatus"]


class _AccountProfileUpdatedWebhookEventData(TypedDict, total=False):
    account: NotRequired["__AccountProfileUpdatedWebhookEventDataAccount"]
    event: Required["__AccountProfileUpdatedWebhookEventDataEvent"]
    profile: Required["__AccountProfileUpdatedWebhookEventDataProfile"]


_AccountSessionAuthPayload: TypeAlias = dict[str, JsonValue]


class _AccountStartedWebhookEventData(TypedDict, total=False):
    event: Required["__AccountStartedWebhookEventDataEvent"]
    runtime_status: Required[Literal["running"]]


class _CallAnsweredWebhookEventData(TypedDict, total=False):
    call: Required["CallEventCall"]
    sender: Required["CallEventSender"]


class _CallEndedWebhookEventDataVariant1(TypedDict, total=False):
    call: Required["__CallEndedWebhookEventDataVariant1Call"]
    duration_seconds: Required[int]
    reason: Required[
        Literal[
            "declined",
            "caller_cancelled",
            "local_hangup",
            "remote_hangup",
            "answer_failed",
            "provider_disconnected",
            "media_failed",
            "expired",
            "remote_busy",
            "no_answer",
            "dial_failed",
        ]
    ]
    sender: Required["CallEventSender"]


class _CallEndedWebhookEventDataVariant2(TypedDict, total=False):
    call: Required["__CallEndedWebhookEventDataVariant2Call"]
    duration_seconds: Required[int]
    reason: Required[
        Literal[
            "declined",
            "caller_cancelled",
            "local_hangup",
            "remote_hangup",
            "answer_failed",
            "provider_disconnected",
            "media_failed",
            "expired",
            "remote_busy",
            "no_answer",
            "dial_failed",
        ]
    ]
    sender: NotRequired["CallEventSender"]


class _CallIncomingWebhookEventData(TypedDict, total=False):
    call: Required["__CallIncomingWebhookEventDataCall"]
    join_url: Required[str]
    sender: Required["CallEventSender"]


class _CallMessageReceivedWebhookEventData(TypedDict, total=False):
    account: NotRequired["__CallMessageReceivedWebhookEventDataAccount"]
    conversation: NotRequired["__CallMessageReceivedWebhookEventDataConversation"]
    event: NotRequired["__CallMessageReceivedWebhookEventDataEvent"]
    message: Required["__CallMessageReceivedWebhookEventDataMessage"]
    sender: NotRequired["__CallMessageReceivedWebhookEventDataSender"]


class _CallMessageUpdatedWebhookEventData(TypedDict, total=False):
    account: NotRequired["__CallMessageUpdatedWebhookEventDataAccount"]
    conversation: NotRequired["__CallMessageUpdatedWebhookEventDataConversation"]
    event: NotRequired["__CallMessageUpdatedWebhookEventDataEvent"]
    message: Required["__CallMessageUpdatedWebhookEventDataMessage"]
    sender: NotRequired["__CallMessageUpdatedWebhookEventDataSender"]


class _CallMessageWebhookEventData(TypedDict, total=False):
    account: NotRequired["__CallMessageWebhookEventDataAccount"]
    conversation: NotRequired["__CallMessageWebhookEventDataConversation"]
    event: NotRequired["__CallMessageWebhookEventDataEvent"]
    message: Required["CallMessage"]
    sender: NotRequired["__CallMessageWebhookEventDataSender"]


class _ConversationDisappearingMessagesUpdatedWebhookEventData(TypedDict, total=False):
    account: NotRequired["ConversationStateAccount"]
    actor: NotRequired["ConversationStateActor"]
    conversation: Required["ConversationStateReference"]
    disappearing_messages: Required["ConversationDisappearingMessagesState"]
    event: Required["ConversationDisappearingMessagesChange"]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _ConversationExtra(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    is_announcement_group: NotRequired[bool]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _ConversationHistoryWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    conversation: Required["__ConversationHistoryWebhookEventDataConversation"]
    history: NotRequired["ConversationHistorySource"]
    messages: Required[list["ConversationHistoryMessage"]]


class _CreateCallRequestTo(TypedDict, total=False):
    id: Required[str]
    type: Required["ConversationType"]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _GroupExtra(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    is_announcement_group: NotRequired[bool]


class _GroupSettingsUpdatedWebhookEventData(TypedDict, total=False):
    account: NotRequired["ConversationStateAccount"]
    actor: NotRequired["ConversationStateActor"]
    changes: Required[list["GroupUpdatedChange"]]
    conversation: Required["ConversationStateReference"]
    event: Required["GroupSettingsEvent"]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageCommerceHistoryWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: NotRequired["__MessageCommerceHistoryWebhookEventDataMessage"]
    messages: Required[list["MessageWithOptionalCommerce"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageCommerceReceivedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessageCommerceReceivedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalCommerce"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageCommerceUpdatedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessageCommerceUpdatedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalCommerce"]]


class _MessageCommerceVariant1Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["__MessageCommerceVariant1ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class _MessageCommerceVariant2Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["__MessageCommerceVariant2OrderTotal"]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageCommerceWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: NotRequired["__MessageCommerceWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalCommerce"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageContactCardsHistoryWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: NotRequired["MessageWithOptionalReferral"]
    messages: Required[list["MessageWithOptionalContactCards"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageContactCardsReceivedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessageContactCardsReceivedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalReferral"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageContactCardsUpdatedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessageContactCardsUpdatedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalReferral"]]


class _MessageInteractiveHeaderVariant2Attachment(TypedDict, total=False):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired["MessageInteractiveAttachmentMetadata"]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired["MessageCommerceHTTPURL"]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired["MessageCommerceHTTPURL"]


class _MessageInteractiveHeaderVariant3Attachment(TypedDict, total=False):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired["MessageInteractiveAttachmentMetadata"]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired["MessageCommerceHTTPURL"]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired["MessageCommerceHTTPURL"]


class _MessageInteractiveHeaderVariant4Attachment(TypedDict, total=False):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired["MessageInteractiveAttachmentMetadata"]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired["MessageCommerceHTTPURL"]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired["MessageCommerceHTTPURL"]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageInteractiveHistoryWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: NotRequired["__MessageInteractiveHistoryWebhookEventDataMessage"]
    messages: Required[list["MessageWithOptionalInteractive"]]


class _MessageInteractiveMessageVariant1InteractiveVariant1(TypedDict, total=False):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required["__MessageInteractiveMessageVariant1InteractiveVariant1Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageInteractiveMessageVariant1InteractiveVariant2(TypedDict, total=False):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired["__MessageInteractiveMessageVariant1InteractiveVariant2Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageInteractiveMessageVariant1InteractiveVariant3(TypedDict, total=False):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired["__MessageInteractiveMessageVariant1InteractiveVariant3Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageInteractiveMessageVariant1InteractiveVariant4(TypedDict, total=False):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired["__MessageInteractiveMessageVariant1InteractiveVariant4Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageInteractiveMessageVariant2InteractiveResponseVariant1(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class _MessageInteractiveMessageVariant2InteractiveResponseVariant2(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class _MessageInteractiveMessageVariant2InteractiveResponseVariant3(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageInteractiveReceivedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessageInteractiveReceivedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalInteractive"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageInteractiveUpdatedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessageInteractiveUpdatedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalInteractive"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageInteractiveWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: NotRequired["__MessageInteractiveWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalInteractive"]]


_MessageLinkPreviewDescriptionVariant1: TypeAlias = Literal[""]


_MessageLinkPreviewDescriptionVariant2: TypeAlias = str


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageLinkPreviewHistoryWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: NotRequired["__MessageLinkPreviewHistoryWebhookEventDataMessage"]
    messages: Required[list["MessageWithOptionalLinkPreview"]]


_MessageLinkPreviewImageUrl: TypeAlias = str


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageLinkPreviewReceivedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessageLinkPreviewReceivedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalLinkPreview"]]


_MessageLinkPreviewTitleVariant1: TypeAlias = Literal[""]


_MessageLinkPreviewTitleVariant2: TypeAlias = str


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageLinkPreviewUpdatedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessageLinkPreviewUpdatedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalLinkPreview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageLinkPreviewWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: NotRequired["__MessageLinkPreviewWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalLinkPreview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageLiveLocationHistoryWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: NotRequired["MessageWithOptionalReferral"]
    messages: Required[list["MessageWithOptionalLiveLocation"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageLiveLocationReceivedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessageLiveLocationReceivedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalReferral"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageLiveLocationUpdatedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessageLiveLocationUpdatedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalReferral"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessagePinUpdatedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    actor: NotRequired["MessagePinParticipant"]
    conversation: NotRequired["__MessagePinUpdatedWebhookEventDataConversation"]
    event: Required["MessagePinChange"]
    message: Required["MessagePinMessage"]
    sender: NotRequired["MessagePinParticipant"]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessagePollHistoryWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: NotRequired["__MessagePollHistoryWebhookEventDataMessage"]
    messages: Required[list["MessageWithOptionalPoll"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessagePollReceivedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessagePollReceivedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalPoll"]]


class _MessagePollVoteUpdatedWebhookEventData(TypedDict, total=False):
    account: NotRequired["ConversationStateAccount"]
    actor: Required["ConversationStateActor"]
    conversation: NotRequired["ConversationStateReference"]
    event: Required["MessagePollVoteChange"]
    message: Required["MessagePollVoteMessage"]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessagePollWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: NotRequired["__MessagePollWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalPoll"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageReferralHistoryWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: NotRequired["MessageWithOptionalReferral"]
    messages: Required[list["MessageWithOptionalReferral"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageReferralReceivedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessageReferralReceivedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalReferral"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageReferralUpdatedWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: Required["__MessageReferralUpdatedWebhookEventDataMessage"]
    messages: NotRequired[list["MessageWithOptionalReferral"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _MessageReferralWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    message: NotRequired["MessageWithOptionalReferral"]
    messages: NotRequired[list["MessageWithOptionalReferral"]]


class _MessageWithOptionalCommerceVariant1Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["__MessageWithOptionalCommerceVariant1ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class _MessageWithOptionalCommerceVariant2Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["__MessageWithOptionalCommerceVariant2OrderTotal"]


class _MessageWithOptionalInteractiveVariant1InteractiveVariant1(TypedDict, total=False):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required["__MessageWithOptionalInteractiveVariant1InteractiveVariant1Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageWithOptionalInteractiveVariant1InteractiveVariant2(TypedDict, total=False):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired["__MessageWithOptionalInteractiveVariant1InteractiveVariant2Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageWithOptionalInteractiveVariant1InteractiveVariant3(TypedDict, total=False):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired["__MessageWithOptionalInteractiveVariant1InteractiveVariant3Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageWithOptionalInteractiveVariant1InteractiveVariant4(TypedDict, total=False):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired["__MessageWithOptionalInteractiveVariant1InteractiveVariant4Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageWithOptionalInteractiveVariant2InteractiveResponseVariant1(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class _MessageWithOptionalInteractiveVariant2InteractiveResponseVariant2(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class _MessageWithOptionalInteractiveVariant2InteractiveResponseVariant3(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


class _MessageWithOptionalInteractiveVariant3Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["__MessageWithOptionalInteractiveVariant3ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class _MessageWithOptionalInteractiveVariant4Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["__MessageWithOptionalInteractiveVariant4OrderTotal"]


class _MessageWithOptionalLinkPreviewVariant2InteractiveVariant1(TypedDict, total=False):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required["__MessageWithOptionalLinkPreviewVariant2InteractiveVariant1Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageWithOptionalLinkPreviewVariant2InteractiveVariant2(TypedDict, total=False):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired["__MessageWithOptionalLinkPreviewVariant2InteractiveVariant2Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageWithOptionalLinkPreviewVariant2InteractiveVariant3(TypedDict, total=False):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired["__MessageWithOptionalLinkPreviewVariant2InteractiveVariant3Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageWithOptionalLinkPreviewVariant2InteractiveVariant4(TypedDict, total=False):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired["__MessageWithOptionalLinkPreviewVariant2InteractiveVariant4Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageWithOptionalLinkPreviewVariant3InteractiveResponseVariant1(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class _MessageWithOptionalLinkPreviewVariant3InteractiveResponseVariant2(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class _MessageWithOptionalLinkPreviewVariant3InteractiveResponseVariant3(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


class _MessageWithOptionalLinkPreviewVariant4Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["__MessageWithOptionalLinkPreviewVariant4ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class _MessageWithOptionalLinkPreviewVariant5Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["__MessageWithOptionalLinkPreviewVariant5OrderTotal"]


class _MessageWithOptionalPollVariant3InteractiveVariant1(TypedDict, total=False):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required["__MessageWithOptionalPollVariant3InteractiveVariant1Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageWithOptionalPollVariant3InteractiveVariant2(TypedDict, total=False):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired["__MessageWithOptionalPollVariant3InteractiveVariant2Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageWithOptionalPollVariant3InteractiveVariant3(TypedDict, total=False):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired["__MessageWithOptionalPollVariant3InteractiveVariant3Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageWithOptionalPollVariant3InteractiveVariant4(TypedDict, total=False):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired["__MessageWithOptionalPollVariant3InteractiveVariant4Header"]
    kind: Required[Literal["buttons", "template"]]


class _MessageWithOptionalPollVariant4InteractiveResponseVariant1(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class _MessageWithOptionalPollVariant4InteractiveResponseVariant2(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class _MessageWithOptionalPollVariant4InteractiveResponseVariant3(TypedDict, total=False):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


class _MessageWithOptionalPollVariant5Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["__MessageWithOptionalPollVariant5ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class _MessageWithOptionalPollVariant6Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["__MessageWithOptionalPollVariant6OrderTotal"]


class _PostCommentCreatedWebhookEventData(TypedDict, total=False):
    account: NotRequired["__PostCommentCreatedWebhookEventDataAccount"]
    comment: Required["PostComment"]
    post: Required["Post"]


_ProviderAuthSessionAuthPayload: TypeAlias = dict[str, JsonValue]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _StartCodeAuthDataAuthPayload(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    type: NotRequired[str]


class _WhatsAppAccountAuthFailedWebhookEventData(TypedDict, total=False):
    auth_status: Required[Literal["failed"]]
    error: NotRequired["__WhatsAppAccountAuthFailedWebhookEventDataError"]
    event: Required["__WhatsAppAccountAuthFailedWebhookEventDataEvent"]
    last_error: NotRequired[str]
    runtime_status: Required[Literal["disconnected"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class _WhatsAppMessageDeviceWebhookEventData(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    account: NotRequired["__WhatsAppMessageDeviceWebhookEventDataAccount"]
    message: NotRequired["__WhatsAppMessageDeviceWebhookEventDataMessage"]
    sender: NotRequired["WhatsAppMessageDeviceSender"]


class __AccountProfileUpdatedWebhookEventDataAccount(TypedDict, total=False):
    provider_account_ref: NotRequired[str]


class __AccountProfileUpdatedWebhookEventDataEvent(TypedDict, total=False):
    changed_fields: NotRequired[
        list[Literal["display_name", "push_name", "business_name", "avatar_url"]]
    ]
    kind: Required[Literal["account_profile_updated"]]
    source: Required[Literal["full_sync", "self_rename", "avatar_change"]]


class __AccountProfileUpdatedWebhookEventDataProfile(TypedDict, total=False):
    avatar_url: Required[str]
    business_name: NotRequired[str]
    display_name: Required[str]
    push_name: Required[str]


class __AccountStartedWebhookEventDataEvent(TypedDict, total=False):
    kind: Required[Literal["account_started"]]
    runtime_status: Required[Literal["running"]]


class __CallEndedWebhookEventDataVariant1Call(TypedDict, total=False):
    direction: Required[Literal["inbound"]]
    id: Required[str]
    media_type: Required[Literal["voice", "video"]]
    state: Required[Literal["ringing", "active", "ended"]]


class __CallEndedWebhookEventDataVariant2Call(TypedDict, total=False):
    direction: Required[Literal["outbound"]]
    id: Required[str]
    media_type: Required[Literal["voice", "video"]]
    state: Required[Literal["ringing", "active", "ended"]]


class __CallIncomingWebhookEventDataCall(TypedDict, total=False):
    direction: Required[Literal["inbound", "outbound"]]
    id: Required[str]
    media_type: Required[Literal["voice", "video"]]
    state: Required[Literal["ringing", "active", "ended"]]


class __CallMessageReceivedWebhookEventDataAccount(TypedDict, total=False):
    provider_account_ref: NotRequired[str]


class __CallMessageReceivedWebhookEventDataConversation(TypedDict, total=False):
    id: Required[str]
    type: Required[Literal["user"]]


class __CallMessageReceivedWebhookEventDataEvent(TypedDict, total=False):
    kind: NotRequired[Literal["message_received", "message_updated"]]


class __CallMessageReceivedWebhookEventDataMessage(TypedDict, total=False):
    call: Required["___CallMessageReceivedWebhookEventDataMessageCall"]
    direction: Required[Literal["inbound"]]
    id: Required[str]
    sent_at: NotRequired[str]
    type: Required[Literal["call"]]


class __CallMessageReceivedWebhookEventDataSender(TypedDict, total=False):
    id: Required[str]
    type: NotRequired[Literal["user"]]


class __CallMessageUpdatedWebhookEventDataAccount(TypedDict, total=False):
    provider_account_ref: NotRequired[str]


class __CallMessageUpdatedWebhookEventDataConversation(TypedDict, total=False):
    id: Required[str]
    type: Required[Literal["user"]]


class __CallMessageUpdatedWebhookEventDataEvent(TypedDict, total=False):
    kind: NotRequired[Literal["message_received", "message_updated"]]


class __CallMessageUpdatedWebhookEventDataMessage(TypedDict, total=False):
    call: Required["___CallMessageUpdatedWebhookEventDataMessageCall"]
    direction: NotRequired[Never]
    id: Required[str]
    sent_at: NotRequired[Never]
    type: Required[Literal["call"]]


class __CallMessageUpdatedWebhookEventDataSender(TypedDict, total=False):
    id: Required[str]
    type: NotRequired[Literal["user"]]


class __CallMessageWebhookEventDataAccount(TypedDict, total=False):
    provider_account_ref: NotRequired[str]


class __CallMessageWebhookEventDataConversation(TypedDict, total=False):
    id: Required[str]
    type: Required[Literal["user"]]


class __CallMessageWebhookEventDataEvent(TypedDict, total=False):
    kind: NotRequired[Literal["message_received", "message_updated"]]


class __CallMessageWebhookEventDataSender(TypedDict, total=False):
    id: Required[str]
    type: NotRequired[Literal["user"]]


class __ConversationHistoryWebhookEventDataConversation(TypedDict, total=False):
    id: Required[str]
    type: Required["ConversationType"]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceHistoryWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: NotRequired[Never]
    product: Required["___MessageCommerceHistoryWebhookEventDataMessageVariant1Product"]
    referral: NotRequired["___MessageCommerceHistoryWebhookEventDataMessageVariant1Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceHistoryWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: Required["___MessageCommerceHistoryWebhookEventDataMessageVariant2Order"]
    product: NotRequired[Never]
    referral: NotRequired["___MessageCommerceHistoryWebhookEventDataMessageVariant2Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceHistoryWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageCommerceHistoryWebhookEventDataMessageVariant3Referral"]
    type: NotRequired[JsonValue]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceReceivedWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: NotRequired[Never]
    product: Required["___MessageCommerceReceivedWebhookEventDataMessageVariant1Product"]
    referral: NotRequired["___MessageCommerceReceivedWebhookEventDataMessageVariant1Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceReceivedWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: Required[Never]
    product: Required[Never]
    referral: NotRequired["___MessageCommerceReceivedWebhookEventDataMessageVariant2Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceReceivedWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: NotRequired[Never]
    product: Required[Never]
    referral: NotRequired["___MessageCommerceReceivedWebhookEventDataMessageVariant3Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceReceivedWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: Required[Never]
    product: Required[Never]
    referral: NotRequired["___MessageCommerceReceivedWebhookEventDataMessageVariant4Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceReceivedWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: Required["___MessageCommerceReceivedWebhookEventDataMessageVariant5Order"]
    product: NotRequired[Never]
    referral: NotRequired["___MessageCommerceReceivedWebhookEventDataMessageVariant5Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceReceivedWebhookEventDataMessageVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: Required[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageCommerceReceivedWebhookEventDataMessageVariant6Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceUpdatedWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    order: NotRequired[Never]
    product: Required["___MessageCommerceUpdatedWebhookEventDataMessageVariant1Product"]
    referral: NotRequired["___MessageCommerceUpdatedWebhookEventDataMessageVariant1Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceUpdatedWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    order: Required[Never]
    product: Required[Never]
    referral: NotRequired["___MessageCommerceUpdatedWebhookEventDataMessageVariant2Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceUpdatedWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    order: NotRequired[Never]
    product: Required[Never]
    referral: NotRequired["___MessageCommerceUpdatedWebhookEventDataMessageVariant3Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceUpdatedWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    order: Required[Never]
    product: Required[Never]
    referral: NotRequired["___MessageCommerceUpdatedWebhookEventDataMessageVariant4Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceUpdatedWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    order: Required["___MessageCommerceUpdatedWebhookEventDataMessageVariant5Order"]
    product: NotRequired[Never]
    referral: NotRequired["___MessageCommerceUpdatedWebhookEventDataMessageVariant5Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceUpdatedWebhookEventDataMessageVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    order: Required[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageCommerceUpdatedWebhookEventDataMessageVariant6Referral"]
    type: Required[Literal["product", "order"]]


class __MessageCommerceVariant1ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class __MessageCommerceVariant2OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: NotRequired[Never]
    product: Required["___MessageCommerceWebhookEventDataMessageVariant1Product"]
    referral: NotRequired["___MessageCommerceWebhookEventDataMessageVariant1Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: Required["___MessageCommerceWebhookEventDataMessageVariant2Order"]
    product: NotRequired[Never]
    referral: NotRequired["___MessageCommerceWebhookEventDataMessageVariant2Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageCommerceWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageCommerceWebhookEventDataMessageVariant3Referral"]
    type: NotRequired[JsonValue]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageContactCardsReceivedWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    contacts: Required[list["ReceivedContactCard"]]
    id: NotRequired[str]
    referral: NotRequired["MessageReferral"]
    text: Required[str]
    type: NotRequired[Literal["contact"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageContactCardsReceivedWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    contacts: Required[list["ReceivedContactCard"]]
    id: Required[str]
    referral: NotRequired["MessageReferral"]
    reply_token: NotRequired[Never]
    text: NotRequired[Never]
    type: Required[Literal["contact"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageContactCardsUpdatedWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    contacts: Required[list["ReceivedContactCard"]]
    id: Required[str]
    referral: NotRequired["MessageReferral"]
    text: Required[str]
    type: NotRequired[Literal["contact"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageContactCardsUpdatedWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    contacts: Required[list["ReceivedContactCard"]]
    id: Required[str]
    referral: NotRequired["MessageReferral"]
    reply_token: NotRequired[Never]
    text: NotRequired[Never]
    type: Required[Literal["contact"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveHistoryWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required["___MessageInteractiveHistoryWebhookEventDataMessageVariant1Interactive"]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveHistoryWebhookEventDataMessageVariant1Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveHistoryWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required[
        "___MessageInteractiveHistoryWebhookEventDataMessageVariant2InteractiveResponse"
    ]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveHistoryWebhookEventDataMessageVariant2Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveHistoryWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: Required["___MessageInteractiveHistoryWebhookEventDataMessageVariant3Product"]
    referral: NotRequired["___MessageInteractiveHistoryWebhookEventDataMessageVariant3Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveHistoryWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    order: Required["___MessageInteractiveHistoryWebhookEventDataMessageVariant4Order"]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveHistoryWebhookEventDataMessageVariant4Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveHistoryWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveHistoryWebhookEventDataMessageVariant5Referral"]
    type: NotRequired[JsonValue]


class __MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant1(TypedDict, total=False):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant2(TypedDict, total=False):
    attachment: Required[
        "___MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant3(TypedDict, total=False):
    attachment: Required[
        "___MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant4(TypedDict, total=False):
    attachment: Required[
        "___MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant1(TypedDict, total=False):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant2(TypedDict, total=False):
    attachment: Required[
        "___MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant3(TypedDict, total=False):
    attachment: Required[
        "___MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant4(TypedDict, total=False):
    attachment: Required[
        "___MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant1(TypedDict, total=False):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant2(TypedDict, total=False):
    attachment: Required[
        "___MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant3(TypedDict, total=False):
    attachment: Required[
        "___MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant4(TypedDict, total=False):
    attachment: Required[
        "___MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant1(TypedDict, total=False):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant2(TypedDict, total=False):
    attachment: Required[
        "___MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant3(TypedDict, total=False):
    attachment: Required[
        "___MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant4(TypedDict, total=False):
    attachment: Required[
        "___MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveReceivedWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required["___MessageInteractiveReceivedWebhookEventDataMessageVariant1Interactive"]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveReceivedWebhookEventDataMessageVariant1Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveReceivedWebhookEventDataMessageVariant10(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveReceivedWebhookEventDataMessageVariant10Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveReceivedWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required[Never]
    interactive_response: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveReceivedWebhookEventDataMessageVariant2Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveReceivedWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required[Never]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: Required[Never]
    referral: NotRequired["___MessageInteractiveReceivedWebhookEventDataMessageVariant3Referral"]
    type: Required[Literal["product"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveReceivedWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required[Never]
    interactive_response: NotRequired[Never]
    order: Required[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveReceivedWebhookEventDataMessageVariant4Referral"]
    type: Required[Literal["order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveReceivedWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required[Never]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveReceivedWebhookEventDataMessageVariant5Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveReceivedWebhookEventDataMessageVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required[Never]
    interactive_response: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveReceivedWebhookEventDataMessageVariant6Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveReceivedWebhookEventDataMessageVariant7(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required[
        "___MessageInteractiveReceivedWebhookEventDataMessageVariant7InteractiveResponse"
    ]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveReceivedWebhookEventDataMessageVariant7Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveReceivedWebhookEventDataMessageVariant8(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required[Never]
    order: NotRequired[Never]
    product: Required[Never]
    referral: NotRequired["___MessageInteractiveReceivedWebhookEventDataMessageVariant8Referral"]
    type: Required[Literal["product"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveReceivedWebhookEventDataMessageVariant9(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required[Never]
    order: Required[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveReceivedWebhookEventDataMessageVariant9Referral"]
    type: Required[Literal["order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveUpdatedWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: Required["___MessageInteractiveUpdatedWebhookEventDataMessageVariant1Interactive"]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveUpdatedWebhookEventDataMessageVariant1Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveUpdatedWebhookEventDataMessageVariant10(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveUpdatedWebhookEventDataMessageVariant10Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveUpdatedWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: Required[Never]
    interactive_response: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveUpdatedWebhookEventDataMessageVariant2Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveUpdatedWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: Required[Never]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: Required[Never]
    referral: NotRequired["___MessageInteractiveUpdatedWebhookEventDataMessageVariant3Referral"]
    type: Required[Literal["product"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveUpdatedWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: Required[Never]
    interactive_response: NotRequired[Never]
    order: Required[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveUpdatedWebhookEventDataMessageVariant4Referral"]
    type: Required[Literal["order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveUpdatedWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: Required[Never]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveUpdatedWebhookEventDataMessageVariant5Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveUpdatedWebhookEventDataMessageVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: Required[Never]
    interactive_response: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveUpdatedWebhookEventDataMessageVariant6Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveUpdatedWebhookEventDataMessageVariant7(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: Required[
        "___MessageInteractiveUpdatedWebhookEventDataMessageVariant7InteractiveResponse"
    ]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveUpdatedWebhookEventDataMessageVariant7Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveUpdatedWebhookEventDataMessageVariant8(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: Required[Never]
    order: NotRequired[Never]
    product: Required[Never]
    referral: NotRequired["___MessageInteractiveUpdatedWebhookEventDataMessageVariant8Referral"]
    type: Required[Literal["product"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveUpdatedWebhookEventDataMessageVariant9(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: Required[Never]
    order: Required[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveUpdatedWebhookEventDataMessageVariant9Referral"]
    type: Required[Literal["order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required["___MessageInteractiveWebhookEventDataMessageVariant1Interactive"]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveWebhookEventDataMessageVariant1Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required[
        "___MessageInteractiveWebhookEventDataMessageVariant2InteractiveResponse"
    ]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveWebhookEventDataMessageVariant2Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: Required["___MessageInteractiveWebhookEventDataMessageVariant3Product"]
    referral: NotRequired["___MessageInteractiveWebhookEventDataMessageVariant3Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    order: Required["___MessageInteractiveWebhookEventDataMessageVariant4Order"]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveWebhookEventDataMessageVariant4Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageInteractiveWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageInteractiveWebhookEventDataMessageVariant5Referral"]
    type: NotRequired[JsonValue]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewHistoryWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required["MessageLinkPreview"]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewHistoryWebhookEventDataMessageVariant1Referral"]
    text: NotRequired[str]
    type: Required[Literal["link_preview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewHistoryWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required["___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2Interactive"]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewHistoryWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required[
        "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3InteractiveResponse"
    ]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewHistoryWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: Required["___MessageLinkPreviewHistoryWebhookEventDataMessageVariant4Product"]
    referral: NotRequired["___MessageLinkPreviewHistoryWebhookEventDataMessageVariant4Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewHistoryWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: Required["___MessageLinkPreviewHistoryWebhookEventDataMessageVariant5Order"]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewHistoryWebhookEventDataMessageVariant5Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewHistoryWebhookEventDataMessageVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewHistoryWebhookEventDataMessageVariant6Referral"]
    type: NotRequired[JsonValue]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewReceivedWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required[
        "___MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreview"
    ]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewReceivedWebhookEventDataMessageVariant1Referral"]
    text: NotRequired[str]
    type: Required[Literal["link_preview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewReceivedWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewReceivedWebhookEventDataMessageVariant2Referral"]
    text: NotRequired[str]
    type: Required[Literal["interactive"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewReceivedWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required[Never]
    link_preview: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewReceivedWebhookEventDataMessageVariant3Referral"]
    text: NotRequired[str]
    type: Required[Literal["interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewReceivedWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required[Never]
    order: NotRequired[Never]
    product: Required[Never]
    referral: NotRequired["___MessageLinkPreviewReceivedWebhookEventDataMessageVariant4Referral"]
    text: NotRequired[str]
    type: Required[Literal["product"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewReceivedWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required[Never]
    order: Required[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewReceivedWebhookEventDataMessageVariant5Referral"]
    text: NotRequired[str]
    type: Required[Literal["order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewReceivedWebhookEventDataMessageVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewReceivedWebhookEventDataMessageVariant6Referral"]
    text: NotRequired[str]
    type: Required[Literal["link_preview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreview"]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1Referral"]
    text: NotRequired[str]
    type: Required[Literal["link_preview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewUpdatedWebhookEventDataMessageVariant10(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: Required[Never]
    referral: NotRequired["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant10Referral"]
    text: NotRequired[str]
    type: Required[Literal["product"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewUpdatedWebhookEventDataMessageVariant11(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: Required[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant11Referral"]
    text: NotRequired[str]
    type: Required[Literal["order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewUpdatedWebhookEventDataMessageVariant12(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant12Referral"]
    text: NotRequired[str]
    type: Required[Literal["text"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewUpdatedWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: Required[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant2Referral"]
    text: NotRequired[str]
    type: Required[Literal["interactive"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewUpdatedWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: Required[Never]
    link_preview: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant3Referral"]
    text: NotRequired[str]
    type: Required[Literal["interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewUpdatedWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required[Never]
    order: NotRequired[Never]
    product: Required[Never]
    referral: NotRequired["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant4Referral"]
    text: NotRequired[str]
    type: Required[Literal["product"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewUpdatedWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required[Never]
    order: Required[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant5Referral"]
    text: NotRequired[str]
    type: Required[Literal["order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewUpdatedWebhookEventDataMessageVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant6Referral"]
    text: NotRequired[str]
    type: Required[Literal["link_preview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewUpdatedWebhookEventDataMessageVariant7(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant7Referral"]
    text: NotRequired[str]
    type: Required[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewUpdatedWebhookEventDataMessageVariant8(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: Required[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant8Referral"]
    text: NotRequired[str]
    type: Required[Literal["interactive"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewUpdatedWebhookEventDataMessageVariant9(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: Required[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant9Referral"]
    text: NotRequired[str]
    type: Required[Literal["interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewWebhookEventDataMessageVariant1(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required["MessageLinkPreview"]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewWebhookEventDataMessageVariant1Referral"]
    text: NotRequired[str]
    type: Required[Literal["link_preview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required["___MessageLinkPreviewWebhookEventDataMessageVariant2Interactive"]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewWebhookEventDataMessageVariant2Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required[
        "___MessageLinkPreviewWebhookEventDataMessageVariant3InteractiveResponse"
    ]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewWebhookEventDataMessageVariant3Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: Required["___MessageLinkPreviewWebhookEventDataMessageVariant4Product"]
    referral: NotRequired["___MessageLinkPreviewWebhookEventDataMessageVariant4Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: Required["___MessageLinkPreviewWebhookEventDataMessageVariant5Order"]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewWebhookEventDataMessageVariant5Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLinkPreviewWebhookEventDataMessageVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessageLinkPreviewWebhookEventDataMessageVariant6Referral"]
    type: NotRequired[JsonValue]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLiveLocationReceivedWebhookEventDataMessage(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    duration_seconds: NotRequired[Never]
    ended_at: NotRequired[Never]
    id: Required[str]
    latitude: NotRequired[Never]
    location: NotRequired[Never]
    longitude: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    reply_token: NotRequired[Never]
    text: NotRequired[Never]
    type: Required[Literal["live_location"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageLiveLocationUpdatedWebhookEventDataMessage(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    duration_seconds: NotRequired[Never]
    ended_at: NotRequired[Never]
    id: Required[str]
    latitude: NotRequired[Never]
    location: NotRequired[Never]
    longitude: NotRequired[Never]
    referral: NotRequired["MessageReferral"]
    reply_token: NotRequired[Never]
    text: NotRequired[Never]
    type: Required[Literal["live_location"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePinUpdatedWebhookEventDataConversation(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    type: Required[Literal["user", "group", "channel"]]


class __MessagePollHistoryWebhookEventDataMessageVariant1(TypedDict, total=False):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: Required[str]
    mentions: NotRequired[list["Mention"]]
    poll: Required["MessagePoll"]
    referral: NotRequired["___MessagePollHistoryWebhookEventDataMessageVariant1Referral"]
    reply_to_message_id: NotRequired[str]
    sender: NotRequired["ConversationStateActor"]
    sent_at: NotRequired[str]
    type: Required[Literal["poll"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollHistoryWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required["MessageLinkPreview"]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollHistoryWebhookEventDataMessageVariant2Referral"]
    text: NotRequired[str]
    type: Required[Literal["link_preview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollHistoryWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required["___MessagePollHistoryWebhookEventDataMessageVariant3Interactive"]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollHistoryWebhookEventDataMessageVariant3Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollHistoryWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required[
        "___MessagePollHistoryWebhookEventDataMessageVariant4InteractiveResponse"
    ]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollHistoryWebhookEventDataMessageVariant4Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollHistoryWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: Required["___MessagePollHistoryWebhookEventDataMessageVariant5Product"]
    referral: NotRequired["___MessagePollHistoryWebhookEventDataMessageVariant5Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollHistoryWebhookEventDataMessageVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: Required["___MessagePollHistoryWebhookEventDataMessageVariant6Order"]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollHistoryWebhookEventDataMessageVariant6Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollHistoryWebhookEventDataMessageVariant7(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollHistoryWebhookEventDataMessageVariant7Referral"]
    type: NotRequired[JsonValue]


class __MessagePollReceivedWebhookEventDataMessageVariant1(TypedDict, total=False):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: Required[str]
    mentions: NotRequired[list["Mention"]]
    poll: Required["___MessagePollReceivedWebhookEventDataMessageVariant1Poll"]
    referral: NotRequired["___MessagePollReceivedWebhookEventDataMessageVariant1Referral"]
    reply_to_message_id: NotRequired[str]
    sender: NotRequired["___MessagePollReceivedWebhookEventDataMessageVariant1Sender"]
    sent_at: NotRequired[str]
    type: Required[Literal["poll"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollReceivedWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required["MessageLinkPreview"]
    mentions: NotRequired[list["Mention"]]
    order: NotRequired[Never]
    poll: Required[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollReceivedWebhookEventDataMessageVariant2Referral"]
    reply_to_message_id: NotRequired[str]
    sender: NotRequired["ConversationStateActor"]
    sent_at: NotRequired[str]
    text: NotRequired[str]
    type: Required[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollReceivedWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: Required[str]
    interactive: Required["___MessagePollReceivedWebhookEventDataMessageVariant3Interactive"]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    mentions: NotRequired[list["Mention"]]
    order: NotRequired[Never]
    poll: Required[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollReceivedWebhookEventDataMessageVariant3Referral"]
    reply_to_message_id: NotRequired[str]
    sender: NotRequired["ConversationStateActor"]
    sent_at: NotRequired[str]
    type: Required[Literal["interactive"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollReceivedWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: Required[
        "___MessagePollReceivedWebhookEventDataMessageVariant4InteractiveResponse"
    ]
    link_preview: NotRequired[Never]
    mentions: NotRequired[list["Mention"]]
    order: NotRequired[Never]
    poll: Required[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollReceivedWebhookEventDataMessageVariant4Referral"]
    reply_to_message_id: NotRequired[str]
    sender: NotRequired["ConversationStateActor"]
    sent_at: NotRequired[str]
    type: Required[Literal["interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollReceivedWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    mentions: NotRequired[list["Mention"]]
    order: NotRequired[Never]
    poll: Required[Never]
    poll_vote: NotRequired[Never]
    product: Required["___MessagePollReceivedWebhookEventDataMessageVariant5Product"]
    referral: NotRequired["___MessagePollReceivedWebhookEventDataMessageVariant5Referral"]
    reply_to_message_id: NotRequired[str]
    sender: NotRequired["ConversationStateActor"]
    sent_at: NotRequired[str]
    type: Required[Literal["product"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollReceivedWebhookEventDataMessageVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    mentions: NotRequired[list["Mention"]]
    order: Required["___MessagePollReceivedWebhookEventDataMessageVariant6Order"]
    poll: Required[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollReceivedWebhookEventDataMessageVariant6Referral"]
    reply_to_message_id: NotRequired[str]
    sender: NotRequired["ConversationStateActor"]
    sent_at: NotRequired[str]
    type: Required[Literal["order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollReceivedWebhookEventDataMessageVariant7(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: Required[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    mentions: NotRequired[list["Mention"]]
    order: NotRequired[Never]
    poll: Required[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollReceivedWebhookEventDataMessageVariant7Referral"]
    reply_to_message_id: NotRequired[str]
    sender: NotRequired["ConversationStateActor"]
    sent_at: NotRequired[str]
    type: Required[Literal["poll"]]


class __MessagePollWebhookEventDataMessageVariant1(TypedDict, total=False):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: Required[str]
    mentions: NotRequired[list["Mention"]]
    poll: Required["MessagePoll"]
    referral: NotRequired["___MessagePollWebhookEventDataMessageVariant1Referral"]
    reply_to_message_id: NotRequired[str]
    sender: NotRequired["ConversationStateActor"]
    sent_at: NotRequired[str]
    type: Required[Literal["poll"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollWebhookEventDataMessageVariant2(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: Required["MessageLinkPreview"]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollWebhookEventDataMessageVariant2Referral"]
    text: NotRequired[str]
    type: Required[Literal["link_preview"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollWebhookEventDataMessageVariant3(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: Required["___MessagePollWebhookEventDataMessageVariant3Interactive"]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollWebhookEventDataMessageVariant3Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollWebhookEventDataMessageVariant4(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: Required[
        "___MessagePollWebhookEventDataMessageVariant4InteractiveResponse"
    ]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollWebhookEventDataMessageVariant4Referral"]
    type: Required[Literal["interactive", "interactive_response"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollWebhookEventDataMessageVariant5(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: Required["___MessagePollWebhookEventDataMessageVariant5Product"]
    referral: NotRequired["___MessagePollWebhookEventDataMessageVariant5Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollWebhookEventDataMessageVariant6(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: Required["___MessagePollWebhookEventDataMessageVariant6Order"]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollWebhookEventDataMessageVariant6Referral"]
    type: Required[Literal["product", "order"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessagePollWebhookEventDataMessageVariant7(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    interactive: NotRequired[Never]
    interactive_response: NotRequired[Never]
    link_preview: NotRequired[Never]
    order: NotRequired[Never]
    poll: NotRequired[Never]
    poll_vote: NotRequired[Never]
    product: NotRequired[Never]
    referral: NotRequired["___MessagePollWebhookEventDataMessageVariant7Referral"]
    type: NotRequired[JsonValue]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageReferralReceivedWebhookEventDataMessage(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: NotRequired[str]
    referral: Required["___MessageReferralReceivedWebhookEventDataMessageReferral"]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __MessageReferralUpdatedWebhookEventDataMessage(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    id: Required[str]
    referral: Required["___MessageReferralUpdatedWebhookEventDataMessageReferral"]


class __MessageWithOptionalCommerceVariant1ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class __MessageWithOptionalCommerceVariant2OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalInteractiveVariant3ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class __MessageWithOptionalInteractiveVariant4OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalLinkPreviewVariant4ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class __MessageWithOptionalLinkPreviewVariant5OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class __MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant1(TypedDict, total=False):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant2(TypedDict, total=False):
    attachment: Required[
        "___MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant3(TypedDict, total=False):
    attachment: Required[
        "___MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant4(TypedDict, total=False):
    attachment: Required[
        "___MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant1(TypedDict, total=False):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant2(TypedDict, total=False):
    attachment: Required[
        "___MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant3(TypedDict, total=False):
    attachment: Required[
        "___MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant4(TypedDict, total=False):
    attachment: Required[
        "___MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant1(TypedDict, total=False):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant2(TypedDict, total=False):
    attachment: Required[
        "___MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant3(TypedDict, total=False):
    attachment: Required[
        "___MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant4(TypedDict, total=False):
    attachment: Required[
        "___MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant1(TypedDict, total=False):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant2(TypedDict, total=False):
    attachment: Required[
        "___MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant3(TypedDict, total=False):
    attachment: Required[
        "___MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant4(TypedDict, total=False):
    attachment: Required[
        "___MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class __MessageWithOptionalPollVariant5ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class __MessageWithOptionalPollVariant6OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class __PostCommentCreatedWebhookEventDataAccount(TypedDict, total=False):
    provider_account_ref: Required[str]


class __WhatsAppAccountAuthFailedWebhookEventDataError(TypedDict, total=False):
    code: Required[Literal["account_auth_failed", "account_logged_out", "account_restricted"]]
    message: Required[str]
    numeric_code: Required[Literal["20100", "20101", "20102"]]


class __WhatsAppAccountAuthFailedWebhookEventDataEvent(TypedDict, total=False):
    auth_status: Required[Literal["failed"]]
    kind: Required[Literal["account_auth_status"]]
    runtime_status: Required[Literal["disconnected"]]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __WhatsAppMessageDeviceWebhookEventDataAccount(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    provider_account_ref: NotRequired[str]


# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。
class __WhatsAppMessageDeviceWebhookEventDataMessage(  # type: ignore[call-arg, unused-ignore]
    TypedDict, total=False, extra_items=JsonValue
):
    direction: NotRequired[Literal["inbound", "outbound"]]
    id: NotRequired[str]


class ___CallMessageReceivedWebhookEventDataMessageCall(TypedDict, total=False):
    accepted_at: NotRequired[Never]
    end_reason: NotRequired[Never]
    ended_by: NotRequired[Never]
    id: Required[str]
    media_type: NotRequired[Literal["audio", "video"]]
    status: Required[Literal["offered"]]


class ___CallMessageUpdatedWebhookEventDataMessageCallVariant1(TypedDict, total=False):
    accepted_at: NotRequired[str]
    end_reason: NotRequired[Never]
    ended_by: NotRequired[Never]
    id: Required[str]
    media_type: NotRequired[Literal["audio", "video"]]
    status: Required[Literal["accepted"]]


class ___CallMessageUpdatedWebhookEventDataMessageCallVariant2(TypedDict, total=False):
    accepted_at: NotRequired[str]
    end_reason: NotRequired[Never]
    ended_by: NotRequired[Never]
    id: Required[str]
    media_type: NotRequired[Literal["audio", "video"]]
    status: Required[Literal["accepted"]]


class ___CallMessageUpdatedWebhookEventDataMessageCallVariant3(TypedDict, total=False):
    accepted_at: NotRequired[Never]
    end_reason: NotRequired[Never]
    ended_by: NotRequired[Literal["remote"]]
    id: Required[str]
    media_type: NotRequired[Literal["audio", "video"]]
    status: Required[Literal["ended"]]


class ___CallMessageUpdatedWebhookEventDataMessageCallVariant4(TypedDict, total=False):
    accepted_at: NotRequired[Never]
    end_reason: NotRequired[Literal["timeout", "rejected_elsewhere"]]
    ended_by: NotRequired[Never]
    id: Required[str]
    media_type: NotRequired[Literal["audio", "video"]]
    status: Required[Literal["ended"]]


class ___MessageCommerceHistoryWebhookEventDataMessageVariant1Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["____MessageCommerceHistoryWebhookEventDataMessageVariant1ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class ___MessageCommerceHistoryWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceHistoryWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceHistoryWebhookEventDataMessageVariant2Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["____MessageCommerceHistoryWebhookEventDataMessageVariant2OrderTotal"]


class ___MessageCommerceHistoryWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceHistoryWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceHistoryWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceHistoryWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceReceivedWebhookEventDataMessageVariant1Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["____MessageCommerceReceivedWebhookEventDataMessageVariant1ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class ___MessageCommerceReceivedWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceReceivedWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceReceivedWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceReceivedWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceReceivedWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceReceivedWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceReceivedWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceReceivedWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceReceivedWebhookEventDataMessageVariant5Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["____MessageCommerceReceivedWebhookEventDataMessageVariant5OrderTotal"]


class ___MessageCommerceReceivedWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceReceivedWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceReceivedWebhookEventDataMessageVariant6Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceReceivedWebhookEventDataMessageVariant6ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceUpdatedWebhookEventDataMessageVariant1Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["____MessageCommerceUpdatedWebhookEventDataMessageVariant1ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class ___MessageCommerceUpdatedWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceUpdatedWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceUpdatedWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceUpdatedWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceUpdatedWebhookEventDataMessageVariant5Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["____MessageCommerceUpdatedWebhookEventDataMessageVariant5OrderTotal"]


class ___MessageCommerceUpdatedWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceUpdatedWebhookEventDataMessageVariant6Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceWebhookEventDataMessageVariant1Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["____MessageCommerceWebhookEventDataMessageVariant1ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class ___MessageCommerceWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceWebhookEventDataMessageVariant2Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["____MessageCommerceWebhookEventDataMessageVariant2OrderTotal"]


class ___MessageCommerceWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageCommerceWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageCommerceWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required[
        "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2(
    TypedDict, total=False
):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired[
        "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveHistoryWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant2InteractiveResponseVariant1(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant2InteractiveResponseVariant2(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant2InteractiveResponseVariant3(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveHistoryWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant3Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["____MessageInteractiveHistoryWebhookEventDataMessageVariant3ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveHistoryWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant4Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["____MessageInteractiveHistoryWebhookEventDataMessageVariant4OrderTotal"]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveHistoryWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveHistoryWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveHistoryWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant10Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant10ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2(
    TypedDict, total=False
):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant6Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant6ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant7InteractiveResponseVariant1(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant7InteractiveResponseVariant2(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant7InteractiveResponseVariant3(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant7Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant7ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant8Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant8ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveReceivedWebhookEventDataMessageVariant9Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveReceivedWebhookEventDataMessageVariant9ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant10Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant10ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2(
    TypedDict, total=False
):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant6Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant7InteractiveResponseVariant1(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant7InteractiveResponseVariant2(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant7InteractiveResponseVariant3(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant7Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant7ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant8Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant8ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveUpdatedWebhookEventDataMessageVariant9Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveUpdatedWebhookEventDataMessageVariant9ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required[
        "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2(
    TypedDict, total=False
):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired[
        "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageInteractiveWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveWebhookEventDataMessageVariant2InteractiveResponseVariant1(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class ___MessageInteractiveWebhookEventDataMessageVariant2InteractiveResponseVariant2(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class ___MessageInteractiveWebhookEventDataMessageVariant2InteractiveResponseVariant3(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


class ___MessageInteractiveWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveWebhookEventDataMessageVariant3Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["____MessageInteractiveWebhookEventDataMessageVariant3ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class ___MessageInteractiveWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveWebhookEventDataMessageVariant4Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["____MessageInteractiveWebhookEventDataMessageVariant4OrderTotal"]


class ___MessageInteractiveWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageInteractiveWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageInteractiveWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required[
        "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2(
    TypedDict, total=False
):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired[
        "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3InteractiveResponseVariant1(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3InteractiveResponseVariant2(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3InteractiveResponseVariant3(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant4Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["____MessageLinkPreviewHistoryWebhookEventDataMessageVariant4ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant5Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["____MessageLinkPreviewHistoryWebhookEventDataMessageVariant5OrderTotal"]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewHistoryWebhookEventDataMessageVariant6Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant6ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreview(
    TypedDict, total=False
):
    description: NotRequired[
        "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewDescription"
    ]
    image_url: NotRequired[
        "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewImageUrl"
    ]
    title: NotRequired[
        "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewTitle"
    ]
    url: Required["____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewUrl"]


class ___MessageLinkPreviewReceivedWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewReceivedWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewReceivedWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewReceivedWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewReceivedWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewReceivedWebhookEventDataMessageVariant6Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant6ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant10Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant10ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant11Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant11ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant12Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant12ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreview(
    TypedDict, total=False
):
    description: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewDescription"
    ]
    image_url: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewImageUrl"
    ]
    title: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewTitle"
    ]
    url: Required["____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewUrl"]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant6Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant7Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant7ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant8Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant8ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant9Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant9ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required[
        "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2(
    TypedDict, total=False
):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired[
        "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessageLinkPreviewWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewWebhookEventDataMessageVariant3InteractiveResponseVariant1(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class ___MessageLinkPreviewWebhookEventDataMessageVariant3InteractiveResponseVariant2(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class ___MessageLinkPreviewWebhookEventDataMessageVariant3InteractiveResponseVariant3(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


class ___MessageLinkPreviewWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewWebhookEventDataMessageVariant4Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["____MessageLinkPreviewWebhookEventDataMessageVariant4ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class ___MessageLinkPreviewWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewWebhookEventDataMessageVariant5Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["____MessageLinkPreviewWebhookEventDataMessageVariant5OrderTotal"]


class ___MessageLinkPreviewWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageLinkPreviewWebhookEventDataMessageVariant6Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageLinkPreviewWebhookEventDataMessageVariant6ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollHistoryWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollHistoryWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollHistoryWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollHistoryWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required[
        "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2(
    TypedDict, total=False
):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired[
        "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessagePollHistoryWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollHistoryWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollHistoryWebhookEventDataMessageVariant4InteractiveResponseVariant1(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class ___MessagePollHistoryWebhookEventDataMessageVariant4InteractiveResponseVariant2(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class ___MessagePollHistoryWebhookEventDataMessageVariant4InteractiveResponseVariant3(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


class ___MessagePollHistoryWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollHistoryWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollHistoryWebhookEventDataMessageVariant5Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["____MessagePollHistoryWebhookEventDataMessageVariant5ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class ___MessagePollHistoryWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollHistoryWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollHistoryWebhookEventDataMessageVariant6Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["____MessagePollHistoryWebhookEventDataMessageVariant6OrderTotal"]


class ___MessagePollHistoryWebhookEventDataMessageVariant6Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollHistoryWebhookEventDataMessageVariant6ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollHistoryWebhookEventDataMessageVariant7Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollHistoryWebhookEventDataMessageVariant7ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollReceivedWebhookEventDataMessageVariant1Poll(TypedDict, total=False):
    max_selections: Required[int]
    options: Required[list["MessagePollOption"]]
    question: Required[str]


class ___MessagePollReceivedWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollReceivedWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollReceivedWebhookEventDataMessageVariant1Sender(TypedDict, total=False):
    id: Required[str]
    name: NotRequired[str]
    type: NotRequired[Literal["user"]]


class ___MessagePollReceivedWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollReceivedWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required[
        "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2(
    TypedDict, total=False
):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired[
        "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4(
    TypedDict, total=False
):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired[
        "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4Header"
    ]
    kind: Required[Literal["buttons", "template"]]


class ___MessagePollReceivedWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollReceivedWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollReceivedWebhookEventDataMessageVariant4InteractiveResponseVariant1(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class ___MessagePollReceivedWebhookEventDataMessageVariant4InteractiveResponseVariant2(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class ___MessagePollReceivedWebhookEventDataMessageVariant4InteractiveResponseVariant3(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


class ___MessagePollReceivedWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollReceivedWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollReceivedWebhookEventDataMessageVariant5Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["____MessagePollReceivedWebhookEventDataMessageVariant5ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class ___MessagePollReceivedWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollReceivedWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollReceivedWebhookEventDataMessageVariant6Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["____MessagePollReceivedWebhookEventDataMessageVariant6OrderTotal"]


class ___MessagePollReceivedWebhookEventDataMessageVariant6Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollReceivedWebhookEventDataMessageVariant6ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollReceivedWebhookEventDataMessageVariant7Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollReceivedWebhookEventDataMessageVariant7ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollWebhookEventDataMessageVariant1Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollWebhookEventDataMessageVariant1ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollWebhookEventDataMessageVariant2Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollWebhookEventDataMessageVariant2ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollWebhookEventDataMessageVariant3InteractiveVariant1(TypedDict, total=False):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: Required["____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1Header"]
    kind: Required[Literal["buttons", "template"]]


class ___MessagePollWebhookEventDataMessageVariant3InteractiveVariant2(TypedDict, total=False):
    body: Required[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired["____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2Header"]
    kind: Required[Literal["buttons", "template"]]


class ___MessagePollWebhookEventDataMessageVariant3InteractiveVariant3(TypedDict, total=False):
    body: NotRequired[str]
    buttons: NotRequired[list["MessageInteractiveButton"]]
    footer: Required[str]
    header: NotRequired["____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3Header"]
    kind: Required[Literal["buttons", "template"]]


class ___MessagePollWebhookEventDataMessageVariant3InteractiveVariant4(TypedDict, total=False):
    body: NotRequired[str]
    buttons: Required[list["MessageInteractiveButton"]]
    footer: NotRequired[str]
    header: NotRequired["____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4Header"]
    kind: Required[Literal["buttons", "template"]]


class ___MessagePollWebhookEventDataMessageVariant3Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollWebhookEventDataMessageVariant3ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollWebhookEventDataMessageVariant4InteractiveResponseVariant1(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: Required[str]
    selected_index: NotRequired[int]
    title: NotRequired[str]


class ___MessagePollWebhookEventDataMessageVariant4InteractiveResponseVariant2(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: Required[int]
    title: NotRequired[str]


class ___MessagePollWebhookEventDataMessageVariant4InteractiveResponseVariant3(
    TypedDict, total=False
):
    kind: Required[Literal["button", "template_button"]]
    selected_id: NotRequired[str]
    selected_index: NotRequired[int]
    title: Required[str]


class ___MessagePollWebhookEventDataMessageVariant4Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollWebhookEventDataMessageVariant4ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollWebhookEventDataMessageVariant5Product(TypedDict, total=False):
    description: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    price: NotRequired["____MessagePollWebhookEventDataMessageVariant5ProductPrice"]
    title: NotRequired[str]
    url: NotRequired[str]


class ___MessagePollWebhookEventDataMessageVariant5Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollWebhookEventDataMessageVariant5ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollWebhookEventDataMessageVariant6Order(TypedDict, total=False):
    id: NotRequired[str]
    item_count: NotRequired[int]
    status: NotRequired[Literal["inquiry", "accepted", "declined"]]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    total: NotRequired["____MessagePollWebhookEventDataMessageVariant6OrderTotal"]


class ___MessagePollWebhookEventDataMessageVariant6Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollWebhookEventDataMessageVariant6ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessagePollWebhookEventDataMessageVariant7Referral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessagePollWebhookEventDataMessageVariant7ReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageReferralReceivedWebhookEventDataMessageReferral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageReferralReceivedWebhookEventDataMessageReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageReferralUpdatedWebhookEventDataMessageReferral(TypedDict, total=False):
    body: NotRequired[str]
    media_type: NotRequired[Literal["image", "video"]]
    media_url: NotRequired[str]
    provider_extensions: NotRequired[
        "____MessageReferralUpdatedWebhookEventDataMessageReferralProviderExtensions"
    ]
    source: NotRequired[Literal["ad"]]
    source_id: NotRequired[str]
    source_url: NotRequired[str]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]


class ___MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ___MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "____MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class ____MessageCommerceHistoryWebhookEventDataMessageVariant1ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageCommerceHistoryWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceHistoryWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceHistoryWebhookEventDataMessageVariant2OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageCommerceHistoryWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceHistoryWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceHistoryWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceHistoryWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceReceivedWebhookEventDataMessageVariant1ProductPrice(
    TypedDict, total=False
):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageCommerceReceivedWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceReceivedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceReceivedWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceReceivedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceReceivedWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceReceivedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceReceivedWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceReceivedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceReceivedWebhookEventDataMessageVariant5OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageCommerceReceivedWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceReceivedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceReceivedWebhookEventDataMessageVariant6ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceReceivedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceUpdatedWebhookEventDataMessageVariant1ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageCommerceUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceUpdatedWebhookEventDataMessageVariant5OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageCommerceUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceWebhookEventDataMessageVariant1ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageCommerceWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceWebhookEventDataMessageVariant2OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageCommerceWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageCommerceWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageCommerceWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant3ProductPrice(
    TypedDict, total=False
):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant4OrderTotal(
    TypedDict, total=False
):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveHistoryWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveHistoryWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant10ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant10ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant6ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant7ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant8ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant8ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveReceivedWebhookEventDataMessageVariant9ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveReceivedWebhookEventDataMessageVariant9ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant10ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant10ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant7ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant8ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant8ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveUpdatedWebhookEventDataMessageVariant9ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant9ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageInteractiveWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveWebhookEventDataMessageVariant3ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageInteractiveWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveWebhookEventDataMessageVariant4OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageInteractiveWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageInteractiveWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageInteractiveWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant4ProductPrice(
    TypedDict, total=False
):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant5OrderTotal(
    TypedDict, total=False
):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewHistoryWebhookEventDataMessageVariant6ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp"
    ]


____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewDescriptionVariant1: TypeAlias = Literal[
    ""
]


____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewDescriptionVariant2: TypeAlias = str


____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewImageUrl: TypeAlias = str


____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewTitleVariant1: TypeAlias = (
    Literal[""]
)


____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewTitleVariant2: TypeAlias = (
    str
)


____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewUrl: TypeAlias = str


class ____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewReceivedWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewReceivedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewReceivedWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewReceivedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewReceivedWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewReceivedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewReceivedWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewReceivedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewReceivedWebhookEventDataMessageVariant6ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewReceivedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant10ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant10ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant11ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant11ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant12ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant12ReferralProviderExtensionsWhatsapp"
    ]


____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewDescriptionVariant1: TypeAlias = Literal[
    ""
]


____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewDescriptionVariant2: TypeAlias = str


____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewImageUrl: TypeAlias = str


____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewTitleVariant1: TypeAlias = (
    Literal[""]
)


____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewTitleVariant2: TypeAlias = (
    str
)


____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewUrl: TypeAlias = str


class ____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant7ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant8ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant8ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant9ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant9ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessageLinkPreviewWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewWebhookEventDataMessageVariant4ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageLinkPreviewWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewWebhookEventDataMessageVariant5OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessageLinkPreviewWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageLinkPreviewWebhookEventDataMessageVariant6ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageLinkPreviewWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollHistoryWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollHistoryWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollHistoryWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollHistoryWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollHistoryWebhookEventDataMessageVariant5ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessagePollHistoryWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollHistoryWebhookEventDataMessageVariant6OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessagePollHistoryWebhookEventDataMessageVariant6ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollHistoryWebhookEventDataMessageVariant7ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollHistoryWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollReceivedWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollReceivedWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollReceivedWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollReceivedWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollReceivedWebhookEventDataMessageVariant5ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessagePollReceivedWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollReceivedWebhookEventDataMessageVariant6OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessagePollReceivedWebhookEventDataMessageVariant6ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollReceivedWebhookEventDataMessageVariant7ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollReceivedWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollWebhookEventDataMessageVariant1ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollWebhookEventDataMessageVariant2ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant1(
    TypedDict, total=False
):
    attachment: NotRequired[Never]
    text: Required[str]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4(
    TypedDict, total=False
):
    attachment: Required[
        "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4Attachment"
    ]
    text: NotRequired[Never]
    type: Required[Literal["text", "image", "video", "document"]]


class ____MessagePollWebhookEventDataMessageVariant3ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollWebhookEventDataMessageVariant4ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollWebhookEventDataMessageVariant5ProductPrice(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessagePollWebhookEventDataMessageVariant5ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollWebhookEventDataMessageVariant6OrderTotal(TypedDict, total=False):
    amount: NotRequired[str]
    currency: NotRequired[str]


class ____MessagePollWebhookEventDataMessageVariant6ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp"
    ]


class ____MessagePollWebhookEventDataMessageVariant7ReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessagePollWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp"
    ]


class ____MessageReferralReceivedWebhookEventDataMessageReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageReferralReceivedWebhookEventDataMessageReferralProviderExtensionsWhatsapp"
    ]


class ____MessageReferralUpdatedWebhookEventDataMessageReferralProviderExtensions(
    TypedDict, total=False
):
    whatsapp: Required[
        "_____MessageReferralUpdatedWebhookEventDataMessageReferralProviderExtensionsWhatsapp"
    ]


class ____MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ____MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class _____MessageCommerceHistoryWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceHistoryWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceHistoryWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceReceivedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceReceivedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceReceivedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceReceivedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceReceivedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceReceivedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageCommerceWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveHistoryWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant10ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant8ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveReceivedWebhookEventDataMessageVariant9ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant10ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant8ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveUpdatedWebhookEventDataMessageVariant9ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageInteractiveWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewHistoryWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewReceivedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewReceivedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewReceivedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewReceivedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewReceivedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant10ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant11ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant12ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant8ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant9ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageLinkPreviewWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollHistoryWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollReceivedWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4Attachment(
    TypedDict, total=False
):
    description: NotRequired[str]
    duration_ms: NotRequired[int]
    expired: NotRequired[bool]
    id: NotRequired[str]
    metadata: NotRequired[
        "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4AttachmentMetadata"
    ]
    mimetype: NotRequired[str]
    size: NotRequired[int]
    thumbnail_url: NotRequired[str]
    title: NotRequired[str]
    type: Required[Literal["image", "video", "document"]]
    url: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessagePollWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageReferralReceivedWebhookEventDataMessageReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class _____MessageReferralUpdatedWebhookEventDataMessageReferralProviderExtensionsWhatsapp(
    TypedDict, total=False
):
    automated_greeting_message_cta_type: NotRequired[str]
    automated_greeting_message_shown: NotRequired[bool]
    click_to_whatsapp_call: NotRequired[bool]
    contains_auto_reply: NotRequired[bool]
    contains_ctwa_flows_auto_reply: NotRequired[bool]
    ctwa_clid: NotRequired[str]
    greeting_message_body: NotRequired[str]
    source_app: NotRequired[str]


class ______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


class ______MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4AttachmentMetadata(
    TypedDict, total=False
):
    file_length: NotRequired[int]
    height: NotRequired[int]
    is_big_file: NotRequired[bool]
    size: NotRequired[int]
    width: NotRequired[int]


CallMessageCall: TypeAlias = Union["CallMessageCallVariant1", "CallMessageCallVariant2"]


ContactCreateRequest: TypeAlias = Union[
    "ContactCreateRequestVariant1", "ContactCreateRequestVariant2"
]


ConversationDisappearingMessagesState: TypeAlias = Union[
    "ConversationDisappearingMessagesStateVariant1", "ConversationDisappearingMessagesStateVariant2"
]


GroupUpdatedChange: TypeAlias = Union[
    "GroupUpdatedChangeVariant1", "GroupUpdatedChangeVariant2", "GroupUpdatedChangeVariant3"
]


MediaMessagePayload: TypeAlias = Union[
    "MediaMessagePayloadVariant1", "MediaMessagePayloadVariant2", "MediaMessagePayloadVariant3"
]


Mention: TypeAlias = Union["MentionVariant1", "MentionVariant2"]


MessageCommerce: TypeAlias = Union["MessageCommerceVariant1", "MessageCommerceVariant2"]


MessageContactCards: TypeAlias = Union["MessageContactCardsVariant1", "MessageContactCardsVariant2"]


MessageInteractive: TypeAlias = Union[
    "MessageInteractiveVariant1",
    "MessageInteractiveVariant2",
    "MessageInteractiveVariant3",
    "MessageInteractiveVariant4",
]


MessageInteractiveButton: TypeAlias = Union[
    "MessageInteractiveButtonVariant1",
    "MessageInteractiveButtonVariant2",
    "MessageInteractiveButtonVariant3",
    "MessageInteractiveButtonVariant4",
    "MessageInteractiveButtonVariant5",
    "MessageInteractiveButtonVariant6",
]


MessageInteractiveHeader: TypeAlias = Union[
    "MessageInteractiveHeaderVariant1",
    "MessageInteractiveHeaderVariant2",
    "MessageInteractiveHeaderVariant3",
    "MessageInteractiveHeaderVariant4",
]


MessageInteractiveMessage: TypeAlias = Union[
    "MessageInteractiveMessageVariant1", "MessageInteractiveMessageVariant2"
]


MessageInteractiveResponse: TypeAlias = Union[
    "MessageInteractiveResponseVariant1",
    "MessageInteractiveResponseVariant2",
    "MessageInteractiveResponseVariant3",
]


MessagePayload: TypeAlias = Union[
    "MessagePayloadVariant1",
    "MessagePayloadVariant2",
    "MessagePayloadVariant3",
    "MessagePayloadVariant4",
    "MessagePayloadVariant5",
    "MessagePayloadVariant6",
    "MessagePayloadVariant7",
    "MessagePayloadVariant8",
    "MessagePayloadVariant9",
    "MessagePayloadVariant10",
]


MessagePinState: TypeAlias = Union["MessagePinStateVariant1", "MessagePinStateVariant2"]


MessagePollVote: TypeAlias = Union["MessagePollVoteVariant1", "MessagePollVoteVariant2"]


MessageWithOptionalCommerce: TypeAlias = Union[
    "MessageWithOptionalCommerceVariant1",
    "MessageWithOptionalCommerceVariant2",
    "MessageWithOptionalCommerceVariant3",
]


MessageWithOptionalInteractive: TypeAlias = Union[
    "MessageWithOptionalInteractiveVariant1",
    "MessageWithOptionalInteractiveVariant2",
    "MessageWithOptionalInteractiveVariant3",
    "MessageWithOptionalInteractiveVariant4",
    "MessageWithOptionalInteractiveVariant5",
]


MessageWithOptionalLinkPreview: TypeAlias = Union[
    "MessageWithOptionalLinkPreviewVariant1",
    "MessageWithOptionalLinkPreviewVariant2",
    "MessageWithOptionalLinkPreviewVariant3",
    "MessageWithOptionalLinkPreviewVariant4",
    "MessageWithOptionalLinkPreviewVariant5",
    "MessageWithOptionalLinkPreviewVariant6",
]


MessageWithOptionalPoll: TypeAlias = Union[
    "MessageWithOptionalPollVariant1",
    "MessageWithOptionalPollVariant2",
    "MessageWithOptionalPollVariant3",
    "MessageWithOptionalPollVariant4",
    "MessageWithOptionalPollVariant5",
    "MessageWithOptionalPollVariant6",
    "MessageWithOptionalPollVariant7",
]


PostCommentListResult: TypeAlias = Union[
    "PostCommentListResultVariant1", "PostCommentListResultVariant2"
]


PostListResult: TypeAlias = Union["PostListResultVariant1", "PostListResultVariant2"]


StickerMessagePayload: TypeAlias = Union[
    "StickerMessagePayloadVariant1",
    "StickerMessagePayloadVariant2",
    "StickerMessagePayloadVariant3",
]


_CallEndedWebhookEventData: TypeAlias = Union[
    "_CallEndedWebhookEventDataVariant1", "_CallEndedWebhookEventDataVariant2"
]


_MessageInteractiveMessageVariant1Interactive: TypeAlias = Union[
    "_MessageInteractiveMessageVariant1InteractiveVariant1",
    "_MessageInteractiveMessageVariant1InteractiveVariant2",
    "_MessageInteractiveMessageVariant1InteractiveVariant3",
    "_MessageInteractiveMessageVariant1InteractiveVariant4",
]


_MessageInteractiveMessageVariant2InteractiveResponse: TypeAlias = Union[
    "_MessageInteractiveMessageVariant2InteractiveResponseVariant1",
    "_MessageInteractiveMessageVariant2InteractiveResponseVariant2",
    "_MessageInteractiveMessageVariant2InteractiveResponseVariant3",
]


_MessageLinkPreviewDescription: TypeAlias = Union[
    "_MessageLinkPreviewDescriptionVariant1", "_MessageLinkPreviewDescriptionVariant2"
]


_MessageLinkPreviewTitle: TypeAlias = Union[
    "_MessageLinkPreviewTitleVariant1", "_MessageLinkPreviewTitleVariant2"
]


_MessageWithOptionalInteractiveVariant1Interactive: TypeAlias = Union[
    "_MessageWithOptionalInteractiveVariant1InteractiveVariant1",
    "_MessageWithOptionalInteractiveVariant1InteractiveVariant2",
    "_MessageWithOptionalInteractiveVariant1InteractiveVariant3",
    "_MessageWithOptionalInteractiveVariant1InteractiveVariant4",
]


_MessageWithOptionalInteractiveVariant2InteractiveResponse: TypeAlias = Union[
    "_MessageWithOptionalInteractiveVariant2InteractiveResponseVariant1",
    "_MessageWithOptionalInteractiveVariant2InteractiveResponseVariant2",
    "_MessageWithOptionalInteractiveVariant2InteractiveResponseVariant3",
]


_MessageWithOptionalLinkPreviewVariant2Interactive: TypeAlias = Union[
    "_MessageWithOptionalLinkPreviewVariant2InteractiveVariant1",
    "_MessageWithOptionalLinkPreviewVariant2InteractiveVariant2",
    "_MessageWithOptionalLinkPreviewVariant2InteractiveVariant3",
    "_MessageWithOptionalLinkPreviewVariant2InteractiveVariant4",
]


_MessageWithOptionalLinkPreviewVariant3InteractiveResponse: TypeAlias = Union[
    "_MessageWithOptionalLinkPreviewVariant3InteractiveResponseVariant1",
    "_MessageWithOptionalLinkPreviewVariant3InteractiveResponseVariant2",
    "_MessageWithOptionalLinkPreviewVariant3InteractiveResponseVariant3",
]


_MessageWithOptionalPollVariant3Interactive: TypeAlias = Union[
    "_MessageWithOptionalPollVariant3InteractiveVariant1",
    "_MessageWithOptionalPollVariant3InteractiveVariant2",
    "_MessageWithOptionalPollVariant3InteractiveVariant3",
    "_MessageWithOptionalPollVariant3InteractiveVariant4",
]


_MessageWithOptionalPollVariant4InteractiveResponse: TypeAlias = Union[
    "_MessageWithOptionalPollVariant4InteractiveResponseVariant1",
    "_MessageWithOptionalPollVariant4InteractiveResponseVariant2",
    "_MessageWithOptionalPollVariant4InteractiveResponseVariant3",
]


__MessageCommerceHistoryWebhookEventDataMessage: TypeAlias = Union[
    "__MessageCommerceHistoryWebhookEventDataMessageVariant1",
    "__MessageCommerceHistoryWebhookEventDataMessageVariant2",
    "__MessageCommerceHistoryWebhookEventDataMessageVariant3",
]


__MessageCommerceReceivedWebhookEventDataMessage: TypeAlias = Union[
    "__MessageCommerceReceivedWebhookEventDataMessageVariant1",
    "__MessageCommerceReceivedWebhookEventDataMessageVariant2",
    "__MessageCommerceReceivedWebhookEventDataMessageVariant3",
    "__MessageCommerceReceivedWebhookEventDataMessageVariant4",
    "__MessageCommerceReceivedWebhookEventDataMessageVariant5",
    "__MessageCommerceReceivedWebhookEventDataMessageVariant6",
]


__MessageCommerceUpdatedWebhookEventDataMessage: TypeAlias = Union[
    "__MessageCommerceUpdatedWebhookEventDataMessageVariant1",
    "__MessageCommerceUpdatedWebhookEventDataMessageVariant2",
    "__MessageCommerceUpdatedWebhookEventDataMessageVariant3",
    "__MessageCommerceUpdatedWebhookEventDataMessageVariant4",
    "__MessageCommerceUpdatedWebhookEventDataMessageVariant5",
    "__MessageCommerceUpdatedWebhookEventDataMessageVariant6",
]


__MessageCommerceWebhookEventDataMessage: TypeAlias = Union[
    "__MessageCommerceWebhookEventDataMessageVariant1",
    "__MessageCommerceWebhookEventDataMessageVariant2",
    "__MessageCommerceWebhookEventDataMessageVariant3",
]


__MessageContactCardsReceivedWebhookEventDataMessage: TypeAlias = Union[
    "__MessageContactCardsReceivedWebhookEventDataMessageVariant1",
    "__MessageContactCardsReceivedWebhookEventDataMessageVariant2",
]


__MessageContactCardsUpdatedWebhookEventDataMessage: TypeAlias = Union[
    "__MessageContactCardsUpdatedWebhookEventDataMessageVariant1",
    "__MessageContactCardsUpdatedWebhookEventDataMessageVariant2",
]


__MessageInteractiveHistoryWebhookEventDataMessage: TypeAlias = Union[
    "__MessageInteractiveHistoryWebhookEventDataMessageVariant1",
    "__MessageInteractiveHistoryWebhookEventDataMessageVariant2",
    "__MessageInteractiveHistoryWebhookEventDataMessageVariant3",
    "__MessageInteractiveHistoryWebhookEventDataMessageVariant4",
    "__MessageInteractiveHistoryWebhookEventDataMessageVariant5",
]


__MessageInteractiveMessageVariant1InteractiveVariant1Header: TypeAlias = Union[
    "__MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant1",
    "__MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant2",
    "__MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant3",
    "__MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant4",
]


__MessageInteractiveMessageVariant1InteractiveVariant2Header: TypeAlias = Union[
    "__MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant1",
    "__MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant2",
    "__MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant3",
    "__MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant4",
]


__MessageInteractiveMessageVariant1InteractiveVariant3Header: TypeAlias = Union[
    "__MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant1",
    "__MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant2",
    "__MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant3",
    "__MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant4",
]


__MessageInteractiveMessageVariant1InteractiveVariant4Header: TypeAlias = Union[
    "__MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant1",
    "__MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant2",
    "__MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant3",
    "__MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant4",
]


__MessageInteractiveReceivedWebhookEventDataMessage: TypeAlias = Union[
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant1",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant2",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant3",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant4",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant5",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant6",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant7",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant8",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant9",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant10",
]


__MessageInteractiveUpdatedWebhookEventDataMessage: TypeAlias = Union[
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant1",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant2",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant3",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant4",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant5",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant6",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant7",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant8",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant9",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant10",
]


__MessageInteractiveWebhookEventDataMessage: TypeAlias = Union[
    "__MessageInteractiveWebhookEventDataMessageVariant1",
    "__MessageInteractiveWebhookEventDataMessageVariant2",
    "__MessageInteractiveWebhookEventDataMessageVariant3",
    "__MessageInteractiveWebhookEventDataMessageVariant4",
    "__MessageInteractiveWebhookEventDataMessageVariant5",
]


__MessageLinkPreviewHistoryWebhookEventDataMessage: TypeAlias = Union[
    "__MessageLinkPreviewHistoryWebhookEventDataMessageVariant1",
    "__MessageLinkPreviewHistoryWebhookEventDataMessageVariant2",
    "__MessageLinkPreviewHistoryWebhookEventDataMessageVariant3",
    "__MessageLinkPreviewHistoryWebhookEventDataMessageVariant4",
    "__MessageLinkPreviewHistoryWebhookEventDataMessageVariant5",
    "__MessageLinkPreviewHistoryWebhookEventDataMessageVariant6",
]


__MessageLinkPreviewReceivedWebhookEventDataMessage: TypeAlias = Union[
    "__MessageLinkPreviewReceivedWebhookEventDataMessageVariant1",
    "__MessageLinkPreviewReceivedWebhookEventDataMessageVariant2",
    "__MessageLinkPreviewReceivedWebhookEventDataMessageVariant3",
    "__MessageLinkPreviewReceivedWebhookEventDataMessageVariant4",
    "__MessageLinkPreviewReceivedWebhookEventDataMessageVariant5",
    "__MessageLinkPreviewReceivedWebhookEventDataMessageVariant6",
]


__MessageLinkPreviewUpdatedWebhookEventDataMessage: TypeAlias = Union[
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant2",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant3",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant4",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant5",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant6",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant7",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant8",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant9",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant10",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant11",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant12",
]


__MessageLinkPreviewWebhookEventDataMessage: TypeAlias = Union[
    "__MessageLinkPreviewWebhookEventDataMessageVariant1",
    "__MessageLinkPreviewWebhookEventDataMessageVariant2",
    "__MessageLinkPreviewWebhookEventDataMessageVariant3",
    "__MessageLinkPreviewWebhookEventDataMessageVariant4",
    "__MessageLinkPreviewWebhookEventDataMessageVariant5",
    "__MessageLinkPreviewWebhookEventDataMessageVariant6",
]


__MessagePollHistoryWebhookEventDataMessage: TypeAlias = Union[
    "__MessagePollHistoryWebhookEventDataMessageVariant1",
    "__MessagePollHistoryWebhookEventDataMessageVariant2",
    "__MessagePollHistoryWebhookEventDataMessageVariant3",
    "__MessagePollHistoryWebhookEventDataMessageVariant4",
    "__MessagePollHistoryWebhookEventDataMessageVariant5",
    "__MessagePollHistoryWebhookEventDataMessageVariant6",
    "__MessagePollHistoryWebhookEventDataMessageVariant7",
]


__MessagePollReceivedWebhookEventDataMessage: TypeAlias = Union[
    "__MessagePollReceivedWebhookEventDataMessageVariant1",
    "__MessagePollReceivedWebhookEventDataMessageVariant2",
    "__MessagePollReceivedWebhookEventDataMessageVariant3",
    "__MessagePollReceivedWebhookEventDataMessageVariant4",
    "__MessagePollReceivedWebhookEventDataMessageVariant5",
    "__MessagePollReceivedWebhookEventDataMessageVariant6",
    "__MessagePollReceivedWebhookEventDataMessageVariant7",
]


__MessagePollWebhookEventDataMessage: TypeAlias = Union[
    "__MessagePollWebhookEventDataMessageVariant1",
    "__MessagePollWebhookEventDataMessageVariant2",
    "__MessagePollWebhookEventDataMessageVariant3",
    "__MessagePollWebhookEventDataMessageVariant4",
    "__MessagePollWebhookEventDataMessageVariant5",
    "__MessagePollWebhookEventDataMessageVariant6",
    "__MessagePollWebhookEventDataMessageVariant7",
]


__MessageWithOptionalInteractiveVariant1InteractiveVariant1Header: TypeAlias = Union[
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant1",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant2",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant3",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant4",
]


__MessageWithOptionalInteractiveVariant1InteractiveVariant2Header: TypeAlias = Union[
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant1",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant2",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant3",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant4",
]


__MessageWithOptionalInteractiveVariant1InteractiveVariant3Header: TypeAlias = Union[
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant1",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant2",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant3",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant4",
]


__MessageWithOptionalInteractiveVariant1InteractiveVariant4Header: TypeAlias = Union[
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant1",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant2",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant3",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant4",
]


__MessageWithOptionalLinkPreviewVariant2InteractiveVariant1Header: TypeAlias = Union[
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant1",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant2",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant3",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant4",
]


__MessageWithOptionalLinkPreviewVariant2InteractiveVariant2Header: TypeAlias = Union[
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant1",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant2",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant3",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant4",
]


__MessageWithOptionalLinkPreviewVariant2InteractiveVariant3Header: TypeAlias = Union[
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant1",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant2",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant3",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant4",
]


__MessageWithOptionalLinkPreviewVariant2InteractiveVariant4Header: TypeAlias = Union[
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant1",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant2",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant3",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant4",
]


__MessageWithOptionalPollVariant3InteractiveVariant1Header: TypeAlias = Union[
    "__MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant1",
    "__MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant2",
    "__MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant3",
    "__MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant4",
]


__MessageWithOptionalPollVariant3InteractiveVariant2Header: TypeAlias = Union[
    "__MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant1",
    "__MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant2",
    "__MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant3",
    "__MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant4",
]


__MessageWithOptionalPollVariant3InteractiveVariant3Header: TypeAlias = Union[
    "__MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant1",
    "__MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant2",
    "__MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant3",
    "__MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant4",
]


__MessageWithOptionalPollVariant3InteractiveVariant4Header: TypeAlias = Union[
    "__MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant1",
    "__MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant2",
    "__MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant3",
    "__MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant4",
]


___CallMessageUpdatedWebhookEventDataMessageCall: TypeAlias = Union[
    "___CallMessageUpdatedWebhookEventDataMessageCallVariant1",
    "___CallMessageUpdatedWebhookEventDataMessageCallVariant2",
    "___CallMessageUpdatedWebhookEventDataMessageCallVariant3",
    "___CallMessageUpdatedWebhookEventDataMessageCallVariant4",
]


___MessageInteractiveHistoryWebhookEventDataMessageVariant1Interactive: TypeAlias = Union[
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4",
]


___MessageInteractiveHistoryWebhookEventDataMessageVariant2InteractiveResponse: TypeAlias = Union[
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant2InteractiveResponseVariant1",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant2InteractiveResponseVariant2",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant2InteractiveResponseVariant3",
]


___MessageInteractiveReceivedWebhookEventDataMessageVariant1Interactive: TypeAlias = Union[
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4",
]


___MessageInteractiveReceivedWebhookEventDataMessageVariant7InteractiveResponse: TypeAlias = Union[
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant7InteractiveResponseVariant1",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant7InteractiveResponseVariant2",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant7InteractiveResponseVariant3",
]


___MessageInteractiveUpdatedWebhookEventDataMessageVariant1Interactive: TypeAlias = Union[
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4",
]


___MessageInteractiveUpdatedWebhookEventDataMessageVariant7InteractiveResponse: TypeAlias = Union[
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant7InteractiveResponseVariant1",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant7InteractiveResponseVariant2",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant7InteractiveResponseVariant3",
]


___MessageInteractiveWebhookEventDataMessageVariant1Interactive: TypeAlias = Union[
    "___MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1",
    "___MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2",
    "___MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3",
    "___MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4",
]


___MessageInteractiveWebhookEventDataMessageVariant2InteractiveResponse: TypeAlias = Union[
    "___MessageInteractiveWebhookEventDataMessageVariant2InteractiveResponseVariant1",
    "___MessageInteractiveWebhookEventDataMessageVariant2InteractiveResponseVariant2",
    "___MessageInteractiveWebhookEventDataMessageVariant2InteractiveResponseVariant3",
]


___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2Interactive: TypeAlias = Union[
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4",
]


___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3InteractiveResponse: TypeAlias = Union[
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3InteractiveResponseVariant1",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3InteractiveResponseVariant2",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3InteractiveResponseVariant3",
]


___MessageLinkPreviewWebhookEventDataMessageVariant2Interactive: TypeAlias = Union[
    "___MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1",
    "___MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2",
    "___MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3",
    "___MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4",
]


___MessageLinkPreviewWebhookEventDataMessageVariant3InteractiveResponse: TypeAlias = Union[
    "___MessageLinkPreviewWebhookEventDataMessageVariant3InteractiveResponseVariant1",
    "___MessageLinkPreviewWebhookEventDataMessageVariant3InteractiveResponseVariant2",
    "___MessageLinkPreviewWebhookEventDataMessageVariant3InteractiveResponseVariant3",
]


___MessagePollHistoryWebhookEventDataMessageVariant3Interactive: TypeAlias = Union[
    "___MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1",
    "___MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2",
    "___MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3",
    "___MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4",
]


___MessagePollHistoryWebhookEventDataMessageVariant4InteractiveResponse: TypeAlias = Union[
    "___MessagePollHistoryWebhookEventDataMessageVariant4InteractiveResponseVariant1",
    "___MessagePollHistoryWebhookEventDataMessageVariant4InteractiveResponseVariant2",
    "___MessagePollHistoryWebhookEventDataMessageVariant4InteractiveResponseVariant3",
]


___MessagePollReceivedWebhookEventDataMessageVariant3Interactive: TypeAlias = Union[
    "___MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1",
    "___MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2",
    "___MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3",
    "___MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4",
]


___MessagePollReceivedWebhookEventDataMessageVariant4InteractiveResponse: TypeAlias = Union[
    "___MessagePollReceivedWebhookEventDataMessageVariant4InteractiveResponseVariant1",
    "___MessagePollReceivedWebhookEventDataMessageVariant4InteractiveResponseVariant2",
    "___MessagePollReceivedWebhookEventDataMessageVariant4InteractiveResponseVariant3",
]


___MessagePollWebhookEventDataMessageVariant3Interactive: TypeAlias = Union[
    "___MessagePollWebhookEventDataMessageVariant3InteractiveVariant1",
    "___MessagePollWebhookEventDataMessageVariant3InteractiveVariant2",
    "___MessagePollWebhookEventDataMessageVariant3InteractiveVariant3",
    "___MessagePollWebhookEventDataMessageVariant3InteractiveVariant4",
]


___MessagePollWebhookEventDataMessageVariant4InteractiveResponse: TypeAlias = Union[
    "___MessagePollWebhookEventDataMessageVariant4InteractiveResponseVariant1",
    "___MessagePollWebhookEventDataMessageVariant4InteractiveResponseVariant2",
    "___MessagePollWebhookEventDataMessageVariant4InteractiveResponseVariant3",
]


____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1Header: TypeAlias = Union[
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant1",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4",
]


____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2Header: TypeAlias = Union[
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant1",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4",
]


____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3Header: TypeAlias = Union[
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant1",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4",
]


____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4Header: TypeAlias = Union[
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant1",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4",
]


____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1Header: TypeAlias = Union[
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant1",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4",
]


____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2Header: TypeAlias = Union[
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant1",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4",
]


____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3Header: TypeAlias = Union[
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant1",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4",
]


____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4Header: TypeAlias = Union[
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant1",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4",
]


____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1Header: TypeAlias = Union[
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant1",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4",
]


____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2Header: TypeAlias = Union[
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant1",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4",
]


____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3Header: TypeAlias = Union[
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant1",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4",
]


____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4Header: TypeAlias = Union[
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant1",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4",
]


____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1Header: TypeAlias = Union[
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant1",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4",
]


____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2Header: TypeAlias = Union[
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant1",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4",
]


____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3Header: TypeAlias = Union[
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant1",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4",
]


____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4Header: TypeAlias = Union[
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant1",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4",
]


____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1Header: TypeAlias = Union[
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant1",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4",
]


____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2Header: TypeAlias = Union[
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant1",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4",
]


____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3Header: TypeAlias = Union[
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant1",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4",
]


____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4Header: TypeAlias = Union[
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant1",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4",
]


____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewDescription: TypeAlias = Union[
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewDescriptionVariant1",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewDescriptionVariant2",
]


____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewTitle: TypeAlias = Union[
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewTitleVariant1",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewTitleVariant2",
]


____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewDescription: TypeAlias = Union[
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewDescriptionVariant1",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewDescriptionVariant2",
]


____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewTitle: TypeAlias = Union[
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewTitleVariant1",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewTitleVariant2",
]


____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1Header: TypeAlias = Union[
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant1",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4",
]


____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2Header: TypeAlias = Union[
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant1",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4",
]


____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3Header: TypeAlias = Union[
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant1",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4",
]


____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4Header: TypeAlias = Union[
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant1",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4",
]


____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1Header: TypeAlias = Union[
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant1",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4",
]


____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2Header: TypeAlias = Union[
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant1",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4",
]


____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3Header: TypeAlias = Union[
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant1",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4",
]


____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4Header: TypeAlias = Union[
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant1",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4",
]


____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1Header: TypeAlias = Union[
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant1",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4",
]


____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2Header: TypeAlias = Union[
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant1",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4",
]


____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3Header: TypeAlias = Union[
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant1",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4",
]


____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4Header: TypeAlias = Union[
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant1",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4",
]


____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1Header: TypeAlias = Union[
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant1",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4",
]


____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2Header: TypeAlias = Union[
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant1",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4",
]


____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3Header: TypeAlias = Union[
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant1",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4",
]


____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4Header: TypeAlias = Union[
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant1",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4",
]


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


CheckAccountQrAuthResponse: TypeAlias = ResponseEnvelope[QRAuthCheckData]


class ConfirmAccountPasskeyPath(TypedDict, total=False):
    account_id: Required[str]


class ConfirmAccountPasskeyQuery(TypedDict, total=False):
    pass


ConfirmAccountPasskeyRequestBody: TypeAlias = None


ConfirmAccountPasskeyResponse: TypeAlias = ResponseEnvelope[FreeFormObject]


class CreateAccountPath(TypedDict, total=False):
    pass


class CreateAccountQuery(TypedDict, total=False):
    pass


CreateAccountRequestBody: TypeAlias = AccountCreateRequest


CreateAccountResponse: TypeAlias = ResponseEnvelope[Account]


class CreateAccountAuthSessionPath(TypedDict, total=False):
    account_id: Required[str]


class CreateAccountAuthSessionQuery(TypedDict, total=False):
    pass


CreateAccountAuthSessionRequestBody: TypeAlias = None


CreateAccountAuthSessionResponse: TypeAlias = ResponseEnvelope[ProviderAuthSession]


class CreateApiKeyPath(TypedDict, total=False):
    pass


class CreateApiKeyQuery(TypedDict, total=False):
    pass


CreateApiKeyRequestBody: TypeAlias = APIKeyCreateRequest


CreateApiKeyResponse: TypeAlias = ResponseEnvelope[APIKeyCreateResult]


class CreateCallPath(TypedDict, total=False):
    pass


class CreateCallQuery(TypedDict, total=False):
    pass


CreateCallRequestBody: TypeAlias = CreateCallRequest


CreateCallResponse: TypeAlias = ResponseEnvelope[CreateCallData]


class CreateContactPath(TypedDict, total=False):
    account_id: Required[str]


class CreateContactQuery(TypedDict, total=False):
    pass


CreateContactRequestBody: TypeAlias = ContactCreateRequest


CreateContactResponse: TypeAlias = ResponseEnvelope[Contact]


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
    account_id: NotRequired[str]


DeactivateWebhookEndpointRequestBody: TypeAlias = None


DeactivateWebhookEndpointResponse: TypeAlias = ResponseEnvelope[WebhookEndpoint]


class DeleteAccountPath(TypedDict, total=False):
    account_id: Required[str]


class DeleteAccountQuery(TypedDict, total=False):
    pass


DeleteAccountRequestBody: TypeAlias = None


DeleteAccountResponse: TypeAlias = ResponseEnvelope[AccountOperation] | None


class DeleteConversationLabelPath(TypedDict, total=False):
    account_id: Required[str]


class DeleteConversationLabelQuery(TypedDict, total=False):
    pass


DeleteConversationLabelRequestBody: TypeAlias = ConversationLabelDeleteRequest


DeleteConversationLabelResponse: TypeAlias = ResponseEnvelope[ConversationLabelDeleteResult]


class DeleteWebhookEndpointPath(TypedDict, total=False):
    endpoint_id: Required[str]


class DeleteWebhookEndpointQuery(TypedDict, total=False):
    account_id: NotRequired[str]


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


class GetAccountOperationPath(TypedDict, total=False):
    operation_id: Required[str]


class GetAccountOperationQuery(TypedDict, total=False):
    pass


GetAccountOperationRequestBody: TypeAlias = None


GetAccountOperationResponse: TypeAlias = ResponseEnvelope[AccountOperation]


class GetActiveCallPath(TypedDict, total=False):
    pass


class GetActiveCallQuery(TypedDict, total=False):
    account_id: Required[str]


GetActiveCallRequestBody: TypeAlias = None


GetActiveCallResponse: TypeAlias = ResponseEnvelope[ActiveCallData | dict[str, JsonValue]]


class GetContactPath(TypedDict, total=False):
    account_id: Required[str]


class GetContactQuery(TypedDict, total=False):
    contact_id: Required[str]


GetContactRequestBody: TypeAlias = None


GetContactResponse: TypeAlias = ResponseEnvelope[Contact]


class GetContactMembershipPath(TypedDict, total=False):
    account_id: Required[str]


class GetContactMembershipQuery(TypedDict, total=False):
    contact_id: Required[str]


GetContactMembershipRequestBody: TypeAlias = None


GetContactMembershipResponse: TypeAlias = ResponseEnvelope[ContactMembership]


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


class GetPostPath(TypedDict, total=False):
    account_id: Required[str]


class GetPostQuery(TypedDict, total=False):
    pass


GetPostRequestBody: TypeAlias = PostInfoRequest


GetPostResponse: TypeAlias = ResponseEnvelope[Post]


class GetWebhookEndpointPath(TypedDict, total=False):
    endpoint_id: Required[str]


class GetWebhookEndpointQuery(TypedDict, total=False):
    account_id: NotRequired[str]


GetWebhookEndpointRequestBody: TypeAlias = None


GetWebhookEndpointResponse: TypeAlias = ResponseEnvelope[WebhookEndpoint]


class GetWorkspacePath(TypedDict, total=False):
    pass


class GetWorkspaceQuery(TypedDict, total=False):
    pass


GetWorkspaceRequestBody: TypeAlias = None


GetWorkspaceResponse: TypeAlias = ResponseEnvelope[Workspace]


class HangupCallPath(TypedDict, total=False):
    call_id: Required[str]


class HangupCallQuery(TypedDict, total=False):
    pass


HangupCallRequestBody: TypeAlias = dict[str, JsonValue]


HangupCallResponse: TypeAlias = ResponseEnvelope[EndedCallData]


class ImportAccountAuthSessionPath(TypedDict, total=False):
    account_id: Required[str]


class ImportAccountAuthSessionQuery(TypedDict, total=False):
    pass


ImportAccountAuthSessionRequestBody: TypeAlias = SessionImportRequest


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
    limit: NotRequired[int]
    cursor: NotRequired[str]


ListAccountsRequestBody: TypeAlias = None


ListAccountsResponse: TypeAlias = ResponseEnvelope[AccountListResult]


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


class ListPostCommentsPath(TypedDict, total=False):
    account_id: Required[str]


class ListPostCommentsQuery(TypedDict, total=False):
    pass


ListPostCommentsRequestBody: TypeAlias = PostCommentListRequest


ListPostCommentsResponse: TypeAlias = ResponseEnvelope[PostCommentListResult]


class ListPostsPath(TypedDict, total=False):
    account_id: Required[str]


class ListPostsQuery(TypedDict, total=False):
    cursor: NotRequired[str]
    limit: NotRequired[int]


ListPostsRequestBody: TypeAlias = None


ListPostsResponse: TypeAlias = ResponseEnvelope[PostListResult]


class ListProviderRegionsPath(TypedDict, total=False):
    provider: Required[ProviderInputName]


class ListProviderRegionsQuery(TypedDict, total=False):
    pass


ListProviderRegionsRequestBody: TypeAlias = None


ListProviderRegionsResponse: TypeAlias = ResponseEnvelope[ProviderRegionsResponse]


class ListWebhookEndpointsPath(TypedDict, total=False):
    pass


class ListWebhookEndpointsQuery(TypedDict, total=False):
    account_id: NotRequired[str]


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


class ReplyPostCommentPath(TypedDict, total=False):
    account_id: Required[str]


class ReplyPostCommentQuery(TypedDict, total=False):
    pass


ReplyPostCommentRequestBody: TypeAlias = PostCommentReplyRequest


ReplyPostCommentResponse: TypeAlias = ResponseEnvelope[PostCommentReplyResult]


class RequestConversationHistoryPath(TypedDict, total=False):
    account_id: Required[str]


class RequestConversationHistoryQuery(TypedDict, total=False):
    pass


RequestConversationHistoryRequestBody: TypeAlias = ConversationHistoryRequest


RequestConversationHistoryResponse: TypeAlias = ResponseEnvelope[ConversationHistoryAccepted]


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


StartAccountAuthResponse: TypeAlias = ResponseEnvelope[StartCodeAuthData]


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


class SubmitAccountPasskeyResponsePath(TypedDict, total=False):
    account_id: Required[str]


class SubmitAccountPasskeyResponseQuery(TypedDict, total=False):
    pass


SubmitAccountPasskeyResponseRequestBody: TypeAlias = PasskeyResponseRequest


SubmitAccountPasskeyResponseResponse: TypeAlias = ResponseEnvelope[FreeFormObject]


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


UpdateAccountRequestBody: TypeAlias = AccountUpdateRequest


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
    "AccountBilling",
    "AccountCreateRequest",
    "AccountListResult",
    "AccountOperation",
    "AccountProfileUpdatedWebhookEvent",
    "AccountSession",
    "AccountStartedWebhookEvent",
    "AccountUpdateRequest",
    "AccountWebhookError",
    "ActiveCallData",
    "AuthField",
    "CallAnsweredWebhookEvent",
    "CallEndedWebhookEvent",
    "CallEventCall",
    "CallEventSender",
    "CallIncomingWebhookEvent",
    "CallMessage",
    "CallMessageCall",
    "CallMessageReceivedWebhookEvent",
    "CallMessageUpdatedWebhookEvent",
    "CallMessageWebhookEvent",
    "Contact",
    "ContactAddressBook",
    "ContactBlocklistResult",
    "ContactCard",
    "ContactCreateRequest",
    "ContactEmail",
    "ContactExtra",
    "ContactIdRequest",
    "ContactListResult",
    "ContactMembership",
    "ContactMessagePayload",
    "ContactNoteRequest",
    "ContactPhone",
    "ContactUpdateChange",
    "ContactUpdateReference",
    "ContactUpdatedData",
    "ContactUpdatedWebhookEvent",
    "Conversation",
    "ConversationDisappearingMessagesChange",
    "ConversationDisappearingMessagesState",
    "ConversationDisappearingMessagesUpdatedWebhookEvent",
    "ConversationHistoryAccepted",
    "ConversationHistoryBefore",
    "ConversationHistoryMessage",
    "ConversationHistoryRequest",
    "ConversationHistorySource",
    "ConversationHistoryWebhookEvent",
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
    "ConversationStateAccount",
    "ConversationStateActor",
    "ConversationStateReference",
    "ConversationType",
    "CreateCallData",
    "CreateCallRequest",
    "EndedCallData",
    "Error",
    "ErrorEnvelope",
    "FreeFormObject",
    "Group",
    "GroupAnnouncementChange",
    "GroupCreateRequest",
    "GroupCreateResult",
    "GroupIdRequest",
    "GroupInfoUpdateRequest",
    "GroupInviteCode",
    "GroupInviteLinkChange",
    "GroupJoinApprovalModeRequest",
    "GroupJoinRequest",
    "GroupJoinRequestsResult",
    "GroupJoinRequestsUpdateRequest",
    "GroupListResult",
    "GroupMemberUpdateRequest",
    "GroupPermissions",
    "GroupSettingsEvent",
    "GroupSettingsUpdatedWebhookEvent",
    "GroupUpdatedChange",
    "LinkPreviewMessagePayload",
    "MediaMessagePayload",
    "Mention",
    "MessageCommerce",
    "MessageCommerceHTTPURL",
    "MessageCommerceHistoryWebhookEvent",
    "MessageCommerceMoney",
    "MessageCommerceReceivedWebhookEvent",
    "MessageCommerceUpdatedWebhookEvent",
    "MessageCommerceWebhookEvent",
    "MessageContactCards",
    "MessageContactCardsHistoryWebhookEvent",
    "MessageContactCardsReceivedWebhookEvent",
    "MessageContactCardsUpdatedWebhookEvent",
    "MessageEditRequest",
    "MessageInteractive",
    "MessageInteractiveAttachment",
    "MessageInteractiveAttachmentMetadata",
    "MessageInteractiveButton",
    "MessageInteractiveHeader",
    "MessageInteractiveHistoryWebhookEvent",
    "MessageInteractiveMessage",
    "MessageInteractiveReceivedWebhookEvent",
    "MessageInteractiveResponse",
    "MessageInteractiveUpdatedWebhookEvent",
    "MessageInteractiveWebhookEvent",
    "MessageLinkPreview",
    "MessageLinkPreviewHTTPURL",
    "MessageLinkPreviewHistoryWebhookEvent",
    "MessageLinkPreviewMessage",
    "MessageLinkPreviewReceivedWebhookEvent",
    "MessageLinkPreviewTextUpdate",
    "MessageLinkPreviewUpdatedWebhookEvent",
    "MessageLinkPreviewWebhookEvent",
    "MessageLiveLocation",
    "MessageLiveLocationHistoryWebhookEvent",
    "MessageLiveLocationReceivedWebhookEvent",
    "MessageLiveLocationUpdatedWebhookEvent",
    "MessageOrder",
    "MessagePayload",
    "MessagePinChange",
    "MessagePinMessage",
    "MessagePinParticipant",
    "MessagePinRequest",
    "MessagePinState",
    "MessagePinUpdatedWebhookEvent",
    "MessagePoll",
    "MessagePollHistoryWebhookEvent",
    "MessagePollMessage",
    "MessagePollOption",
    "MessagePollReceivedWebhookEvent",
    "MessagePollVote",
    "MessagePollVoteChange",
    "MessagePollVoteMessage",
    "MessagePollVoteUpdatedWebhookEvent",
    "MessagePollWebhookEvent",
    "MessageProduct",
    "MessageReactionRequest",
    "MessageReferral",
    "MessageReferralHistoryWebhookEvent",
    "MessageReferralProviderExtensions",
    "MessageReferralReceivedWebhookEvent",
    "MessageReferralUpdatedWebhookEvent",
    "MessageReferralWebhookEvent",
    "MessageRevokeRequest",
    "MessageTargetRequest",
    "MessageWithOptionalCommerce",
    "MessageWithOptionalContactCards",
    "MessageWithOptionalInteractive",
    "MessageWithOptionalLinkPreview",
    "MessageWithOptionalLiveLocation",
    "MessageWithOptionalPoll",
    "MessageWithOptionalReferral",
    "OkData",
    "PasskeyResponseRequest",
    "PollMessagePayload",
    "Post",
    "PostAuthor",
    "PostComment",
    "PostCommentCreatedWebhookEvent",
    "PostCommentListRequest",
    "PostCommentListResult",
    "PostCommentReplyRequest",
    "PostCommentReplyResult",
    "PostInfoRequest",
    "PostListResult",
    "PostResourceID",
    "ProviderAuthSession",
    "ProviderInputName",
    "ProviderName",
    "ProviderProfile",
    "ProviderRegionsResponse",
    "QRAuthCheckData",
    "QRAuthCheckPayload",
    "ReceivedContactCard",
    "Recipient",
    "RegionAvailability",
    "ReplyTo",
    "ResponseMeta",
    "RuntimeActionResult",
    "RuntimeStatus",
    "SendMessageLinkPreview",
    "SendMessagePoll",
    "SendMessagePollOption",
    "SendMessageProviderData",
    "SendMessageRequest",
    "SendMessageResult",
    "SessionImportRequest",
    "StandardEventType",
    "StartCodeAuthData",
    "StickerMessagePayload",
    "TextMessagePayload",
    "WebhookEndpoint",
    "WebhookEndpointRequest",
    "WhatsAppAccountAuthFailedWebhookEvent",
    "WhatsAppContactCreateOptions",
    "WhatsAppDeviceID",
    "WhatsAppMessageDeviceSender",
    "WhatsAppMessageDeviceWebhookEvent",
    "WhatsAppMessageReferralExtension",
    "WhatsAppProtocolSessionImportParams",
    "Workspace",
    "WorkspaceStatus",
    "WorkspaceUpdateRequest",
)


DEPENDENT_REQUIRED: Final[MappingProxyType[str, MappingProxyType[str, tuple[str, ...]]]] = (
    MappingProxyType({})
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
    "AccountBilling",
    "AccountCreateRequest",
    "AccountListResult",
    "AccountOperation",
    "AccountProfileUpdatedWebhookEvent",
    "AccountSession",
    "AccountStartedWebhookEvent",
    "AccountUpdateRequest",
    "AccountWebhookError",
    "ActiveCallData",
    "AuthField",
    "CallAnsweredWebhookEvent",
    "CallEndedWebhookEvent",
    "CallEventCall",
    "CallEventSender",
    "CallIncomingWebhookEvent",
    "CallMessage",
    "CallMessageCall",
    "CallMessageCallVariant1",
    "CallMessageCallVariant2",
    "CallMessageReceivedWebhookEvent",
    "CallMessageUpdatedWebhookEvent",
    "CallMessageWebhookEvent",
    "Contact",
    "ContactAddressBook",
    "ContactBlocklistResult",
    "ContactCard",
    "ContactCreateRequest",
    "ContactCreateRequestVariant1",
    "ContactCreateRequestVariant2",
    "ContactEmail",
    "ContactExtra",
    "ContactIdRequest",
    "ContactListResult",
    "ContactMembership",
    "ContactMessagePayload",
    "ContactNoteRequest",
    "ContactPhone",
    "ContactUpdateChange",
    "ContactUpdateReference",
    "ContactUpdatedData",
    "ContactUpdatedWebhookEvent",
    "Conversation",
    "ConversationDisappearingMessagesChange",
    "ConversationDisappearingMessagesState",
    "ConversationDisappearingMessagesStateVariant1",
    "ConversationDisappearingMessagesStateVariant2",
    "ConversationDisappearingMessagesUpdatedWebhookEvent",
    "ConversationHistoryAccepted",
    "ConversationHistoryBefore",
    "ConversationHistoryMessage",
    "ConversationHistoryRequest",
    "ConversationHistorySource",
    "ConversationHistoryWebhookEvent",
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
    "ConversationStateAccount",
    "ConversationStateActor",
    "ConversationStateReference",
    "ConversationType",
    "CreateCallData",
    "CreateCallRequest",
    "EndedCallData",
    "Error",
    "ErrorEnvelope",
    "FreeFormObject",
    "Group",
    "GroupAnnouncementChange",
    "GroupCreateRequest",
    "GroupCreateResult",
    "GroupIdRequest",
    "GroupInfoUpdateRequest",
    "GroupInviteCode",
    "GroupInviteLinkChange",
    "GroupJoinApprovalModeRequest",
    "GroupJoinRequest",
    "GroupJoinRequestsResult",
    "GroupJoinRequestsUpdateRequest",
    "GroupListResult",
    "GroupMemberUpdateRequest",
    "GroupPermissions",
    "GroupSettingsEvent",
    "GroupSettingsUpdatedWebhookEvent",
    "GroupUpdatedChange",
    "GroupUpdatedChangeVariant1",
    "GroupUpdatedChangeVariant2",
    "GroupUpdatedChangeVariant3",
    "LinkPreviewMessagePayload",
    "MediaMessagePayload",
    "MediaMessagePayloadVariant1",
    "MediaMessagePayloadVariant2",
    "MediaMessagePayloadVariant3",
    "Mention",
    "MentionVariant1",
    "MentionVariant2",
    "MessageCommerce",
    "MessageCommerceHTTPURL",
    "MessageCommerceHistoryWebhookEvent",
    "MessageCommerceMoney",
    "MessageCommerceReceivedWebhookEvent",
    "MessageCommerceUpdatedWebhookEvent",
    "MessageCommerceVariant1",
    "MessageCommerceVariant2",
    "MessageCommerceWebhookEvent",
    "MessageContactCards",
    "MessageContactCardsHistoryWebhookEvent",
    "MessageContactCardsReceivedWebhookEvent",
    "MessageContactCardsUpdatedWebhookEvent",
    "MessageContactCardsVariant1",
    "MessageContactCardsVariant2",
    "MessageEditRequest",
    "MessageInteractive",
    "MessageInteractiveAttachment",
    "MessageInteractiveAttachmentMetadata",
    "MessageInteractiveButton",
    "MessageInteractiveButtonVariant1",
    "MessageInteractiveButtonVariant2",
    "MessageInteractiveButtonVariant3",
    "MessageInteractiveButtonVariant4",
    "MessageInteractiveButtonVariant5",
    "MessageInteractiveButtonVariant6",
    "MessageInteractiveHeader",
    "MessageInteractiveHeaderVariant1",
    "MessageInteractiveHeaderVariant2",
    "MessageInteractiveHeaderVariant3",
    "MessageInteractiveHeaderVariant4",
    "MessageInteractiveHistoryWebhookEvent",
    "MessageInteractiveMessage",
    "MessageInteractiveMessageVariant1",
    "MessageInteractiveMessageVariant2",
    "MessageInteractiveReceivedWebhookEvent",
    "MessageInteractiveResponse",
    "MessageInteractiveResponseVariant1",
    "MessageInteractiveResponseVariant2",
    "MessageInteractiveResponseVariant3",
    "MessageInteractiveUpdatedWebhookEvent",
    "MessageInteractiveVariant1",
    "MessageInteractiveVariant2",
    "MessageInteractiveVariant3",
    "MessageInteractiveVariant4",
    "MessageInteractiveWebhookEvent",
    "MessageLinkPreview",
    "MessageLinkPreviewHTTPURL",
    "MessageLinkPreviewHistoryWebhookEvent",
    "MessageLinkPreviewMessage",
    "MessageLinkPreviewReceivedWebhookEvent",
    "MessageLinkPreviewTextUpdate",
    "MessageLinkPreviewUpdatedWebhookEvent",
    "MessageLinkPreviewWebhookEvent",
    "MessageLiveLocation",
    "MessageLiveLocationHistoryWebhookEvent",
    "MessageLiveLocationReceivedWebhookEvent",
    "MessageLiveLocationUpdatedWebhookEvent",
    "MessageOrder",
    "MessagePayload",
    "MessagePayloadVariant1",
    "MessagePayloadVariant10",
    "MessagePayloadVariant2",
    "MessagePayloadVariant3",
    "MessagePayloadVariant4",
    "MessagePayloadVariant5",
    "MessagePayloadVariant6",
    "MessagePayloadVariant7",
    "MessagePayloadVariant8",
    "MessagePayloadVariant9",
    "MessagePinChange",
    "MessagePinMessage",
    "MessagePinParticipant",
    "MessagePinRequest",
    "MessagePinState",
    "MessagePinStateVariant1",
    "MessagePinStateVariant2",
    "MessagePinUpdatedWebhookEvent",
    "MessagePoll",
    "MessagePollHistoryWebhookEvent",
    "MessagePollMessage",
    "MessagePollOption",
    "MessagePollReceivedWebhookEvent",
    "MessagePollVote",
    "MessagePollVoteChange",
    "MessagePollVoteMessage",
    "MessagePollVoteUpdatedWebhookEvent",
    "MessagePollVoteVariant1",
    "MessagePollVoteVariant2",
    "MessagePollWebhookEvent",
    "MessageProduct",
    "MessageReactionRequest",
    "MessageReferral",
    "MessageReferralHistoryWebhookEvent",
    "MessageReferralProviderExtensions",
    "MessageReferralReceivedWebhookEvent",
    "MessageReferralUpdatedWebhookEvent",
    "MessageReferralWebhookEvent",
    "MessageRevokeRequest",
    "MessageTargetRequest",
    "MessageWithOptionalCommerce",
    "MessageWithOptionalCommerceVariant1",
    "MessageWithOptionalCommerceVariant2",
    "MessageWithOptionalCommerceVariant3",
    "MessageWithOptionalContactCards",
    "MessageWithOptionalInteractive",
    "MessageWithOptionalInteractiveVariant1",
    "MessageWithOptionalInteractiveVariant2",
    "MessageWithOptionalInteractiveVariant3",
    "MessageWithOptionalInteractiveVariant4",
    "MessageWithOptionalInteractiveVariant5",
    "MessageWithOptionalLinkPreview",
    "MessageWithOptionalLinkPreviewVariant1",
    "MessageWithOptionalLinkPreviewVariant2",
    "MessageWithOptionalLinkPreviewVariant3",
    "MessageWithOptionalLinkPreviewVariant4",
    "MessageWithOptionalLinkPreviewVariant5",
    "MessageWithOptionalLinkPreviewVariant6",
    "MessageWithOptionalLiveLocation",
    "MessageWithOptionalPoll",
    "MessageWithOptionalPollVariant1",
    "MessageWithOptionalPollVariant2",
    "MessageWithOptionalPollVariant3",
    "MessageWithOptionalPollVariant4",
    "MessageWithOptionalPollVariant5",
    "MessageWithOptionalPollVariant6",
    "MessageWithOptionalPollVariant7",
    "MessageWithOptionalReferral",
    "OkData",
    "PasskeyResponseRequest",
    "PollMessagePayload",
    "Post",
    "PostAuthor",
    "PostComment",
    "PostCommentCreatedWebhookEvent",
    "PostCommentListRequest",
    "PostCommentListResult",
    "PostCommentListResultVariant1",
    "PostCommentListResultVariant2",
    "PostCommentReplyRequest",
    "PostCommentReplyResult",
    "PostInfoRequest",
    "PostListResult",
    "PostListResultVariant1",
    "PostListResultVariant2",
    "PostResourceID",
    "ProviderAuthSession",
    "ProviderInputName",
    "ProviderName",
    "ProviderProfile",
    "ProviderRegionsResponse",
    "QRAuthCheckData",
    "QRAuthCheckPayload",
    "ReceivedContactCard",
    "Recipient",
    "RegionAvailability",
    "ReplyTo",
    "ResponseMeta",
    "RuntimeActionResult",
    "RuntimeStatus",
    "SendMessageLinkPreview",
    "SendMessagePoll",
    "SendMessagePollOption",
    "SendMessageProviderData",
    "SendMessageRequest",
    "SendMessageResult",
    "SessionImportRequest",
    "StandardEventType",
    "StartCodeAuthData",
    "StickerMessagePayload",
    "StickerMessagePayloadVariant1",
    "StickerMessagePayloadVariant2",
    "StickerMessagePayloadVariant3",
    "TextMessagePayload",
    "WebhookEndpoint",
    "WebhookEndpointRequest",
    "WhatsAppAccountAuthFailedWebhookEvent",
    "WhatsAppContactCreateOptions",
    "WhatsAppDeviceID",
    "WhatsAppMessageDeviceSender",
    "WhatsAppMessageDeviceWebhookEvent",
    "WhatsAppMessageReferralExtension",
    "WhatsAppProtocolSessionImportParams",
    "Workspace",
    "WorkspaceStatus",
    "WorkspaceUpdateRequest",
    "_AccountProfileUpdatedWebhookEventData",
    "_AccountSessionAuthPayload",
    "_AccountStartedWebhookEventData",
    "_CallAnsweredWebhookEventData",
    "_CallEndedWebhookEventData",
    "_CallEndedWebhookEventDataVariant1",
    "_CallEndedWebhookEventDataVariant2",
    "_CallIncomingWebhookEventData",
    "_CallMessageReceivedWebhookEventData",
    "_CallMessageUpdatedWebhookEventData",
    "_CallMessageWebhookEventData",
    "_ConversationDisappearingMessagesUpdatedWebhookEventData",
    "_ConversationExtra",
    "_ConversationHistoryWebhookEventData",
    "_CreateCallRequestTo",
    "_GroupExtra",
    "_GroupSettingsUpdatedWebhookEventData",
    "_MessageCommerceHistoryWebhookEventData",
    "_MessageCommerceReceivedWebhookEventData",
    "_MessageCommerceUpdatedWebhookEventData",
    "_MessageCommerceVariant1Product",
    "_MessageCommerceVariant2Order",
    "_MessageCommerceWebhookEventData",
    "_MessageContactCardsHistoryWebhookEventData",
    "_MessageContactCardsReceivedWebhookEventData",
    "_MessageContactCardsUpdatedWebhookEventData",
    "_MessageInteractiveHeaderVariant2Attachment",
    "_MessageInteractiveHeaderVariant3Attachment",
    "_MessageInteractiveHeaderVariant4Attachment",
    "_MessageInteractiveHistoryWebhookEventData",
    "_MessageInteractiveMessageVariant1Interactive",
    "_MessageInteractiveMessageVariant1InteractiveVariant1",
    "_MessageInteractiveMessageVariant1InteractiveVariant2",
    "_MessageInteractiveMessageVariant1InteractiveVariant3",
    "_MessageInteractiveMessageVariant1InteractiveVariant4",
    "_MessageInteractiveMessageVariant2InteractiveResponse",
    "_MessageInteractiveMessageVariant2InteractiveResponseVariant1",
    "_MessageInteractiveMessageVariant2InteractiveResponseVariant2",
    "_MessageInteractiveMessageVariant2InteractiveResponseVariant3",
    "_MessageInteractiveReceivedWebhookEventData",
    "_MessageInteractiveUpdatedWebhookEventData",
    "_MessageInteractiveWebhookEventData",
    "_MessageLinkPreviewDescription",
    "_MessageLinkPreviewDescriptionVariant1",
    "_MessageLinkPreviewDescriptionVariant2",
    "_MessageLinkPreviewHistoryWebhookEventData",
    "_MessageLinkPreviewImageUrl",
    "_MessageLinkPreviewReceivedWebhookEventData",
    "_MessageLinkPreviewTitle",
    "_MessageLinkPreviewTitleVariant1",
    "_MessageLinkPreviewTitleVariant2",
    "_MessageLinkPreviewUpdatedWebhookEventData",
    "_MessageLinkPreviewWebhookEventData",
    "_MessageLiveLocationHistoryWebhookEventData",
    "_MessageLiveLocationReceivedWebhookEventData",
    "_MessageLiveLocationUpdatedWebhookEventData",
    "_MessagePinUpdatedWebhookEventData",
    "_MessagePollHistoryWebhookEventData",
    "_MessagePollReceivedWebhookEventData",
    "_MessagePollVoteUpdatedWebhookEventData",
    "_MessagePollWebhookEventData",
    "_MessageReferralHistoryWebhookEventData",
    "_MessageReferralReceivedWebhookEventData",
    "_MessageReferralUpdatedWebhookEventData",
    "_MessageReferralWebhookEventData",
    "_MessageWithOptionalCommerceVariant1Product",
    "_MessageWithOptionalCommerceVariant2Order",
    "_MessageWithOptionalInteractiveVariant1Interactive",
    "_MessageWithOptionalInteractiveVariant1InteractiveVariant1",
    "_MessageWithOptionalInteractiveVariant1InteractiveVariant2",
    "_MessageWithOptionalInteractiveVariant1InteractiveVariant3",
    "_MessageWithOptionalInteractiveVariant1InteractiveVariant4",
    "_MessageWithOptionalInteractiveVariant2InteractiveResponse",
    "_MessageWithOptionalInteractiveVariant2InteractiveResponseVariant1",
    "_MessageWithOptionalInteractiveVariant2InteractiveResponseVariant2",
    "_MessageWithOptionalInteractiveVariant2InteractiveResponseVariant3",
    "_MessageWithOptionalInteractiveVariant3Product",
    "_MessageWithOptionalInteractiveVariant4Order",
    "_MessageWithOptionalLinkPreviewVariant2Interactive",
    "_MessageWithOptionalLinkPreviewVariant2InteractiveVariant1",
    "_MessageWithOptionalLinkPreviewVariant2InteractiveVariant2",
    "_MessageWithOptionalLinkPreviewVariant2InteractiveVariant3",
    "_MessageWithOptionalLinkPreviewVariant2InteractiveVariant4",
    "_MessageWithOptionalLinkPreviewVariant3InteractiveResponse",
    "_MessageWithOptionalLinkPreviewVariant3InteractiveResponseVariant1",
    "_MessageWithOptionalLinkPreviewVariant3InteractiveResponseVariant2",
    "_MessageWithOptionalLinkPreviewVariant3InteractiveResponseVariant3",
    "_MessageWithOptionalLinkPreviewVariant4Product",
    "_MessageWithOptionalLinkPreviewVariant5Order",
    "_MessageWithOptionalPollVariant3Interactive",
    "_MessageWithOptionalPollVariant3InteractiveVariant1",
    "_MessageWithOptionalPollVariant3InteractiveVariant2",
    "_MessageWithOptionalPollVariant3InteractiveVariant3",
    "_MessageWithOptionalPollVariant3InteractiveVariant4",
    "_MessageWithOptionalPollVariant4InteractiveResponse",
    "_MessageWithOptionalPollVariant4InteractiveResponseVariant1",
    "_MessageWithOptionalPollVariant4InteractiveResponseVariant2",
    "_MessageWithOptionalPollVariant4InteractiveResponseVariant3",
    "_MessageWithOptionalPollVariant5Product",
    "_MessageWithOptionalPollVariant6Order",
    "_PostCommentCreatedWebhookEventData",
    "_ProviderAuthSessionAuthPayload",
    "_StartCodeAuthDataAuthPayload",
    "_WhatsAppAccountAuthFailedWebhookEventData",
    "_WhatsAppMessageDeviceWebhookEventData",
    "__AccountProfileUpdatedWebhookEventDataAccount",
    "__AccountProfileUpdatedWebhookEventDataEvent",
    "__AccountProfileUpdatedWebhookEventDataProfile",
    "__AccountStartedWebhookEventDataEvent",
    "__CallEndedWebhookEventDataVariant1Call",
    "__CallEndedWebhookEventDataVariant2Call",
    "__CallIncomingWebhookEventDataCall",
    "__CallMessageReceivedWebhookEventDataAccount",
    "__CallMessageReceivedWebhookEventDataConversation",
    "__CallMessageReceivedWebhookEventDataEvent",
    "__CallMessageReceivedWebhookEventDataMessage",
    "__CallMessageReceivedWebhookEventDataSender",
    "__CallMessageUpdatedWebhookEventDataAccount",
    "__CallMessageUpdatedWebhookEventDataConversation",
    "__CallMessageUpdatedWebhookEventDataEvent",
    "__CallMessageUpdatedWebhookEventDataMessage",
    "__CallMessageUpdatedWebhookEventDataSender",
    "__CallMessageWebhookEventDataAccount",
    "__CallMessageWebhookEventDataConversation",
    "__CallMessageWebhookEventDataEvent",
    "__CallMessageWebhookEventDataSender",
    "__ConversationHistoryWebhookEventDataConversation",
    "__MessageCommerceHistoryWebhookEventDataMessage",
    "__MessageCommerceHistoryWebhookEventDataMessageVariant1",
    "__MessageCommerceHistoryWebhookEventDataMessageVariant2",
    "__MessageCommerceHistoryWebhookEventDataMessageVariant3",
    "__MessageCommerceReceivedWebhookEventDataMessage",
    "__MessageCommerceReceivedWebhookEventDataMessageVariant1",
    "__MessageCommerceReceivedWebhookEventDataMessageVariant2",
    "__MessageCommerceReceivedWebhookEventDataMessageVariant3",
    "__MessageCommerceReceivedWebhookEventDataMessageVariant4",
    "__MessageCommerceReceivedWebhookEventDataMessageVariant5",
    "__MessageCommerceReceivedWebhookEventDataMessageVariant6",
    "__MessageCommerceUpdatedWebhookEventDataMessage",
    "__MessageCommerceUpdatedWebhookEventDataMessageVariant1",
    "__MessageCommerceUpdatedWebhookEventDataMessageVariant2",
    "__MessageCommerceUpdatedWebhookEventDataMessageVariant3",
    "__MessageCommerceUpdatedWebhookEventDataMessageVariant4",
    "__MessageCommerceUpdatedWebhookEventDataMessageVariant5",
    "__MessageCommerceUpdatedWebhookEventDataMessageVariant6",
    "__MessageCommerceVariant1ProductPrice",
    "__MessageCommerceVariant2OrderTotal",
    "__MessageCommerceWebhookEventDataMessage",
    "__MessageCommerceWebhookEventDataMessageVariant1",
    "__MessageCommerceWebhookEventDataMessageVariant2",
    "__MessageCommerceWebhookEventDataMessageVariant3",
    "__MessageContactCardsReceivedWebhookEventDataMessage",
    "__MessageContactCardsReceivedWebhookEventDataMessageVariant1",
    "__MessageContactCardsReceivedWebhookEventDataMessageVariant2",
    "__MessageContactCardsUpdatedWebhookEventDataMessage",
    "__MessageContactCardsUpdatedWebhookEventDataMessageVariant1",
    "__MessageContactCardsUpdatedWebhookEventDataMessageVariant2",
    "__MessageInteractiveHistoryWebhookEventDataMessage",
    "__MessageInteractiveHistoryWebhookEventDataMessageVariant1",
    "__MessageInteractiveHistoryWebhookEventDataMessageVariant2",
    "__MessageInteractiveHistoryWebhookEventDataMessageVariant3",
    "__MessageInteractiveHistoryWebhookEventDataMessageVariant4",
    "__MessageInteractiveHistoryWebhookEventDataMessageVariant5",
    "__MessageInteractiveMessageVariant1InteractiveVariant1Header",
    "__MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant1",
    "__MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant2",
    "__MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant3",
    "__MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant4",
    "__MessageInteractiveMessageVariant1InteractiveVariant2Header",
    "__MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant1",
    "__MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant2",
    "__MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant3",
    "__MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant4",
    "__MessageInteractiveMessageVariant1InteractiveVariant3Header",
    "__MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant1",
    "__MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant2",
    "__MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant3",
    "__MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant4",
    "__MessageInteractiveMessageVariant1InteractiveVariant4Header",
    "__MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant1",
    "__MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant2",
    "__MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant3",
    "__MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant4",
    "__MessageInteractiveReceivedWebhookEventDataMessage",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant1",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant10",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant2",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant3",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant4",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant5",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant6",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant7",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant8",
    "__MessageInteractiveReceivedWebhookEventDataMessageVariant9",
    "__MessageInteractiveUpdatedWebhookEventDataMessage",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant1",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant10",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant2",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant3",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant4",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant5",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant6",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant7",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant8",
    "__MessageInteractiveUpdatedWebhookEventDataMessageVariant9",
    "__MessageInteractiveWebhookEventDataMessage",
    "__MessageInteractiveWebhookEventDataMessageVariant1",
    "__MessageInteractiveWebhookEventDataMessageVariant2",
    "__MessageInteractiveWebhookEventDataMessageVariant3",
    "__MessageInteractiveWebhookEventDataMessageVariant4",
    "__MessageInteractiveWebhookEventDataMessageVariant5",
    "__MessageLinkPreviewHistoryWebhookEventDataMessage",
    "__MessageLinkPreviewHistoryWebhookEventDataMessageVariant1",
    "__MessageLinkPreviewHistoryWebhookEventDataMessageVariant2",
    "__MessageLinkPreviewHistoryWebhookEventDataMessageVariant3",
    "__MessageLinkPreviewHistoryWebhookEventDataMessageVariant4",
    "__MessageLinkPreviewHistoryWebhookEventDataMessageVariant5",
    "__MessageLinkPreviewHistoryWebhookEventDataMessageVariant6",
    "__MessageLinkPreviewReceivedWebhookEventDataMessage",
    "__MessageLinkPreviewReceivedWebhookEventDataMessageVariant1",
    "__MessageLinkPreviewReceivedWebhookEventDataMessageVariant2",
    "__MessageLinkPreviewReceivedWebhookEventDataMessageVariant3",
    "__MessageLinkPreviewReceivedWebhookEventDataMessageVariant4",
    "__MessageLinkPreviewReceivedWebhookEventDataMessageVariant5",
    "__MessageLinkPreviewReceivedWebhookEventDataMessageVariant6",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessage",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant10",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant11",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant12",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant2",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant3",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant4",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant5",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant6",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant7",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant8",
    "__MessageLinkPreviewUpdatedWebhookEventDataMessageVariant9",
    "__MessageLinkPreviewWebhookEventDataMessage",
    "__MessageLinkPreviewWebhookEventDataMessageVariant1",
    "__MessageLinkPreviewWebhookEventDataMessageVariant2",
    "__MessageLinkPreviewWebhookEventDataMessageVariant3",
    "__MessageLinkPreviewWebhookEventDataMessageVariant4",
    "__MessageLinkPreviewWebhookEventDataMessageVariant5",
    "__MessageLinkPreviewWebhookEventDataMessageVariant6",
    "__MessageLiveLocationReceivedWebhookEventDataMessage",
    "__MessageLiveLocationUpdatedWebhookEventDataMessage",
    "__MessagePinUpdatedWebhookEventDataConversation",
    "__MessagePollHistoryWebhookEventDataMessage",
    "__MessagePollHistoryWebhookEventDataMessageVariant1",
    "__MessagePollHistoryWebhookEventDataMessageVariant2",
    "__MessagePollHistoryWebhookEventDataMessageVariant3",
    "__MessagePollHistoryWebhookEventDataMessageVariant4",
    "__MessagePollHistoryWebhookEventDataMessageVariant5",
    "__MessagePollHistoryWebhookEventDataMessageVariant6",
    "__MessagePollHistoryWebhookEventDataMessageVariant7",
    "__MessagePollReceivedWebhookEventDataMessage",
    "__MessagePollReceivedWebhookEventDataMessageVariant1",
    "__MessagePollReceivedWebhookEventDataMessageVariant2",
    "__MessagePollReceivedWebhookEventDataMessageVariant3",
    "__MessagePollReceivedWebhookEventDataMessageVariant4",
    "__MessagePollReceivedWebhookEventDataMessageVariant5",
    "__MessagePollReceivedWebhookEventDataMessageVariant6",
    "__MessagePollReceivedWebhookEventDataMessageVariant7",
    "__MessagePollWebhookEventDataMessage",
    "__MessagePollWebhookEventDataMessageVariant1",
    "__MessagePollWebhookEventDataMessageVariant2",
    "__MessagePollWebhookEventDataMessageVariant3",
    "__MessagePollWebhookEventDataMessageVariant4",
    "__MessagePollWebhookEventDataMessageVariant5",
    "__MessagePollWebhookEventDataMessageVariant6",
    "__MessagePollWebhookEventDataMessageVariant7",
    "__MessageReferralReceivedWebhookEventDataMessage",
    "__MessageReferralUpdatedWebhookEventDataMessage",
    "__MessageWithOptionalCommerceVariant1ProductPrice",
    "__MessageWithOptionalCommerceVariant2OrderTotal",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant1Header",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant1",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant2",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant3",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant4",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant2Header",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant1",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant2",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant3",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant4",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant3Header",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant1",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant2",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant3",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant4",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant4Header",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant1",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant2",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant3",
    "__MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant4",
    "__MessageWithOptionalInteractiveVariant3ProductPrice",
    "__MessageWithOptionalInteractiveVariant4OrderTotal",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant1Header",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant1",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant2",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant3",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant4",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant2Header",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant1",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant2",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant3",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant4",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant3Header",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant1",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant2",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant3",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant4",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant4Header",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant1",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant2",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant3",
    "__MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant4",
    "__MessageWithOptionalLinkPreviewVariant4ProductPrice",
    "__MessageWithOptionalLinkPreviewVariant5OrderTotal",
    "__MessageWithOptionalPollVariant3InteractiveVariant1Header",
    "__MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant1",
    "__MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant2",
    "__MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant3",
    "__MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant4",
    "__MessageWithOptionalPollVariant3InteractiveVariant2Header",
    "__MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant1",
    "__MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant2",
    "__MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant3",
    "__MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant4",
    "__MessageWithOptionalPollVariant3InteractiveVariant3Header",
    "__MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant1",
    "__MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant2",
    "__MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant3",
    "__MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant4",
    "__MessageWithOptionalPollVariant3InteractiveVariant4Header",
    "__MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant1",
    "__MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant2",
    "__MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant3",
    "__MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant4",
    "__MessageWithOptionalPollVariant5ProductPrice",
    "__MessageWithOptionalPollVariant6OrderTotal",
    "__PostCommentCreatedWebhookEventDataAccount",
    "__WhatsAppAccountAuthFailedWebhookEventDataError",
    "__WhatsAppAccountAuthFailedWebhookEventDataEvent",
    "__WhatsAppMessageDeviceWebhookEventDataAccount",
    "__WhatsAppMessageDeviceWebhookEventDataMessage",
    "___CallMessageReceivedWebhookEventDataMessageCall",
    "___CallMessageUpdatedWebhookEventDataMessageCall",
    "___CallMessageUpdatedWebhookEventDataMessageCallVariant1",
    "___CallMessageUpdatedWebhookEventDataMessageCallVariant2",
    "___CallMessageUpdatedWebhookEventDataMessageCallVariant3",
    "___CallMessageUpdatedWebhookEventDataMessageCallVariant4",
    "___MessageCommerceHistoryWebhookEventDataMessageVariant1Product",
    "___MessageCommerceHistoryWebhookEventDataMessageVariant1Referral",
    "___MessageCommerceHistoryWebhookEventDataMessageVariant2Order",
    "___MessageCommerceHistoryWebhookEventDataMessageVariant2Referral",
    "___MessageCommerceHistoryWebhookEventDataMessageVariant3Referral",
    "___MessageCommerceReceivedWebhookEventDataMessageVariant1Product",
    "___MessageCommerceReceivedWebhookEventDataMessageVariant1Referral",
    "___MessageCommerceReceivedWebhookEventDataMessageVariant2Referral",
    "___MessageCommerceReceivedWebhookEventDataMessageVariant3Referral",
    "___MessageCommerceReceivedWebhookEventDataMessageVariant4Referral",
    "___MessageCommerceReceivedWebhookEventDataMessageVariant5Order",
    "___MessageCommerceReceivedWebhookEventDataMessageVariant5Referral",
    "___MessageCommerceReceivedWebhookEventDataMessageVariant6Referral",
    "___MessageCommerceUpdatedWebhookEventDataMessageVariant1Product",
    "___MessageCommerceUpdatedWebhookEventDataMessageVariant1Referral",
    "___MessageCommerceUpdatedWebhookEventDataMessageVariant2Referral",
    "___MessageCommerceUpdatedWebhookEventDataMessageVariant3Referral",
    "___MessageCommerceUpdatedWebhookEventDataMessageVariant4Referral",
    "___MessageCommerceUpdatedWebhookEventDataMessageVariant5Order",
    "___MessageCommerceUpdatedWebhookEventDataMessageVariant5Referral",
    "___MessageCommerceUpdatedWebhookEventDataMessageVariant6Referral",
    "___MessageCommerceWebhookEventDataMessageVariant1Product",
    "___MessageCommerceWebhookEventDataMessageVariant1Referral",
    "___MessageCommerceWebhookEventDataMessageVariant2Order",
    "___MessageCommerceWebhookEventDataMessageVariant2Referral",
    "___MessageCommerceWebhookEventDataMessageVariant3Referral",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant1Interactive",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant1Referral",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant2InteractiveResponse",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant2InteractiveResponseVariant1",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant2InteractiveResponseVariant2",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant2InteractiveResponseVariant3",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant2Referral",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant3Product",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant3Referral",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant4Order",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant4Referral",
    "___MessageInteractiveHistoryWebhookEventDataMessageVariant5Referral",
    "___MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant2Attachment",
    "___MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant3Attachment",
    "___MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant4Attachment",
    "___MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant2Attachment",
    "___MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant3Attachment",
    "___MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant4Attachment",
    "___MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant2Attachment",
    "___MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant3Attachment",
    "___MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant4Attachment",
    "___MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant2Attachment",
    "___MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant3Attachment",
    "___MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant4Attachment",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant10Referral",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant1Interactive",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant1Referral",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant2Referral",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant3Referral",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant4Referral",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant5Referral",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant6Referral",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant7InteractiveResponse",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant7InteractiveResponseVariant1",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant7InteractiveResponseVariant2",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant7InteractiveResponseVariant3",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant7Referral",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant8Referral",
    "___MessageInteractiveReceivedWebhookEventDataMessageVariant9Referral",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant10Referral",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant1Interactive",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant1Referral",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant2Referral",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant3Referral",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant4Referral",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant5Referral",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant6Referral",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant7InteractiveResponse",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant7InteractiveResponseVariant1",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant7InteractiveResponseVariant2",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant7InteractiveResponseVariant3",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant7Referral",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant8Referral",
    "___MessageInteractiveUpdatedWebhookEventDataMessageVariant9Referral",
    "___MessageInteractiveWebhookEventDataMessageVariant1Interactive",
    "___MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1",
    "___MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2",
    "___MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3",
    "___MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4",
    "___MessageInteractiveWebhookEventDataMessageVariant1Referral",
    "___MessageInteractiveWebhookEventDataMessageVariant2InteractiveResponse",
    "___MessageInteractiveWebhookEventDataMessageVariant2InteractiveResponseVariant1",
    "___MessageInteractiveWebhookEventDataMessageVariant2InteractiveResponseVariant2",
    "___MessageInteractiveWebhookEventDataMessageVariant2InteractiveResponseVariant3",
    "___MessageInteractiveWebhookEventDataMessageVariant2Referral",
    "___MessageInteractiveWebhookEventDataMessageVariant3Product",
    "___MessageInteractiveWebhookEventDataMessageVariant3Referral",
    "___MessageInteractiveWebhookEventDataMessageVariant4Order",
    "___MessageInteractiveWebhookEventDataMessageVariant4Referral",
    "___MessageInteractiveWebhookEventDataMessageVariant5Referral",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant1Referral",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2Interactive",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant2Referral",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3InteractiveResponse",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3InteractiveResponseVariant1",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3InteractiveResponseVariant2",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3InteractiveResponseVariant3",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant3Referral",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant4Product",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant4Referral",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant5Order",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant5Referral",
    "___MessageLinkPreviewHistoryWebhookEventDataMessageVariant6Referral",
    "___MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreview",
    "___MessageLinkPreviewReceivedWebhookEventDataMessageVariant1Referral",
    "___MessageLinkPreviewReceivedWebhookEventDataMessageVariant2Referral",
    "___MessageLinkPreviewReceivedWebhookEventDataMessageVariant3Referral",
    "___MessageLinkPreviewReceivedWebhookEventDataMessageVariant4Referral",
    "___MessageLinkPreviewReceivedWebhookEventDataMessageVariant5Referral",
    "___MessageLinkPreviewReceivedWebhookEventDataMessageVariant6Referral",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant10Referral",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant11Referral",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant12Referral",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreview",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1Referral",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant2Referral",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant3Referral",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant4Referral",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant5Referral",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant6Referral",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant7Referral",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant8Referral",
    "___MessageLinkPreviewUpdatedWebhookEventDataMessageVariant9Referral",
    "___MessageLinkPreviewWebhookEventDataMessageVariant1Referral",
    "___MessageLinkPreviewWebhookEventDataMessageVariant2Interactive",
    "___MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1",
    "___MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2",
    "___MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3",
    "___MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4",
    "___MessageLinkPreviewWebhookEventDataMessageVariant2Referral",
    "___MessageLinkPreviewWebhookEventDataMessageVariant3InteractiveResponse",
    "___MessageLinkPreviewWebhookEventDataMessageVariant3InteractiveResponseVariant1",
    "___MessageLinkPreviewWebhookEventDataMessageVariant3InteractiveResponseVariant2",
    "___MessageLinkPreviewWebhookEventDataMessageVariant3InteractiveResponseVariant3",
    "___MessageLinkPreviewWebhookEventDataMessageVariant3Referral",
    "___MessageLinkPreviewWebhookEventDataMessageVariant4Product",
    "___MessageLinkPreviewWebhookEventDataMessageVariant4Referral",
    "___MessageLinkPreviewWebhookEventDataMessageVariant5Order",
    "___MessageLinkPreviewWebhookEventDataMessageVariant5Referral",
    "___MessageLinkPreviewWebhookEventDataMessageVariant6Referral",
    "___MessagePollHistoryWebhookEventDataMessageVariant1Referral",
    "___MessagePollHistoryWebhookEventDataMessageVariant2Referral",
    "___MessagePollHistoryWebhookEventDataMessageVariant3Interactive",
    "___MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1",
    "___MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2",
    "___MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3",
    "___MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4",
    "___MessagePollHistoryWebhookEventDataMessageVariant3Referral",
    "___MessagePollHistoryWebhookEventDataMessageVariant4InteractiveResponse",
    "___MessagePollHistoryWebhookEventDataMessageVariant4InteractiveResponseVariant1",
    "___MessagePollHistoryWebhookEventDataMessageVariant4InteractiveResponseVariant2",
    "___MessagePollHistoryWebhookEventDataMessageVariant4InteractiveResponseVariant3",
    "___MessagePollHistoryWebhookEventDataMessageVariant4Referral",
    "___MessagePollHistoryWebhookEventDataMessageVariant5Product",
    "___MessagePollHistoryWebhookEventDataMessageVariant5Referral",
    "___MessagePollHistoryWebhookEventDataMessageVariant6Order",
    "___MessagePollHistoryWebhookEventDataMessageVariant6Referral",
    "___MessagePollHistoryWebhookEventDataMessageVariant7Referral",
    "___MessagePollReceivedWebhookEventDataMessageVariant1Poll",
    "___MessagePollReceivedWebhookEventDataMessageVariant1Referral",
    "___MessagePollReceivedWebhookEventDataMessageVariant1Sender",
    "___MessagePollReceivedWebhookEventDataMessageVariant2Referral",
    "___MessagePollReceivedWebhookEventDataMessageVariant3Interactive",
    "___MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1",
    "___MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2",
    "___MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3",
    "___MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4",
    "___MessagePollReceivedWebhookEventDataMessageVariant3Referral",
    "___MessagePollReceivedWebhookEventDataMessageVariant4InteractiveResponse",
    "___MessagePollReceivedWebhookEventDataMessageVariant4InteractiveResponseVariant1",
    "___MessagePollReceivedWebhookEventDataMessageVariant4InteractiveResponseVariant2",
    "___MessagePollReceivedWebhookEventDataMessageVariant4InteractiveResponseVariant3",
    "___MessagePollReceivedWebhookEventDataMessageVariant4Referral",
    "___MessagePollReceivedWebhookEventDataMessageVariant5Product",
    "___MessagePollReceivedWebhookEventDataMessageVariant5Referral",
    "___MessagePollReceivedWebhookEventDataMessageVariant6Order",
    "___MessagePollReceivedWebhookEventDataMessageVariant6Referral",
    "___MessagePollReceivedWebhookEventDataMessageVariant7Referral",
    "___MessagePollWebhookEventDataMessageVariant1Referral",
    "___MessagePollWebhookEventDataMessageVariant2Referral",
    "___MessagePollWebhookEventDataMessageVariant3Interactive",
    "___MessagePollWebhookEventDataMessageVariant3InteractiveVariant1",
    "___MessagePollWebhookEventDataMessageVariant3InteractiveVariant2",
    "___MessagePollWebhookEventDataMessageVariant3InteractiveVariant3",
    "___MessagePollWebhookEventDataMessageVariant3InteractiveVariant4",
    "___MessagePollWebhookEventDataMessageVariant3Referral",
    "___MessagePollWebhookEventDataMessageVariant4InteractiveResponse",
    "___MessagePollWebhookEventDataMessageVariant4InteractiveResponseVariant1",
    "___MessagePollWebhookEventDataMessageVariant4InteractiveResponseVariant2",
    "___MessagePollWebhookEventDataMessageVariant4InteractiveResponseVariant3",
    "___MessagePollWebhookEventDataMessageVariant4Referral",
    "___MessagePollWebhookEventDataMessageVariant5Product",
    "___MessagePollWebhookEventDataMessageVariant5Referral",
    "___MessagePollWebhookEventDataMessageVariant6Order",
    "___MessagePollWebhookEventDataMessageVariant6Referral",
    "___MessagePollWebhookEventDataMessageVariant7Referral",
    "___MessageReferralReceivedWebhookEventDataMessageReferral",
    "___MessageReferralUpdatedWebhookEventDataMessageReferral",
    "___MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant2Attachment",
    "___MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant3Attachment",
    "___MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant4Attachment",
    "___MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant2Attachment",
    "___MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant3Attachment",
    "___MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant4Attachment",
    "___MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant2Attachment",
    "___MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant3Attachment",
    "___MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant4Attachment",
    "___MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant2Attachment",
    "___MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant3Attachment",
    "___MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant4Attachment",
    "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant2Attachment",
    "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant3Attachment",
    "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant4Attachment",
    "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant2Attachment",
    "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant3Attachment",
    "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant4Attachment",
    "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant2Attachment",
    "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant3Attachment",
    "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant4Attachment",
    "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant2Attachment",
    "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant3Attachment",
    "___MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant4Attachment",
    "___MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant2Attachment",
    "___MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant3Attachment",
    "___MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant4Attachment",
    "___MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant2Attachment",
    "___MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant3Attachment",
    "___MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant4Attachment",
    "___MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant2Attachment",
    "___MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant3Attachment",
    "___MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant4Attachment",
    "___MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant2Attachment",
    "___MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant3Attachment",
    "___MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant4Attachment",
    "____MessageCommerceHistoryWebhookEventDataMessageVariant1ProductPrice",
    "____MessageCommerceHistoryWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessageCommerceHistoryWebhookEventDataMessageVariant2OrderTotal",
    "____MessageCommerceHistoryWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessageCommerceHistoryWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessageCommerceReceivedWebhookEventDataMessageVariant1ProductPrice",
    "____MessageCommerceReceivedWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessageCommerceReceivedWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessageCommerceReceivedWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessageCommerceReceivedWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessageCommerceReceivedWebhookEventDataMessageVariant5OrderTotal",
    "____MessageCommerceReceivedWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessageCommerceReceivedWebhookEventDataMessageVariant6ReferralProviderExtensions",
    "____MessageCommerceUpdatedWebhookEventDataMessageVariant1ProductPrice",
    "____MessageCommerceUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessageCommerceUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessageCommerceUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessageCommerceUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessageCommerceUpdatedWebhookEventDataMessageVariant5OrderTotal",
    "____MessageCommerceUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessageCommerceUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensions",
    "____MessageCommerceWebhookEventDataMessageVariant1ProductPrice",
    "____MessageCommerceWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessageCommerceWebhookEventDataMessageVariant2OrderTotal",
    "____MessageCommerceWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessageCommerceWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1Header",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant1",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2Header",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant1",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3Header",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant1",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4Header",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant1",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant3ProductPrice",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant4OrderTotal",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessageInteractiveHistoryWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "____MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "____MessageInteractiveMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "____MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "____MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "____MessageInteractiveMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "____MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "____MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "____MessageInteractiveMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "____MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "____MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "____MessageInteractiveMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant10ReferralProviderExtensions",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1Header",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant1",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2Header",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant1",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3Header",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant1",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4Header",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant1",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant6ReferralProviderExtensions",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant7ReferralProviderExtensions",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant8ReferralProviderExtensions",
    "____MessageInteractiveReceivedWebhookEventDataMessageVariant9ReferralProviderExtensions",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant10ReferralProviderExtensions",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1Header",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant1",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2Header",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant1",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3Header",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant1",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4Header",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant1",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensions",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant7ReferralProviderExtensions",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant8ReferralProviderExtensions",
    "____MessageInteractiveUpdatedWebhookEventDataMessageVariant9ReferralProviderExtensions",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1Header",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant1",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2Header",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant1",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3Header",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant1",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4Header",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant1",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3",
    "____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4",
    "____MessageInteractiveWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessageInteractiveWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessageInteractiveWebhookEventDataMessageVariant3ProductPrice",
    "____MessageInteractiveWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessageInteractiveWebhookEventDataMessageVariant4OrderTotal",
    "____MessageInteractiveWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessageInteractiveWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1Header",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant1",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2Header",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant1",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3Header",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant1",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4Header",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant1",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant4ProductPrice",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant5OrderTotal",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessageLinkPreviewHistoryWebhookEventDataMessageVariant6ReferralProviderExtensions",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewDescription",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewDescriptionVariant1",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewDescriptionVariant2",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewImageUrl",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewTitle",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewTitleVariant1",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewTitleVariant2",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1LinkPreviewUrl",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessageLinkPreviewReceivedWebhookEventDataMessageVariant6ReferralProviderExtensions",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant10ReferralProviderExtensions",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant11ReferralProviderExtensions",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant12ReferralProviderExtensions",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewDescription",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewDescriptionVariant1",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewDescriptionVariant2",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewImageUrl",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewTitle",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewTitleVariant1",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewTitleVariant2",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1LinkPreviewUrl",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensions",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant7ReferralProviderExtensions",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant8ReferralProviderExtensions",
    "____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant9ReferralProviderExtensions",
    "____MessageLinkPreviewWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1Header",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant1",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2Header",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant1",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3Header",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant1",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4Header",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant1",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4",
    "____MessageLinkPreviewWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessageLinkPreviewWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessageLinkPreviewWebhookEventDataMessageVariant4ProductPrice",
    "____MessageLinkPreviewWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessageLinkPreviewWebhookEventDataMessageVariant5OrderTotal",
    "____MessageLinkPreviewWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessageLinkPreviewWebhookEventDataMessageVariant6ReferralProviderExtensions",
    "____MessagePollHistoryWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessagePollHistoryWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1Header",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant1",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2Header",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant1",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3Header",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant1",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4Header",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant1",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3",
    "____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4",
    "____MessagePollHistoryWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessagePollHistoryWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessagePollHistoryWebhookEventDataMessageVariant5ProductPrice",
    "____MessagePollHistoryWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessagePollHistoryWebhookEventDataMessageVariant6OrderTotal",
    "____MessagePollHistoryWebhookEventDataMessageVariant6ReferralProviderExtensions",
    "____MessagePollHistoryWebhookEventDataMessageVariant7ReferralProviderExtensions",
    "____MessagePollReceivedWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessagePollReceivedWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1Header",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant1",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2Header",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant1",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3Header",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant1",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4Header",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant1",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3",
    "____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4",
    "____MessagePollReceivedWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessagePollReceivedWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessagePollReceivedWebhookEventDataMessageVariant5ProductPrice",
    "____MessagePollReceivedWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessagePollReceivedWebhookEventDataMessageVariant6OrderTotal",
    "____MessagePollReceivedWebhookEventDataMessageVariant6ReferralProviderExtensions",
    "____MessagePollReceivedWebhookEventDataMessageVariant7ReferralProviderExtensions",
    "____MessagePollWebhookEventDataMessageVariant1ReferralProviderExtensions",
    "____MessagePollWebhookEventDataMessageVariant2ReferralProviderExtensions",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1Header",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant1",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2Header",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant1",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3Header",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant1",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4Header",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant1",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3",
    "____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4",
    "____MessagePollWebhookEventDataMessageVariant3ReferralProviderExtensions",
    "____MessagePollWebhookEventDataMessageVariant4ReferralProviderExtensions",
    "____MessagePollWebhookEventDataMessageVariant5ProductPrice",
    "____MessagePollWebhookEventDataMessageVariant5ReferralProviderExtensions",
    "____MessagePollWebhookEventDataMessageVariant6OrderTotal",
    "____MessagePollWebhookEventDataMessageVariant6ReferralProviderExtensions",
    "____MessagePollWebhookEventDataMessageVariant7ReferralProviderExtensions",
    "____MessageReferralReceivedWebhookEventDataMessageReferralProviderExtensions",
    "____MessageReferralUpdatedWebhookEventDataMessageReferralProviderExtensions",
    "____MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "____MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "____MessageWithOptionalInteractiveVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "____MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "____MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "____MessageWithOptionalInteractiveVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "____MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "____MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "____MessageWithOptionalInteractiveVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "____MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "____MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "____MessageWithOptionalInteractiveVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata",
    "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "____MessageWithOptionalLinkPreviewVariant2InteractiveVariant4HeaderVariant4AttachmentMetadata",
    "____MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "____MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "____MessageWithOptionalPollVariant3InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "____MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "____MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "____MessageWithOptionalPollVariant3InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "____MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "____MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "____MessageWithOptionalPollVariant3InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "____MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "____MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "____MessageWithOptionalPollVariant3InteractiveVariant4HeaderVariant4AttachmentMetadata",
    "_____MessageCommerceHistoryWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceHistoryWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceHistoryWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceReceivedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceReceivedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceReceivedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceReceivedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceReceivedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceReceivedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessageCommerceWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2Attachment",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3Attachment",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4Attachment",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2Attachment",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3Attachment",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4Attachment",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2Attachment",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3Attachment",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4Attachment",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2Attachment",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3Attachment",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4Attachment",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveHistoryWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant10ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2Attachment",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3Attachment",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4Attachment",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2Attachment",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3Attachment",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4Attachment",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2Attachment",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3Attachment",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4Attachment",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2Attachment",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3Attachment",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4Attachment",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant8ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveReceivedWebhookEventDataMessageVariant9ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant10ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2Attachment",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3Attachment",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4Attachment",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2Attachment",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3Attachment",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4Attachment",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2Attachment",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3Attachment",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4Attachment",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2Attachment",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3Attachment",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4Attachment",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant8ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveUpdatedWebhookEventDataMessageVariant9ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2Attachment",
    "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3Attachment",
    "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4Attachment",
    "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2Attachment",
    "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3Attachment",
    "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4Attachment",
    "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2Attachment",
    "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3Attachment",
    "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4Attachment",
    "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2Attachment",
    "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3Attachment",
    "_____MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4Attachment",
    "_____MessageInteractiveWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessageInteractiveWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2Attachment",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3Attachment",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4Attachment",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2Attachment",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3Attachment",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4Attachment",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2Attachment",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3Attachment",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4Attachment",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2Attachment",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3Attachment",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4Attachment",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewHistoryWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewReceivedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewReceivedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewReceivedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewReceivedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewReceivedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewReceivedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant10ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant11ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant12ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant8ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewUpdatedWebhookEventDataMessageVariant9ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2Attachment",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3Attachment",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4Attachment",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2Attachment",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3Attachment",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4Attachment",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2Attachment",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3Attachment",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4Attachment",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2Attachment",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3Attachment",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4Attachment",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessageLinkPreviewWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp",
    "_____MessagePollHistoryWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessagePollHistoryWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2Attachment",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3Attachment",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4Attachment",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2Attachment",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3Attachment",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4Attachment",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2Attachment",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3Attachment",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4Attachment",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2Attachment",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3Attachment",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4Attachment",
    "_____MessagePollHistoryWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessagePollHistoryWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessagePollHistoryWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessagePollHistoryWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp",
    "_____MessagePollHistoryWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp",
    "_____MessagePollReceivedWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessagePollReceivedWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2Attachment",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3Attachment",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4Attachment",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2Attachment",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3Attachment",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4Attachment",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2Attachment",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3Attachment",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4Attachment",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2Attachment",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3Attachment",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4Attachment",
    "_____MessagePollReceivedWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessagePollReceivedWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessagePollReceivedWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessagePollReceivedWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp",
    "_____MessagePollReceivedWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp",
    "_____MessagePollWebhookEventDataMessageVariant1ReferralProviderExtensionsWhatsapp",
    "_____MessagePollWebhookEventDataMessageVariant2ReferralProviderExtensionsWhatsapp",
    "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2Attachment",
    "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3Attachment",
    "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4Attachment",
    "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2Attachment",
    "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3Attachment",
    "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4Attachment",
    "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2Attachment",
    "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3Attachment",
    "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4Attachment",
    "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2Attachment",
    "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3Attachment",
    "_____MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4Attachment",
    "_____MessagePollWebhookEventDataMessageVariant3ReferralProviderExtensionsWhatsapp",
    "_____MessagePollWebhookEventDataMessageVariant4ReferralProviderExtensionsWhatsapp",
    "_____MessagePollWebhookEventDataMessageVariant5ReferralProviderExtensionsWhatsapp",
    "_____MessagePollWebhookEventDataMessageVariant6ReferralProviderExtensionsWhatsapp",
    "_____MessagePollWebhookEventDataMessageVariant7ReferralProviderExtensionsWhatsapp",
    "_____MessageReferralReceivedWebhookEventDataMessageReferralProviderExtensionsWhatsapp",
    "_____MessageReferralUpdatedWebhookEventDataMessageReferralProviderExtensionsWhatsapp",
    "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveHistoryWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveReceivedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveUpdatedWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "______MessageInteractiveWebhookEventDataMessageVariant1InteractiveVariant4HeaderVariant4AttachmentMetadata",
    "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "______MessageLinkPreviewHistoryWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4AttachmentMetadata",
    "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "______MessageLinkPreviewWebhookEventDataMessageVariant2InteractiveVariant4HeaderVariant4AttachmentMetadata",
    "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "______MessagePollHistoryWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4AttachmentMetadata",
    "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "______MessagePollReceivedWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4AttachmentMetadata",
    "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant2AttachmentMetadata",
    "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant3AttachmentMetadata",
    "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant1HeaderVariant4AttachmentMetadata",
    "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant2AttachmentMetadata",
    "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant3AttachmentMetadata",
    "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant2HeaderVariant4AttachmentMetadata",
    "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant2AttachmentMetadata",
    "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant3AttachmentMetadata",
    "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant3HeaderVariant4AttachmentMetadata",
    "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant2AttachmentMetadata",
    "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant3AttachmentMetadata",
    "______MessagePollWebhookEventDataMessageVariant3InteractiveVariant4HeaderVariant4AttachmentMetadata",
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
    "ConfirmAccountPasskeyPath",
    "ConfirmAccountPasskeyQuery",
    "ConfirmAccountPasskeyRequestBody",
    "ConfirmAccountPasskeyResponse",
    "CreateAccountPath",
    "CreateAccountQuery",
    "CreateAccountRequestBody",
    "CreateAccountResponse",
    "CreateAccountAuthSessionPath",
    "CreateAccountAuthSessionQuery",
    "CreateAccountAuthSessionRequestBody",
    "CreateAccountAuthSessionResponse",
    "CreateApiKeyPath",
    "CreateApiKeyQuery",
    "CreateApiKeyRequestBody",
    "CreateApiKeyResponse",
    "CreateCallPath",
    "CreateCallQuery",
    "CreateCallRequestBody",
    "CreateCallResponse",
    "CreateContactPath",
    "CreateContactQuery",
    "CreateContactRequestBody",
    "CreateContactResponse",
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
    "GetAccountOperationPath",
    "GetAccountOperationQuery",
    "GetAccountOperationRequestBody",
    "GetAccountOperationResponse",
    "GetActiveCallPath",
    "GetActiveCallQuery",
    "GetActiveCallRequestBody",
    "GetActiveCallResponse",
    "GetContactPath",
    "GetContactQuery",
    "GetContactRequestBody",
    "GetContactResponse",
    "GetContactMembershipPath",
    "GetContactMembershipQuery",
    "GetContactMembershipRequestBody",
    "GetContactMembershipResponse",
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
    "GetPostPath",
    "GetPostQuery",
    "GetPostRequestBody",
    "GetPostResponse",
    "GetWebhookEndpointPath",
    "GetWebhookEndpointQuery",
    "GetWebhookEndpointRequestBody",
    "GetWebhookEndpointResponse",
    "GetWorkspacePath",
    "GetWorkspaceQuery",
    "GetWorkspaceRequestBody",
    "GetWorkspaceResponse",
    "HangupCallPath",
    "HangupCallQuery",
    "HangupCallRequestBody",
    "HangupCallResponse",
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
    "ListPostCommentsPath",
    "ListPostCommentsQuery",
    "ListPostCommentsRequestBody",
    "ListPostCommentsResponse",
    "ListPostsPath",
    "ListPostsQuery",
    "ListPostsRequestBody",
    "ListPostsResponse",
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
    "ReplyPostCommentPath",
    "ReplyPostCommentQuery",
    "ReplyPostCommentRequestBody",
    "ReplyPostCommentResponse",
    "RequestConversationHistoryPath",
    "RequestConversationHistoryQuery",
    "RequestConversationHistoryRequestBody",
    "RequestConversationHistoryResponse",
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
    "SubmitAccountPasskeyResponsePath",
    "SubmitAccountPasskeyResponseQuery",
    "SubmitAccountPasskeyResponseRequestBody",
    "SubmitAccountPasskeyResponseResponse",
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
