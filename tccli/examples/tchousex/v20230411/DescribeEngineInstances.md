**Example 1: 测试示例**



Input: 

```
tccli tchousex DescribeEngineInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name abc \
    --Filters.0.Values abc
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "TotalCount": 1,
        "InstancesList": [
            {
                "ClusterId": "abc",
                "ClusterName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

