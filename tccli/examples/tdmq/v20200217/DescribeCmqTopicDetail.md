**Example 1: cmq查询主题详情**



Input: 

```
tccli tdmq DescribeCmqTopicDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "cbeef60c-6525-484a-83e8-6c590e81e749",
        "TopicDescribe": {
            "TopicId": "cmqt-w4nb4z27",
            "TopicName": "rmqbroker-nj",
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
            "NamespaceName": "CMQ_TOPIC-rmqbroker-nj",
            "Status": 1,
            "BrokerType": 1,
            "SubscriptionCount": 1
        }
    }
}
```

