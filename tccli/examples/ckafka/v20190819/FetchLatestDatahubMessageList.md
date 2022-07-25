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
        "RequestId": "weqnhgf-dfsfdsdsg-fdsgyrttjh-jjfdasdsa"
    }
}
```

