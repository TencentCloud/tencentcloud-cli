**Example 1: 查询实例错误日志**



Input: 

```
tccli cdb DescribeErrorLogData --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --Limit 400 \
    --StartTime 1585142640 \
    --Offset 0 \
    --KeyWords keywords0 \
    --EndTime 1585142640
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 1,
        "Items": [
            {
                "Content": "show master status",
                "Timestamp": 1585142640
            }
        ]
    }
}
```

