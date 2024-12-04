**Example 1: 根据offset查询消息**



Input: 

```
tccli ckafka FetchLatestDatahubMessageList --cli-unfold-argument  \
    --Name sourceName \
    --Partition 1 \
    --Offset 1 \
    --MessageCount 20
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

