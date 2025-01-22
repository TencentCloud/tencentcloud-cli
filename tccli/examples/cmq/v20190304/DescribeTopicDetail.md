**Example 1: 查询主题详情**



Input: 

```
tccli cmq DescribeTopicDetail --cli-unfold-argument  \
    --TagKey keyq \
    --Limit 1 \
    --TopicName testtopic \
    --Filters.0.Values testtopic \
    --Filters.0.Name TopicName \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TopicSet": [
            {
                "Tags": [],
                "TopicId": "topic-388k6x98",
                "TopicName": "testtopic",
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

