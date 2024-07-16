**Example 1: 获取队列详情**



Input: 

```
tccli tdmq DescribeRocketMQTopicStats --cli-unfold-argument  \
    --ClusterId rocketmq-7j8m97bqpx5d \
    --NamespaceId sla_rop_namespace_504344 \
    --TopicName topic-253348
```

Output: 
```
{
    "Response": {
        "RequestId": "5d5e666b-48d5-4abd-b628-fd2d15d0ee57",
        "TopicStatsList": [
            {
                "BrokerName": "rocketmq-7j8m97bqpx5d-1",
                "QueueId": 0,
                "MinOffset": 0,
                "MaxOffset": 1,
                "MessageCount": 1,
                "LastUpdateTimestamp": 1695298841001
            }
        ]
    }
}
```

