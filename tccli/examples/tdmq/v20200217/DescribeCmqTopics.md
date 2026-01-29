**Example 1: 枚举主题（不区分用户）**



Input: 

```
tccli tdmq DescribeCmqTopics --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3fe52209-a1e2-462c-a948-defb864d14e3",
        "TotalCount": 1,
        "TopicList": [
            {
                "TopicId": "cmqt-w4nb4zonn",
                "TopicName": "rtopic",
                "MaxMsgSize": 1048576,
                "FilterType": 1,
                "MsgRetentionSeconds": 86400,
                "Qps": 5000,
                "CreateTime": 1692691276000,
                "LastModifyTime": 1692691276000,
                "MsgCount": 0,
                "CreateUin": null,
                "Trace": null,
                "Tags": null,
                "TenantId": "cmq-1317947242",
                "NamespaceName": "CMQ_TOPIC-rtopic",
                "Status": 1,
                "BrokerType": 1,
                "SubscriptionCount": 1
            }
        ]
    }
}
```

