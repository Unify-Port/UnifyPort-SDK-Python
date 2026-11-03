"""Generated public Webhook examples; update the contract and regenerate."""

from unifyport import models

# 公开样例必须接受生成类型检查，保留稀疏字段和显式零值。
example_0: models.FacebookMessageReceivedWebhookEvent = {
    "id": "evt_facebook_example_1",
    "type": "message.received",
    "provider": "facebook",
    "account_id": "acc_example",
    "occurred_at": "2026-01-01T00:00:00.123456789Z",
    "data": {
        "account": {"provider_account_ref": "9007199254740997"},
        "conversation": {"id": "9007199254740995", "type": "user"},
        "sender": {"id": "9007199254740995", "type": "user"},
        "message": {
            "id": "9007199254740993",
            "direction": "inbound",
            "text": "Hello",
            "sent_at": "2026-01-01T00:00:00.123456789Z",
            "reply_to_message_id": "9007199254740991",
        },
        "event": {"kind": "message_received"},
    },
}
example_1: models.FacebookMessageReceivedWebhookEvent = {
    "id": "evt_facebook_example_2",
    "type": "message.received",
    "provider": "facebook",
    "account_id": "acc_example",
    "occurred_at": "2026-01-01T00:00:00.123456789Z",
    "data": {
        "account": {"provider_account_ref": "9007199254740997"},
        "conversation": {"id": "9007199254740995", "type": "user"},
        "sender": {"id": "9007199254740997", "type": "user"},
        "message": {"id": "9007199254740994", "direction": "outbound", "text": ""},
        "event": {"kind": "message_received"},
    },
}
example_2: models.FacebookMessageReceivedWebhookEvent = {
    "id": "evt_facebook_example_3",
    "type": "message.received",
    "provider": "facebook",
    "account_id": "acc_example",
    "occurred_at": "2026-01-01T00:00:00.123456789Z",
    "data": {
        "account": {"provider_account_ref": "9007199254740997"},
        "conversation": {"id": "9007199254740995", "type": "user"},
        "sender": {"id": "9007199254740995", "type": "user"},
        "message": {
            "id": "9007199254740996",
            "direction": "inbound",
            "attachments": [
                {
                    "id": "image_example",
                    "type": "image",
                    "url": "https://media.example.com/image.jpg",
                    "thumbnail_url": "https://media.example.com/preview.jpg",
                    "size": 0,
                    "metadata": {
                        "filename": "example.jpg",
                        "width": 0,
                        "height": 0,
                        "animated": False,
                        "download_status": "ready",
                    },
                },
                {
                    "id": "audio_example",
                    "type": "audio",
                    "metadata": {
                        "duration": 0,
                        "ptt": False,
                        "download_status": "failed",
                        "error_code": "download_failed",
                    },
                },
            ],
        },
        "event": {"kind": "message_received"},
    },
}
example_3: models.FacebookMessageReceivedWebhookEvent = {
    "id": "evt_facebook_example_4",
    "type": "message.received",
    "provider": "facebook",
    "account_id": "acc_example",
    "occurred_at": "2026-01-01T00:00:00.123456789Z",
    "data": {
        "account": {"provider_account_ref": "9007199254740997"},
        "conversation": {"id": "9007199254740995", "type": "user"},
        "sender": {"id": "9007199254740995", "type": "user"},
        "message": {
            "id": "9007199254740998",
            "direction": "inbound",
            "type": "sticker",
            "attachments": [
                {"type": "image", "metadata": {"sticker_id": "sticker_example", "animated": False}}
            ],
        },
        "event": {"kind": "message_received"},
    },
}
example_4: models.FacebookMessageReceivedWebhookEvent = {
    "id": "evt_facebook_example_5",
    "type": "message.received",
    "provider": "facebook",
    "account_id": "acc_example",
    "occurred_at": "2026-01-01T00:00:00.123456789Z",
    "data": {
        "account": {"provider_account_ref": "9007199254740997"},
        "conversation": {"id": "9007199254740995", "type": "user"},
        "sender": {"id": "9007199254740995", "type": "user"},
        "message": {
            "id": "9007199254740999",
            "direction": "inbound",
            "attachments": [
                {
                    "type": "document",
                    "metadata": {"filename": "example.pdf", "download_status": "restricted"},
                }
            ],
        },
        "event": {"kind": "message_received"},
    },
}
example_5: models.FacebookAccountAuthSucceededWebhookEvent = {
    "id": "evt_facebook_example_6",
    "type": "account.auth.succeeded",
    "provider": "facebook",
    "account_id": "acc_example",
    "occurred_at": "2026-01-01T00:00:00.123456789Z",
    "data": {
        "account": {"provider_account_ref": "9007199254740997"},
        "event": {"kind": "account_auth_succeeded", "runtime_status": "running"},
        "runtime_status": "running",
        "auth_status": "authorized",
    },
}
example_6: models.FacebookAccountStatusUpdatedWebhookEvent = {
    "id": "evt_facebook_example_7",
    "type": "account.status.updated",
    "provider": "facebook",
    "account_id": "acc_example",
    "occurred_at": "2026-01-01T00:00:00.123456789Z",
    "data": {
        "account": {"provider_account_ref": "9007199254740997"},
        "event": {"kind": "account_status_updated", "runtime_status": "error"},
        "runtime_status": "error",
        "last_error": "network_timeout",
    },
}
example_7: models.FacebookAccountAuthFailedWebhookEvent = {
    "id": "evt_facebook_example_8",
    "type": "account.auth.failed",
    "provider": "facebook",
    "account_id": "acc_example",
    "occurred_at": "2026-01-01T00:00:00.123456789Z",
    "data": {
        "account": {"provider_account_ref": "9007199254740997"},
        "event": {"kind": "account_auth_failed", "runtime_status": "disconnected"},
        "runtime_status": "disconnected",
        "auth_status": "failed",
        "last_error": "cookie_expired",
    },
}
example_8: models.ContactUpdatedWebhookEvent = {
    "id": "evt_example_127019",
    "type": "contact.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-20T03:00:00Z",
    "data": {
        "contact": {
            "id": "15550000002@s.whatsapp.net",
            "conversation_id": "100000000000002@lid",
            "address_book": {"full_name": "Example customer", "first_name": "Example"},
        },
        "event": {
            "kind": "contact_updated",
            "source": "address_book",
            "changed_fields": ["address_book.full_name", "address_book.first_name"],
            "changed_at": "2026-09-20T03:00:00Z",
        },
    },
}
example_9: models.ContactUpdatedWebhookEvent = {
    "id": "evt_example_127947",
    "type": "contact.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-20T03:05:00Z",
    "data": {
        "contact": {"id": "15550000002@s.whatsapp.net", "address_book": {"full_name": ""}},
        "event": {
            "kind": "contact_updated",
            "source": "address_book",
            "changed_fields": ["address_book.full_name"],
            "changed_at": "2026-09-20T03:05:00Z",
        },
    },
}
example_10: models.ContactUpdatedWebhookEvent = {
    "id": "evt_example_128706",
    "type": "contact.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-20T03:10:00Z",
    "data": {
        "contact": {
            "id": "100000000000002@lid",
            "conversation_id": "100000000000002@lid",
            "address_book": {"first_name": "Example"},
        },
        "event": {
            "kind": "contact_updated",
            "source": "full_sync",
            "changed_fields": ["address_book.first_name"],
        },
    },
}
example_11: models.ConversationDisappearingMessagesUpdatedWebhookEvent = {
    "id": "evt_example_130476",
    "type": "conversation.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00.123Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "disappearing_messages": {"enabled": True, "duration_seconds": 86400},
        "actor": {"id": "100000000000003@lid", "type": "user", "name": "Example contact"},
        "event": {
            "kind": "conversation_updated",
            "change_type": "disappearing_messages",
            "changed_at": "2026-09-21T03:00:00.123Z",
        },
    },
}
example_12: models.ConversationDisappearingMessagesUpdatedWebhookEvent = {
    "id": "evt_example_131405",
    "type": "conversation.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:05:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "disappearing_messages": {"enabled": True, "duration_seconds": 604800},
        "actor": {"id": "100000000000003@lid", "type": "user", "name": "Example contact"},
        "event": {
            "kind": "conversation_updated",
            "change_type": "disappearing_messages",
            "changed_at": "2026-09-21T03:05:00Z",
        },
    },
}
example_13: models.ConversationDisappearingMessagesUpdatedWebhookEvent = {
    "id": "evt_example_132320",
    "type": "conversation.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:10:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "disappearing_messages": {"enabled": False, "duration_seconds": 0},
        "actor": {"id": "100000000000003@lid", "type": "user", "name": "Example contact"},
        "event": {
            "kind": "conversation_updated",
            "change_type": "disappearing_messages",
            "changed_at": "2026-09-21T03:10:00Z",
        },
    },
}
example_14: models.ConversationDisappearingMessagesUpdatedWebhookEvent = {
    "id": "evt_example_133252",
    "type": "conversation.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:15:00Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "disappearing_messages": {"enabled": True, "duration_seconds": 86400},
        "event": {"kind": "conversation_updated", "change_type": "disappearing_messages"},
    },
}
example_15: models.MessagePinUpdatedWebhookEvent = {
    "id": "evt_example_134940",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00.123Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "message": {
            "id": "MSG_PIN_TARGET",
            "pin": {
                "pinned": True,
                "duration_seconds": 86400,
                "expires_at": "2026-09-22T03:00:00.123Z",
            },
        },
        "actor": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000003@lid", "type": "user"},
        "event": {
            "kind": "message_updated",
            "change_type": "message_pin",
            "changed_at": "2026-09-21T03:00:00.123Z",
        },
    },
}
example_16: models.MessagePinUpdatedWebhookEvent = {
    "id": "evt_example_136025",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:05:00Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "message": {"id": "MSG_PIN_TARGET", "pin": {"pinned": False}},
        "actor": {"id": "100000000000002@lid", "type": "user"},
        "event": {
            "kind": "message_updated",
            "change_type": "message_pin",
            "changed_at": "2026-09-21T03:05:00Z",
        },
    },
}
example_17: models.MessagePinUpdatedWebhookEvent = {
    "id": "evt_example_136901",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:10:00Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "message": {"id": "MSG_PIN_TARGET", "pin": {"pinned": True, "duration_seconds": 0}},
        "event": {"kind": "message_updated", "change_type": "message_pin"},
    },
}
example_18: models.MessagePollReceivedWebhookEvent = {
    "id": "evt_example_138228",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00.123Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "sender": {"id": "100000000000001@lid", "type": "user"},
        "message": {
            "id": "POLL_EXAMPLE",
            "type": "poll",
            "poll": {
                "question": "Which date works?",
                "options": [
                    {"id": "option_monday", "title": "Monday"},
                    {"id": "option_tuesday", "title": "Tuesday"},
                ],
                "max_selections": 1,
            },
            "direction": "outbound",
        },
        "event": {"kind": "message_received"},
    },
}
example_19: models.MessagePollVoteUpdatedWebhookEvent = {
    "id": "evt_example_140068",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00.123Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "message": {
            "id": "POLL_EXAMPLE",
            "type": "poll",
            "poll_vote": {
                "status": "decoded",
                "voter_id": "100000000000002@lid",
                "voted_at": "2026-09-22T03:00:00.123Z",
                "selected_option_ids": ["option_monday"],
            },
        },
        "actor": {"id": "100000000000002@lid", "type": "user"},
        "event": {"kind": "message_updated", "change_type": "poll_vote"},
    },
}
example_20: models.MessagePollVoteUpdatedWebhookEvent = {
    "id": "evt_example_141122",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00.123Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "message": {
            "id": "POLL_EXAMPLE",
            "type": "poll",
            "poll_vote": {
                "status": "decoded",
                "voter_id": "100000000000002@lid",
                "voted_at": "2026-09-22T03:00:00.123Z",
                "selected_option_ids": ["option_tuesday"],
            },
        },
        "actor": {"id": "100000000000002@lid", "type": "user"},
        "event": {"kind": "message_updated", "change_type": "poll_vote"},
    },
}
example_21: models.MessagePollVoteUpdatedWebhookEvent = {
    "id": "evt_example_142170",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00.123Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "message": {
            "id": "POLL_EXAMPLE",
            "type": "poll",
            "poll_vote": {
                "status": "decoded",
                "voter_id": "100000000000002@lid",
                "voted_at": "2026-09-22T03:00:00.123Z",
                "selected_option_ids": [],
            },
        },
        "actor": {"id": "100000000000002@lid", "type": "user"},
        "event": {"kind": "message_updated", "change_type": "poll_vote"},
    },
}
example_22: models.MessagePollVoteUpdatedWebhookEvent = {
    "id": "evt_example_143180",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00.123Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "message": {
            "id": "POLL_EXAMPLE",
            "type": "poll",
            "poll_vote": {
                "status": "unavailable",
                "voter_id": "100000000000002@lid",
                "voted_at": "2026-09-22T03:00:00.123Z",
                "reason": "unknown",
            },
        },
        "actor": {"id": "100000000000002@lid", "type": "user"},
        "event": {"kind": "message_updated", "change_type": "poll_vote"},
    },
}
example_23: models.MessagePollHistoryWebhookEvent = {
    "id": "evt_example_144750",
    "type": "conversation.history",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00.123Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "messages": [
            {
                "id": "POLL_EXAMPLE",
                "type": "poll",
                "poll": {
                    "question": "Which date works?",
                    "options": [
                        {"id": "option_monday", "title": "Monday"},
                        {"id": "option_tuesday", "title": "Tuesday"},
                    ],
                    "max_selections": 1,
                },
                "direction": "outbound",
            },
            {"id": "TEXT_EXAMPLE", "type": "text", "text": "Ordinary message"},
        ],
        "event": {"kind": "conversation_history"},
    },
}
example_24: models.MessageLinkPreviewReceivedWebhookEvent = {
    "id": "evt_example_146824",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000001@lid", "type": "user"},
        "message": {
            "id": "MSG_PREVIEW_EXAMPLE",
            "type": "link_preview",
            "text": "See https://example.com/product",
            "direction": "outbound",
            "link_preview": {
                "url": "https://example.com/product",
                "title": "Example product",
                "description": "Product introduction",
            },
        },
        "event": {"kind": "message_received"},
    },
}
example_25: models.MessageLinkPreviewReceivedWebhookEvent = {
    "id": "evt_example_147918",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:01:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_PREVIEW_PARTIAL",
            "type": "link_preview",
            "text": "See https://example.com/details",
            "direction": "inbound",
            "link_preview": {"url": "https://example.com/details"},
        },
        "event": {"kind": "message_received"},
    },
}
example_26: models.MessageLinkPreviewUpdatedWebhookEvent = {
    "id": "evt_example_149615",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:02:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_PREVIEW_EXAMPLE",
            "type": "link_preview",
            "link_preview": {
                "url": "https://example.com/product",
                "title": "Updated product title",
            },
        },
        "event": {"kind": "message_updated"},
    },
}
example_27: models.MessageLinkPreviewUpdatedWebhookEvent = {
    "id": "evt_example_150448",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:04:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_PREVIEW_EXAMPLE",
            "type": "link_preview",
            "link_preview": {"url": "https://example.com/product", "title": "", "description": ""},
        },
        "event": {"kind": "message_updated"},
    },
}
example_28: models.MessageLinkPreviewUpdatedWebhookEvent = {
    "id": "evt_example_151301",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:03:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_PREVIEW_EXAMPLE",
            "type": "text",
            "text": "Product information is being updated.",
        },
        "event": {"kind": "message_updated"},
    },
}
example_29: models.MessageLinkPreviewHistoryWebhookEvent = {
    "id": "evt_example_152781",
    "type": "conversation.history",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T04:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "messages": [
            {
                "id": "MSG_PREVIEW_EXAMPLE",
                "type": "link_preview",
                "text": "See https://example.com/product",
                "direction": "outbound",
                "link_preview": {"url": "https://example.com/product", "title": "Example product"},
                "referral": {"source": "ad", "source_id": "ad_example"},
                "sent_at": "2026-09-22T03:00:00Z",
            },
            {
                "id": "MSG_PLAIN_URL_EXAMPLE",
                "type": "text",
                "text": "https://example.com/plain",
                "sent_at": "2026-09-22T03:01:00Z",
            },
            {
                "id": "MSG_PRODUCT_EXAMPLE",
                "type": "product",
                "product": {"id": "product_example", "title": "Example product"},
            },
            {
                "id": "MSG_RESPONSE_EXAMPLE",
                "type": "interactive_response",
                "interactive_response": {"kind": "button", "selected_id": "details"},
            },
        ],
    },
}
example_30: models.MessageInteractiveReceivedWebhookEvent = {
    "id": "evt_example_155214",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_BUTTONS_EXAMPLE",
            "type": "interactive",
            "direction": "inbound",
            "text": "How can we help?",
            "interactive": {
                "kind": "buttons",
                "header": {"type": "text", "text": "Choose a topic"},
                "body": "How can we help?",
                "footer": "Select one option",
                "buttons": [
                    {"type": "reply", "id": "sales", "title": "Sales"},
                    {"type": "reply", "id": "support", "title": "Support"},
                ],
            },
            "referral": {"source": "ad", "source_id": "ad_example_001"},
        },
        "event": {"kind": "message_received"},
    },
}
example_31: models.MessageInteractiveReceivedWebhookEvent = {
    "id": "evt_example_156729",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_TEMPLATE_EXAMPLE",
            "type": "interactive",
            "direction": "inbound",
            "interactive": {
                "kind": "template",
                "header": {
                    "type": "image",
                    "attachment": {
                        "type": "image",
                        "mimetype": "image/jpeg",
                        "metadata": {"width": 640, "height": 480},
                    },
                },
                "body": "Choose how to continue",
                "buttons": [
                    {"type": "reply", "id": "details", "title": "Details"},
                    {
                        "type": "url",
                        "title": "Website",
                        "url": "https://example.com?campaign=example",
                    },
                    {"type": "phone", "title": "Call", "phone_number": "+12025550123"},
                ],
            },
        },
        "event": {"kind": "message_received"},
    },
}
example_32: models.MessageInteractiveReceivedWebhookEvent = {
    "id": "evt_example_158417",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_BUTTON_RESPONSE_EXAMPLE",
            "type": "interactive_response",
            "direction": "inbound",
            "text": "Support",
            "reply_to_message_id": "MSG_BUTTONS_EXAMPLE",
            "interactive_response": {
                "kind": "button",
                "selected_id": "support",
                "title": "Support",
            },
        },
        "event": {"kind": "message_received"},
    },
}
example_33: models.MessageInteractiveReceivedWebhookEvent = {
    "id": "evt_example_159498",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_TEMPLATE_RESPONSE_EXAMPLE",
            "type": "interactive_response",
            "direction": "inbound",
            "text": "Details",
            "interactive_response": {"kind": "template_button", "title": "Details"},
        },
        "event": {"kind": "message_received"},
    },
}
example_34: models.MessageInteractiveUpdatedWebhookEvent = {
    "id": "evt_example_161269",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_BUTTONS_EXAMPLE",
            "type": "interactive",
            "direction": "inbound",
            "interactive": {"kind": "buttons", "footer": "Support is available"},
        },
        "event": {"kind": "message_updated"},
    },
}
example_35: models.MessageInteractiveHistoryWebhookEvent = {
    "id": "evt_example_163002",
    "type": "conversation.history",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T04:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "messages": [
            {
                "id": "MSG_BUTTONS_EXAMPLE",
                "type": "interactive",
                "direction": "inbound",
                "text": "How can we help?",
                "interactive": {
                    "kind": "buttons",
                    "header": {"type": "text", "text": "Choose a topic"},
                    "body": "How can we help?",
                    "footer": "Select one option",
                    "buttons": [
                        {"type": "reply", "id": "sales", "title": "Sales"},
                        {"type": "reply", "id": "support", "title": "Support"},
                    ],
                },
                "referral": {"source": "ad", "source_id": "ad_example_001"},
                "sent_at": "2026-09-21T03:00:00Z",
            },
            {
                "id": "MSG_BUTTON_RESPONSE_EXAMPLE",
                "type": "interactive_response",
                "direction": "inbound",
                "text": "Support",
                "reply_to_message_id": "MSG_BUTTONS_EXAMPLE",
                "interactive_response": {
                    "kind": "button",
                    "selected_id": "support",
                    "title": "Support",
                },
                "sent_at": "2026-09-21T03:01:00Z",
            },
            {
                "id": "MSG_PRODUCT_EXAMPLE",
                "type": "product",
                "product": {"id": "product_example", "title": "Example product"},
            },
            {"id": "MSG_TEXT_EXAMPLE", "type": "text", "text": "Thank you."},
        ],
    },
}
example_36: models.MessageCommerceReceivedWebhookEvent = {
    "id": "evt_example_166040",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_PRODUCT_EXAMPLE_001",
            "type": "product",
            "direction": "inbound",
            "product": {
                "id": "product_example_001",
                "title": "Example product",
                "description": "Product introduction",
                "url": "https://example.com/product?campaign=example",
                "image_url": "https://example.com/product.jpg",
                "price": {"amount": "12.345", "currency": "USD"},
            },
            "referral": {"source": "ad", "source_id": "ad_example_001"},
        },
        "event": {"kind": "message_received"},
    },
}
example_37: models.MessageCommerceReceivedWebhookEvent = {
    "id": "evt_example_167385",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_ORDER_EXAMPLE_001",
            "type": "order",
            "direction": "inbound",
            "order": {
                "id": "order_example_001",
                "title": "Example order",
                "item_count": 0,
                "status": "inquiry",
                "total": {"amount": "0.000", "currency": "USD"},
            },
        },
        "event": {"kind": "message_received"},
    },
}
example_38: models.MessageCommerceUpdatedWebhookEvent = {
    "id": "evt_example_169196",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_PRODUCT_EXAMPLE_001",
            "type": "product",
            "direction": "inbound",
            "product": {"id": "product_example_001", "title": "Updated product title"},
        },
        "event": {"kind": "message_updated"},
    },
}
example_39: models.MessageCommerceUpdatedWebhookEvent = {
    "id": "evt_example_170114",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_ORDER_EXAMPLE_001",
            "type": "order",
            "direction": "inbound",
            "order": {
                "id": "order_example_001",
                "status": "accepted",
                "total": {"amount": "9007199254740.993"},
            },
        },
        "event": {"kind": "message_updated"},
    },
}
example_40: models.MessageCommerceHistoryWebhookEvent = {
    "id": "evt_example_171797",
    "type": "conversation.history",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T04:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "messages": [
            {
                "id": "MSG_PRODUCT_EXAMPLE_001",
                "type": "product",
                "direction": "inbound",
                "product": {
                    "id": "product_example_001",
                    "title": "Example product",
                    "description": "Product introduction",
                    "url": "https://example.com/product?campaign=example",
                    "image_url": "https://example.com/product.jpg",
                    "price": {"amount": "12.345", "currency": "USD"},
                },
                "referral": {"source": "ad", "source_id": "ad_example_001"},
                "sent_at": "2026-09-21T03:00:00Z",
                "sender": {"id": "100000000000002@lid"},
            },
            {
                "id": "MSG_ORDER_EXAMPLE_001",
                "type": "order",
                "direction": "inbound",
                "order": {
                    "id": "order_example_001",
                    "title": "Example order",
                    "item_count": 0,
                    "status": "inquiry",
                    "total": {"amount": "0.000", "currency": "USD"},
                },
                "sent_at": "2026-09-21T03:01:00Z",
                "sender": {"id": "100000000000002@lid"},
            },
            {
                "id": "MSG_TEXT_EXAMPLE_001",
                "type": "text",
                "text": "Thank you.",
                "direction": "inbound",
                "sent_at": "2026-09-21T03:02:00Z",
                "sender": {"id": "100000000000002@lid"},
            },
        ],
    },
}
example_41: models.WhatsAppMessageDeviceWebhookEvent = {
    "id": "evt_example_174750",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-23T08:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000001@lid", "device_id": 8},
        "message": {"id": "wa_message_example_001", "direction": "outbound", "text": "Example"},
    },
}
example_42: models.MessageReferralReceivedWebhookEvent = {
    "id": "evt_example_176338",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-20T03:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_AD_EXAMPLE_001",
            "text": "I would like to know more.",
            "direction": "inbound",
            "referral": {
                "source": "ad",
                "source_id": "ad_example_001",
                "source_url": "https://example.com/ad?campaign=demo&content=example",
                "title": "Example promotion",
                "body": "Learn more about the product.",
                "media_type": "image",
                "thumbnail_url": "https://example.com/ad-thumbnail.jpg",
                "media_url": "https://example.com/ad-image.jpg",
                "provider_extensions": {
                    "whatsapp": {
                        "ctwa_clid": "click_example_001",
                        "greeting_message_body": "Hello! How can we help?",
                        "automated_greeting_message_shown": True,
                        "automated_greeting_message_cta_type": "example_cta",
                        "source_app": "example_app",
                        "click_to_whatsapp_call": True,
                        "contains_auto_reply": False,
                        "contains_ctwa_flows_auto_reply": False,
                    }
                },
            },
        },
        "event": {"kind": "message_received"},
    },
}
example_43: models.MessageReferralReceivedWebhookEvent = {
    "id": "evt_example_178242",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-20T03:02:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "text": "Please send more details.",
            "direction": "inbound",
            "referral": {"source": "ad", "source_id": "ad_example_001"},
        },
        "event": {"kind": "message_received"},
    },
}
example_44: models.MessageReferralUpdatedWebhookEvent = {
    "id": "evt_example_179990",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-20T03:03:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000002@lid", "type": "user"},
        "message": {
            "id": "MSG_AD_EXAMPLE_001",
            "text": "I would like to know the price.",
            "direction": "inbound",
            "referral": {
                "source": "ad",
                "source_id": "ad_example_001",
                "source_url": "https://example.com/ad?campaign=demo&content=example",
                "title": "Example promotion",
                "body": "Learn more about the product.",
                "media_type": "image",
                "thumbnail_url": "https://example.com/ad-thumbnail.jpg",
                "media_url": "https://example.com/ad-image.jpg",
                "provider_extensions": {
                    "whatsapp": {
                        "ctwa_clid": "click_example_001",
                        "greeting_message_body": "Hello! How can we help?",
                        "automated_greeting_message_shown": True,
                        "automated_greeting_message_cta_type": "example_cta",
                        "source_app": "example_app",
                        "click_to_whatsapp_call": True,
                        "contains_auto_reply": False,
                        "contains_ctwa_flows_auto_reply": False,
                    }
                },
            },
        },
        "event": {"kind": "message_updated"},
    },
}
example_45: models.ConversationHistoryWebhookEvent = {
    "id": "evt_example_183342",
    "type": "conversation.history",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-28T03:01:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "history": {"source": "on_demand"},
        "messages": [
            {
                "id": "MSG_HISTORY_EXAMPLE_001",
                "type": "text",
                "text": "Earlier message.",
                "direction": "inbound",
                "sent_at": "2026-09-28T02:00:00Z",
                "sender": {"id": "100000000000002@lid"},
            }
        ],
    },
}
example_46: models.ConversationHistoryWebhookEvent = {
    "id": "evt_example_184219",
    "type": "conversation.history",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-28T03:02:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "history": {"source": "on_demand"},
        "messages": [],
    },
}
example_47: models.MessageReferralHistoryWebhookEvent = {
    "id": "evt_example_185631",
    "type": "conversation.history",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-20T04:00:00Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "messages": [
            {
                "id": "MSG_AD_EXAMPLE_001",
                "type": "text",
                "text": "I would like to know more.",
                "direction": "inbound",
                "sent_at": "2026-09-20T03:00:00Z",
                "sender": {"id": "100000000000002@lid", "name": "Example customer"},
                "referral": {
                    "source": "ad",
                    "source_id": "ad_example_001",
                    "source_url": "https://example.com/ad?campaign=demo&content=example",
                    "title": "Example promotion",
                    "body": "Learn more about the product.",
                    "media_type": "image",
                    "thumbnail_url": "https://example.com/ad-thumbnail.jpg",
                    "media_url": "https://example.com/ad-image.jpg",
                    "provider_extensions": {
                        "whatsapp": {
                            "ctwa_clid": "click_example_001",
                            "greeting_message_body": "Hello! How can we help?",
                            "automated_greeting_message_shown": True,
                            "automated_greeting_message_cta_type": "example_cta",
                            "source_app": "example_app",
                            "click_to_whatsapp_call": True,
                            "contains_auto_reply": False,
                            "contains_ctwa_flows_auto_reply": False,
                        }
                    },
                },
            },
            {
                "id": "MSG_NORMAL_EXAMPLE_002",
                "type": "text",
                "text": "Thank you.",
                "direction": "inbound",
                "sent_at": "2026-09-20T03:01:00Z",
                "sender": {"id": "100000000000002@lid"},
            },
        ],
    },
}
example_48: models.CallMessageReceivedWebhookEvent = {
    "id": "evt_example_call_offered_001",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-17T08:00:00Z",
    "data": {
        "conversation": {"id": "100000000000001@lid", "type": "user"},
        "sender": {"id": "100000000000001@lid", "type": "user"},
        "message": {
            "id": "call_record_example_001",
            "type": "call",
            "direction": "inbound",
            "call": {"id": "call_example_001", "media_type": "audio", "status": "offered"},
        },
    },
}
example_49: models.CallMessageUpdatedWebhookEvent = {
    "id": "evt_example_call_accepted_001",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-17T08:00:05Z",
    "data": {
        "conversation": {"id": "100000000000001@lid", "type": "user"},
        "sender": {"id": "100000000000001@lid", "type": "user"},
        "message": {
            "id": "call_record_example_001",
            "type": "call",
            "call": {
                "id": "call_example_001",
                "status": "accepted",
                "accepted_at": "2026-09-17T08:00:05Z",
            },
        },
    },
}
example_50: models.CallMessageUpdatedWebhookEvent = {
    "id": "evt_example_call_ended_001",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-17T08:00:10Z",
    "data": {
        "conversation": {"id": "100000000000001@lid", "type": "user"},
        "sender": {"id": "100000000000001@lid", "type": "user"},
        "message": {
            "id": "call_record_example_001",
            "type": "call",
            "call": {"id": "call_example_001", "status": "ended"},
        },
    },
}
example_51: models.CallMessageUpdatedWebhookEvent = {
    "id": "evt_example_call_ended_001",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-17T08:00:30Z",
    "data": {
        "message": {
            "id": "call_record_example_001",
            "type": "call",
            "call": {"id": "call_example_001", "status": "ended", "end_reason": "timeout"},
        }
    },
}
example_52: models.CallMessageUpdatedWebhookEvent = {
    "id": "evt_example_call_ended_002",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-17T08:01:10Z",
    "data": {
        "message": {
            "id": "call_record_example_002",
            "type": "call",
            "call": {
                "id": "call_example_002",
                "status": "ended",
                "end_reason": "rejected_elsewhere",
            },
        }
    },
}
example_53: models.WhatsAppAccountAuthFailedWebhookEvent = {
    "id": "evt_whatsapp_example_auth_failed",
    "type": "account.auth.failed",
    "provider": "whatsapp",
    "account_id": "acc_example_account",
    "occurred_at": "2026-09-07T01:00:00Z",
    "data": {
        "auth_status": "failed",
        "runtime_status": "disconnected",
        "event": {
            "kind": "account_auth_status",
            "auth_status": "failed",
            "runtime_status": "disconnected",
        },
        "error": {
            "code": "account_restricted",
            "numeric_code": "20102",
            "message": "Account login is restricted. Check the official WhatsApp app for details.",
        },
    },
}
example_54: models.AccountProfileUpdatedWebhookEvent = {
    "id": "evt_profile_7e91d2c4",
    "type": "account.profile.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-08-28T09:51:51Z",
    "data": {
        "account": {"provider_account_ref": "provider_account_example"},
        "profile": {
            "display_name": "Example Business",
            "business_name": "Example Business",
            "push_name": "Example Account",
            "avatar_url": "https://assets.example.com/accounts/avatar.jpg",
        },
        "event": {
            "kind": "account_profile_updated",
            "source": "self_rename",
            "changed_fields": ["display_name", "push_name", "business_name"],
        },
    },
}
example_55: models.AccountProfileUpdatedWebhookEvent = {
    "id": "evt_profile_avatar_a21e7d9c",
    "type": "account.profile.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-03T02:00:00Z",
    "data": {
        "account": {"provider_account_ref": "provider_account_example"},
        "profile": {
            "display_name": "Example Account",
            "push_name": "Example Account",
            "avatar_url": "https://assets.example.com/accounts/avatar-new.jpg",
        },
        "event": {
            "kind": "account_profile_updated",
            "source": "avatar_change",
            "changed_fields": ["avatar_url"],
        },
    },
}
example_56: models.AccountStartedWebhookEvent = {
    "id": "evt_acc_2b3c4d5e6f",
    "type": "account.started",
    "provider": "whatsapp",
    "account_id": "acc_8c21d0",
    "occurred_at": "2026-06-08T13:21:00Z",
    "data": {
        "runtime_status": "running",
        "event": {"kind": "account_started", "runtime_status": "running"},
    },
}
