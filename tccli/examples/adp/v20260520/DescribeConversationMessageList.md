**Example 1: 查询会话历史消息记录**



Input: 

```
tccli adp DescribeConversationMessageList --cli-unfold-argument  \
    --ConversationId e165174b-7576-47ce-9c71-59188df6b5db \
    --Type 1 \
    --Limit 50 \
    --RecordId  \
    --RecordQueryDirection 1
```

Output: 
```
{
    "Response": {
        "FirstRecordId": "uAQ_20260715_191619_939_quAEKJCT",
        "HasMoreAfter": false,
        "HasMoreBefore": false,
        "LastRecordId": "oxX_20260715_191643_698_cohcnDRd",
        "MessageList": [
            {
                "ContentList": [
                    {
                        "CustomParamList": [],
                        "CustomParams": [],
                        "OptionCardList": [],
                        "OptionCards": [],
                        "QuoteInfoList": [],
                        "QuoteInfos": [],
                        "ReferenceList": [],
                        "References": [],
                        "TaskList": [],
                        "Tasks": [],
                        "Text": "你好",
                        "Type": "text"
                    }
                ],
                "Contents": [
                    {
                        "CustomParamList": [],
                        "CustomParams": [],
                        "OptionCardList": [],
                        "OptionCards": [],
                        "QuoteInfoList": [],
                        "QuoteInfos": [],
                        "ReferenceList": [],
                        "References": [],
                        "TaskList": [],
                        "Tasks": [],
                        "Text": "你好",
                        "Type": "text"
                    }
                ],
                "ConversationId": "e165174b-7576-47ce-9c71-59188df6b5db",
                "Icon": "",
                "MessageId": "rpl_uAQ_20260715_191619_939_quAEKJCT",
                "Name": "question",
                "RecordId": "uAQ_20260715_191619_939_quAEKJCT",
                "Role": "user",
                "Status": "success",
                "StatusDesc": "回复完成",
                "Title": "用户提问",
                "Type": "question"
            }
        ],
        "Messages": [
            {
                "ContentList": [
                    {
                        "CustomParamList": [],
                        "CustomParams": [],
                        "OptionCardList": [],
                        "OptionCards": [],
                        "QuoteInfoList": [],
                        "QuoteInfos": [],
                        "ReferenceList": [],
                        "References": [],
                        "TaskList": [],
                        "Tasks": [],
                        "Text": "你好",
                        "Type": "text"
                    }
                ],
                "Contents": [
                    {
                        "CustomParamList": [],
                        "CustomParams": [],
                        "OptionCardList": [],
                        "OptionCards": [],
                        "QuoteInfoList": [],
                        "QuoteInfos": [],
                        "ReferenceList": [],
                        "References": [],
                        "TaskList": [],
                        "Tasks": [],
                        "Text": "你好",
                        "Type": "text"
                    }
                ],
                "ConversationId": "e165174b-7576-47ce-9c71-59188df6b5db",
                "Icon": "",
                "MessageId": "rpl_uAQ_20260715_191619_939_quAEKJCT",
                "Name": "question",
                "RecordId": "uAQ_20260715_191619_939_quAEKJCT",
                "Role": "user",
                "Status": "success",
                "StatusDesc": "回复完成",
                "Title": "用户提问",
                "Type": "question"
            }
        ],
        "ResetInfo": {
            "ResetThroughRecordId": "oxX_20260715_191643_698_cohcnDRd",
            "ResetTime": "1784561474000"
        },
        "RequestId": "b6fbe0ec-8e8f-4ed4-afd2-7279e732f020"
    }
}
```

