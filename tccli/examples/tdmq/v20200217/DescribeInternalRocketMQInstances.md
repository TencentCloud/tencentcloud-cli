**Example 1: 查询实例列表**

查询实例列表

Input: 

```
tccli tdmq DescribeInternalRocketMQInstances --cli-unfold-argument  \
    --Filters.0.Name Name \
    --Filters.0.Values test \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Instances": [
            {
                "InstanceId": "abc",
                "Name": "abc",
                "AppId": 1,
                "Uin": "abc",
                "PayStatus": "abc",
                "ClusterId": "abc",
                "MaxNamespaces": 1,
                "MaxTopics": 1,
                "MaxGroups": 1,
                "MaxQueuesPerTopic": 1,
                "RateLimit": 1,
                "IsVIP": true,
                "Retention": 0,
                "MaxRetention": 0,
                "MinRetention": 0,
                "AclEnabled": true
            }
        ],
        "RequestId": "abc"
    }
}
```

