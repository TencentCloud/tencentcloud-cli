**Example 1: 获取生产者概览**



Input: 

```
tccli tdmq DescribePublisherSummary --cli-unfold-argument  \
    --ClusterId pulsar-xk3ne8k2qkp8 \
    --Namespace devNs \
    --Topic devTopic
```

Output: 
```
{
    "Response": {
        "MsgRateIn": 0,
        "MsgThroughputIn": 0,
        "PublisherCount": 0,
        "StorageSize": 0,
        "RequestId": "1004f1de-6fb8-41d5-965e-3aae8c87183a"
    }
}
```

