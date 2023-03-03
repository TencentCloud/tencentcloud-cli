**Example 1: 无**

创建后付费分布式DB实例

Input: 

```
tccli dcdb CreateHourDCDBInstance --cli-unfold-argument  \
    --ShardCount 2 \
    --ShardMemory 2 \
    --ShardNodeCount 2 \
    --ShardStorage 10
```

Output: 
```
{
    "Response": {
        "RequestId": "14f6980a-7fe1-11ea-b896-525400542aa6",
        "InstanceIds": [
            "tdsql-xxxxxx"
        ],
        "DealName": "20200409111543",
        "FlowId": 1122
    }
}
```

