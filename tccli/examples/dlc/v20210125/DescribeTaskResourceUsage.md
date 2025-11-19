**Example 1: 任务洞察资源用量**



Input: 

```
tccli dlc DescribeTaskResourceUsage --cli-unfold-argument  \
    --TaskInstanceId 15eb48854c1c11f083e8525400e26adf
```

Output: 
```
{
    "Response": {
        "RequestId": "请求ID的值",
        "CoreInfo": {
            "Timestamp": [
                1750238853000
            ],
            "CoreUsage": [
                1
            ]
        }
    }
}
```

