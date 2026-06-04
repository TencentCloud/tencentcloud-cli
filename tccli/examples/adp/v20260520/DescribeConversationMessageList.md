**Example 1: ClawAgent模式会话消息查询**



Input: 

```
tccli adp DescribeConversationMessageList --cli-unfold-argument  \
    --ConversationId 4abd149a-e010-4a6c-bc52-1132658f149d \
    --Type 2 \
    --AppKey 1 \
    --RecordId msg_db8387b0-8b9f-49c9-9d05-253c7e9748a6_1 \
    --RecordQueryDirection 1 \
    --ShareCode 1 \
    --UserId 1 \
    --Limit 50 \
    --LoginSubAccountUin 700001046587 \
    --LoginUin 700001046587
```

Output: 
```
{
    "Response": {
        "FirstRecordId": "req_2f90efac-e51f-4c6e-b1b4-2e1234c1319d",
        "HasMoreAfter": false,
        "HasMoreBefore": false,
        "LastRecordId": "rcd_db8387b0-8b9f-49c9-9d05-253c7e9748a6",
        "Messages": [
            {
                "Contents": [
                    {
                        "CustomParams": [],
                        "OptionCards": [],
                        "QuoteInfos": [],
                        "References": [],
                        "Tasks": [],
                        "Text": "你好",
                        "Type": "text"
                    }
                ],
                "ConversationId": "4abd149a-e010-4a6c-bc52-1132658f149d",
                "Icon": "",
                "MessageId": "user_2f90efac-e51f-4c6e-b1b4-2e1234c1319d_content",
                "Name": "question",
                "RecordId": "req_2f90efac-e51f-4c6e-b1b4-2e1234c1319d",
                "Role": "user",
                "Status": "success",
                "StatusDesc": "回复完成",
                "Title": "用户提问",
                "Type": "question"
            }
        ],
        "RequestId": "59eb048d-7ad3-486b-85e5-e44f38178bba"
    }
}
```

