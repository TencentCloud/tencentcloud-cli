**Example 1: 消息查询**



Input: 

```
tccli ckafka FetchMessageListByTimestamp --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --Topic topic-test \
    --Partition 1 \
    --StartTime 1577808000000 \
    --SinglePartitionRecordNumber 20
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "Topic": "topic-test",
                "Partition": 0,
                "Offset": 0,
                "Key": "key",
                "Value": "value",
                "Timestamp": 0,
                "Headers": "head"
            }
        ],
        "RequestId": "84770b4b-df34-4ccf-8e22-41d3b1d0fe0d"
    }
}
```

