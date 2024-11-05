**Example 1: 获取队列详情**



Input: 

```
tccli tdmq DescribeRocketMQTopicStats --cli-unfold-argument  \
    --ClusterId rocketmq-7j8m97bqpx5d \
    --NamespaceId test_namespace \
    --TopicName test_topic
```

Output: 
```
{
    "Response": {
        "RequestId": "5d5e666b-48d5-4abd-b628-fd2d15d0ee57",
        "TopicStatsList": [
            {
                "BrokerName": "rocketmq-7j8m97bqpx5d-1",
                "QueueId": 1,
                "MinOffset": 0,
                "MaxOffset": 100,
                "MessageCount": 100,
                "LastUpdateTimestamp": 1695298841001
            }
        ]
    }
}
```

