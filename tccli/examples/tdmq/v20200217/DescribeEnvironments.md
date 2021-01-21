**Example 1: 获取命名空间列表**



Input: 

```
tccli tdmq DescribeEnvironments --cli-unfold-argument  \
    --EnvironmentId default \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EnvironmentSet": [
            {
                "EnvironmentId": "xx",
                "Remark": "xx",
                "NamespaceName": "xx",
                "UpdateTime": "2020-09-22 00:00:00",
                "NamespaceId": "xx",
                "MsgTTL": 0,
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "2235829c-2c9d-44b0-bce4-0ce0a147cce0"
    }
}
```

