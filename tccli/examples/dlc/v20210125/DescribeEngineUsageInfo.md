**Example 1: 查询数据引擎资源使用情况**

查询数据引擎资源使用情况

Input: 

```
tccli dlc DescribeEngineUsageInfo --cli-unfold-argument  \
    --DataEngineId DataEngine-r0xxxkls
```

Output: 
```
{
    "Response": {
        "Available": 24,
        "RequestId": "6068a77d-5538-4e1d-a93f-cf5800c98e1b",
        "Total": 64,
        "Used": 40,
        "AvailPercent": 37
    }
}
```

