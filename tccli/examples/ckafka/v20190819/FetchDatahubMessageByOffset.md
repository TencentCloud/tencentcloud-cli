**Example 1: 消息查询**



Input: 

```
tccli ckafka FetchDatahubMessageByOffset --cli-unfold-argument  \
    --Name xxx \
    --Partition 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Result": {
            "Topic": "abc",
            "Partition": 0,
            "Offset": 0,
            "Key": "abc",
            "Value": "abc",
            "Timestamp": 0,
            "Headers": "abc"
        },
        "RequestId": "abc"
    }
}
```

