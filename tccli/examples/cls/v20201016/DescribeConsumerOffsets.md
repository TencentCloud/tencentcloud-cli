**Example 1: 获取消费组点位信息**

获取消费组点位信息

Input: 

```
tccli cls DescribeConsumerOffsets --cli-unfold-argument  \
    --ConsumerGroup test-123 \
    --TopicId 6f6ded3f-948c-4616-9c7c-956a95d8c1a3 \
    --PartitionId 0 \
    --From 1709708964 \
    --LogsetId 6f6ded3f-948c-4616-9c7c-956a95d8c1a3
```

Output: 
```
{
    "Response": {
        "ConsumerGroup": "test-123",
        "TopicPartitionOffsetsInfo": [
            {
                "TopicID": "6f6ded3f-948c-4616-9c7c-956a95d8c1a3",
                "PartitionOffsets": [
                    {
                        "PartitionId": 1,
                        "Offset": 1
                    }
                ]
            }
        ],
        "RequestId": "6f6ded3f-948c-4616-9c7c-956a95d8c1a3"
    }
}
```

