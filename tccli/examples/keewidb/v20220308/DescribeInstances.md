**Example 1: 示例1**

查询Keewidb实例列表

Input: 

```
tccli keewidb DescribeInstances --cli-unfold-argument  \
    --Status 0 1 2 \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "Appid": 251223628,
                "AutoRenewFlag": 0,
                "BillingMode": 1,
                "ClientLimit": 10000,
                "ClientLimitMax": 40000,
                "ClientLimitMin": 10000,
                "CloseTime": "0000-00-00 00:00:00",
                "Createtime": "2023-04-17 11:32:18",
                "DeadlineTime": "2023-05-17 11:32:18",
                "DiskSize": 0,
                "DtsStatus": 0,
                "Engine": "Keewidb",
                "InstanceId": "kee-4nmzc0ul",
                "InstanceName": "Keewidb_automation_is_awesome",
                "InstanceTags": [],
                "InstanceTitle": "添加实例中",
                "MonitorVersion": "5s",
                "NetLimit": 24,
                "NoAuth": false,
                "NodeSet": [
                    {
                        "NodeId": 336948,
                        "NodeType": 0,
                        "ZoneId": 100002,
                        "ZoneName": ""
                    },
                    {
                        "NodeId": 336946,
                        "NodeType": 1,
                        "ZoneId": 100003,
                        "ZoneName": ""
                    },
                    {
                        "NodeId": 336947,
                        "NodeType": 1,
                        "ZoneId": 100004,
                        "ZoneName": ""
                    }
                ],
                "OfflineTime": "",
                "PasswordFree": 0,
                "Port": 6379,
                "PriceId": 1000848,
                "ProductType": "standalone",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "ReadOnly": 0,
                "RedisReplicasNum": 2,
                "RedisShardNum": 1,
                "RedisShardSize": 4096,
                "Region": "ap-guangzhou",
                "RegionId": 1,
                "RemainBandwidthDuration": "",
                "Size": 4096,
                "SlaveReadWeight": 0,
                "Status": 1,
                "SubStatus": 37,
                "SubnetId": 2282634,
                "Tags": [],
                "Type": 15,
                "UniqSubnetId": "subnet-1ed4w7to",
                "UniqVpcId": "vpc-mjwornzj",
                "Vip6": "",
                "VpcId": 11133673,
                "WanIp": "10.0.1.61",
                "ZoneId": 100002,
                "DiskShardSize": 60,
                "DiskReplicasNum": 3,
                "Compression": "",
                "MachineMemory": 16,
                "DiskShardNum": 1
            },
            {
                "Appid": 251223628,
                "AutoRenewFlag": 0,
                "BillingMode": 1,
                "ClientLimit": 10000,
                "ClientLimitMax": 40000,
                "ClientLimitMin": 10000,
                "CloseTime": "0000-00-00 00:00:00",
                "Createtime": "2023-04-17 11:47:02",
                "DeadlineTime": "2023-05-17 11:47:01",
                "DiskSize": 0,
                "DtsStatus": 0,
                "Engine": "Keewidb",
                "InstanceId": "kee-46njvft9",
                "InstanceName": "Keewidb_automation_is_awesome",
                "InstanceTags": [],
                "InstanceTitle": "运行中",
                "MonitorVersion": "5s",
                "NetLimit": 24,
                "NoAuth": false,
                "NodeSet": [
                    {
                        "NodeId": 336951,
                        "NodeType": 0,
                        "ZoneId": 100002,
                        "ZoneName": ""
                    },
                    {
                        "NodeId": 336949,
                        "NodeType": 1,
                        "ZoneId": 100003,
                        "ZoneName": ""
                    },
                    {
                        "NodeId": 336950,
                        "NodeType": 1,
                        "ZoneId": 100004,
                        "ZoneName": ""
                    }
                ],
                "OfflineTime": "",
                "PasswordFree": 0,
                "Port": 6379,
                "PriceId": 1000848,
                "ProductType": "standalone",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "ReadOnly": 0,
                "RedisReplicasNum": 2,
                "RedisShardNum": 1,
                "RedisShardSize": 4096,
                "Region": "ap-guangzhou",
                "RegionId": 1,
                "RemainBandwidthDuration": "",
                "Size": 4096,
                "SlaveReadWeight": 0,
                "Status": 2,
                "SubStatus": 19,
                "SubnetId": 2282634,
                "Tags": [],
                "Type": 6,
                "UniqSubnetId": "subnet-1ed4w7to",
                "UniqVpcId": "vpc-mjwornzj",
                "Vip6": "",
                "VpcId": 11133673,
                "WanIp": "10.0.1.71",
                "ZoneId": 100002,
                "DiskShardSize": 60,
                "DiskReplicasNum": 3,
                "Compression": "",
                "MachineMemory": 16,
                "DiskShardNum": 1
            }
        ],
        "RequestId": "3fb5a4d2-680c-45a2-aa88-0213b76d1489",
        "TotalCount": 8
    }
}
```

