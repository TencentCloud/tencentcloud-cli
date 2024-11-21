**Example 1: 获取命名空间列表**



Input: 

```
tccli tdmq DescribeEnvironments --cli-unfold-argument  \
    --EnvironmentId devNs \
    --Offset 1 \
    --Limit 1 \
    --ClusterId pulsar-xk3ne8k2qkp8
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EnvironmentSet": [
            {
                "EnvironmentId": "devNs",
                "Remark": "devDemo",
                "MsgTTL": 100,
                "CreateTime": "2020-09-22 00:00:00",
                "UpdateTime": "2020-09-22 00:00:00",
                "NamespaceName": "devNs",
                "NamespaceId": "nsId",
                "TopicNum": 0,
                "RetentionPolicy": {
                    "TimeInMinutes": 0,
                    "SizeInMB": 0
                },
                "AutoSubscriptionCreation": true
            }
        ],
        "RequestId": "1004f1de-6fb8-41d5-965e-3aae8c87183a"
    }
}
```

