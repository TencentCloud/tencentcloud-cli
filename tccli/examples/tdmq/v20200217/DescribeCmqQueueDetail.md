**Example 1: 获取cmq队列详情**

获取队列详情

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
            "QueueId": "abc",
            "QueueName": "abc",
            "Qps": 1,
            "Bps": 1,
            "MaxDelaySeconds": 1,
            "MaxMsgHeapNum": 1,
            "PollingWaitSeconds": 1,
            "MsgRetentionSeconds": 1,
            "VisibilityTimeout": 1,
            "MaxMsgSize": 1,
            "RewindSeconds": 1,
            "CreateTime": 1,
            "LastModifyTime": 1,
            "ActiveMsgNum": 1,
            "InactiveMsgNum": 1,
            "DelayMsgNum": 1,
            "RewindMsgNum": 1,
            "MinMsgTime": 1,
            "Transaction": true,
            "DeadLetterSource": [
                {
                    "QueueId": "abc",
                    "QueueName": "abc"
                }
            ],
            "DeadLetterPolicy": {
                "DeadLetterQueue": "abc",
                "Policy": 1,
                "MaxTimeToLive": 1,
                "MaxReceiveCount": 1
            },
            "TransactionPolicy": {
                "FirstQueryInterval": 1,
                "MaxQueryCount": 1
            },
            "CreateUin": 1,
            "Tags": null,
            "Trace": true,
            "TenantId": "abc",
            "NamespaceName": "abc",
            "Status": 0,
            "MaxUnackedMsgNum": 0,
            "MaxMsgBacklogSize": 0,
            "RetentionSizeInMB": 1
        },
        "RequestId": "abc"
    }
}
```

