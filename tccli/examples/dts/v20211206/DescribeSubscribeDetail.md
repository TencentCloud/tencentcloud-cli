**Example 1: 查询订阅任务详情**



Input: 

```
tccli dts DescribeSubscribeDetail --cli-unfold-argument  \
    --SubscribeId subs-0b2up6hk4u
```

Output: 
```
{
    "Response": {
        "Region": "ap-guangzhou",
        "AccessType": "cdb",
        "AutoRenewFlag": 0,
        "Broker": "guangzhoutest-kafka-3.cdb-dts.tencentcs.com.cn:32339",
        "CreateTime": "2023-12-06 14:31:27",
        "Endpoints": [
            {
                "DatabaseRegion": "ap-guangzhou",
                "EncryptConn": "UnEncrypted",
                "InstanceId": "cdb-kdxona7h",
                "User": "root"
            }
        ],
        "ExpireTime": "0000-00-00 00:00:00",
        "InstanceId": "cdb-kdxona7h",
        "InstanceStatus": "running",
        "IsolateTime": "0000-00-00 00:00:00",
        "KafkaConfig": {
            "DistributeRules": [
                {
                    "DbPattern": "db1",
                    "RuleType": "cols",
                    "TablePattern": "table1",
                    "Columns": [
                        "id"
                    ]
                },
                {
                    "DbPattern": ".*",
                    "RuleType": "table",
                    "TablePattern": ".*",
                    "Columns": null
                }
            ],
            "NumberOfPartitions": 8
        },
        "ModifyTime": "2023-12-06 14:33:47",
        "OfflineTime": "0000-00-00 00:00:00",
        "PayType": 0,
        "Product": "mysql",
        "Protocol": "json",
        "Status": "normal",
        "SubsStatus": "running",
        "SubscribeId": "subs-0b2up6hk4u",
        "SubscribeName": "test",
        "SubscribeMode": "all",
        "Topic": "topic-subs-0b2up6hk4u-cdb-kdxona7h",
        "RequestId": "7bd11a40-9406-11ee-9689-216abbbe2107"
    }
}
```

