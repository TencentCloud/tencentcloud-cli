**Example 1: 获取命名空间列表**



Input: 

```
tccli tdmq DescribeEnvironments --cli-unfold-argument  \
    --EnvironmentId abc \
    --Offset 1 \
    --Limit 1 \
    --ClusterId abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EnvironmentSet": [
            {
                "EnvironmentId": "abc",
                "Remark": "abc",
                "MsgTTL": 0,
                "CreateTime": "2020-09-22 00:00:00",
                "UpdateTime": "2020-09-22 00:00:00",
                "NamespaceId": "abc",
                "NamespaceName": "abc",
                "TopicNum": 0,
                "RetentionPolicy": {
                    "TimeInMinutes": 0,
                    "SizeInMB": 0
                },
                "AutoSubscriptionCreation": true
            }
        ],
        "RequestId": "abc"
    }
}
```

