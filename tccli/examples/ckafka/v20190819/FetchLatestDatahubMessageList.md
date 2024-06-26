**Example 1: 根据offset查询消息**



Input: 

```
tccli ckafka FetchLatestDatahubMessageList --cli-unfold-argument  \
    --Name xxx \
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

