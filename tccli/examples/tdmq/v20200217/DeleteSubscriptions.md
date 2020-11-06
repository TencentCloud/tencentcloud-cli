**Example 1: 删除订阅关系**



Input: 

```
tccli tdmq DeleteSubscriptions --cli-unfold-argument  \
    --SubscriptionTopicSets.0.EnvironmentId default \
    --SubscriptionTopicSets.0.TopicName sun_topic \
    --SubscriptionTopicSets.0.SubscriptionName test_2_1
```

Output: 
```
{
    "Response": {
        "SubscriptionTopicSets": [
            {
                "EnvironmentId": "default",
                "SubscriptionName": "test_2_1",
                "TopicName": "sun_topic"
            }
        ],
        "RequestId": "cd14f283-ccb5-4b13-b858-a0a38fa6348b"
    }
}
```

