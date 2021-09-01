**Example 1: 查询订阅详情**



Input: 

```
tccli tdmq DescribeCmqSubscriptionDetail --cli-unfold-argument  \
    --TopicName Conn
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SubscriptionSet": [
            {
                "SubscriptionName": "ConnSub",
                "SubscriptionId": "subsc-8y7fn4t2",
                "TopicOwner": 0,
                "MsgCount": 0,
                "LastModifyTime": 1590632987,
                "CreateTime": 1590632987,
                "BindingKey": null,
                "Endpoint": "test1",
                "FilterTags": [],
                "Protocol": "queue",
                "NotifyStrategy": "EXPONENTIAL_DECAY_RETRY",
                "NotifyContentFormat": "SIMPLIFIED"
            }
        ],
        "RequestId": "72cd2d9d-d666-45ad-963a-cf5065a1984c"
    }
}
```

