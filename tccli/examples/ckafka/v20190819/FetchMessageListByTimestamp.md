**Example 1: 消息查询**



Input: 

```
tccli ckafka FetchMessageListByTimestamp --cli-unfold-argument  \
    --InstanceId xxx \
    --Topic xxx \
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
                "Topic": "abc",
                "Partition": 0,
                "Offset": 0,
                "Key": "abc",
                "Value": "abc",
                "Timestamp": 0,
                "Headers": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

