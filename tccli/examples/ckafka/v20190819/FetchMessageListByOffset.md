**Example 1: 根据offset查询消息**



Input: 

```
tccli ckafka FetchMessageListByOffset --cli-unfold-argument  \
    --InstanceId xxx \
    --Topic xxx \
    --Partition 1 \
    --Offset 1 \
    --SinglePartitionRecordNumber 20
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "Topic": "xxx",
                "Partition": 2,
                "Offset": 1,
                "Key": "xxx",
                "Value": "xxx",
                "Timestamp": 1
            },
            {
                "Topic": "xxx",
                "Partition": 2,
                "Offset": 2,
                "Key": "xxx",
                "Value": "xxx",
                "Timestamp": 1
            }
        ],
        "RequestId": "62d589e0-53d5-47e0-95ff-237c48b8fb77"
    }
}
```

