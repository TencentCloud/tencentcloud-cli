**Example 1: 获取生产者概览**



Input: 

```
tccli tdmq DescribePublisherSummary --cli-unfold-argument  \
    --Topic xx \
    --Namespace xx \
    --ClusterId xx
```

Output: 
```
{
    "Response": {
        "MsgRateIn": 0.0,
        "PublisherCount": 0,
        "StorageSize": 0,
        "RequestId": "xx",
        "MsgThroughputIn": 0.0
    }
}
```

