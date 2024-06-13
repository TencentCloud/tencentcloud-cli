**Example 1: 获取生产者概览**



Input: 

```
tccli tdmq DescribePublisherSummary --cli-unfold-argument  \
    --ClusterId abc \
    --Namespace abc \
    --Topic abc
```

Output: 
```
{
    "Response": {
        "MsgRateIn": 0,
        "MsgThroughputIn": 0,
        "PublisherCount": 0,
        "StorageSize": 0,
        "RequestId": "abc"
    }
}
```

