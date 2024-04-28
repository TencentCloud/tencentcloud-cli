**Example 1: 会话记录**



Input: 

```
tccli lke GetMsgRecord --cli-unfold-argument  \
    --Type 2 \
    --Count 15 \
    --SessionId your session id \
    --LastRecordId 
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Content": "abc",
                "RecordId": "abc",
                "RelatedRecordId": "abc",
                "IsFromSelf": true,
                "FromName": "abc",
                "FromAvatar": "abc",
                "Timestamp": "abc",
                "HasRead": true,
                "Score": 1,
                "CanRating": true,
                "Type": 1,
                "References": [
                    {
                        "Id": "abc",
                        "Url": "abc",
                        "Type": 1,
                        "Name": "abc",
                        "DocId": "abc"
                    }
                ],
                "Reasons": [
                    "abc"
                ],
                "IsLlmGenerated": true,
                "ImageUrls": [
                    ""
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

