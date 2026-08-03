**Example 1: 查询会话历史消息记录**



Input: 

```
tccli adp DescribeConversationMessageList --cli-unfold-argument  \
    --ConversationId 27fe97d2-b9a7-457f-b2a2-73dc901f2959 \
    --Type 2 \
    --RecordQueryDirection 1
```

Output: 
```
{
    "Response": {
        "FirstRecordId": "req_65faffa4-0d6f-402d-8511-60eb472880ae",
        "HasMoreAfter": false,
        "HasMoreBefore": false,
        "LastRecordId": "rcd_70b72a39-b7fc-405f-a0b9-32f786a3effc",
        "MessageList": [
            {
                "ContentList": [
                    {
                        "CustomParamList": [],
                        "OptionCardList": [],
                        "QuoteInfoList": [],
                        "ReferenceList": [],
                        "TaskList": [],
                        "Tasks": [],
                        "Text": "你好",
                        "Type": "text"
                    }
                ],
                "ConversationId": "27fe97d2-b9a7-457f-b2a2-73dc901f2959",
                "Icon": "",
                "MessageId": "user_65faffa4-0d6f-402d-8511-60eb472880ae_turn_65faffa4-0d6f-402d-8511-60eb472880ae_content",
                "Name": "question",
                "RecordId": "req_65faffa4-0d6f-402d-8511-60eb472880ae",
                "Role": "user",
                "Status": "success",
                "StatusDesc": "回复完成",
                "Title": "用户提问",
                "Type": "question"
            }
        ],
        "RecordSummaryList": [
            {
                "ErrorInfo": null,
                "RecordId": "rcd_65faffa4-0d6f-402d-8511-60eb472880ae",
                "RelatedRecordId": "req_65faffa4-0d6f-402d-8511-60eb472880ae",
                "Status": "success",
                "TimeUsage": {
                    "Elapsed": "3139",
                    "FirstTokenCost": "3397",
                    "TotalCost": "3139"
                },
                "TokenUsage": {
                    "CachedTokens": "0",
                    "InputTokens": "17190",
                    "OutputTokens": "29",
                    "ReasoningTokens": "20",
                    "TotalTokens": "17219"
                }
            }
        ],
        "ResetInfo": {
            "ResetThroughRecordId": "",
            "ResetTime": "0"
        },
        "RequestId": "a36c0228-248b-4b38-8e5b-396aaf89ab41"
    }
}
```

