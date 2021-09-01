**Example 1: 获取帐号统计列表数据**

获取帐号统计列表数据

Input: 

```
tccli yunjing DescribeAccountStatistics --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AccountStatistics": [
            {
                "Username": "nginx",
                "MachineNum": 10
            }
        ],
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 100
    }
}
```

