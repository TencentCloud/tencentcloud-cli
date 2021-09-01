**Example 1: cmq查询主题详情**



Input: 

```
tccli tdmq DescribeCmqTopicDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TopicDescribe": {
            "MsgCount": 1,
            "TopicId": "xx",
            "MaxMsgSize": 1,
            "Trace": true,
            "Tags": [
                {
                    "TagKey": "xx",
                    "TagValue": "xx"
                }
            ],
            "CreateUin": 1,
            "FilterType": 1,
            "TenantId": "xx",
            "LastModifyTime": 1,
            "MsgRetentionSeconds": 1,
            "NamespaceName": "xx",
            "Qps": 1,
            "CreateTime": 1,
            "TopicName": "xx"
        },
        "RequestId": "xx"
    }
}
```

