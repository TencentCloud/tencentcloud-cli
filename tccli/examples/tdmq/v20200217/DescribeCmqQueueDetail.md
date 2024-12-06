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
        "RequestId": "3d7a859c-4991-4d1d-bb8c-a25676c049d6",
        "QueueDescribe": {
            "QueueId": "cmqq-d88rxnbv2",
            "QueueName": "test1120",
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
            "CreateTime": 1732096676000,
            "LastModifyTime": 1732096676000,
            "ActiveMsgNum": 20,
            "InactiveMsgNum": 0,
            "DelayMsgNum": 0,
            "RewindMsgNum": null,
            "MinMsgTime": null,
            "MaxUnackedMsgNum": 100000,
            "DeadLetterPolicy": null,
            "DeadLetterSource": null,
            "Transaction": null,
            "TransactionPolicy": null,
            "CreateUin": null,
            "Trace": null,
            "Tags": null,
            "TenantId": "cmq-131242",
            "NamespaceName": "CMQ_QUEUE-test1120",
            "Status": 1,
            "MaxMsgBacklogSize": 10737418240
        }
    }
}
```

