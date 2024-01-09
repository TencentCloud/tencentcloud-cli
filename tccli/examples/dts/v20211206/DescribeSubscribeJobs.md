**Example 1: 查询订阅任务列表**



Input: 

```
tccli dts DescribeSubscribeJobs --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "SubscribeId": "subs-5ft0e2nrc0",
                "SubscribeName": "name-5ft0e2nrc0",
                "Topic": "topic-subs-5ft0e2nrc0-cdb-kdxona7h",
                "Product": "mysql",
                "InstanceId": "cdb-kdxona7h",
                "InstanceStatus": "running",
                "Status": "normal",
                "SubsStatus": "running",
                "ModifyTime": "2023-10-01 12:00:00",
                "CreateTime": "2023-09-01 12:00:00",
                "IsolateTime": "0000-00-00 00:00:00",
                "ExpireTime": "2023-11-01 12:00:00",
                "OfflineTime": "0000-00-00 00:00:00",
                "PayType": 0,
                "AutoRenewFlag": 0,
                "Region": "ap-guangzhou",
                "AccessType": "cdb",
                "Endpoints": [
                    {
                        "DatabaseRegion": "ap-guangzhou",
                        "InstanceId": "cdb-kdxona7h",
                        "EncryptConn": "Encrypted",
                        "User": "root"
                    }
                ],
                "SubscribeVersion": "kafka"
            }
        ],
        "RequestId": "cd6eebd0-9405-11ee-9689-216abbbe2107"
    }
}
```

