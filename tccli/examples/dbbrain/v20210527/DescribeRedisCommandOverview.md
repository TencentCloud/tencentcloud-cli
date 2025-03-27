**Example 1: 查询实例访问命令列表**



Input: 

```
tccli dbbrain DescribeRedisCommandOverview --cli-unfold-argument  \
    --InstanceId crs-2il4docj \
    --Product redis \
    --StartTime 2025-03-17T15:36:29+00:00 \
    --EndTime 2025-03-17T15:39:29+00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "f58c83d0-0302-11f0-82f8-47cbad998253",
        "CmdList": [
            {
                "Cmd": "auth",
                "Count": 28300
            },
            {
                "Cmd": "select",
                "Count": 23884
            },
            {
                "Cmd": "eval",
                "Count": 23883
            },
            {
                "Cmd": "get",
                "Count": 17418
            },
            {
                "Cmd": "incrby",
                "Count": 14667
            },
            {
                "Cmd": "ping",
                "Count": 3825
            },
            {
                "Cmd": "set",
                "Count": 22
            }
        ]
    }
}
```

