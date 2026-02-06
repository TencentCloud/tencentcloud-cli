**Example 1: 枚举队列（不区分用户）**



Input: 

```
tccli tdmq DescribeCmqQueues --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "730b0b3e-4c67-4a11-a15b-90e6f7c18402",
        "TotalCount": 1,
        "QueueList": [
            {
                "QueueId": "cmqq-bzgqn83nv",
                "QueueName": "test0829",
                "Qps": 5000,
                "Bps": 52428800,
                "MaxDelaySeconds": 3600,
                "MaxMsgHeapNum": 1000000,
                "PollingWaitSeconds": 3,
                "MsgRetentionSeconds": 7200,
                "VisibilityTimeout": 30,
                "MaxMsgSize": 1048576,
                "RewindSeconds": 0,
                "RetentionSizeInMB": 0,
                "CreateTime": 1724918937000,
                "LastModifyTime": 1724924966000,
                "ActiveMsgNum": 0,
                "InactiveMsgNum": 0,
                "DelayMsgNum": null,
                "RewindMsgNum": null,
                "MinMsgTime": null,
                "MaxUnackedMsgNum": 100000,
                "DeadLetterPolicy": {
                    "DeadLetterQueue": "rmqbroker-nj",
                    "Policy": 0,
                    "MaxTimeToLive": 0,
                    "MaxReceiveCount": 22
                },
                "DeadLetterSource": null,
                "Transaction": null,
                "TransactionPolicy": null,
                "CreateUin": null,
                "Trace": null,
                "Tags": null,
                "TenantId": "cmq-13179472",
                "NamespaceName": "CMQ_QUEUE-test0829",
                "Status": 1,
                "MaxMsgBacklogSize": 10737418240
            }
        ]
    }
}
```

