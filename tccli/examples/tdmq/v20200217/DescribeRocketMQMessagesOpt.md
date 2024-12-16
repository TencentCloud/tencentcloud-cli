**Example 1: test**



Input: 

```
tccli tdmq DescribeRocketMQMessagesOpt --cli-unfold-argument  \
    --ClusterName tdmq_txy_gz_01 \
    --TenantId rocketmq-pngrpmk94d5o \
    --Namespace namespace \
    --QueryType simple \
    --Topic topic1 \
    --GroupId  \
    --MessageKey  \
    --MessageId  \
    --TaskId  \
    --BeginTime 1647792000000 \
    --EndTime 1648540224000 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "1d9ccf57-4ebb-493e-9367-4442ab4b2c56",
        "TotalCount": 100,
        "MessageSets": [
            {
                "QueueId": 1,
                "StoreSize": 336,
                "QueueOffset": 0,
                "SysFlag": 0,
                "BornTimestamp": 1648451275256,
                "BornHost": "xxx.xx.xx.xxx:25556",
                "StoreTimestamp": 1648451275033,
                "StoreHost": "xx.xx.xx.xx:8911",
                "MsgId": "C0A81FD3380C18B4AAC28E4AEDF8002C",
                "CommitLogOffset": 6198418,
                "BodyCRC": 1645723418,
                "ReconsumeTimes": 0,
                "PreparedTransactionOffset": 0,
                "Topic": "rocketmq-pngrpmk94d5o|namespace%xtopic1",
                "Flag": 0,
                "Keys": "KEY",
                "Tags": "TAG",
                "Properties": "xx",
                "MessageBody": "Hello RocketMQ Client this is a test message15"
            },
            {
                "QueueId": 12,
                "StoreSize": 336,
                "QueueOffset": 0,
                "SysFlag": 0,
                "BornTimestamp": 1648451275140,
                "BornHost": "xxx.xx.20.1x:25555",
                "StoreTimestamp": 1648451274915,
                "StoreHost": "x.xx.xxx.3x:8911",
                "MsgId": "C0A81FD3380C18B4AAC28E4AED84001D",
                "CommitLogOffset": 6500629,
                "BodyCRC": 310201237,
                "ReconsumeTimes": 0,
                "PreparedTransactionOffset": 0,
                "Topic": "rocketmq-pngrpmk94d5o|namespace%topic1",
                "Flag": 0,
                "Keys": "KEY",
                "Tags": "TAG",
                "Properties": "xx",
                "MessageBody": "Hello RocketMQ Client this is a test message10"
            }
        ],
        "TaskId": "7F00000159A418B4AAC20262936A0000"
    }
}
```

