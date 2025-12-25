**Example 1: 提交心跳信息**

提交心跳信息

Input: 

```
tccli cls CommitConsumerOffsets --cli-unfold-argument  \
    --ConsumerGroup test-123 \
    --Consumer test-123-01 \
    --LogsetId 6f6ded3f-948c-4616-9c7c-956a95d8c1a3 \
    --TopicPartitionOffsetsInfo.0.TopicID 6f6ded3f-948c-4616-9c7c-956a95d8c1a3 \
    --TopicPartitionOffsetsInfo.0.PartitionOffsets.0.PartitionId 1 \
    --TopicPartitionOffsetsInfo.0.PartitionOffsets.0.Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6f6ded3f-948c-4616-9c7c-956a95d8c1a3"
    }
}
```

