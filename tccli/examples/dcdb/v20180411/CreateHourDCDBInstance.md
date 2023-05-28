**Example 1: 创建TDSQL按量计费实例**

创建TDSQL按量计费实例

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

