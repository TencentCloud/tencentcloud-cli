**Example 1: 获取多个投递项配置**



Input: 

```
tccli tsf DescribeDeliveryConfigs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "Content": [
                {
                    "ConfigId": "abc",
                    "ConfigName": "abc",
                    "CollectPath": [
                        "abc"
                    ],
                    "Groups": [
                        {
                            "GroupId": "abc",
                            "GroupName": "abc",
                            "ClusterId": "abc",
                            "ClusterName": "abc",
                            "ClusterType": "abc",
                            "NamespaceName": "abc",
                            "AssociateTime": "abc"
                        }
                    ],
                    "CreateTime": "abc",
                    "KafkaVIp": "abc",
                    "KafkaAddress": "abc",
                    "KafkaVPort": "abc",
                    "Topic": "abc",
                    "LineRule": "abc",
                    "CustomRule": "abc",
                    "EnableGlobalLineRule": true,
                    "EnableAuth": true,
                    "Username": "abc",
                    "Password": "abc",
                    "KafkaInfos": [
                        {
                            "Topic": "abc",
                            "Path": [
                                "abc"
                            ],
                            "LineRule": "abc",
                            "CustomRule": "abc"
                        }
                    ]
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

