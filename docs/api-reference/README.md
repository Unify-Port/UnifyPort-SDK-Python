<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->

[English](README.md) | [简体中文](../zh-CN/api-reference/README.md)

# Device API Reference

Every public operation maps to one static snake_case Python method.

| Python method | Node operationId | HTTP |
| --- | --- | --- |
| [`block_contact`](block-contact.md) | `blockContact` | `POST /v1/accounts/{account_id}/contacts/block` |
| [`cancel_account_auth`](cancel-account-auth.md) | `cancelAccountAuth` | `POST /v1/accounts/{account_id}/auth/cancel` |
| [`check_account_qr_auth`](check-account-qr-auth.md) | `checkAccountQrAuth` | `POST /v1/accounts/{account_id}/auth/qr/check` |
| [`confirm_account_passkey`](confirm-account-passkey.md) | `confirmAccountPasskey` | `POST /v1/accounts/{account_id}/auth/passkey-confirm` |
| [`create_account`](create-account.md) | `createAccount` | `POST /v1/accounts` |
| [`create_account_auth_session`](create-account-auth-session.md) | `createAccountAuthSession` | `POST /v1/accounts/{account_id}/auth-sessions` |
| [`create_api_key`](create-api-key.md) | `createApiKey` | `POST /v1/api-keys` |
| [`create_call`](create-call.md) | `createCall` | `POST /v1/calls` |
| [`create_contact`](create-contact.md) | `createContact` | `POST /v1/accounts/{account_id}/contacts/add` |
| [`create_group`](create-group.md) | `createGroup` | `POST /v1/accounts/{account_id}/groups/create` |
| [`create_webhook_endpoint`](create-webhook-endpoint.md) | `createWebhookEndpoint` | `POST /v1/webhook-endpoints` |
| [`deactivate_webhook_endpoint`](deactivate-webhook-endpoint.md) | `deactivateWebhookEndpoint` | `POST /v1/webhook-endpoints/{endpoint_id}/deactivate` |
| [`delete_account`](delete-account.md) | `deleteAccount` | `DELETE /v1/accounts/{account_id}` |
| [`delete_conversation_label`](delete-conversation-label.md) | `deleteConversationLabel` | `POST /v1/accounts/{account_id}/conversations/labels/delete` |
| [`delete_webhook_endpoint`](delete-webhook-endpoint.md) | `deleteWebhookEndpoint` | `DELETE /v1/webhook-endpoints/{endpoint_id}` |
| [`edit_message`](edit-message.md) | `editMessage` | `POST /v1/messages/edit` |
| [`get_account`](get-account.md) | `getAccount` | `GET /v1/accounts/{account_id}` |
| [`get_account_auth_state`](get-account-auth-state.md) | `getAccountAuthState` | `GET /v1/accounts/{account_id}/auth` |
| [`get_account_operation`](get-account-operation.md) | `getAccountOperation` | `GET /v1/account-operations/{operation_id}` |
| [`get_active_call`](get-active-call.md) | `getActiveCall` | `GET /v1/calls/active` |
| [`get_contact`](get-contact.md) | `getContact` | `GET /v1/accounts/{account_id}/contacts/info` |
| [`get_contact_membership`](get-contact-membership.md) | `getContactMembership` | `GET /v1/accounts/{account_id}/contacts/membership` |
| [`get_conversation`](get-conversation.md) | `getConversation` | `GET /v1/accounts/{account_id}/conversations/info` |
| [`get_group`](get-group.md) | `getGroup` | `GET /v1/accounts/{account_id}/groups/info` |
| [`get_group_invite_code`](get-group-invite-code.md) | `getGroupInviteCode` | `GET /v1/accounts/{account_id}/groups/invite-code` |
| [`get_post`](get-post.md) | `getPost` | `POST /v1/accounts/{account_id}/posts/info` |
| [`get_webhook_endpoint`](get-webhook-endpoint.md) | `getWebhookEndpoint` | `GET /v1/webhook-endpoints/{endpoint_id}` |
| [`get_workspace`](get-workspace.md) | `getWorkspace` | `GET /v1/workspace` |
| [`hangup_call`](hangup-call.md) | `hangupCall` | `POST /v1/calls/{call_id}/hangup` |
| [`import_account_auth_session`](import-account-auth-session.md) | `importAccountAuthSession` | `POST /v1/accounts/{account_id}/auth/session` |
| [`leave_group`](leave-group.md) | `leaveGroup` | `POST /v1/accounts/{account_id}/groups/leave` |
| [`list_accounts`](list-accounts.md) | `listAccounts` | `GET /v1/accounts` |
| [`list_api_keys`](list-api-keys.md) | `listApiKeys` | `GET /v1/api-keys` |
| [`list_contact_blocklist`](list-contact-blocklist.md) | `listContactBlocklist` | `GET /v1/accounts/{account_id}/contacts/blocklist` |
| [`list_contacts`](list-contacts.md) | `listContacts` | `GET /v1/accounts/{account_id}/contacts` |
| [`list_conversation_labels`](list-conversation-labels.md) | `listConversationLabels` | `GET /v1/accounts/{account_id}/conversations/labels` |
| [`list_conversation_members`](list-conversation-members.md) | `listConversationMembers` | `GET /v1/accounts/{account_id}/conversations/members` |
| [`list_conversations`](list-conversations.md) | `listConversations` | `GET /v1/accounts/{account_id}/conversations` |
| [`list_group_join_requests`](list-group-join-requests.md) | `listGroupJoinRequests` | `GET /v1/accounts/{account_id}/groups/join-requests` |
| [`list_groups`](list-groups.md) | `listGroups` | `GET /v1/accounts/{account_id}/groups` |
| [`list_post_comments`](list-post-comments.md) | `listPostComments` | `POST /v1/accounts/{account_id}/posts/comments/list` |
| [`list_posts`](list-posts.md) | `listPosts` | `GET /v1/accounts/{account_id}/posts` |
| [`list_provider_regions`](list-provider-regions.md) | `listProviderRegions` | `GET /v1/providers/{provider}/regions` |
| [`list_webhook_endpoints`](list-webhook-endpoints.md) | `listWebhookEndpoints` | `GET /v1/webhook-endpoints` |
| [`mark_conversation_read`](mark-conversation-read.md) | `markConversationRead` | `POST /v1/accounts/{account_id}/conversations/read` |
| [`mark_conversation_unread`](mark-conversation-unread.md) | `markConversationUnread` | `POST /v1/accounts/{account_id}/conversations/unread` |
| [`mute_conversation`](mute-conversation.md) | `muteConversation` | `POST /v1/accounts/{account_id}/conversations/mute` |
| [`pin_conversation`](pin-conversation.md) | `pinConversation` | `POST /v1/accounts/{account_id}/conversations/pin` |
| [`pin_message`](pin-message.md) | `pinMessage` | `POST /v1/messages/pin` |
| [`react_message`](react-message.md) | `reactMessage` | `POST /v1/messages/reaction` |
| [`reconnect_account_runtime`](reconnect-account-runtime.md) | `reconnectAccountRuntime` | `POST /v1/accounts/{account_id}/runtime/reconnect` |
| [`refresh_account_runtime`](refresh-account-runtime.md) | `refreshAccountRuntime` | `POST /v1/accounts/{account_id}/runtime/refresh` |
| [`reply_post_comment`](reply-post-comment.md) | `replyPostComment` | `POST /v1/accounts/{account_id}/posts/comments/reply` |
| [`request_conversation_history`](request-conversation-history.md) | `requestConversationHistory` | `POST /v1/accounts/{account_id}/conversations/history/request` |
| [`revoke_message`](revoke-message.md) | `revokeMessage` | `POST /v1/messages/revoke` |
| [`rotate_api_key`](rotate-api-key.md) | `rotateApiKey` | `POST /v1/api-keys/{key_id}/rotate` |
| [`send_message`](send-message.md) | `sendMessage` | `POST /v1/messages` |
| [`set_contact_note`](set-contact-note.md) | `setContactNote` | `POST /v1/accounts/{account_id}/contacts/note` |
| [`set_conversation_label_members`](set-conversation-label-members.md) | `setConversationLabelMembers` | `POST /v1/accounts/{account_id}/conversations/labels` |
| [`set_group_join_approval_mode`](set-group-join-approval-mode.md) | `setGroupJoinApprovalMode` | `POST /v1/accounts/{account_id}/groups/join-approval-mode` |
| [`start_account_auth`](start-account-auth.md) | `startAccountAuth` | `POST /v1/accounts/{account_id}/auth/start` |
| [`start_account_qr_auth`](start-account-qr-auth.md) | `startAccountQrAuth` | `POST /v1/accounts/{account_id}/auth/qr/start` |
| [`start_account_runtime`](start-account-runtime.md) | `startAccountRuntime` | `POST /v1/accounts/{account_id}/runtime/start` |
| [`stop_account_runtime`](stop-account-runtime.md) | `stopAccountRuntime` | `POST /v1/accounts/{account_id}/runtime/stop` |
| [`submit_account_auth_code`](submit-account-auth-code.md) | `submitAccountAuthCode` | `POST /v1/accounts/{account_id}/auth/code` |
| [`submit_account_auth_password`](submit-account-auth-password.md) | `submitAccountAuthPassword` | `POST /v1/accounts/{account_id}/auth/password` |
| [`submit_account_passkey_response`](submit-account-passkey-response.md) | `submitAccountPasskeyResponse` | `POST /v1/accounts/{account_id}/auth/passkey-response` |
| [`unblock_contact`](unblock-contact.md) | `unblockContact` | `POST /v1/accounts/{account_id}/contacts/unblock` |
| [`unmute_conversation`](unmute-conversation.md) | `unmuteConversation` | `POST /v1/accounts/{account_id}/conversations/unmute` |
| [`unpin_conversation`](unpin-conversation.md) | `unpinConversation` | `POST /v1/accounts/{account_id}/conversations/unpin` |
| [`update_account`](update-account.md) | `updateAccount` | `PATCH /v1/accounts/{account_id}` |
| [`update_api_key_status`](update-api-key-status.md) | `updateApiKeyStatus` | `PATCH /v1/api-keys/{key_id}` |
| [`update_group_info`](update-group-info.md) | `updateGroupInfo` | `POST /v1/accounts/{account_id}/groups/update-info` |
| [`update_group_join_requests`](update-group-join-requests.md) | `updateGroupJoinRequests` | `POST /v1/accounts/{account_id}/groups/join-requests/update` |
| [`update_group_members`](update-group-members.md) | `updateGroupMembers` | `POST /v1/accounts/{account_id}/groups/members` |
| [`update_webhook_endpoint`](update-webhook-endpoint.md) | `updateWebhookEndpoint` | `PATCH /v1/webhook-endpoints/{endpoint_id}` |
| [`update_workspace`](update-workspace.md) | `updateWorkspace` | `PATCH /v1/workspace` |
| [`upsert_conversation_label`](upsert-conversation-label.md) | `upsertConversationLabel` | `POST /v1/accounts/{account_id}/conversations/labels/upsert` |
