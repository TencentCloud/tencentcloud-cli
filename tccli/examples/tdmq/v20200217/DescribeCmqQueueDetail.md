**Example 1: 获取cmq队列详情**



Input: 

```
tccli tdmq DescribeCmqQueueDetail --cli-unfold-argument  \
    --QueueName cmq-xxx
```

Output: 
```
{
    "Response": {
        "QueueDescribe": {
            "QueueId": "xx",
            "RewindSeconds": 1,
            "CreateUin": 1,
            "TenantId": "xx",
            "LastModifyTime": 1,
            "VisibilityTimeout": 1,
            "QueueName": "xx",
            "Trace": true,
            "Tags": [
                {
                    "TagKey": "xx",
                    "TagValue": "xx"
                }
            ],
            "NamespaceName": "xx",
            "RewindMsgNum": 1,
            "MaxDelaySeconds": 1,
            "TransactionPolicy": {
                "MaxQueryCount": 1,
                "FirstQueryInterval": 1
            },
            "MsgRetentionSeconds": 1,
            "DelayMsgNum": 1,
            "MaxMsgHeapNum": 1,
            "PollingWaitSeconds": 1,
            "Bps": 1,
            "InactiveMsgNum": 1,
            "DeadLetterPolicy": {
                "DeadLetterQueue": "xx",
                "Policy": 1,
                "MaxTimeToLive": 1,
                "MaxReceiveCount": 1
            },
            "ActiveMsgNum": 1,
            "MaxMsgSize": 1,
            "MinMsgTime": 1,
            "DeadLetterSource": [
                {
                    "QueueId": "xx",
                    "QueueName": "xx"
                }
            ],
            "Transaction": true,
            "Qps": 1,
            "CreateTime": 1
        },
        "RequestId": "xx"
    }
}
```

