**Example 1: 查询主题详情**



Input: 

```
tccli cmq DescribeTopicDetail --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "TopicSet": [
            {
                "Tags": [],
                "TopicId": "topic-rga4l1o4",
                "TopicName": "ConnTopic",
                "CreateUin": 20548499,
                "MsgRetentionSeconds": 10000,
                "MaxMsgSize": 20000,
                "Qps": 10000,
                "FilterType": 1,
                "CreateTime": 1581516588,
                "LastModifyTime": 1581563581,
                "MsgCount": 0
            },
            {
                "Tags": [],
                "TopicId": "topic-388k6x98",
                "TopicName": "test123",
                "CreateUin": 20548499,
                "MsgRetentionSeconds": 86400,
                "MaxMsgSize": 65536,
                "Qps": 5000,
                "FilterType": 1,
                "CreateTime": 1581493669,
                "LastModifyTime": 1581495310,
                "MsgCount": 0
            }
        ],
        "RequestId": "68ebb46b-5eac-467a-9942-1a5da83a65ca"
    }
}
```

