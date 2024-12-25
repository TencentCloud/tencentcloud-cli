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
                    "ConfigId": "apm-busi-log-cfg-6a79x94v",
                    "ConfigName": "toKafkaCfg",
                    "CollectPath": [
                        "/var/log"
                    ],
                    "Groups": [
                        {
                            "GroupId": "group-6a79x94v",
                            "GroupName": "java-demo",
                            "ClusterId": "cls-6a79x94v",
                            "ClusterName": "k8s-cls",
                            "ClusterType": "C",
                            "NamespaceName": "default",
                            "AssociateTime": "2022-12-23 10:23:12"
                        }
                    ],
                    "CreateTime": "2022-12-22 10:12:32",
                    "KafkaVIp": "10.23.0.4",
                    "KafkaAddress": "kafka.tencent.com",
                    "KafkaVPort": "30111",
                    "Topic": "TO_KAFKA_TOPIC",
                    "LineRule": ".*",
                    "CustomRule": ".*",
                    "EnableGlobalLineRule": true,
                    "EnableAuth": true,
                    "Username": "root",
                    "Password": "passxxxxxxxxx",
                    "KafkaInfos": [
                        {
                            "Topic": "TO_KAFKA_TOPIC",
                            "Path": [
                                "/var/log"
                            ],
                            "LineRule": ".*",
                            "CustomRule": "null"
                        }
                    ]
                }
            ]
        },
        "RequestId": "f1183607-d21b-dde1-d99c-94643d32c62e"
    }
}
```

