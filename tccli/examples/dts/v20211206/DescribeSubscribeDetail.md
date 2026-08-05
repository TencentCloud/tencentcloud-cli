**Example 1: 查询订阅任务详情**



Input: 

```
tccli dts DescribeSubscribeDetail --cli-unfold-argument  \
    --SubscribeId subs-p383pfn0
```

Output: 
```
{
    "Response": {
        "AccessType": "cdb",
        "AutoRenewFlag": 1,
        "Broker": "21.84.0.234:9092",
        "ConsumerSubnetId": "subnet-hyscbnec",
        "ConsumerVpcId": "vpc-gvemho5j",
        "CreateTime": "2026-07-28 19:38:57",
        "Endpoints": [
            {
                "CcnId": "",
                "CcnOwnerUin": "",
                "ChildInstanceId": "",
                "ChildInstanceType": "",
                "CvmInstanceId": "",
                "DatabaseNetEnv": "",
                "DatabaseRegion": "ap-guangzhou",
                "EncryptConn": "",
                "ExtraAttr": [],
                "HostName": "",
                "InstanceId": "tdsqlshard-dg58wo8z",
                "Password": "",
                "Port": 0,
                "SubnetId": "",
                "UniqDcgId": "",
                "UniqVpnGwId": "",
                "User": "user_00",
                "VpcId": ""
            }
        ],
        "Errors": null,
        "ExpireTime": "2026-08-28 19:38:57",
        "ExtraAttr": [],
        "InstanceClass": "small",
        "InstanceId": "tdsqlshard-dg58wo8z",
        "InstanceStatus": "running",
        "IsolateTime": "0000-00-00 00:00:00",
        "KafkaConfig": {
            "DefaultRuleType": "",
            "DistributeRules": [],
            "NumberOfPartitions": 0
        },
        "KafkaVersion": "2.8.1",
        "ModifyTime": "2026-08-05 16:35:33",
        "OfflineTime": "2026-09-04 19:38:57",
        "PayType": 0,
        "PipelineInfo": [],
        "Product": "tdsqlpercona",
        "Protocol": "",
        "Region": "ap-guangzhou",
        "RequestId": "3c417b08-e79d-473a-9de6-8ce0883df94e",
        "Status": "normal",
        "SubsStatus": "running",
        "SubscribeId": "subs-p383pfn0",
        "SubscribeMode": "dml",
        "SubscribeName": "jf-order-center-new-cluster",
        "SubscribeObjects": [
            {
                "Database": "order_center",
                "ObjectType": "table",
                "Tables": [
                    "deal"
                ]
            }
        ],
        "SubscribeVersion": "kafkaPro",
        "Tags": [
            {
                "TagKey": "备份负责人",
                "TagValue": "leohlliu"
            },
            {
                "TagKey": "二级业务",
                "TagValue": "[交易][order_center]_1230743"
            },
            {
                "TagKey": "一级业务",
                "TagValue": "[N][腾讯云计费产品其它]_979685"
            },
            {
                "TagKey": "负责人",
                "TagValue": "shaynefei"
            },
            {
                "TagKey": "运营产品",
                "TagValue": "腾讯云计费产品其它_1649"
            },
            {
                "TagKey": "运营部门",
                "TagValue": "计费产品中心_1013"
            }
        ],
        "Topic": "topic-subs-p383pfn0"
    }
}
```

