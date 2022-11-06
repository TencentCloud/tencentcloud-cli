**Example 1: 枚举主题（不区分用户）**



Input: 

```
tccli tdmq DescribeCmqTopics --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 360,
        "TopicList": [
            {
                "Tags": [],
                "TopicId": "topic-catv1v6h",
                "TopicName": "QTA-6d1dfa44-5c70-11ea-8575-460d8830b47a",
                "CreateUin": 100002742997,
                "MsgRetentionSeconds": 86400,
                "MaxMsgSize": 65536,
                "Qps": 5000,
                "FilterType": 1,
                "CreateTime": 1583144853,
                "LastModifyTime": 1583144874,
                "MsgCount": 0
            },
            {
                "Tags": [],
                "TopicId": "topic-caysfz7j",
                "TopicName": "QTA-8f9162e2-5c6f-11ea-8dea-460d8830b47a",
                "CreateUin": 100002742997,
                "MsgRetentionSeconds": 86400,
                "MaxMsgSize": 1025,
                "Qps": 5000,
                "FilterType": 1,
                "CreateTime": 1583144481,
                "LastModifyTime": 1583144484,
                "MsgCount": 0
            }
        ],
        "RequestId": "104f0831-f81a-4d65-81e4-ff0c6217ae23"
    }
}
```

