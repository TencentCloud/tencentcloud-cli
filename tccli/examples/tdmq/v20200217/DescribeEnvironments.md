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
                "RetentionPolicy": {
                    "TimeInMinutes": 0,
                    "SizeInMB": 0
                },
                "TopicNum": 0,
                "MsgTTL": 0,
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```

