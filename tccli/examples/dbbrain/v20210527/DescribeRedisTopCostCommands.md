**Example 1: DescribeRedisTopCostCommands**

获取访问命令 TOP N

Input: 

```
tccli dbbrain DescribeRedisTopCostCommands --cli-unfold-argument  \
    --StartTime 2025-09-03T10:41:59+08:00 \
    --EndTime 2025-09-03T10:41:59+08:00 \
    --InstanceId crs-qjdkzcsat \
    --Product redis \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "e8ceb4ae-871f-4587-b379-f694ba395686",
        "TopCostCmdList": [
            {
                "Cmd": "ping",
                "MaxCost": 2
            },
            {
                "Cmd": "auth",
                "MaxCost": 1
            }
        ]
    }
}
```

