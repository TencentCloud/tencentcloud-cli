**Example 1: 枚举队列（不区分用户）**



Input: 

```
tccli tdmq DescribeCmqQueues --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2005,
        "QueueList": [
            {
                "Tags": [],
                "QueueId": "queue-6zs45b15",
                "QueueName": "QTA-5cd25c1e-5c7c-11ea-b510-460d8830b47a",
                "CreateUin": 100002742997,
                "Qps": 5000,
                "Bps": 52428800,
                "MaxDelaySeconds": 3600,
                "MaxMsgHeapNum": 10000000,
                "PollingWaitSeconds": 0,
                "MsgRetentionSeconds": 345600,
                "VisibilityTimeout": 30,
                "MaxMsgSize": 65536,
                "RewindSeconds": 43200,
                "CreateTime": 1583149980,
                "LastModifyTime": 1583149980,
                "Transaction": false,
                "DeadLetterSource": [],
                "DeadLetterPolicy": [],
                "TransactionPolicy": [],
                "ActiveMsgNum": 0,
                "InactiveMsgNum": 0,
                "DelayMsgNum": 0,
                "RewindMsgNum": 0,
                "MinMsgTime": 0
            }
        ],
        "RequestId": "6bab9048-bc14-4142-80c6-3ec119729bed"
    }
}
```

