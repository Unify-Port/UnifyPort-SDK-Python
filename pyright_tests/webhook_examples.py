"""Public contract examples exercise nested Webhook types without network access."""

from unifyport import models

# 公开样例覆盖稀疏事件与空值，避免生成类型在嵌套对象中退化成普通字典。
example_0: models.ContactUpdatedWebhookEvent = {
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

example_1: models.ContactUpdatedWebhookEvent = {
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

example_2: models.ContactUpdatedWebhookEvent = {
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

example_3: models.ConversationDisappearingMessagesUpdatedWebhookEvent = {
    "id": "evt_example_130476",
    "type": "conversation.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00.123000Z",
    "data": {
        "conversation": {"id": "100000000000002@lid", "type": "user"},
        "disappearing_messages": {"enabled": True, "duration_seconds": 86400},
        "actor": {"id": "100000000000003@lid", "type": "user", "name": "Example contact"},
        "event": {
            "kind": "conversation_updated",
            "change_type": "disappearing_messages",
            "changed_at": "2026-09-21T03:00:00.123000Z",
        },
    },
}

example_4: models.ConversationDisappearingMessagesUpdatedWebhookEvent = {
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

example_5: models.ConversationDisappearingMessagesUpdatedWebhookEvent = {
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

example_6: models.ConversationDisappearingMessagesUpdatedWebhookEvent = {
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

example_7: models.MessagePinUpdatedWebhookEvent = {
    "id": "evt_example_134940",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example_001",
    "occurred_at": "2026-09-21T03:00:00.123000Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "message": {
            "id": "MSG_PIN_TARGET",
            "pin": {
                "pinned": True,
                "duration_seconds": 86400,
                "expires_at": "2026-09-22T03:00:00.123000Z",
            },
        },
        "actor": {"id": "100000000000002@lid", "type": "user"},
        "sender": {"id": "100000000000003@lid", "type": "user"},
        "event": {
            "kind": "message_updated",
            "change_type": "message_pin",
            "changed_at": "2026-09-21T03:00:00.123000Z",
        },
    },
}

example_8: models.MessagePinUpdatedWebhookEvent = {
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

example_9: models.MessagePinUpdatedWebhookEvent = {
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

example_10: models.MessagePollReceivedWebhookEvent = {
    "id": "evt_example_138228",
    "type": "message.received",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00.123000Z",
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

example_11: models.MessagePollVoteUpdatedWebhookEvent = {
    "id": "evt_example_140068",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00.123000Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "message": {
            "id": "POLL_EXAMPLE",
            "type": "poll",
            "poll_vote": {
                "status": "decoded",
                "voter_id": "100000000000002@lid",
                "voted_at": "2026-09-22T03:00:00.123000Z",
                "selected_option_ids": ["option_monday"],
            },
        },
        "actor": {"id": "100000000000002@lid", "type": "user"},
        "event": {"kind": "message_updated", "change_type": "poll_vote"},
    },
}

example_12: models.MessagePollVoteUpdatedWebhookEvent = {
    "id": "evt_example_141122",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00.123000Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "message": {
            "id": "POLL_EXAMPLE",
            "type": "poll",
            "poll_vote": {
                "status": "decoded",
                "voter_id": "100000000000002@lid",
                "voted_at": "2026-09-22T03:00:00.123000Z",
                "selected_option_ids": ["option_tuesday"],
            },
        },
        "actor": {"id": "100000000000002@lid", "type": "user"},
        "event": {"kind": "message_updated", "change_type": "poll_vote"},
    },
}

example_13: models.MessagePollVoteUpdatedWebhookEvent = {
    "id": "evt_example_142170",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00.123000Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "message": {
            "id": "POLL_EXAMPLE",
            "type": "poll",
            "poll_vote": {
                "status": "decoded",
                "voter_id": "100000000000002@lid",
                "voted_at": "2026-09-22T03:00:00.123000Z",
                "selected_option_ids": [],
            },
        },
        "actor": {"id": "100000000000002@lid", "type": "user"},
        "event": {"kind": "message_updated", "change_type": "poll_vote"},
    },
}

example_14: models.MessagePollVoteUpdatedWebhookEvent = {
    "id": "evt_example_143180",
    "type": "message.updated",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00.123000Z",
    "data": {
        "conversation": {"id": "120000000000001@g.us", "type": "group"},
        "message": {
            "id": "POLL_EXAMPLE",
            "type": "poll",
            "poll_vote": {
                "status": "unavailable",
                "voter_id": "100000000000002@lid",
                "voted_at": "2026-09-22T03:00:00.123000Z",
                "reason": "unknown",
            },
        },
        "actor": {"id": "100000000000002@lid", "type": "user"},
        "event": {"kind": "message_updated", "change_type": "poll_vote"},
    },
}

example_15: models.MessagePollHistoryWebhookEvent = {
    "id": "evt_example_144750",
    "type": "conversation.history",
    "provider": "whatsapp",
    "account_id": "acc_example",
    "occurred_at": "2026-09-22T03:00:00.123000Z",
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

example_16: models.MessageLinkPreviewReceivedWebhookEvent = {
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

example_17: models.MessageLinkPreviewReceivedWebhookEvent = {
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

example_18: models.MessageLinkPreviewUpdatedWebhookEvent = {
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

example_19: models.MessageLinkPreviewUpdatedWebhookEvent = {
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

example_20: models.MessageLinkPreviewUpdatedWebhookEvent = {
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

example_21: models.MessageLinkPreviewHistoryWebhookEvent = {
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

example_22: models.MessageInteractiveReceivedWebhookEvent = {
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

example_23: models.MessageInteractiveReceivedWebhookEvent = {
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

example_24: models.MessageInteractiveReceivedWebhookEvent = {
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

example_25: models.MessageInteractiveReceivedWebhookEvent = {
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

example_26: models.MessageInteractiveUpdatedWebhookEvent = {
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

example_27: models.MessageInteractiveHistoryWebhookEvent = {
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

example_28: models.MessageCommerceReceivedWebhookEvent = {
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

example_29: models.MessageCommerceReceivedWebhookEvent = {
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

example_30: models.MessageCommerceUpdatedWebhookEvent = {
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

example_31: models.MessageCommerceUpdatedWebhookEvent = {
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

example_32: models.MessageCommerceHistoryWebhookEvent = {
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

example_33: models.WhatsAppMessageDeviceWebhookEvent = {
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

example_34: models.MessageReferralReceivedWebhookEvent = {
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

example_35: models.MessageReferralReceivedWebhookEvent = {
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

example_36: models.MessageReferralUpdatedWebhookEvent = {
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

example_37: models.ConversationHistoryWebhookEvent = {
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

example_38: models.ConversationHistoryWebhookEvent = {
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

example_39: models.MessageReferralHistoryWebhookEvent = {
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

example_40: models.CallMessageReceivedWebhookEvent = {
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

example_41: models.CallMessageUpdatedWebhookEvent = {
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

example_42: models.CallMessageUpdatedWebhookEvent = {
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

example_43: models.CallMessageUpdatedWebhookEvent = {
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

example_44: models.CallMessageUpdatedWebhookEvent = {
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

example_45: models.WhatsAppAccountAuthFailedWebhookEvent = {
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

example_46: models.AccountProfileUpdatedWebhookEvent = {
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

example_47: models.AccountProfileUpdatedWebhookEvent = {
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

example_48: models.AccountStartedWebhookEvent = {
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
