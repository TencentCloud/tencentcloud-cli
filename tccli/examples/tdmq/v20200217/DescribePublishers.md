**Example 1: 获取生产者列表**



Input: 

```
tccli tdmq DescribePublishers --cli-unfold-argument  \
    --ClusterId pulsar-xk3ne8k2qkp8 \
    --Namespace devNs \
    --Topic devTopic \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Publishers": [
            {
                "ProducerId": 0,
                "ProducerName": "p1",
                "Address": "127.0.0.1",
                "ClientVersion": "2.9",
                "MsgRateIn": 0,
                "MsgThroughputIn": 0,
                "AverageMsgSize": 0,
                "ConnectedSince": "dev",
                "Partition": 0
            }
        ],
        "RequestId": "1004f1de-6fb8-41d5-965e-3aae8c87183a"
    }
}
```

