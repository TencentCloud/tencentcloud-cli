**Example 1: 消费者心跳接口**

SendConsumerHeartbeat

Input: 

```
tccli cls SendConsumerHeartbeat --cli-unfold-argument  \
    --ConsumerGroup test-123 \
    --Consumer test-123-1 \
    --LogsetId 6f6ded3f-948c-4616-9c7c-956a95d8c1a3 \
    --TopicPartitionsInfo.0.TopicID 6f6ded3f-948c-4616-9c7c-956a95d8c1a3 \
    --TopicPartitionsInfo.0.Partitions 1
```

Output: 
```
{
    "Response": {
        "ConsumerGroup": "test-123",
        "TopicPartitionsInfo": [
            {
                "TopicID": "6f6ded3f-948c-4616-9c7c-956a95d8c1a3",
                "Partitions": [
                    1
                ]
            }
        ],
        "RequestId": "6f6ded3f-948c-4616-9c7c-956a95d8c1a3"
    }
}
```

