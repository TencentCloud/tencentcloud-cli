**Example 1: 获取队列列表**



Input: 

```
tccli cmq DescribeQueueDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "QueueSet": [
            {
                "Tags": [],
                "QueueId": "queue-kc7m75to",
                "QueueName": "test",
                "CreateUin": 20548499,
                "Qps": 5000,
                "Bps": 52428800,
                "MaxDelaySeconds": 3600,
                "MaxMsgHeapNum": 100000000,
                "PollingWaitSeconds": 0,
                "MsgRetentionSeconds": 345600,
                "VisibilityTimeout": 30,
                "MaxMsgSize": 65536,
                "RewindSeconds": 0,
                "CreateTime": 1581471003,
                "LastModifyTime": 1581471003,
                "Transaction": null,
                "DeadLetterSource": [],
                "DeadLetterPolicy": {
                    "DeadLetterQueue": "queue-0v0y40j4",
                    "DeadLetterQueueName": "test123",
                    "Policy": 0,
                    "MaxReceiveCount": 1,
                    "MaxTimeToLive": null
                },
                "TransactionPolicy": null,
                "ActiveMsgNum": 0,
                "InactiveMsgNum": 0,
                "DelayMsgNum": 0,
                "RewindMsgNum": 0,
                "MinMsgTime": 1582015467
            },
            {
                "Tags": [],
                "QueueId": "queue-0v0y40j4",
                "QueueName": "test123",
                "CreateUin": 20548499,
                "Qps": 5000,
                "Bps": 52428800,
                "MaxDelaySeconds": 3600,
                "MaxMsgHeapNum": 23232323,
                "PollingWaitSeconds": 3,
                "MsgRetentionSeconds": 232323,
                "VisibilityTimeout": 12,
                "MaxMsgSize": 121223,
                "RewindSeconds": 0,
                "CreateTime": 1581412802,
                "LastModifyTime": 1581471003,
                "Transaction": null,
                "DeadLetterSource": [
                    {
                        "QueueId": "queue-kc7m75to",
                        "QueueName": "test"
                    }
                ],
                "DeadLetterPolicy": null,
                "TransactionPolicy": null,
                "ActiveMsgNum": 0,
                "InactiveMsgNum": 0,
                "DelayMsgNum": 0,
                "RewindMsgNum": 0,
                "MinMsgTime": 1582015467
            },
            {
                "Tags": [],
                "QueueId": "queue-dvukxexc",
                "QueueName": "dead",
                "CreateUin": 20548499,
                "Qps": 5000,
                "Bps": 52428800,
                "MaxDelaySeconds": 3600,
                "MaxMsgHeapNum": 100000000,
                "PollingWaitSeconds": 0,
                "MsgRetentionSeconds": 345600,
                "VisibilityTimeout": 30,
                "MaxMsgSize": 65536,
                "RewindSeconds": 0,
                "CreateTime": 1581418590,
                "LastModifyTime": 1581418590,
                "Transaction": null,
                "DeadLetterSource": [],
                "DeadLetterPolicy": null,
                "TransactionPolicy": null,
                "ActiveMsgNum": 0,
                "InactiveMsgNum": 0,
                "DelayMsgNum": 0,
                "RewindMsgNum": 0,
                "MinMsgTime": 1582015467
            },
            {
                "Tags": [],
                "QueueId": "queue-cdb91yt6",
                "QueueName": "test21",
                "CreateUin": 20548499,
                "Qps": 5000,
                "Bps": 52428800,
                "MaxDelaySeconds": 3600,
                "MaxMsgHeapNum": 100000000,
                "PollingWaitSeconds": 0,
                "MsgRetentionSeconds": 345600,
                "VisibilityTimeout": 30,
                "MaxMsgSize": 65536,
                "RewindSeconds": 0,
                "CreateTime": 1581413384,
                "LastModifyTime": 1581413384,
                "Transaction": null,
                "DeadLetterSource": [],
                "DeadLetterPolicy": null,
                "TransactionPolicy": null,
                "ActiveMsgNum": 0,
                "InactiveMsgNum": 0,
                "DelayMsgNum": 0,
                "RewindMsgNum": 0,
                "MinMsgTime": 1582015467
            }
        ],
        "RequestId": "3f9a8b31-ac0d-4abd-8af2-e8564ceac30a"
    }
}
```

