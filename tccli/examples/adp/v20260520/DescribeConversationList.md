**Example 1: DescribeConversationList**



Input: 

```
tccli adp DescribeConversationList --cli-unfold-argument  \
    --Type 2 \
    --AppId 2056226819910862592
```

Output: 
```
{
    "Response": {
        "ConversationList": [
            {
                "AppId": "2056226819910862592",
                "ConversationId": "1038a37e-93b6-4f1f-b4cc-a73ce87a1c39",
                "CreateTime": "2026-05-18T21:58:38+08:00",
                "Type": 2,
                "UpdateTime": "2026-05-19T16:12:32+08:00"
            }
        ],
        "TotalCount": "4",
        "RequestId": "9b13a60e-39cc-4390-8a09-f6741b2c73f1"
    }
}
```

