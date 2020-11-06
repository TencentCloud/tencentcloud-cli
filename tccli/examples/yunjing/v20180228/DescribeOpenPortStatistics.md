**Example 1: 获取端口统计列表**

获取端口统计列表

Input: 

```
tccli yunjing DescribeOpenPortStatistics --cli-unfold-argument  \
    --Filters.0.Name Port \
    --Filters.0.Values 22 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "OpenPortStatistics": [
            {
                "Port": 80,
                "MachineNum": 10
            },
            {
                "Port": 3306,
                "MachineNum": 5
            }
        ],
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 100
    }
}
```

