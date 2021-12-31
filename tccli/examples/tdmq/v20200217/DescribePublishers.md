**Example 1: 获取生产者列表**



Input: 

```
tccli tdmq DescribePublishers --cli-unfold-argument  \
    --Sort.Name xx \
    --Sort.Order xx \
    --ClusterId xx \
    --Namespace xx \
    --Topic xx \
    --Limit 0 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "Publishers": [
            {
                "ConnectedSince": "xx",
                "MsgThroughputIn": 0.0,
                "ClientVersion": "xx",
                "ProducerId": 0,
                "Partition": 0,
                "AverageMsgSize": 0.0,
                "ProducerName": "xx",
                "Address": "xx",
                "MsgRateIn": 0.0
            }
        ]
    }
}
```

