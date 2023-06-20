**Example 1: 查询数据引擎资源使用情况**

查询数据引擎资源使用情况

Input: 

```
tccli dlc DescribeEngineUsageInfo --cli-unfold-argument  \
    --DataEngineId abc
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Used": 0,
        "Available": 0,
        "RequestId": "abc"
    }
}
```

