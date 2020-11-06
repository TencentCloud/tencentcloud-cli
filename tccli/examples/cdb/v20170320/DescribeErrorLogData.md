**Example 1: Querying instance error logs**



Input: 

```
tccli cdb DescribeErrorLogData --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --StartTime 1585142640 \
    --EndTime 1585142640 \
    --KeyWords keywords0 \
    --Limit 400 \
    --Offset 0
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

