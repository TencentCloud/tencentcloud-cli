**Example 1: 获取生产者列表**



Input: 

```
tccli tdmq DescribePublishers --cli-unfold-argument  \
    --ClusterId abc \
    --Namespace abc \
    --Topic abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Offset 0 \
    --Limit 0 \
    --Sort.Name abc \
    --Sort.Order abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Publishers": [
            {
                "ProducerId": 0,
                "ProducerName": "abc",
                "Address": "abc",
                "ClientVersion": "abc",
                "MsgRateIn": 0,
                "MsgThroughputIn": 0,
                "AverageMsgSize": 0,
                "ConnectedSince": "abc",
                "Partition": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

